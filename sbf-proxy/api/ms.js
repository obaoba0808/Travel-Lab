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
  '2605021152246963': { specId: '2605021152246964', name: '\u611b\u6587\u8292\u679c\u6c34\u679c\u7980\u76d2' },
  '2605011150175300': { specId: '2605011150175301', name: '\u91d1\u9e3d\u9鳳\u68a8\u7980\u76d2' },
  '2605021152260362': { specId: '2605021152260363', name: '\u5de8\u5cf0\u8461\u8404\u6c34\u679c\u7980\u76d2' },
  '2605021152270007': { specId: '2605021152270008', name: '\u6afb\u6843\u6c34\u679c\u7980\u76d2' },
  '2605021152272368': { specId: '2605021152272369', name: '\u6c34\u871c\u6843\u6c34\u679c\u7980\u76d2' },
  '2605021152278900': { specId: '2605021152278901', name: '\u69b4\u69e3\u6c34\u679c\u7980\u76d2' },
  '2605021152287723': { specId: '2605021152287724', name: '\u6a19\u6e96\u6c34\u679c\u7b31' },
  '2605021152293023': { specId: '2605021152293024', name: '\u8c6a\u83ef\u7b31' },
};

// Critical CSS to inline
const CRITICAL_CSS = `
<style data-proxy="critical">
*{box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;margin:0;padding:20px;line-height:1.6;color:#333}
.container{max-width:800px;margin:0 auto;background:#fff;padding:30px;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.1)}
h1{color:#e65100;margin-bottom:20px;font-size:24px}
.error{background:#ffebee;color:#c62828;padding:20px;border-radius:8px;margin:20px 0;border-left:4px solid #f44336}
</style>`;

