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

const PRODUCT_MAP = {
  '2605021152246963': { specId: '2605021152246964', name: '\u611b\u6587\u8292\u679c\u6c34\u679c\u7980\u76d2' },
  '2605011150175300': { specId: '2605011150175301', name: '\u91d1\u9e3d\u9cf3\u68a8\u7980\u76d2' },
  '2605021152260362': { specId: '2605021152260363', name: '\u5de8\u5cf0\u8461\u8404\u6c34\u679c\u7980\u76d2' },
  '2605021152270007': { specId: '2605021152270008', name: '\u6afb\u6843\u6c34\u679c\u7980\u76d2' },
  '2605021152272368': { specId: '2605021152272369', name: '\u6c34\u871c\u6843\u6c34\u679c\u7980\u76d2' },
  '2605021152278900': { specId: '2605021152278901', name: '\u69b4\u69e3\u6c34\u679c\u7980\u76d2' },
  '2605021152287723': { specId: '2605021152287724', name: '\u6a19\u6e96\u6c34\u679c\u7b31' },
  '2605021152293023': { specId: '2605021152293024', name: '\u8c6a\u83ef\u7b31' },
};

// Full inline CSS for beautiful rendering when external CSS is blocked (403)
const BEAUTIFY_CSS = `
<style id="sbf-beautify">
/* ===== RESET & BASE ===== */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{font-size:16px;-webkit-text-size-adjust:100%}
body{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Microsoft JhengHei",Roboto,sans-serif;
  line-height:1.6;color:#333;background:#f5f5f5;
  padding-top:60px!important; /* space for fixed banner */
}
a{color:#ff7043;text-decoration:none}
a:hover{color:#e64a19;text-decoration:underline}
img{max-width:100%;height:auto;border-radius:8px}

/* ===== BANNER ===== */
#sbf-banner{
  display:block!important;visibility:visible!important;opacity:1!important;
  position:fixed!important;top:0!important;left:0!important;right:0!important;width:100%!important;
  min-height:56px!important;
  background:linear-gradient(135deg,#ff7043,#ffb74d)!important;
  color:#fff!important;text-align:center!important;padding:14px 20px!important;
  font-size:15px!important;font-weight:700!important;z-index:2147483647!important;
  font-family:-apple-system,BlinkMacSystemFont,sans-serif!important;line-height:1.5!important;
  box-shadow:0 4px 20px rgba(255,112,67,0.4)!important;cursor:pointer!important;
  overflow:visible!important;clip:auto!important;clip-path:none!important;
  -webkit-clip-path:none!important;transform:none!important;filter:none!important;
  pointer-events:auto!important;border:none!important;margin:0!important;float:none!important;
  letter-spacing:0.5px;
}
#sbf-banner:hover{background:linear-gradient(135deg,#ff5722,#ffa726)!important}

/* ===== LAYOUT ===== */
.container,.container-fluid{max-width:1100px;margin:0 auto;padding:0 16px}
.row{display:flex;flex-wrap:wrap;margin:0 -8px}
.col-md-3,.col-sm-6,.col-xs-12{padding:8px;flex:1;min-width:200px}

/* ===== HEADER / SHOP INFO ===== */
.shop-header{text-align:center;padding:24px 16px;background:#fff;margin-bottom:16px;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.06)}
.shop-header h1{font-size:24px;font-weight:800;color:#e64a19;margin-bottom:8px}
.shop-header .shop-subtitle{color:#888;font-size:14px}

/* ===== PRODUCT GRID ===== */
.product-list{display:flex;flex-wrap:wrap;gap:16px;padding:16px;max-width:1100px;margin:0 auto}
.product-card{
  background:#fff;border-radius:14px;overflow:hidden;
  box-shadow:0 2px 12px rgba(0,0,0,0.08);transition:all 0.3s ease;
  flex:1;min-width:240px;max-width:280px;position:relative
}
.product-card:hover{transform:translateY(-4px);box-shadow:0 8px 28px rgba(230,74,25,0.18)}
.product-img{width:100%;height:180px;object-fit:cover;background:linear-gradient(135deg,#ffe0b2,#ffcc80)}
.product-info{padding:14px}
.product-name{font-size:15px;font-weight:700;color:#333;margin-bottom:6px;line-height:1.4}
.product-price{font-size:22px;font-weight:900;color:#e64a19;margin-bottom:10px}
.product-price .original{font-size:13px;color:#999;text-decoration:line-through;font-weight:400;margin-right:6px}
.product-spec{margin-bottom:10px}
.spec-btn{
  display:inline-block;padding:6px 14px;border:2px solid #ffcc80;border-radius:20px;
  font-size:13px;font-weight:600;color:#e65100;cursor:pointer;transition:all 0.2s;
  margin:2px;background:#fff
}
.spec-btn.active{background:linear-gradient(135deg,#ff7043,#ffb74d);border-color:#ff7043;color:#fff}
.spec-btn:hover:not(.active){border-color:#ff7043;background:#fff3e0}
.btn-add-cart{
  display:block;width:100%;padding:10px;border:none;border-radius:25px;
  background:linear-gradient(135deg,#ff7043,#ffb74d);color:#fff;
  font-size:14px;font-weight:700;cursor:pointer;transition:all 0.3s
}
.btn-add-cart:hover{background:linear-gradient(135deg,#ff5722,#ffa726);box-shadow:0 4px 12px rgba(255,112,67,0.4)}

/* ===== LOGIN AREA ===== */
.login-area{text-align:center;padding:40px 20px;background:#fff;margin:16px;border-radius:12px;max-width:600px;margin-left:auto;margin-right:auto}
.login-area h2{font-size:18px;color:#333;margin-bottom:16px}
.login-btn{
  display:inline-block;padding:12px 32px;border-radius:30px;
  font-size:15px;font-weight:700;cursor:pointer;transition:all 0.3s;
  margin:6px;border:none
}
.login-btn-line{background:linear-gradient(135deg,#06c755,#00b900);color:#fff}
.login-btn-line:hover{box-shadow:0 4px 16px rgba(6,199,85,0.4);transform:scale(1.03)}
.login-btn-fb{background:linear-gradient(135deg,#1877f2,#42a5f5);color:#fff}
.login-btn-fb:hover{box-shadow:0 4px 16px rgba(24,119,242,0.4);transform:scale(1.03)}

/* ===== FOOTER ===== */
.footer-area{background:#fff;margin-top:24px;padding:24px 16px;text-align:center;border-top:1px solid #eee;color:#888;font-size:13px}

/* ===== MODAL OVERRIDE ===== */
.modal{display:none!important}.ajs-modal{display:none!important}.ajs-overlay{display:none!important}
.ajs-dialog{display:none!important}

/* ===== UTILITY ===== */
.text-center{text-align:center}.text-danger{color:#e53935}.text-muted{color:#999}
.hidden{display:none!important}.clearfix::after{content:"";display:table;clear:both}

/* ===== RESPONSIVE ===== */
@media(max-width:600px){
  body{font-size:14px;padding-top:52px!important}
  #sbf-banner{font-size:13px!important;padding:10px 16px!important;min-height:46px!important}
  .product-card{min-width:160px;max-width:100%}
  .product-list{gap:10px;padding:10px}
}
</style>`;

