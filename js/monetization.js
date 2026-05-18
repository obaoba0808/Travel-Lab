// add-monetization.js - Travel Lab 变现组件
// Adds floating toolbar and in-article CTA blocks

(function() {
  // Skip toolbar on homepage
  const isHomepage = window.location.pathname === '/' || window.location.pathname === '/index.html' || window.location.pathname.endsWith('/index.html');
  const page = window.location.pathname;
  
  // === 1. FLOATING BOTTOM TOOLBAR ===
  if (!isHomepage) {
  const toolbar = document.createElement('div');
  toolbar.id = 'travel-toolbar';
  toolbar.innerHTML = `
    <div class="toolbar-inner">
      <a href="https://www.agoda.com/zh-tw/?tag=e9ea26c2-c046-468f-939d-97d11075d6e0" target="_blank" rel="noopener sponsored" class="toolbar-btn" data-affiliate="agoda">
        <span class="toolbar-icon">🏨</span>
        <span class="toolbar-label">订房优惠</span>
      </a>
      <a href="https://www.skyscanner.com.tw/" target="_blank" rel="noopener sponsored" class="toolbar-btn" data-affiliate="skyscanner">
        <span class="toolbar-icon">✈️</span>
        <span class="toolbar-label">比价机票</span>
      </a>
      <a href="https://www.klook.com/zh-TW/?dd_referrer=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Faffiliate%2F" target="_blank" rel="noopener sponsored" class="toolbar-btn" data-affiliate="klook">
        <span class="toolbar-icon">🎫</span>
        <span class="toolbar-label">景点门票</span>
      </a>
      <a href="https://www.airalo.com/" target="_blank" rel="noopener sponsored" class="toolbar-btn" data-affiliate="airalo">
        <span class="toolbar-icon">📱</span>
        <span class="toolbar-label">eSIM网卡</span>
      </a>
      <a href="https://tw.trip.com/sale/w/4823/flight-deals.html?locale=zh-TW&promo_referer=3952_4823_6&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078938" target="_blank" rel="noopener sponsored" class="toolbar-btn" data-affiliate="trip">
        <span class="toolbar-icon">🧳</span>
        <span class="toolbar-label">Trip.com</span>
      </a>
    </div>
  `;

  // Toolbar CSS
  const toolbarCSS = document.createElement('style');
  toolbarCSS.textContent = `
    #travel-toolbar {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 9999;
      background: rgba(15, 23, 42, 0.97);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-top: 1px solid rgba(255,255,255,0.08);
      transform: translateY(100%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 -4px 24px rgba(0,0,0,0.2);
    }
    #travel-toolbar.visible { transform: translateY(0); }
    .toolbar-inner {
      display: flex;
      justify-content: center;
      gap: 4px;
      max-width: 600px;
      margin: 0 auto;
      padding: 6px 12px;
    }
    .toolbar-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      padding: 8px 16px;
      border-radius: 10px;
      text-decoration: none;
      transition: background 0.2s, transform 0.15s;
      flex: 1;
      min-width: 0;
    }
    .toolbar-btn:hover { background: rgba(255,255,255,0.08); transform: translateY(-2px); }
    .toolbar-btn:active { transform: translateY(0); }
    .toolbar-icon { font-size: 20px; line-height: 1; }
    .toolbar-label { font-size: 11px; color: rgba(255,255,255,0.75); font-weight: 500; white-space: nowrap; letter-spacing: 0.3px; }
    .toolbar-btn:hover .toolbar-label { color: #fff; }

    /* In-article CTA block */
    .article-cta {
      background: linear-gradient(135deg, #f0fcfc 0%, #e8f8f8 100%);
      border: 2px solid #e0f7f7;
      border-radius: 18px;
      padding: 28px;
      margin: 36px 0;
    }
    .article-cta-title {
      font-size: 16px;
      font-weight: 700;
      color: #1a1a2e;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .article-cta-desc {
      font-size: 13px;
      color: #666;
      margin-bottom: 18px;
      line-height: 1.6;
    }
    .cta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 10px;
    }
    .cta-card {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 14px 16px;
      border-radius: 12px;
      text-decoration: none;
      transition: transform 0.2s, box-shadow 0.2s;
      border: 1.5px solid transparent;
    }
    .cta-card:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
    .cta-card-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      flex-shrink: 0;
    }
    .cta-card-text { font-size: 13px; font-weight: 600; }
    .cta-card-sub { font-size: 11px; color: #888; font-weight: 400; }

    .cta-agoda { background: #fff; border-color: #fde8d8; }
    .cta-agoda .cta-card-icon { background: linear-gradient(135deg, #f5a623, #e8941c); }
    .cta-agoda .cta-card-text { color: #e8941c; }

    .cta-skyscanner { background: #fff; border-color: #d6eef8; }
    .cta-skyscanner .cta-card-icon { background: linear-gradient(135deg, #00A2DF, #0090c8); }
    .cta-skyscanner .cta-card-text { color: #0090c8; }

    .cta-klook { background: #fff; border-color: #fde0e1; }
    .cta-klook .cta-card-icon { background: linear-gradient(135deg, #FF5A5F, #e04a4f); }
    .cta-klook .cta-card-text { color: #e04a4f; }

    .cta-airalo { background: #fff; border-color: #e0e0e0; }
    .cta-airalo .cta-card-icon { background: linear-gradient(135deg, #333, #222); }
    .cta-airalo .cta-card-text { color: #333; }
    .cta-trip { background: #fff; border-color: #cce5ff; }
    .cta-trip .cta-card-icon { background: linear-gradient(135deg, #0077cc, #005bb5); }
    .cta-trip .cta-card-text { color: #0077cc; }

    /* Package service CTA (for Taiwan pages) */
    .pkg-cta {
      background: linear-gradient(135deg, #0ABAB5 0%, #089693 100%);
      border-radius: 18px;
      padding: 28px;
      margin: 36px 0;
      text-align: center;
    }
    .pkg-cta h4 { color: #fff; font-size: 18px; font-weight: 700; margin-bottom: 8px; }
    .pkg-cta p { color: rgba(255,255,255,0.85); font-size: 14px; margin-bottom: 18px; }
    .pkg-cta .pkg-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #fff;
      color: #089693;
      padding: 12px 28px;
      border-radius: 30px;
      font-size: 15px;
      font-weight: 700;
      text-decoration: none;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .pkg-cta .pkg-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.2); }

    /* Responsive */
    @media (max-width: 480px) {
      .toolbar-inner { gap: 2px; padding: 4px 6px; }
      .toolbar-btn { padding: 6px 8px; }
      .toolbar-icon { font-size: 18px; }
      .toolbar-label { font-size: 10px; }
      .cta-grid { grid-template-columns: 1fr 1fr; }
      .article-cta { padding: 20px; }
    }
  `;
  document.head.appendChild(toolbarCSS);
  document.body.appendChild(toolbar);

  // Show toolbar after scrolling 300px
  let toolbarShown = false;
  const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting && !toolbarShown) {
        toolbar.classList.add('visible');
        toolbarShown = true;
      }
    });
  }, { threshold: 0 });
  const sentinel = document.querySelector('.site-topbar');
  if (sentinel) scrollObserver.observe(sentinel);
  // Fallback: show after 1s if still hidden
  setTimeout(() => { if (!toolbarShown) { toolbar.classList.add('visible'); toolbarShown = true; } }, 1500);
  } // end if (!isHomepage)

  // === 2. IN-ARTICLE CTA BLOCK ===
  const mainContent = document.querySelector('.content-area') || document.querySelector('.article-container');
  if (mainContent) {
    // Detect destination from page
    // page already defined at top of IIFE
    let destLabel = '';
    let destSearch = '';
    if (page.includes('japan') || page.includes('tokyo') || page.includes('kansai') || page.includes('hokkaido') || page.includes('okinawa') || page.includes('kyoto')) {
      destLabel = '日本';
      destSearch = 'Japan';
    } else if (page.includes('korea') || page.includes('seoul') || page.includes('busan') || page.includes('jeju')) {
      destLabel = '韩国';
      destSearch = 'Korea';
    } else if (page.includes('taiwan') || page.includes('hualien') || page.includes('tainan') || page.includes('kenting')) {
      destLabel = '台湾';
      destSearch = 'Taiwan';
    } else if (page.includes('southeast') || page.includes('chiang-mai') || page.includes('bangkok')) {
      destLabel = '东南亚';
      destSearch = 'Southeast Asia';
    }

    if (destLabel) {
      const ctaBlock = document.createElement('div');
      ctaBlock.className = 'article-cta';
      ctaBlock.innerHTML = `
        <div class="article-cta-title">🎒 ${destLabel}旅行实用工具</div>
        <div class="article-cta-desc">出发前先搞定这四件事，省时又省钱</div>
        <div class="cta-grid">
          <a href="https://www.agoda.com/zh-tw/search/${destSearch}?tag=e9ea26c2-c046-468f-939d-97d11075d6e0" target="_blank" rel="noopener sponsored" class="cta-card cta-agoda" data-affiliate="agoda">
            <div class="cta-card-icon">🏨</div>
            <div>
              <div class="cta-card-text">订酒店</div>
              <div class="cta-card-sub">Agoda 折扣</div>
            </div>
          </a>
          <a href="https://www.skyscanner.com.tw/" target="_blank" rel="noopener sponsored" class="cta-card cta-skyscanner" data-affiliate="skyscanner">
            <div class="cta-card-icon">✈️</div>
            <div>
              <div class="cta-card-text">比机票</div>
              <div class="cta-card-sub">Skyscanner</div>
            </div>
          </a>
          <a href="https://www.klook.com/zh-TW/search/results?keyword=${encodeURIComponent(destLabel)}&dd_referrer=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Faffiliate%2F" target="_blank" rel="noopener sponsored" class="cta-card cta-klook" data-affiliate="klook">
            <div class="cta-card-icon">🎫</div>
            <div>
              <div class="cta-card-text">买门票</div>
              <div class="cta-card-sub">Klook 立折</div>
            </div>
          </a>
          <a href="https://www.airalo.com/" target="_blank" rel="noopener sponsored" class="cta-card cta-airalo" data-affiliate="airalo">
            <div class="cta-card-icon">📱</div>
            <div>
              <div class="cta-card-text">买eSIM</div>
              <div class="cta-card-sub">免换卡上网</div>
            </div>
          </a>
          <a href="https://tw.trip.com/sale/w/4823/flight-deals.html?locale=zh-TW&promo_referer=3952_4823_6&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078938" target="_blank" rel="noopener sponsored" class="cta-card cta-trip" data-affiliate="trip">
            <div class="cta-card-icon">🧳</div>
            <div>
              <div class="cta-card-text">Trip.com</div>
              <div class="cta-card-sub">机票酒店特惠</div>
            </div>
          </a>
        </div>
      `;
      // Insert CTA after first 200px of content or after first h2
      const firstH2 = mainContent.querySelector('h2');
      if (firstH2) {
        firstH2.parentNode.insertBefore(ctaBlock, firstH2.nextSibling);
      } else {
        mainContent.appendChild(ctaBlock);
      }
    }
  }

  // === 3. PACKAGE SERVICE CTA (Taiwan pages only) ===
  if (mainContent && (page.includes('taiwan') || page.includes('hualien') || page.includes('tainan') || page.includes('kenting'))) {
    const pkgBlock = document.createElement('div');
    pkgBlock.className = 'pkg-cta';
    pkgBlock.innerHTML = `
      <h4>🚐 台湾包车服务</h4>
      <p>花东、垦丁、台南…专车接送，中文司机，行程自由安排</p>
      <a href="https://line.me/ti/g/NbNGnW4Eh6" target="_blank" rel="noopener" class="pkg-btn">
        💬 LINE 立即询价
      </a>
    `;
    // Insert near the end of content
    mainContent.appendChild(pkgBlock);
  }

  // === 4. TRIP.COM PROMO BANNER (now embedded directly in HTML, no JS injection needed) ===
  /* REMOVED - banners are now hardcoded in each HTML page */
  if (false) { const tripBanners = {
    japan:   { img: 'images/trip-japan.webp', alt: 'Trip.com 日本旅遊優惠', link: 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n' },
    tokyo:   { img: 'images/trip-japan.webp', alt: 'Trip.com 東京機票酒店優惠', link: 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n' },
    kansai:  { img: 'images/trip-japan.webp', alt: 'Trip.com 關西機票酒店優惠', link: 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n' },
    hokkaido:{ img: 'images/trip-japan.webp', alt: 'Trip.com 北海道機票酒店優惠', link: 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n' },
    okinawa: { img: 'images/trip-okinawa.webp', alt: 'Trip.com 快閃沖繩 機+酒折$1000', link: 'https://tw.trip.com/sale/w/17859/okinawapromotion.html?locale=zh-TW&promo_referer=3952_17859_2&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011395' },
    kyoto:   { img: 'images/trip-japan.webp', alt: 'Trip.com 京都機票酒店優惠', link: 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n' },
    osaka:   { img: 'images/trip-japan.webp', alt: 'Trip.com 大阪機票酒店優惠', link: 'https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n' },
    korea:   { img: 'images/trip-korea.webp', alt: 'Trip.com 暢遊韓國五折起', link: 'https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353' },
    seoul:   { img: 'images/trip-korea.webp', alt: 'Trip.com 首爾機票酒店優惠', link: 'https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353' },
    busan:   { img: 'images/trip-busan.webp', alt: 'Trip.com 釜山遊 機+酒$999起', link: 'https://tw.trip.com/sale/w/31376/superbusan-promotion.html?locale=zh-TW&promo_referer=3952_31376_3&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011416' },
    jeju:    { img: 'images/trip-korea.webp', alt: 'Trip.com 濟州島機票酒店優惠', link: 'https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&promo_referer=3952_4337_8&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011353' },
    taiwan:  { img: 'images/trip-taiwan.webp', alt: 'Trip.com 台灣飯店五折起', link: 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507' },
    hualien: { img: 'images/trip-taiwan.webp', alt: 'Trip.com 台灣飯店五折起', link: 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507' },
    tainan:  { img: 'images/trip-taiwan.webp', alt: 'Trip.com 台灣飯店五折起', link: 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507' },
    kenting: { img: 'images/trip-taiwan.webp', alt: 'Trip.com 台灣飯店五折起', link: 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507' },
    taipei:  { img: 'images/trip-taiwan.webp', alt: 'Trip.com 台灣飯店五折起', link: 'https://tw.trip.com/sale/w/4823/hotel-deals.html?locale=zh-TW&promo_referer=3952_4823_11&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17011507' },
    chiangmai:{ img: 'images/trip-thailand.webp', alt: 'Trip.com 泰國五折優惠', link: 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987' },
    bangkok: { img: 'images/trip-thailand.webp', alt: 'Trip.com 曼谷五折優惠', link: 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987' },
    southeast:{ img: 'images/trip-thailand.webp', alt: 'Trip.com 東南亞機票優惠', link: 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987' },
    vietnam: { img: 'images/trip-thailand.webp', alt: 'Trip.com 東南亞機票優惠', link: 'https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987' },
    hongkong:{ img: 'images/trip-hongkong.webp', alt: 'Trip.com 港澳快閃優惠', link: '#' },
  }; }

  // Add padding to body bottom for toolbar (only on non-homepage pages)
  if (!isHomepage) {
    document.body.style.paddingBottom = '64px';
  }
})();
