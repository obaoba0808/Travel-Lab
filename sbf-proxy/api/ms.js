// Reverse proxy for myship.7-11.com.tw
// All requests to /api/ms/* are forwarded to myship with cookies
// HTML responses are rewritten to replace URLs and inject auto-fill JS

const MYSHIP_ORIGIN = 'https://myship.7-11.com.tw';

export const config = {
  api: {
    bodyParser: false,
    responseLimit: false,
  },
};

// Product ID mapping for auto-fill
const PRODUCT_MAP = {
  '2605021152246963': { specId: '2605021152246964', name: '愛文芒果水果禮盒' },
  '2605011150175300': { specId: '2605011150175301', name: '金鑽鳳梨禮盒' },
  '2605021152260362': { specId: '2605021152260363', name: '巨峰葡萄水果禮盒' },
  '2605021152270007': { specId: '2605021152270008', name: '櫻桃水果禮盒' },
  '2605021152272368': { specId: '2605021152272369', name: '水蜜桃水果禮盒' },
  '2605021152278900': { specId: '2605021152278901', name: '榴槤水果禮盒' },
  '2605021152287723': { specId: '2605021152287724', name: '標準水果箱' },
  '2605021152293023': { specId: '2605021152293024', name: '豪華箱' },
};

// Critical CSS to inline - ensures page renders even if external CSS fails
const CRITICAL_CSS = `
<style data-proxy="critical">
*{box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;margin:0;padding:20px;line-height:1.6;color:#333}
.container{max-width:800px;margin:0 auto;background:#fff;padding:30px;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.1)}
h1{color:#e65100;margin-bottom:20px;font-size:24px}
.product-info{background:linear-gradient(135deg,#fff3e0 0%,#ffe0b2 100%);padding:20px;border-radius:12px;margin:20px 0;border-left:4px solid #ff9800}
.product-name{font-size:20px;font-weight:700;color:#e65100;margin-bottom:10px}
.product-price{font-size:32px;font-weight:900;color:#ff5722;margin:10px 0}
.btn-buy{display:inline-block;background:linear-gradient(90deg,#ff7a00,#ffb703);color:#fff;padding:16px 40px;border-radius:50px;font-size:18px;font-weight:700;text-decoration:none;box-shadow:0 4px 15px rgba(255,122,0,0.3);transition:all 0.3s;border:none;cursor:pointer}
.btn-buy:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(255,122,0,0.4)}
.loading{text-align:center;padding:40px;color:#666}
.spinner{display:inline-block;width:40px;height:40px;border:3px solid #f3f3f3;border-top:3px solid #ff9800;border-radius:50%;animation:spin 1s linear infinite}
@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.error{background:#ffebee;color:#c62828;padding:20px;border-radius:8px;margin:20px 0;border-left:4px solid #f44336}
.success{background:#e8f5e9;color:#2e7d32;padding:20px;border-radius:8px;margin:20px 0;border-left:4px solid #4caf50}
</style>`;

// Error page HTML
function getErrorPage(message, isHtml = true) {
  if (!isHtml) return message;
  return `<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>賣貨便連線問題</title>
${CRITICAL_CSS}
</head>
<body>
<div class="container">
<div class="error">
<h1>⚠️ 連線問題</h1>
<p>${message}</p>
<p>請嘗試以下方式：</p>
<ul>
<li>直接前往 <a href="https://myship.7-11.com.tw/general/detail?id=GM2605018541234" target="_blank">賣貨便商店</a></li>
<li>或聯繫客服 LINE: @sweetburst</li>
</ul>
</div>
</div>
</body>
</html>`;
}

function getProxyBase(host) {
  return `https://${host}/api/ms`;
}

function rewriteUrl(url, host) {
  if (!url) return url;
  return url.replace(MYSHIP_ORIGIN, getProxyBase(host));
}

function rewriteSetCookie(cookieStr, host) {
  return cookieStr.replace(/;\s*Domain=[^;]+/gi, '');
}

