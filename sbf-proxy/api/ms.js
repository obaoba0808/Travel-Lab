// sbf-proxy: Beautiful wrapper page + reverse proxy for myship.7-11.com.tw
// Strategy: Show our own beautiful landing page with iframe for myshop content
// This avoids all CSS/JS 403 issues from myship's static resources

const MYSHIP_ORIGIN = 'https://myship.7-11.com.tw';

export const config = {
  api: {
    bodyParser: false,
    responseLimit: false,
  },
};

const PRODUCT_MAP = {
  '2605021152246963': { specId: '2605021152246964', name: '\u611b\u6587\u8292\u679c\u6c34\u679c\u79ae\u76d2', price: 1380, origPrice: 1680, emoji: '\ud83c\udf51' },
  '2605011150175300': { specId: '2605011150175301', name: '\u91d1\u9e3d\u9cf3\u68a8\u79ae\u76d2', price: 799, origPrice: 999, emoji: '\ud83e\uded5' },
  '2605021152260362': { specId: '2605021152260363', name: '\u5de8\u5cf0\u8461\u8404\u6c34\u679c\u79ae\u76d2', price: 1280, origPrice: 1580, emoji: '\ud83c\udf47' },
  '2605021152270007': { specId: '2605021152270008', name: '\u6afb\u6843\u6c34\u679c\u79ae\u76d2', price: 1280, origPrice: 1580, emoji: '\ud83e\udd52' },
  '2605021152272368': { specId: '2605021152272369', name: '\u6c34\u871c\u6843\u6c34\u679c\u79ae\u76d2', price: 1280, origPrice: 1580, emoji: '\ud83e\udd51' },
  '2605021152278900': { specId: '2605021152278901', name: '\u69b4\u69e3\u6c34\u679c\u79ae\u76d2', price: 1980, origPrice: 2380, emoji: '\ud83e\uded6' },
  '2605021152287723': { specId: '2605021152287724', name: '\u6a19\u6e96\u6c34\u679c\u7b31', price: 999, origPrice: 1280, emoji: '\ud83c\udf4e' },
  '2605021152293023': { specId: '2605021152293024', name: '\u8c6a\u83ef\u7b31', price: 1680, origPrice: 1980, emoji: '\ud83c\udf4e' },
};