function getErrorPage(message) {
  return `<!DOCTYPE html>
<html lang="zh-TW">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>\u8ce3\u8ca8\u4fbf\u9023\u7dda</title>${BEAUTIFY_CSS}</head>
<body>
<div class="container"><div class="shop-header"><h1>\u26a0\ufe0f \u9023\u7dda\u554f\u984c</h1>
<p>${message}</p><p style="margin-top:16px">
<a href="https://myship.7-11.com.tw/general/detail?id=GM2605018541234" target="_blank" class="login-btn login-btn-line" style="color:#fff">\u76f4\u63a5\u524d\u5f80\u8ce3\u8ca8\u4fbf</a></p></div></div></body></html>`;
}

function getProxyBase(host) { return `https://${host}/api/ms`; }
function rewriteUrl(url, host) { return url ? url.replace(MYSHIP_ORIGIN, getProxyBase(host)) : url; }
function rewriteSetCookie(s) { return s.replace(/;\s*Domain=[^;]+/gi, ''); }

function injectBanner(html, productName) {
  const bs = html.indexOf('<body');
  if (bs === -1) return html;
  const be = html.indexOf('>', bs);
  if (be === -1) return html;
  const name = (productName || '\u5546\u54c1').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  const banner = '<div id="sbf-banner" onclick="this.style.display=\'none\'">'
    + '<span style="font-size:18px;margin-right:6px">\ud83c\udf4f</span>'
    + '\ud83d\uded2 \u5df2\u9078\u597d\u300c' + name + '\u300d\uff01'
    + '\u8acb\u767b\u5165\u5f8c\u6309\u300c\u76f4\u63a5\u7d50\u5e33\u300d'
    + ' \u2014 <strong style="text-decoration:underline">\u9ede\u64ca\u95dc\u9589</strong>'
    + '</div>';
  return html.slice(0, be+1) + banner + html.slice(be+1);
}