function rewriteHtml(html, host, checkoutParams) {
  const proxyBase = getProxyBase(host);
  
  // Rewrite absolute URLs
  let result = html.replace(/https?:\/\/myship\.7-11\.com\.tw/g, proxyBase);
  
  // Inject critical CSS right after <head>
  if (result.includes('<head>')) {
    result = result.replace('<head>', '<head>' + CRITICAL_CSS + '<base href="' + proxyBase + '/">');
  } else if (result.includes('<html')) {
    result = result.replace(/<html([^>]*)>/, '<html$1><head>' + CRITICAL_CSS + '<base href="' + proxyBase + '/"></head>');
  }
  
  // Inject auto-fill JavaScript if checkout params present
  if (checkoutParams) {
    const productName = PRODUCT_MAP[checkoutParams.carProduct]?.name || '';
    
    // Head injection: override alertify BEFORE page scripts run
    const headInject = `
<script data-proxy="override">
(function(){
  // Suppress alertify login prompt - intercept before it fires
  var _origAlert = null;
  Object.defineProperty(window, 'alertify', {
    configurable: true,
    get: function() { return _origAlert; },
    set: function(val) {
      _origAlert = val;
      if (val && typeof val.alert === 'function') {
        val.alert = function(msg, fn) {
          // Silently dismiss login-related alerts
          if (fn && typeof fn === 'function') { fn(); return; }
          if (_origAlert && _origAlert !== val && _origAlert.alert) {
            return _origAlert.alert.call(_origAlert, msg, fn);
          }
        };
      }
    }
  });
})();
</script>`;
    
    // Body injection: auto-fill logic with robust timing
    const bodyInject = `
<script data-proxy="true">
(function(){
  var params = ${JSON.stringify(checkoutParams)};
  var productName = ${JSON.stringify(productName)};
  var _done = false;

  function showBanner(msg, bgColor) {
    if (!document.body) return;
    var el = document.createElement('div');
    el.style.cssText = 'position:fixed;top:0;left:0;right:0;background:' + (bgColor||'linear-gradient(90deg,#ff7a00,#ffb703)') + ';color:#fff;text-align:center;padding:14px 16px;font-size:16px;font-weight:900;z-index:999999;font-family:sans-serif,-apple-system,BlinkMacSystemFont;box-shadow:0 2px 8px rgba(0,0,0,0.2);pointer-events:auto';
    el.textContent = msg;
    document.body.insertBefore(el, document.body.firstChild);
  }

  function doAutoFill() {
    if (_done) return;
    _done = true;

    // Fill hidden form fields
    var cp = document.querySelector('input[name=CarProduct]');
    var ci = document.querySelector('input[name=CarItem]');
    var cq = document.querySelector('input[name=CarQty]');
    var cm = document.querySelector('input[name=CarMinQty]');
    if (cp) cp.value = params.carProduct;
    if (ci) ci.value = params.carItem;
    if (cq) cq.value = params.carQty || '1';
    if (cm) cm.value = params.carMinQty || '1';

    // Auto-select product spec
    document.querySelectorAll('.product_size_switch span').forEach(function(s) {
      if (s.dataset.productId === params.carProduct && s.dataset.specId === params.carItem) {
        if (!s.classList.contains('active')) s.click();
      }
    });

    // Fix ReturnUrl in social login forms
    var cs = new URLSearchParams(location.search).get('_checkout');
    if (cs) {
      document.querySelectorAll('form[action*="ExternalLogin"]').forEach(function(form) {
        var act = form.getAttribute('action') || '';
        var m = act.match(/ReturnUrl=([^&]+)/);
        if (m) {
          var ru = decodeURIComponent(m[1]);
          if (!ru.includes('_checkout')) {
            ru += '&_checkout=' + encodeURIComponent(cs);
            form.setAttribute('action', act.replace(/ReturnUrl=[^&]+/, 'ReturnUrl=' + encodeURIComponent(ru)));
          }
        }
      });
    }

    // Store in localStorage
    try { localStorage.setItem('_sbf_checkout', JSON.stringify(params)); } catch(e) {}

    // Check login status
    var loggedIn = !document.querySelector('a[data-target="#loginModal"]');

    // Dismiss any existing alertify dialog
    setTimeout(function() {
      var okBtn = document.querySelector('.ajs-ok');
      if (okBtn) okBtn.click();
      // Also try clicking overlay to close modal
      var overlay = document.querySelector('.ajs-overlay');
      if (overlay) overlay.click();
    }, 600);

    if (loggedIn) {
      showBanner('\u26A1 \u81EA\u52D5\u7D50\u5E33\u4E2D... \u8ACB\u7A0D\u5019');
      var form = document.querySelector('#formBuyProducts');
      if (form) setTimeout(function() { form.submit(); }, 1000);
    } else {
      showBanner(
        '\uD83D\uDED2 \u5DF2\u9078\u597D\u300C' + (productName || '\u5546\u54C1') + '\u300D\uFF01\u8ACB\u767B\u5165\u5F8C\u6309\u300C\u76F4\u63A5\u7D50\u5E33\u300D',
        'linear-gradient(90deg,#4CAF50,#66BB6A)'
      );
    }
  }

  // Triple fallback strategy:
  // 1. DOMContentLoaded (normal case)
  // 2. MutationObserver (if DOM is still building)
  // 3. setTimeout 3s (ultimate fallback)
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', doAutoFill);
  } else {
    doAutoFill();
  }

  // Fallback: observe body for form elements
  var observer = new MutationObserver(function(mutations) {
    if (document.querySelector('input[name=CarProduct]') || document.querySelector('#loginModal')) {
      setTimeout(doAutoFill, 200);
    }
  });
  if (document.body) {
    observer.observe(document.body, { childList: true, subtree: true });
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      observer.observe(document.body, { childList: true, subtree: true });
    });
  }

  // Ultimate timeout fallback
  setTimeout(doAutoFill, 3000);
})();
</script>`;
    // Inject head override (suppress alertify) after <head> or critical CSS
    if (result.includes('<head>')) {
      result = result.replace('<head>', '<head>' + headInject);
    } else if (result.includes(CRITICAL_CSS)) {
      result = result.replace(CRITICAL_CSS, CRITICAL_CSS + headInject);
    }
    
    // Inject body script before </body>
    if (result.includes('</body>')) {
      result = result.replace('</body>', bodyInject + '\n</body>');
    } else {
      result += bodyInject;
    }
  }
  
  return result;
}