function getLandingPage(host, checkoutParams) {
  const p = checkoutParams ? PRODUCT_MAP[checkoutParams.carProduct] : null;
  const pn = p ? p.name.replace(/</g,'&lt;').replace(/>/g,'&gt;') : '\u5546\u54c1';
  const pe = p ? p.emoji : '\ud83c\udf4f';
  const pp = p ? p.price : 0;
  const po = p ? p.origPrice : 0;
  const cp = checkoutParams ? JSON.stringify(checkoutParams).replace(/"/g,'&quot;') : '';
  const iframeSrc = `https://${host}/api/ms/general/detail?id=GM2605018541234` +
    (checkoutParams ? '&_checkout=' + encodeURIComponent(JSON.stringify(checkoutParams)) : '');

  return `<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>\u7206\u751c\u6c34\u679c\u92ea | \u8ce3\u8ca8\u4fbf\u4e0b\u55ae</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --primary:#ff7043;--primary-dark:#e64a19;--primary-light:#ffab91;
  --accent:#ffb74d;--bg:#fff8f3;--card:#ffffff;
  --text:#333;--text-light:#666;--text-muted:#999;
  --radius:16px;--shadow:0 4px 24px rgba(230,74,25,0.12);
  --shadow-hover:0 8px 40px rgba(230,74,25,0.20)
}
body{font-family:'Noto Sans TC',-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}

/* ===== TOP BANNER ===== */
.top-banner{
  background:linear-gradient(135deg,#ff7043 0%,#ffb74d 100%);
  color:#fff;text-align:center;padding:18px 24px;font-size:15px;font-weight:700;
  position:sticky;top:0;z-index:100;box-shadow:0 4px 20px rgba(255,112,67,0.35);
  display:flex;align-items:center;justify-content:center;gap:10px
}
.top-banner .emoji{font-size:24px}
.top-banner .close-btn{margin-left:auto;background:rgba(255,255,255,0.25);border:none;color:#fff;
  width:28px;height:28px;border-radius:50%;cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center}
.top-banner .close-btn:hover{background:rgba(255,255,255,0.4)}

/* ===== HERO ===== */
.hero{text-align:center;padding:48px 24px 36px;background:linear-gradient(180deg,var(--bg) 0%,#fff 100%)}
.hero-icon{font-size:64px;margin-bottom:16px;animation:bounce 2s ease infinite}
@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.hero h1{font-size:32px;font-weight:900;color:var(--primary-dark);margin-bottom:8px}
.hero h1 span{color:var(--primary)}
.hero p{font-size:16px;color:var(--text-light);max-width:520px;margin:0 auto}

/* ===== PRODUCT CARD ===== */
.product-section{max-width:600px;margin:0 auto;padding:0 20px 32px}
.prod-card{
  background:var(--card);border-radius:var(--radius);padding:28px;
  box-shadow:var(--shadow);border:2px solid var(--primary-light);
  text-align:center;position:relative;overflow:hidden
}
.prod-card::before{content:'';position:absolute;top:-40px;right:-40px;width:120px;height:120px;
  background:radial-gradient(circle,var(--primary-light) 0%,transparent 70%);opacity:0.5;border-radius:50%}
.prod-badge{
  position:absolute;top:16px;left:16px;background:linear-gradient(135deg,var(--primary),var(--accent));
  color:#fff;padding:6px 16px;border-radius:20px;font-size:13px;font-weight:700;z-index:1
}
.prod-emoji{font-size:56px;margin-bottom:12px;position:relative}
.prod-name{font-size:20px;font-weight:800;color:var(--text);margin-bottom:16px;position:relative}
.prod-price-wrap{margin-bottom:24px;position:relative}
.prod-price{font-size:42px;font-weight:900;color:var(--primary-dark)}
.prod-price small{font-size:16px;font-weight:700}
.prod-original{font-size:18px;color:var(--text-muted);text-decoration:line-through;margin-left:8px}
.prod-savings{
  display:inline-block;background:linear-gradient(135deg,#4caf50,#81c784);color:#fff;
  padding:4px 14px;border-radius:12px;font-size:13px;font-weight:700;margin-top:8px
}

/* ===== CTA BUTTONS ===== */
.cta-group{display:flex;flex-direction:column;gap:12px;position:relative}
.btn-primary{
  display:block;width:100%;padding:16px 32px;border:none;border-radius:30px;
  font-size:17px;font-weight:800;cursor:pointer;transition:all 0.3s;
  font-family:inherit;text-align:center;text-decoration:none
}
.btn-orange{background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;box-shadow:0 4px 16px rgba(255,112,67,0.35)}
.btn-orange:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(255,112,67,0.45)}
.btn-outline{
  background:transparent;color:var(--primary);border:2.5px solid var(--primary);
  padding:14px 32px
}
.btn-outline:hover{background:var(--primary);color:#fff}

/* ===== STEPS ===== */
.steps{max-width:700px;margin:0 auto;padding:0 20px 48px}
.steps h2{font-size:22px;font-weight:800;text-align:center;color:var(--text);margin-bottom:24px}
.step-list{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.step-item{
  flex:1;min-width:160px;max-width:200px;background:var(--card);
  border-radius:var(--radius);padding:24px 16px;text-align:center;
  box-shadow:var(--shadow);transition:transform 0.3s
}
.step-item:hover{transform:translateY(-4px)}
.step-num{
  width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,var(--primary),var(--accent));
  color:#fff;font-size:20px;font-weight:900;display:flex;align-items:center;
  justify-content:center;margin:0 auto 12px
}
.step-title{font-size:15px;font-weight:700;color:var(--text);margin-bottom:6px}
.step-desc{font-size:13px;color:var(--text-muted);line-height:1.5}

/* ===== TRUST BADGES ===== */
.trust{max-width:600px;margin:0 auto;padding:0 20px 48px;text-align:center}
.trust h3{font-size:16px;font-weight:700;color:var(--text-muted);margin-bottom:16px}
.badges{display:flex;gap:20px;justify-content:center;flex-wrap:wrap}
.badge{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text-light)}
.badge-icon{font-size:24px}

/* ===== FOOTER ===== */
.footer{text-align:center;padding:24px;color:var(--text-muted);font-size:13px;border-top:1px solid #eee;background:#fff}

/* ===== IFRAME HIDDEN ===== */
#iframe-container{display:none}

/* ===== RESPONSIVE ===== */
@media(max-width:600px){
  .hero h1{font-size:24px}.prod-price{font-size:34px}
  .step-list{flex-direction:column;align-items:center}
  .step-item{max-width:280px}.top-banner{font-size:13px;padding:14px 16px}
  .top-banner .emoji{font-size:20px}
}
</style>
</head>
<body>

<!-- Top Banner -->
<div class="top-banner" id="topBanner">
  <span class="emoji">${pe}</span>
  <span>\ud83d\uded2 \u5df2\u9078\u64c7\u300c${pn}\u300d</span>
  <span style="opacity:0.85;font-weight:400">| NT$${pp}</span>
  <button class="close-btn" onclick="document.getElementById('topBanner').style.display='none'">\u2715</button>
</div>

<!-- Hero -->
<div class="hero">
  <div class="hero-icon">${pe}</div>
  <h1>\u7206\u751c\u6c34\u679c\u92ea <span>| 7-11 \u8ce3\u8ca8\u4fbf</span></h1>
  <p>\u53f0\u7063\u65b0\u9bae\u6c34\u679c\uff0c5\u5206\u9418\u5b8c\u6210\u4e0b\u55ae<br>\u5168\u53f0 7-11 \u8d85\u5546\u53d6\u8ca8\u4ed8\u6b3e</p>
</div>

<!-- Product Card -->
<div class="product-section">
  <div class="prod-card">
    <div class="prod-badge">\u71b1\u92b7\u4e2d</div>
    <div class="prod-emoji">${pe}</div>
    <div class="prod-name">${pn}</div>
    <div class="prod-price-wrap">
      <div class="prod-price"><small>NT$</small>${pp}</div>
      ${po > pp ? `<div class="prod-original">NT$${po}</div><div class="prod-savings">\u7701 NT$${po - pp} (${Math.round((1-pp/po)*100)}%OFF)</div>` : ''}
    </div>
    <div class="cta-group">
      <a href="${iframeSrc}" target="_blank" class="btn-primary btn-orange"
         onclick="this.innerHTML='\u26a1 \u6b63\u5728\u958b\u555f\u8ce3\u8ca8\u4fbf...'">
        \ud83d\uded2 \u524d\u5f80\u8ce3\u8ca8\u4fbf\u4e0b\u55ae &rarr;
      </a>
      <a href="https://line.me/ti/p/@sweetburst" target="_blank" class="btn-primary btn-outline">
        \ud83d\udc47 LINE \u79c1\u8a0a\u8a62\u554f
      </a>
    </div>
  </div>
</div>

<!-- Steps -->
<div class="steps">
  <h2>\ud83d\ude80 \u4e09\u6b65\u5b8c\u6210\u4e0b\u55ae</h2>
  <div class="step-list">
    <div class="step-item">
      <div class="step-num">1</div>
      <div class="step-title">\u9078\u64c7\u5546\u54c1</div>
      <div class="step-desc">\u5728\u672c\u9ef4\u9ede\u64ca\u4e0b\u55ae\u6309\u9215</div>
    </div>
    <div class="step-item">
      <div class="step-num">2</div>
      <div class="step-title">LINE/FB \u767b\u5165</div>
      <div class="step-desc">\u8df3\u8f49\u81f3\u8ce3\u8ca8\u4fbf\u5feb\u901f\u767b\u5165</div>
    </div>
    <div class="step-item">
      <div class="step-num">3</div>
      <div class="step-title">7-11 \u53d6\u8ca8</div>
      <div class="step-desc">\u9078\u64c7\u9644\u8fd1\u8d85\u5546\u53d6\u8ca8\u4ed8\u6b3e</div>
    </div>
  </div>
</div>

<!-- Trust -->
<div class="trust">
  <h3>\u70ba\u4ec0\u9ebc\u9078\u64c7\u7206\u751c\u6c34\u679c\u92ea</h3>
  <div class="badges">
    <div class="badge"><span class="badge-icon">\ud83c\udf51</span> \u53f0\u7063\u7522\u5730\u76f4\u9001</div>
    <div class="badge"><span class="badge-icon">\u2705</span> \u65b0\u9bae\u4fdd\u8b49</div>
    <div class="badge"><span class="badge-icon">\ud83d\ude9b</span> \u5168\u53f0 7-11 \u53d6\u8ca8</div>
    <div class="badge"><span class="badge-icon">\ud83d\udcb8</span> \u8ca8\u5230\u518d\u4ed8\u6b3e</div>
  </div>
</div>

<!-- Footer -->
<div class="footer">
  <p>\u7206\u751c\u6c34\u679c\u92ea Sweet Burst Fruits &copy; 2026</p>
  <p style="margin-top:4px;font-size:12px">\u672c\u9ef4\u975e 7-11 \u5b98\u65b9\u7db2\u7ad9\uff0c\u63d0\u4f9b\u8ce3\u8ca8\u4fbf\u5feb\u901f\u4e0b\u55ae\u5165\u53e3</p>
</div>

<!-- Hidden data -->
<div id="sbf-data" data-checkout="${cp}" style="display:none"></div>

</body>
</html>`;
}

function getProxyBase(host) { return `https://${host}/api/ms`; }
function rewriteUrl(url, host) { return url ? url.replace(MYSHIP_ORIGIN, getProxyBase(host)) : url; }
function rewriteSetCookie(s) { return s.replace(/;\s*Domain=[^;]+/gi, ''); }

export default async function handler(req, res) {
  const host = req.headers.host || req.headers['x-forwarded-host'] || 'localhost:3000';
  const urlObj = new URL(req.url, `https://${host}`);
  let pathPart = urlObj.pathname.replace(/^\/api\/ms\/?/, '') || '';

  // If this is the main shop detail page with _checkout param → show landing page
  if ((pathPart === '' || pathPart === 'general/detail') && urlObj.searchParams.get('_checkout')) {
    let cp = null;
    try { cp = JSON.parse(decodeURIComponent(urlObj.searchParams.get('_checkout'))); } catch(e) {}
    res.writeHead(200, {'Content-Type':'text/html;charset=utf-8'});
    res.end(getLandingPage(host, cp));
    return;
  }

  // Also show landing for bare shop detail visits
  if (pathPart === '' || pathPart === 'general/detail') {
    res.writeHead(200, {'Content-Type':'text/html;charset=utf-8'});
    res.end(getLandingPage(host, null));
    return;
  }

  // All other requests: proxy to myship
  const targetUrl = MYSHIP_ORIGIN + (pathPart ? '/' + pathPart : '') + urlObj.search;

  const fwdHeaders = {};
  const skip = ['host','connection','content-length','transfer-encoding','x-forwarded-for','x-forwarded-host','x-forwarded-proto'];
  for (const [k,v] of Object.entries(req.headers)) {
    if (!skip.includes(k.toLowerCase())) fwdHeaders[k] = v;
  }
  fwdHeaders['host'] = 'myship.7-11.com.tw';
  fwdHeaders['origin'] = MYSHIP_ORIGIN;
  fwdHeaders['referer'] = MYSHIP_ORIGIN + '/general/detail?id=GM2605018541234';
  fwdHeaders['user-agent'] = fwdHeaders['user-agent'] || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36';
  fwdHeaders['accept'] = fwdHeaders['accept'] || '*/*';
  fwdHeaders['accept-language'] = fwdHeaders['accept-language'] || 'zh-TW,zh;q=0.9,en;q=0.8';

  try {
    const fetchOpts = { method: req.method, headers: fwdHeaders, redirect: 'manual' };
    if (req.method !== 'GET' && req.method !== 'HEAD') {
      const chunks = [];
      for await (const chunk of req) chunks.push(chunk);
      if (chunks.length > 0) fetchOpts.body = Buffer.concat(chunks);
    }

    const myshipRes = await fetch(targetUrl, fetchOpts);

    // Handle redirects
    if ([301,302,303,307,308].includes(myshipRes.status)) {
      const loc = myshipRes.headers.get('location') || '';
      res.writeHead(myshipRes.status, { 'Location': rewriteUrl(loc, host) });
      res.end();
      return;
    }

    // Build response headers
    const respHeaders = {};
    for (const [k,v] of myshipRes.headers.entries()) {
      const kl = k.toLowerCase();
      if (kl === 'set-cookie') {
        respHeaders['set-cookie'] = Array.isArray(v) ? v : [v].map(c => rewriteSetCookie(c));
      } else if (kl === 'location') {
        respHeaders['location'] = rewriteUrl(v, host);
      } else if (!['transfer-encoding','content-encoding','content-length'].includes(kl)) {
        respHeaders[k] = v;
      }
    }

    const ct = myshipRes.headers.get('content-type') || '';

    // HTML responses: rewrite URLs
    if (ct.includes('text/html')) {
      let html = await myshipRes.text();

      // Parse checkout params for auto-fill injection
      let checkoutParams = null;
      const csParam = urlObj.searchParams.get('_checkout');
      if (csParam) {
        try { checkoutParams = JSON.parse(decodeURIComponent(csParam)); } catch(e) {}
      }

      // Rewrite all myship URLs to proxy
      let result = html.replace(/https?:\/\/myship\.7-11\.com\.tw/g, getProxyBase(host));

      // Inject base tag
      const headIdx = result.indexOf('<head>');
      if (headIdx !== -1) {
        const pos = headIdx + '<head>'.length;
        result = result.slice(0, pos) +
          '<base href="' + getProxyBase(host) + '/">' +
          result.slice(pos);
      }

      // Auto-fill JS injection for form fields
      if (checkoutParams) {
        const afScript = '<script data-proxy="af">(function(){'
          + 'var P=' + JSON.stringify(checkoutParams) + ';var done=false;'
          + 'function go(){if(done)return;done=true;'
          + 'var f=document.querySelector("input[name=CarProduct]");'
          + 'if(f)f.value=P.carProduct;'
          + 'f=document.querySelector("input[name=CarItem]");if(f)f.value=P.carItem;'
          + 'f=document.querySelector("input[name=CarQty]");if(f)f.value=(P.carQty||"1");'
          + 'f=document.querySelector("input[name=CarMinQty]");if(f)f.value=(P.carMinQty||"1");'
          + '}'
          + 'if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",go);else go();setTimeout(go,3000);'
          + '})()<\/script>';
        const bodyClose = result.lastIndexOf('</body>');
        if (bodyClose !== -1) {
          result = result.slice(0, bodyClose) + afScript + result.slice(bodyClose);
        } else {
          result += afScript;
        }
      }

      respHeaders['content-type'] = 'text/html;charset=utf-8';
      res.writeHead(myshipRes.status, respHeaders);
      res.end(result);
      return;
    }

    // Non-HTML resources: handle 403 gracefully
    if (myshipRes.status === 403 || myshipRes.status === 404) {
      if (ct.includes('css')) {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.end('/* */');
      } else if (ct.includes('javascript')) {
        res.writeHead(200, { 'Content-Type': 'application/javascript' });
        res.end('//');
      } else if (ct.includes('image')) {
        const px = Buffer.from('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7', 'base64');
        res.writeHead(200, { 'Content-Type': 'image/gif', 'Content-Length': px.length });
        res.end(px);
      } else {
        res.writeHead(200, { 'Content-Type': ct || 'application/octet-stream' });
        res.end('');
      }
      return;
    }

    // Pass through other responses
    res.writeHead(myshipRes.status, respHeaders);
    res.end(Buffer.from(await myshipRes.arrayBuffer()));

  } catch(err) {
    console.error('Proxy error:', err);
    res.writeHead(502, { 'Content-Type': 'text/html;charset=utf-8' });
    res.end(getLandingPage(host, null).replace(
      '\u7206\u751c\u6c34\u679c\u92ea',
      '\u26a0\ufe0f \u9023\u7dda\u6642\u9593: ' + err.message
    ));
  }
}
