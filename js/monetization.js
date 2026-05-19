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
      <a href="https://www.agoda.com/zh-tw/?tag=e9ea26c2-c046-468f-939d-97d11075d6e0" target="_blank" rel="noopener sponsored" data-affiliate="agoda" class="toolbar-item">
        <span class="tb-icon">🏨</span>
        <span class="tb-label">Agoda 訂房</span>
      </a>
      <a href="https://www.skyscanner.net.tw/?affiliateId=skyscan-ch&label=travel-lab" target="_blank" rel="noopener sponsored" data-affiliate="skyscanner" class="toolbar-item">
        <span class="tb-icon">✈️</span>
        <span class="tb-label">Skyscanner 機票</span>
      </a>
      <a href="https://www.klook.com/zh-TW/?aid=13014149&aff_label=travellab" target="_blank" rel="noopener sponsored" data-affiliate="klook" class="toolbar-item">
        <span class="tb-icon">🎫</span>
        <span class="tb-label">Klook 門票</span>
      </a>
      <a href="https://airalo.prf.hn/click/camref:1011lwbU/pubref:travellab/destination:https%3A%2F%2Fairalo.com%2Fzh-tw%2F" target="_blank" rel="noopener sponsored" data-affiliate="airalo" class="toolbar-item">
        <span class="tb-icon">📱</span>
        <span class="tb-label">Airalo eSIM</span>
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
          <a href="https://www.agoda.com/zh-tw/search/${destSearch}?tag=e9ea26c2-c046-468f-939d-97d11075d6e0" target="_blank" rel="noopener sponsored" class="cta-card cta-agoda" data-affiliate="agoda">
            <div class="cta-card-icon">🏨</div>
            <div>
              <div class="cta-card-text">飯店住宿</div>
              <div class="cta-card-sub">Agoda 比價</div>
            </div>
          </a>
          <a href="https://www.skyscanner.net.tw/transport/flights/tpe/${destSearch.toLowerCase()}?affiliateId=skyscan-ch&label=travel-lab" target="_blank" rel="noopener sponsored" class="cta-card cta-skyscanner" data-affiliate="skyscanner">
            <div class="cta-card-icon">✈️</div>
            <div>
              <div class="cta-card-text">機票比價</div>
              <div class="cta-card-sub">Skyscanner</div>
            </div>
          </a>
          <a href="https://www.klook.com/zh-TW/search/?keyword=${destSearch}&aid=13014149&aff_label=travellab" target="_blank" rel="noopener sponsored" class="cta-card cta-klook" data-affiliate="klook">
            <div class="cta-card-icon">🎫</div>
            <div>
              <div class="cta-card-text">當地體驗</div>
              <div class="cta-card-sub">Klook</div>
            </div>
          </a>
          <a href="https://airalo.prf.hn/click/camref:1011lwbU/pubref:travellab/destination:https%3A%2F%2Fairalo.com%2Fzh-tw%2F" target="_blank" rel="noopener sponsored" class="cta-card cta-esim" data-affiliate="airalo">
            <div class="cta-card-icon">📱</div>
            <div>
              <div class="cta-card-text">上網卡</div>
              <div class="cta-card-sub">Airalo eSIM</div>
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
  // Auto-insert Trip.com promo banner based on destination
  function insertTripBanner() {
    const container = document.querySelector('.article-container') || document.querySelector('.col-center');
    if (!container) return;
    
    let bannerHtml = '';
    
    if (page.includes('japan') || page.includes('tokyo') || page.includes('kansai') || page.includes('hokkaido') || page.includes('okinawa') || page.includes('kyoto')
      || page.includes('korea') || page.includes('seoul') || page.includes('busan') || page.includes('jeju')
      || page.includes('taiwan') || page.includes('hualien') || page.includes('tainan') || page.includes('kenting')
      || page.includes('southeast') || page.includes('chiang-mai') || page.includes('bangkok')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17138130?Allianceid=8237671&SID=312406690&trip_sub1=" frameborder="0" scrolling="no" id="DB17138130"></iframe>';
    }
    
    if (bannerHtml) {
      const wrapper = document.createElement('div');
      wrapper.className = 'trip-banner-wrapper';
      wrapper.innerHTML = bannerHtml;
      
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