function rewriteHtml(html, host, checkoutParams) {
  const proxyBase = getProxyBase(host);
  let result = html.replace(/https?:\/\/myship\.7-11\.com\.tw/g, proxyBase);

  // Inject beautify CSS after <head>
  const hi = result.indexOf('<head>');
  if (hi !== -1) {
    const pos = hi + '<head>'.length;
    result = result.slice(0, pos) + BEAUTIFY_CSS + '<base href="' + proxyBase + '/">' + result.slice(pos);
  }

  if (!checkoutParams) return result;

  const productName = PRODUCT_MAP[checkoutParams.carProduct]?.name || '';

  // 1. Static banner
  result = injectBanner(result, productName);

  // 2. Nuclear override CSS for banner visibility
  const nCSS = '<style id="sbf-nuclear">#sbf-banner{display:block!important;visibility:visible!important;opacity:1!important;position:fixed!important;top:0!important;left:0!important;z-index:2147483647!important;transform:none!important;clip:auto!important;clip-path:none!important;-webkit-clip-path:none!important}html,body{padding-top:60px!important}</style>';
  const hc = result.indexOf('</head>');
  if (hc !== -1) result = result.slice(0, hc) + nCSS + result.slice(hc);

  // 3. Alertify override
  const ao = '<script data-proxy="ao">(function(){var a=null;Object.defineProperty(window,"alertify",{configurable:true,get:function(){return a},set:function(v){a=v;if(v&&typeof v.alert==="function"){v.alert=function(m,fn){if(typeof fn==="function")fn();};}}});})();<\/script>';
  const hpos = result.indexOf('<head>');
  if (hpos !== -1) {
    const p2 = hpos + '<head>'.length;
    result = result.slice(0, p2) + ao + result.slice(p2);
  }

  // 4. Auto-fill JS
  const afJS = '<script data-proxy="af">(function(){'
    + 'var P=' + JSON.stringify(checkoutParams) + ';var d=false;'
    + 'function go(){if(d)return;d=true;'
    + 'var cp=document.querySelector("input[name=CarProduct]");'
    + 'var ci=document.querySelector("input[name=CarItem]");'
    + 'var cq=document.querySelector("input[name=CarQty]");'
    + 'var cm=document.querySelector("input[name=CarMinQty]");'
    + 'if(cp)cp.value=P.carProduct;if(ci)ci.value=P.carItem;'
    + 'if(cq)cq.value=P.carQty||"1";if(cm)cm.value=P.carMinQty||"1";'
    + 'document.querySelectorAll(".product_size_switch span").forEach(function(s){'
    + 'if(s.dataset.productId===P.carProduct&&s.dataset.specId===P.carItem&&!s.classList.contains("active"))s.click();'
    + '});'
    + 'try{localStorage.setItem("_sbf",JSON.stringify(P));}catch(e){}'
    + '}'
    + 'if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",go);else go();setTimeout(go,3000);'
    + '})();<\/script>';
  const bc = result.lastIndexOf('</body>');
  if (bc !== -1) result = result.slice(0, bc) + afJS + result.slice(bc);
  else result += afJS;

  return result;
}

