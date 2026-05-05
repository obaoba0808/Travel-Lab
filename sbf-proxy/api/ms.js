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

function getProxyBase(host) {
  return `https://${host}/api/ms`;
}

function rewriteUrl(url, host) {
  if (!url) return url;
  return url.replace(MYSHIP_ORIGIN, getProxyBase(host));
}

function rewriteSetCookie(cookieStr, host) {
  // Remove Domain attribute so browser sets cookie on proxy domain
  return cookieStr.replace(/;\s*Domain=[^;]+/gi, '');
}

function rewriteHtml(html, host, checkoutParams) {
  const proxyBase = getProxyBase(host);
  
  // Rewrite absolute URLs
  let result = html.replace(/https?:\/\/myship\.7-11\.com\.tw/g, proxyBase);
  
  // Add <base> tag so relative CSS/JS URLs resolve through proxy
  if (result.includes('<head>')) {
    result = result.replace('<head>', '<head><base href="' + proxyBase + '/">');
  } else if (result.includes('<html')) {
    result = result.replace(/<html([^>]*)>/, '<html$1><head><base href="' + proxyBase + '/"></head>');
  }
  
  // Inject auto-fill JavaScript if checkout params present
  if (checkoutParams) {
    const inject = `
<script data-proxy="true">
(function(){
  var params = ${JSON.stringify(checkoutParams)};
  function tryAutoFill() {
    var cp = document.querySelector('input[name=CarProduct]');
    var ci = document.querySelector('input[name=CarItem]');
    var cq = document.querySelector('input[name=CarQty]');
    var cm = document.querySelector('input[name=CarMinQty]');
    if (cp && ci && cq && cm) {
      cp.value = params.carProduct;
      ci.value = params.carItem;
      cq.value = params.carQty;
      cm.value = params.carMinQty;
      var form = cp.closest('form');
      if (form) {
        document.body.insertAdjacentHTML('beforeend',
          '<div style="position:fixed;top:0;left:0;right:0;background:linear-gradient(90deg,#ff7a00,#ffb703);color:#fff;text-align:center;padding:14px;font-size:16px;font-weight:900;z-index:99999;font-family:sans-serif">\\u26A1 \\u81EA\\u52D5\\u7D50\\u5E33\\u4E2D... \\u8ACB\\u7A0D\\u5019</div>'
        );
        form.submit();
        return true;
      }
    }
    return false;
  }
  if (!tryAutoFill()) {
    var observer = new MutationObserver(function() {
      if (tryAutoFill()) observer.disconnect();
    });
    observer.observe(document.body, { childList: true, subtree: true });
    setTimeout(function() { observer.disconnect(); }, 5000);
  }
})();
</script>`;
    // Inject before </body> if exists, otherwise append to end
    if (result.includes('</body>')) {
      result = result.replace('</body>', inject + '\n</body>');
    } else {
      result += inject;
    }
  }
  
  return result;
}

export default async function handler(req, res) {
  const host = req.headers.host || req.headers['x-forwarded-host'] || 'localhost:3000';
  
  // Parse the myship path from the URL
  // URL format: /api/ms/myship/path?query  OR  /myship/path?query (catch-all)
  const urlObj = new URL(req.url, `https://${host}`);
  let proxyPath = urlObj.pathname.replace(/^\/api\/ms\/?/, '');
  // If path still starts with / (absolute path like /css/style.js), use it directly
  if (!proxyPath) {
    proxyPath = '';
  }
  const myshipUrl = MYSHIP_ORIGIN + (proxyPath ? '/' + proxyPath : '') + urlObj.search;
  
  // Build headers for myship request
  const forwardHeaders = {};
  const skipHeaders = ['host', 'connection', 'content-length', 'transfer-encoding', 'x-forwarded-for', 'x-forwarded-host', 'x-forwarded-proto', 'x-vercel-forwarded-for', 'x-vercel-ip-country', 'x-vercel-ip-country-region', 'x-vercel-ip-city', 'x-vercel-ip-latitude', 'x-vercel-ip-longitude'];
  
  for (const [key, value] of Object.entries(req.headers)) {
    const lower = key.toLowerCase();
    if (!skipHeaders.includes(lower)) {
      forwardHeaders[key] = value;
    }
  }
  forwardHeaders['host'] = 'myship.7-11.com.tw';
  forwardHeaders['origin'] = MYSHIP_ORIGIN;
  forwardHeaders['referer'] = MYSHIP_ORIGIN + '/general/detail?id=GM2605018541234';
  forwardHeaders['user-agent'] = forwardHeaders['user-agent'] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36';
  forwardHeaders['accept'] = forwardHeaders['accept'] || 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8';
  forwardHeaders['accept-language'] = forwardHeaders['accept-language'] || 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7';
  
  // Fetch from myship
  try {
    const fetchOptions = {
      method: req.method,
      headers: forwardHeaders,
      redirect: 'manual',
    };
    
    if (req.method !== 'GET' && req.method !== 'HEAD') {
      // Forward request body
      const chunks = [];
      for await (const chunk of req) {
        chunks.push(chunk);
      }
      if (chunks.length > 0) {
        fetchOptions.body = Buffer.concat(chunks);
      }
    }
    
    const myshipResp = await fetch(myshipUrl, fetchOptions);
    
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
        // Rewrite cookie - remove Domain attribute
        const cookies = Array.isArray(value) ? value : [value];
        respHeaders['set-cookie'] = cookies.map(c => rewriteSetCookie(c, host));
      } else if (lower === 'location') {
        respHeaders['location'] = rewriteUrl(value, host);
      } else if (!['transfer-encoding', 'content-encoding', 'content-length'].includes(lower)) {
        respHeaders[key] = value;
      }
    }
    
    // Get response body
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
      // Pass through non-HTML responses
      const buffer = Buffer.from(await myshipResp.arrayBuffer());
      res.writeHead(myshipResp.status, respHeaders);
      res.end(buffer);
    }
  } catch (err) {
    console.error('Proxy error:', err);
    res.writeHead(502, { 'Content-Type': 'text/plain' });
    res.end('Proxy error: ' + err.message);
  }
}