function getErrorPage(message) {
  return `<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>\u8ce3\u8ca8\u4fbf\u9023\u7dda\u554f\u984c</title>
${CRITICAL_CSS}
</head>
<body>
<div class="container">
<div class="error">
<h1>\u26a0\ufe0f \u9023\u7dda\u554f\u984c</h1>
<p>${message}</p>
<ul>
<li>\u76f4\u63a5\u524d\u5f80 <a href="https://myship.7-11.com.tw/general/detail?id=GM2605018541234" target="_blank">\u8ce3\u8ca8\u4fbf\u5546\u5e97</a></li>
<li>\u6216\u806f\u7e6b\u5ba2\u670d LINE: @sweetburst</li>
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

function rewriteSetCookie(cookieStr) {
  return cookieStr.replace(/;\s*Domain=[^;]+/gi, '');
}

function injectBanner(html, productName) {
  // Find <body ...> tag end using indexOf - more reliable than regex
  const bodyStart = html.indexOf('<body');
  if (bodyStart === -1) return html;
  const bodyTagEnd = html.indexOf('>', bodyStart);
  if (bodyTagEnd === -1) return html;

  // Banner HTML - all Chinese as Unicode escapes to avoid encoding issues
  const name = (productName || '\u5546\u54c1').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const bannerHtml = '<div id="sbf-banner" style="'
    + 'display:block!important;'
    + 'visibility:visible!important;'
    + 'opacity:1!important;'
    + 'position:fixed!important;'
    + 'top:0!important;'
    + 'left:0!important;'
    + 'right:0!important;'
    + 'width:100%!important;'
    + 'min-height:52px!important;'
    + 'background:linear-gradient(90deg,#43a047,#66bb6a)!important;'
    + 'color:#fff!important;'
    + 'text-align:center!important;'
    + 'padding:14px 20px!important;'
    + 'font-size:16px!important;'
    + 'font-weight:900!important;'
    + 'z-index:2147483647!important;'
    + 'font-family:-apple-system,BlinkMacSystemFont,sans-serif!important;'
    + 'line-height:1.5!important;'
    + 'box-shadow:0 4px 12px rgba(0,0,0,0.4)!important;'
    + 'cursor:pointer!important;'
    + 'overflow:visible!important;'
    + 'clip:auto!important;'
    + 'clip-path:none!important;'
    + '-webkit-clip-path:none!important;'
    + 'transform:none!important;'
    + 'filter:none!important;'
    + 'pointer-events:auto!important;'
    + 'border:none!important;'
    + 'margin:0!important;'
    + 'float:none!important;'
    + 'max-width:none!important;"'
    + ' onclick="this.style.display=\'none\'">'
    + '\ud83d\uded2 \u5df2\u9078\u597d\u300c' + name + '\u300d\uff01\u8acb\u767b\u5165\u5f8c\u6309\u300c\u76f4\u63a5\u7d50\u5e33\u300d \u2014 \u9ede\u64ca\u95dc\u9589'
    + '</div>';

  // Insert right after <body...>
  return html.slice(0, bodyTagEnd + 1) + bannerHtml + html.slice(bodyTagEnd + 1);
}

function rewriteHtml(html, host, checkoutParams) {
  const proxyBase = getProxyBase(host);

  // Rewrite absolute URLs
  let result = html.replace(/https?:\/\/myship\.7-11\.com\.tw/g, proxyBase);

  // Inject critical CSS + base tag right after <head>
  const headIdx = result.indexOf('<head>');
  if (headIdx !== -1) {
    const insertAfterHead = headIdx + '<head>'.length;
    result = result.slice(0, insertAfterHead)
      + CRITICAL_CSS
      + '<base href="' + proxyBase + '/">'
      + result.slice(insertAfterHead);
  }

  if (!checkoutParams) return result;

  const productName = PRODUCT_MAP[checkoutParams.carProduct]?.name || '';

  // 1. Inject static banner (no JS dependency)
  result = injectBanner(result, productName);

  // 2. Inject nuclear CSS override in <head> to ensure banner is always visible
  const nuclearCSS = '<style id="sbf-css">'
    + 'html,body{padding-top:60px!important}'
    + '#sbf-banner{'
    + 'display:block!important;'
    + 'visibility:visible!important;'
    + 'opacity:1!important;'
    + 'position:fixed!important;'
    + 'top:0!important;'
    + 'left:0!important;'
    + 'z-index:2147483647!important;'
    + 'transform:none!important;'
    + 'clip:auto!important;'
    + 'clip-path:none!important;'
    + '-webkit-clip-path:none!important}'
    + '</style>';
  const headCloseIdx = result.indexOf('</head>');
  if (headCloseIdx !== -1) {
    result = result.slice(0, headCloseIdx) + nuclearCSS + result.slice(headCloseIdx);
  }

  // 3. Inject alertify override in head (suppress login popup)
  const alertifyOverride = '<script data-proxy="override">'
    + '(function(){'
    + 'var _a=null;'
    + 'Object.defineProperty(window,"alertify",{'
    + 'configurable:true,'
    + 'get:function(){return _a;},'
    + 'set:function(v){'
    + '_a=v;'
    + 'if(v&&typeof v.alert==="function"){'
    + 'v.alert=function(m,fn){if(typeof fn==="function")fn();};'
    + '}'
    + '}'
    + '});'
    + '})();'
    + '<\/script>';
  const headOpenEnd = result.indexOf('<head>');
  if (headOpenEnd !== -1) {
    const pos = headOpenEnd + '<head>'.length;
    result = result.slice(0, pos) + alertifyOverride + result.slice(pos);
  }

  // 4. Inject auto-fill JS before </body>
  const autoFillJS = '<script data-proxy="fill">'
    + '(function(){'
    + 'var P=' + JSON.stringify(checkoutParams) + ';'
    + 'var done=false;'
    + 'function fill(){'
    + 'if(done)return;done=true;'
    + 'var cp=document.querySelector("input[name=CarProduct]");'
    + 'var ci=document.querySelector("input[name=CarItem]");'
    + 'var cq=document.querySelector("input[name=CarQty]");'
    + 'var cm=document.querySelector("input[name=CarMinQty]");'
    + 'if(cp)cp.value=P.carProduct;'
    + 'if(ci)ci.value=P.carItem;'
    + 'if(cq)cq.value=P.carQty||"1";'
    + 'if(cm)cm.value=P.carMinQty||"1";'
    + 'document.querySelectorAll(".product_size_switch span").forEach(function(s){'
    + 'if(s.dataset.productId===P.carProduct&&s.dataset.specId===P.carItem&&!s.classList.contains("active"))s.click();'
    + '});'
    + 'var cs=new URLSearchParams(location.search).get("_checkout");'
    + 'if(cs)document.querySelectorAll("form[action*=ExternalLogin]").forEach(function(f){'
    + 'var a=f.getAttribute("action")||"";'
    + 'var m=a.match(/ReturnUrl=([^&]+)/);'
    + 'if(m){var ru=decodeURIComponent(m[1]);if(!ru.includes("_checkout")){ru+="&_checkout="+encodeURIComponent(cs);f.setAttribute("action",a.replace(/ReturnUrl=[^&]+/,"ReturnUrl="+encodeURIComponent(ru)));}'
    + '}});'
    + 'try{localStorage.setItem("_sbf",JSON.stringify(P));}catch(e){}'
    + 'if(!document.querySelector("a[data-target=\'#loginModal\']")){'
    + 'var form=document.querySelector("#formBuyProducts");'
    + 'if(form)setTimeout(function(){form.submit();},800);'
    + '}'
    + '}'
    + 'if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",fill);'
    + 'else fill();'
    + 'setTimeout(fill,3000);'
    + '})();'
    + '<\/script>';

  const bodyCloseIdx = result.lastIndexOf('</body>');
  if (bodyCloseIdx !== -1) {
    result = result.slice(0, bodyCloseIdx) + autoFillJS + result.slice(bodyCloseIdx);
  } else {
    result += autoFillJS;
  }

  return result;
}

export default async function handler(req, res) {
  const host = req.headers.host || req.headers['x-forwarded-host'] || 'localhost:3000';

  const urlObj = new URL(req.url, `https://${host}`);
  let proxyPath = urlObj.pathname.replace(/^\/api\/ms\/?/, '');
  if (!proxyPath) proxyPath = '';
  const myshipUrl = MYSHIP_ORIGIN + (proxyPath ? '/' + proxyPath : '') + urlObj.search;

  const forwardHeaders = {};
  const skipHeaders = ['host','connection','content-length','transfer-encoding','x-forwarded-for','x-forwarded-host','x-forwarded-proto'];
  for (const [k, v] of Object.entries(req.headers)) {
    if (!skipHeaders.includes(k.toLowerCase())) forwardHeaders[k] = v;
  }
  forwardHeaders['host'] = 'myship.7-11.com.tw';
  forwardHeaders['origin'] = MYSHIP_ORIGIN;
  forwardHeaders['referer'] = MYSHIP_ORIGIN + '/general/detail?id=GM2605018541234';
  forwardHeaders['user-agent'] = forwardHeaders['user-agent'] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';
  forwardHeaders['accept'] = forwardHeaders['accept'] || 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8';
  forwardHeaders['accept-language'] = forwardHeaders['accept-language'] || 'zh-TW,zh;q=0.9,en;q=0.8';

  try {
    const fetchOptions = { method: req.method, headers: forwardHeaders, redirect: 'manual' };

    if (req.method !== 'GET' && req.method !== 'HEAD') {
      const chunks = [];
      for await (const chunk of req) chunks.push(chunk);
      if (chunks.length > 0) fetchOptions.body = Buffer.concat(chunks);
    }

    const myshipResp = await fetch(myshipUrl, fetchOptions);

    if (myshipResp.status === 403) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(getErrorPage('\u8ce3\u8ca8\u4fbf\u4f3a\u670d\u5668\u66ab\u6642\u7121\u6cd5\u5b58\u53d6\uff08403\uff09\u3002'));
      return;
    }

    if ([301,302,303,307,308].includes(myshipResp.status)) {
      const location = myshipResp.headers.get('location') || '';
      res.writeHead(myshipResp.status, { 'Location': rewriteUrl(location, host) });
      res.end();
      return;
    }

    const respHeaders = {};
    for (const [k, v] of myshipResp.headers.entries()) {
      const lower = k.toLowerCase();
      if (lower === 'set-cookie') {
        const cookies = Array.isArray(v) ? v : [v];
        respHeaders['set-cookie'] = cookies.map(c => rewriteSetCookie(c));
      } else if (lower === 'location') {
        respHeaders['location'] = rewriteUrl(v, host);
      } else if (!['transfer-encoding','content-encoding','content-length'].includes(lower)) {
        respHeaders[k] = v;
      }
    }

    const contentType = myshipResp.headers.get('content-type') || '';
    const isHtml = contentType.includes('text/html');

    if (isHtml) {
      let html = await myshipResp.text();
      let checkoutParams = null;
      const checkoutStr = urlObj.searchParams.get('_checkout');
      if (checkoutStr) {
        try { checkoutParams = JSON.parse(decodeURIComponent(checkoutStr)); } catch(e) {}
      }
      html = rewriteHtml(html, host, checkoutParams);
      respHeaders['content-type'] = 'text/html; charset=utf-8';
      res.writeHead(myshipResp.status, respHeaders);
      res.end(html);
    } else {
      if (myshipResp.status === 403 || myshipResp.status === 404) {
        if (contentType.includes('css')) {
          res.writeHead(200, { 'Content-Type': 'text/css' });
          res.end('/* blocked */');
        } else if (contentType.includes('javascript')) {
          res.writeHead(200, { 'Content-Type': 'application/javascript' });
          res.end('');
        } else if (contentType.includes('image')) {
          const gif = Buffer.from('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7', 'base64');
          res.writeHead(200, { 'Content-Type': 'image/gif', 'Content-Length': gif.length });
          res.end(gif);
        } else {
          res.writeHead(200, { 'Content-Type': contentType || 'application/octet-stream' });
          res.end('');
        }
        return;
      }
      const buffer = Buffer.from(await myshipResp.arrayBuffer());
      res.writeHead(myshipResp.status, respHeaders);
      res.end(buffer);
    }
  } catch (err) {
    console.error('Proxy error:', err);
    res.writeHead(502, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(getErrorPage('\u9023\u7dda\u5931\u6557\uff1a' + err.message));
  }
}