export default async function handler(req, res) {
  const host = req.headers.host || req.headers['x-forwarded-host'] || 'localhost:3000';
  const urlObj = new URL(req.url, `https://${host}`);
  let pp = urlObj.pathname.replace(/^\/api\/ms\/?/, '');
  if (!pp) pp = '';
  const mu = MYSHIP_ORIGIN + (pp ? '/' + pp : '') + urlObj.search;

  const fh = {};
  const skip = ['host','connection','content-length','transfer-encoding','x-forwarded-for','x-forwarded-host','x-forwarded-proto'];
  for (const [k,v] of Object.entries(req.headers)) {
    if (!skip.includes(k.toLowerCase())) fh[k] = v;
  }
  fh['host'] = 'myship.7-11.com.tw';
  fh['origin'] = MYSHIP_ORIGIN;
  fh['referer'] = MYSHIP_ORIGIN + '/general/detail?id=GM2605018541234';
  fh['user-agent'] = fh['user-agent'] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';
  fh['accept'] = fh['accept'] || 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8';
  fh['accept-language'] = fh['accept-language'] || 'zh-TW,zh;q=0.9,en;q=0.8';

  try {
    const fo = { method: req.method, headers: fh, redirect: 'manual' };
    if (req.method !== 'GET' && req.method !== 'HEAD') {
      const chunks = [];
      for await (const chunk of req) chunks.push(chunk);
      if (chunks.length > 0) fo.body = Buffer.concat(chunks);
    }

    const mr = await fetch(mu, fo);

    if (mr.status === 403) {
      res.writeHead(200, {'Content-Type':'text/html;charset=utf-8'});
      res.end(getErrorPage('\u8ce3\u8ca8\u4fbf\u4f3a\u670d\u5668\u66ab\u6642\u7121\u6cd5\u5b58\u53d6'));
      return;
    }
    if ([301,302,303,307,308].includes(mr.status)) {
      res.writeHead(mr.status,{'Location':rewriteUrl(mr.headers.get('location')||'',host)});
      res.end();return;
    }

    const rh = {};
    for (const [k,v] of mr.headers.entries()) {
      const l = k.toLowerCase();
      if(l==='set-cookie'){rh['set-cookie']=Array.isArray(v)?v:[v].map(c=>rewriteSetCookie(c));}
      else if(l==='location'){rh['location']=rewriteUrl(v,host);}
      else if(!['transfer-encoding','content-encoding','content-length'].includes(l)){rh[k]=v;}
    }
    const ct = mr.headers.get('content-type')||'';

    if (ct.includes('text/html')) {
      let h = await mr.text();
      let cp=null;
      const cs=urlObj.searchParams.get('_checkout');
      if(cs){try{cp=JSON.parse(decodeURIComponent(cs));}catch(e){}}
      h=rewriteHtml(h,host,cp);
      rh['content-type']='text/html;charset=utf-8';
      res.writeHead(mr.status,rh);res.end(h);
    } else {
      if(mr.status===403||mr.status===404){
        if(ct.includes('css')){res.writeHead(200,{'Content-Type':'text/css'});res.end('/* */');}
        else if(ct.includes('javascript')){res.writeHead(200,{'Content-Type':'application/javascript'});res.end('//')}
        else if(ct.includes('image')){
          const g=Buffer.from('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7','base64');
          res.writeHead(200,{'Content-Type':'image/gif','Content-Length':g.length});res.end(g);
        } else {res.writeHead(200,{'Content-Type':ct||'application/octet-stream'});res.end('');}
        return;
      }
      res.writeHead(mr.status,rh);res.end(Buffer.from(await mr.arrayBuffer()));
    }
  } catch(err) {
    console.error('Proxy error:',err);
    res.writeHead(502,{'Content-Type':'text/html;charset=utf-8'});
    res.end(getErrorPage('\u9023\u7dda\u5931\u6557:'+err.message));
  }
}