export default async function handler(req, res) {
  const host = req.headers.host || req.headers['x-forwarded-host'] || 'localhost:3000';
  
  const urlObj = new URL(req.url, `https://${host}`);
  let proxyPath = urlObj.pathname.replace(/^\/api\/ms\/?/, '');
  if (!proxyPath) proxyPath = '';
  const myshipUrl = MYSHIP_ORIGIN + (proxyPath ? '/' + proxyPath : '') + urlObj.search;
  
  // Build headers for myship request
  const forwardHeaders = {};
  const skipHeaders = ['host', 'connection', 'content-length', 'transfer-encoding', 'x-forwarded-for', 'x-forwarded-host', 'x-forwarded-proto'];
  
  for (const [key, value] of Object.entries(req.headers)) {
    const lower = key.toLowerCase();
    if (!skipHeaders.includes(lower)) {
      forwardHeaders[key] = value;
    }
  }
  forwardHeaders['host'] = 'myship.7-11.com.tw';
  forwardHeaders['origin'] = MYSHIP_ORIGIN;
  forwardHeaders['referer'] = MYSHIP_ORIGIN + '/general/detail?id=GM2605018541234';
  forwardHeaders['user-agent'] = forwardHeaders['user-agent'] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';
  forwardHeaders['accept'] = forwardHeaders['accept'] || 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8';
  forwardHeaders['accept-language'] = forwardHeaders['accept-language'] || 'zh-TW,zh;q=0.9,en;q=0.8';
  
  try {
    const fetchOptions = {
      method: req.method,
      headers: forwardHeaders,
      redirect: 'manual',
    };
    
    if (req.method !== 'GET' && req.method !== 'HEAD') {
      const chunks = [];
      for await (const chunk of req) {
        chunks.push(chunk);
      }
      if (chunks.length > 0) {
        fetchOptions.body = Buffer.concat(chunks);
      }
    }
    
    const myshipResp = await fetch(myshipUrl, fetchOptions);
    
    // Handle 403 errors - return friendly error page
    if (myshipResp.status === 403) {
      const errorHtml = getErrorPage('賣貨便伺服器暫時無法存取（403）。這通常是因為賣貨便對靜態資源有存取限制。');
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(errorHtml);
      return;
    }
    
    // Handle redirects
    if ([301, 302, 303, 307, 308].includes(myshipResp.status)) {
      const location = myshipResp.headers.get('location') || '';
      const rewritten = rewriteUrl(location, host);
      res.writeHead(myshipResp.status, { 'Location': rewritten });
      res.end();
      return;
    }
    
    // Build response headers
    const respHeaders = {};
    for (const [key, value] of myshipResp.headers.entries()) {
      const lower = key.toLowerCase();
      if (lower === 'set-cookie') {
        const cookies = Array.isArray(value) ? value : [value];
        respHeaders['set-cookie'] = cookies.map(c => rewriteSetCookie(c, host));
      } else if (lower === 'location') {
        respHeaders['location'] = rewriteUrl(value, host);
      } else if (!['transfer-encoding', 'content-encoding', 'content-length'].includes(lower)) {
        respHeaders[key] = value;
      }
    }
    
    const contentType = myshipResp.headers.get('content-type') || '';
    const isHtml = contentType.includes('text/html');
    
    if (isHtml) {
      let html = await myshipResp.text();
      
      // Parse checkout params from query string
      let checkoutParams = null;
      const checkoutStr = urlObj.searchParams.get('_checkout');
      if (checkoutStr) {
        try {
          checkoutParams = JSON.parse(decodeURIComponent(checkoutStr));
        } catch(e) {}
      }
      
      // Rewrite HTML
      html = rewriteHtml(html, host, checkoutParams);
      
      respHeaders['content-type'] = 'text/html; charset=utf-8';
      res.writeHead(myshipResp.status, respHeaders);
      res.end(html);
    } else {
      // For non-HTML (CSS/JS/images), return empty/transparent if 403
      if (myshipResp.status === 403 || myshipResp.status === 404) {
        // Return empty for CSS/JS, transparent pixel for images
        if (contentType.includes('css')) {
          res.writeHead(200, { 'Content-Type': 'text/css' });
          res.end('/* CSS blocked by myship */');
        } else if (contentType.includes('javascript')) {
          res.writeHead(200, { 'Content-Type': 'application/javascript' });
          res.end('// JS blocked by myship');
        } else if (contentType.includes('image')) {
          // Return 1x1 transparent GIF
          const transparentGif = Buffer.from('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7', 'base64');
          res.writeHead(200, { 'Content-Type': 'image/gif', 'Content-Length': transparentGif.length });
          res.end(transparentGif);
        } else {
          res.writeHead(200, { 'Content-Type': contentType || 'application/octet-stream' });
          res.end('');
        }
        return;
      }
      
      // Pass through successful non-HTML responses
      const buffer = Buffer.from(await myshipResp.arrayBuffer());
      res.writeHead(myshipResp.status, respHeaders);
      res.end(buffer);
    }
  } catch (err) {
    console.error('Proxy error:', err);
    const errorHtml = getErrorPage('連線失敗：' + err.message);
    res.writeHead(502, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(errorHtml);
  }
}
