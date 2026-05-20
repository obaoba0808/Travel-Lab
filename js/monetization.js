// add-monetization.js - Travel Lab 聯盟行銷工具
// Adds floating toolbar and in-article CTA blocks

(function() {
  // Skip toolbar on homepage
  const isHomepage = window.location.pathname === '/' || window.location.pathname === '/index.html' || window.location.pathname.endsWith('/index.html');
  const page = window.location.pathname;
  
  // === 1. FLOATING BOTTOM TOOLBAR ===
  if (!isHomepage) {
  const toolbar = document.createElement('div');
  toolbar.id = 'travel-toolbar';
  
  // Toolbar HTML
  toolbar.innerHTML = `
    <div class="toolbar-inner">
      <a href="https://www.trip.com/t/KzJgDXR8mU2" target="_blank" rel="noopener sponsored" data-affiliate="tripcom-hotel" class="toolbar-item">
        <span class="tb-icon">🏨</span>
        <span class="tb-label">飯店比價</span>
      </a>
      <a href="https://www.trip.com/t/FBEyG4BCmU2" target="_blank" rel="noopener sponsored" data-affiliate="tripcom-flight" class="toolbar-item">
        <span class="tb-icon">✈️</span>
        <span class="tb-label">機票比價</span>
      </a>
      <a href="https://www.trip.com/t/wbFhPgGCmU2" target="_blank" rel="noopener sponsored" data-affiliate="tripcom-activity" class="toolbar-item">
        <span class="tb-icon">🎫</span>
        <span class="tb-label">當地體驗</span>
      </a>
      <a href="https://www.trip.com/t/VDqCdSyBmU2" target="_blank" rel="noopener sponsored" data-affiliate="tripcom-transfer" class="toolbar-item">
        <span class="tb-icon">🚐</span>
        <span class="tb-label">機場接送</span>
      </a>
      <a href="https://www.trip.com.tw/?Allianceid=8237671&SID=312406690" target="_blank" rel="noopener sponsored" data-affiliate="tripcom" class="toolbar-item">
        <span class="tb-icon">🌏</span>
        <span class="tb-label">Trip.com</span>
      </a>
    </div>
  `;
  
  // Insert into page
  const body = document.body;
  if (body) body.appendChild(toolbar);
  }
  
  // === 2. IN-ARTICLE CTA BLOCKS ===
  // Only insert on article pages (not homepage, not tools/contact/about)
  const articleContainer = document.querySelector('.article-container') || document.querySelector('.col-center') || document.querySelector('.site-content');
  
  if (articleContainer && !isHomepage) {
    
    // Detect destination from page
    let destLabel = '';
    let destSearch = '';
    if (page.includes('japan') || page.includes('tokyo') || page.includes('kansai') || page.includes('hokkaido') || page.includes('okinawa') || page.includes('kyoto')) {
      destLabel = '日本';
      destSearch = 'Japan';
    } else if (page.includes('korea') || page.includes('seoul') || page.includes('busan') || page.includes('jeju')) {
      destLabel = '韓國';
      destSearch = 'Korea';
    } else if (page.includes('taiwan') || page.includes('hualien') || page.includes('tainan') || page.includes('kenting')) {
      destLabel = '台灣';
      destSearch = 'Taiwan';
    } else if (page.includes('southeast') || page.includes('chiang-mai') || page.includes('bangkok')) {
      destLabel = '東南亞';
      destSearch = 'Southeast Asia';
    }

    if (destLabel) {
      const ctaBlock = document.createElement('div');
      ctaBlock.className = 'article-cta';
      ctaBlock.innerHTML = `
        <div class="article-cta-title">📍 ${destLabel}旅遊推薦工具</div>
        <div class="article-cta-desc">預訂以下行程服務，享受最優惠價格與專屬折扣</div>
        <div class="cta-grid">
          <a href="https://www.trip.com/t/KzJgDXR8mU2" target="_blank" rel="noopener sponsored" class="cta-card cta-agoda" data-affiliate="tripcom-hotel">
            <div class="cta-card-icon">🏨</div>
            <div>
              <div class="cta-card-text">飯店住宿</div>
              <div class="cta-card-sub">TRIP 比價</div>
            </div>
          </a>
          <a href="https://www.trip.com/t/FBEyG4BCmU2" target="_blank" rel="noopener sponsored" class="cta-card cta-skyscanner" data-affiliate="tripcom-flight">
            <div class="cta-card-icon">✈️</div>
            <div>
              <div class="cta-card-text">機票比價</div>
              <div class="cta-card-sub">TRIP 比價</div>
            </div>
          </a>
          <a href="https://www.trip.com/t/wbFhPgGCmU2" target="_blank" rel="noopener sponsored" class="cta-card cta-klook" data-affiliate="tripcom-activity">
            <div class="cta-card-icon">🎫</div>
            <div>
              <div class="cta-card-text">當地體驗</div>
              <div class="cta-card-sub">TRIP 預訂</div>
            </div>
          </a>
          <a href="https://www.trip.com/t/VDqCdSyBmU2" target="_blank" rel="noopener sponsored" class="cta-card cta-esim" data-affiliate="tripcom-transfer">
            <div class="cta-card-icon">🚐</div>
            <div>
              <div class="cta-card-text">機場接送</div>
              <div class="cta-card-sub">TRIP 預訂</div>
            </div>
          </a>
        </div>
      `;
      
      // Insert AFTER related-posts (user request 2026-05-19)
      // Priority: related-posts > FAQ section > fallback
      const relatedPosts = document.querySelector('.related-posts');
      const faqSection = document.querySelector('.faq-section') || document.querySelector('.faq-accordion-beautify') || articleContainer.querySelector('.faq-section') || articleContainer.querySelector('.faq-accordion-beautify');
      if (relatedPosts) {
        relatedPosts.after(ctaBlock);
      } else if (faqSection) {
        faqSection.after(ctaBlock);
      } else {
        // Fallback: insert after first day-card or after first 3 paragraphs
        const dayCard = articleContainer.querySelector('.day-card');
        const ps = articleContainer.querySelectorAll('p');
        if (dayCard && dayCard.nextElementSibling) {
          dayCard.parentNode.insertBefore(ctaBlock, dayCard.nextElementSibling);
        } else if (ps.length >= 3) {
          ps[2].parentNode.insertBefore(ctaBlock, ps[2].nextSibling);
        } else {
          articleContainer.appendChild(ctaBlock);
        }
      }
    }
    
    // === 3. TAIWAN CAR CHARTER CTA ===
    // Show on Taiwan-related pages only
    if (page.includes('taiwan') || page.includes('hualien') || page.includes('tainan') || page.includes('kenting')) {
      const carCta = document.createElement('div');
      carCta.className = 'car-cta-block';
      carCta.innerHTML = `
        <div class="car-cta-inner">
          <div class="car-cta-icon">🚐</div>
          <div class="car-cta-body">
            <div class="car-cta-title">台灣包車服務 · 一日遊專車接送</div>
            <div class="car-cta-desc">花東、墾丁、台南等地區，司機導覽、客製化行程，出發前報價無隱藏費用</div>
          </div>
          <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener" class="car-cta-btn">LINE 立即詢問</a>
        </div>
      `;
      
      articleContainer.appendChild(carCta);
    }
  }

  // === 4. TRIP.COM PROMO BANNER ===
  // Auto-insert destination-specific Trip.com DYNAMIC banners
  function insertTripBanner() {
    const container = document.querySelector('.article-container') || document.querySelector('.col-center');
    if (!container) return;
    
    // Destination → Trip.com dynamic banner ID mapping (user provided 2026-05-20)
    const bannerConfig = {
      'tokyo':       { id: 'DB17161314', w: 468, h: 60 },
      'osaka':       { id: 'DB17161349', w: 468, h: 60 },
      'kyoto':       { id: 'DB17161349', w: 468, h: 60 },
      'kansai':      { id: 'DB17161349', w: 468, h: 60 },
      'hokkaido':    { id: 'DB17161468', w: 468, h: 60 },
      'sapporo':     { id: 'DB17161468', w: 468, h: 60 },
      'okinawa':     { id: 'DB17161314', w: 468, h: 60 },
      'japan':       { id: 'DB17161314', w: 468, h: 60 },
      'seoul':       { id: 'DB17161370', w: 468, h: 60 },
      'busan':       { id: 'DB17161545', w: 468, h: 60 },
      'jeju':        { id: 'DB17161370', w: 468, h: 60 },
      'korea':       { id: 'DB17161370', w: 468, h: 60 },
      'chiang-mai':  { id: 'DB17161559', w: 468, h: 60 },
      'bangkok':     { id: 'DB17161132', w: 468, h: 60 },
      'thailand':    { id: 'DB17161132', w: 468, h: 60 },
      'taipei':      { id: 'DB17138130', w: 728, h: 90 },
      'taiwan':      { id: 'DB17138130', w: 728, h: 90 },
      'hualien':     { id: 'DB17138130', w: 728, h: 90 },
      'tainan':      { id: 'DB17138130', w: 728, h: 90 },
      'kenting':     { id: 'DB17138130', w: 728, h: 90 },
      'jiufen':      { id: 'DB17138130', w: 728, h: 90 },
      'hongkong':    { id: 'DB17165486', w: 468, h: 60 },
      'vietnam':     { id: 'DB17165612', w: 468, h: 60 },
      'danang':      { id: 'DB17165612', w: 468, h: 60 },
      'hanoi':       { id: 'DB17165710', w: 468, h: 60 }
    };
    
    // Detect destination from page path (priority: specific > general)
    let matchedConfig = null;
    const pageLower = page.toLowerCase();
    
    if (pageLower.includes('busan')) {
      matchedConfig = bannerConfig['busan'];
    } else if (pageLower.includes('hongkong')) {
      matchedConfig = bannerConfig['hongkong'];
    } else if (pageLower.includes('hanoi')) {
      matchedConfig = bannerConfig['hanoi'];
    } else if (pageLower.includes('seoul') || pageLower.includes('jeju')) {
      matchedConfig = bannerConfig['seoul'];
    } else if (pageLower.includes('bangkok') || pageLower.includes('thailand')) {
      matchedConfig = bannerConfig['bangkok'];
    } else if (pageLower.includes('chiang-mai')) {
      matchedConfig = bannerConfig['chiang-mai'];
    } else if (pageLower.includes('tokyo') || pageLower.includes('osaka') || pageLower.includes('kyoto') || pageLower.includes('kansai') || pageLower.includes('hokkaido') || pageLower.includes('sapporo') || pageLower.includes('okinawa')) {
      // Match specific city first, fallback to japan
      if (pageLower.includes('tokyo'))    matchedConfig = bannerConfig['tokyo'];
      else if (pageLower.includes('osaka'))   matchedConfig = bannerConfig['osaka'];
      else if (pageLower.includes('kyoto'))   matchedConfig = bannerConfig['kyoto'];
      else if (pageLower.includes('kansai'))  matchedConfig = bannerConfig['kansai'];
      else if (pageLower.includes('hokkaido') || pageLower.includes('sapporo')) matchedConfig = bannerConfig['hokkaido'];
      else if (pageLower.includes('okinawa')) matchedConfig = bannerConfig['okinawa'];
      else                                 matchedConfig = bannerConfig['japan'];
    } else if (pageLower.includes('taipei') || pageLower.includes('taiwan') || pageLower.includes('hualien') || pageLower.includes('tainan') || pageLower.includes('kenting') || pageLower.includes('jiufen')) {
      matchedConfig = bannerConfig['taiwan'];
    } else if (pageLower.includes('vietnam') || pageLower.includes('danang')) {
      matchedConfig = bannerConfig['vietnam'];
    }
    
    if (matchedConfig) {
      const iframeHtml = `<iframe border="0" src="https://tw.trip.com/partners/ad/${matchedConfig.id}?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:${matchedConfig.w}px;height:${matchedConfig.h}px" frameborder="0" scrolling="no" style="border:none;max-width:100%" id="${matchedConfig.id}"></iframe>`;
      
      const wrapper = document.createElement('div');
      wrapper.className = 'trip-banner-wrapper';
      wrapper.innerHTML = iframeHtml;
      
      // Insert before the FAQ section or at end of article
      const faqSection = container.querySelector('.faq-section');
      if (faqSection) {
        container.insertBefore(wrapper, faqSection);
      } else {
        container.appendChild(wrapper);
      }
    }
  }
  
  // Run after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', insertTripBanner);
  } else {
    insertTripBanner();
  }

  // === 5. AFFILIATE CLICK TRACKING ===
  // Track affiliate link clicks for GA4
  document.addEventListener('click', function(e) {
    const link = e.target.closest('[data-affiliate]');
    if (!link) return;
    
    const affiliateName = link.getAttribute('data-affiliate') || 'unknown';
    const pageTitle = document.title || '';
    
    // Send to GA4 if available
    if (typeof gtag !== 'undefined') {
      gtag('event', 'affiliate_click', {
        affiliate_name: affiliateName,
        page_location: page,
        page_title: pageTitle
      });
    }
    
    console.log('[Affiliate Click]', affiliateName, page);
  });

})();
