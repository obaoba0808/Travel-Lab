# -*- coding: utf-8 -*-
"""
restructure_travel_v3.py — Travel Lab 文章頁統一 14 區塊排版 v3

對每個文章頁面：
1. 保留 <!DOCTYPE>...<head>...<body>
2. 保留 topbar（到 "✈ 用最少預算，走最多地方"</div>\n</div>\n</div> 為止）
3. 插入 CHARTER BANNER
4. 包裹 three-col-wrapper（sidebar + col-center）
5. 在 article-container 內補齊缺失區塊
6. 統一 footer
"""
import glob, re, os, sys

# ─── 區塊模板 ────────────────────────────────────────────────

CHARTER_BANNER = '''<!-- CHARTER BANNER -->
<div style="max-width:900px;margin:0 auto 30px;padding:0 20px;">
<a href="about.html"><img alt="台灣包車自由行" height="722" src="images/charter-banner.webp" style="width:100%;border-radius:12px;display:block;" width="2179"/></a>
</div>'''

STD_FOOTER = '''<!-- site-footer -->
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <a href="index.html" class="footer-logo">golightly<span class="logo-dot">.fun</span></a>
      <p class="footer-tagline">✈ 用最少預算，走最多地方</p>
    </div>
    <div class="footer-links">
      <div class="footer-col">
        <h4>日本旅遊</h4>
        <ul>
          <li><a href="tokyo-5days.html">東京5天4夜</a></li>
          <li><a href="japan-drugstore-checklist.html">藥妝必買</a></li>
          <li><a href="kansai-pass.html">關西周遊券</a></li>
          <li><a href="okinawa.html">沖繩自駕</a></li>
          <li><a href="osaka-food.html">大阪美食</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>韓國旅遊</h4>
        <ul>
          <li><a href="seoul-food.html">首爾美食</a></li>
          <li><a href="busan-capsule.html">釜山膠囊列車</a></li>
          <li><a href="jeju-island.html">濟州島</a></li>
          <li><a href="korea-budget.html">韓國預算</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>東南亞旅遊</h4>
        <ul>
          <li><a href="chiang-mai.html">清邁遊牧</a></li>
          <li><a href="bangkok-3days.html">曼谷攻略</a></li>
          <li><a href="vietnam-danang.html">越南峴港</a></li>
          <li><a href="singapore-3days.html">新加坡</a></li>
          <li><a href="kualalumpur-3days.html">吉隆坡</a></li>
          <li><a href="angkor-wat-2days.html">吳哥窟</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>台灣旅遊</h4>
        <ul>
          <li><a href="hualien-taitung.html">花東三天</a></li>
          <li><a href="tainan-food.html">台南美食</a></li>
          <li><a href="kenting.html">墾丁</a></li>
          <li><a href="taipei-food.html">台北美食</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>旅遊工具</h4>
        <ul>
          <li><a href="travel-tools.html">工具合集</a></li>
          <li><a href="power-plug-guide.html">插座指南</a></li>
          <li><a href="budget-airline-guide.html">廉航攻略</a></li>
          <li><a href="miles-calculator.html">里程試算</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2024-2026 均在路上 Travel Lab. All rights reserved.</p>
      <p class="footer-meta">
        <a href="privacy.html">隱私政策</a> · <a href="terms.html">使用條款</a> · <a href="about.html">關於我們</a> · <a href="contact.html">聯絡我們</a>
      </p>
    </div>
  </div>
</footer>'''

# ─── 頁面配置 ────────────────────────────────────────────────
# region: portal link | sidebar link | sidebar img | trip promo img | trip.com dest link
PAGE_CONFIG = {
    "angkor-wat-2days.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"southeast-asia.html","sb_img":"angkor-sidebar.webp","trip_img":"trip-cambodia.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-cambodia.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "bangkok-4days.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"chiang-mai.html","sb_img":"bangkok-sidebar.webp","trip_img":"trip-thailand.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "bangkok-massage.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"bangkok-3days.html","sb_img":"bangkok-sidebar.webp","trip_img":"trip-thailand.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "busan-4days.html": {"region":"韓國","portal":"korea-travel.html","sb_link":"seoul-food.html","sb_img":"busan-sidebar.webp","trip_img":"trip-korea.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-korea.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "chiang-mai.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"bangkok-3days.html","sb_img":"chiangmai-sidebar.webp","trip_img":"trip-thailand.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "fukuoka-5days.html": {"region":"日本","portal":"japan-travel.html","sb_link":"tokyo-5days.html","sb_img":"fukuoka-sidebar.webp","trip_img":"trip-japan.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-japan.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "japan-budget-guide.html": {"region":"日本","portal":"japan-travel.html","sb_link":"tokyo-5days.html","sb_img":"japan-sidebar.webp","trip_img":"trip-japan.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-japan.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "jeju-island.html": {"region":"韓國","portal":"korea-travel.html","sb_link":"seoul-food.html","sb_img":"jeju-sidebar.webp","trip_img":"trip-korea.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-korea.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "jiufen.html": {"region":"台灣","portal":"taiwan-travel.html","sb_link":"taipei-food.html","sb_img":"jiufen-sidebar.webp","trip_img":"trip-taiwan.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-taiwan.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "korea-budget.html": {"region":"韓國","portal":"korea-travel.html","sb_link":"seoul-food.html","sb_img":"korea-sidebar.webp","trip_img":"trip-korea.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-korea.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "korea-transport.html": {"region":"韓國","portal":"korea-travel.html","sb_link":"seoul-food.html","sb_img":"korea-sidebar.webp","trip_img":"trip-korea.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-korea.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "kualalumpur-3days.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"southeast-asia.html","sb_img":"kualalumpur-sidebar.webp","trip_img":"trip-malaysia.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-malaysia.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "osaka-food.html": {"region":"日本","portal":"japan-travel.html","sb_link":"tokyo-5days.html","sb_img":"osaka-sidebar.webp","trip_img":"trip-japan.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-japan.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "osaka-usj.html": {"region":"日本","portal":"japan-travel.html","sb_link":"tokyo-5days.html","sb_img":"osaka-sidebar.webp","trip_img":"trip-japan.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-japan.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "seoul-5days.html": {"region":"韓國","portal":"korea-travel.html","sb_link":"seoul-food.html","sb_img":"seoul-sidebar.webp","trip_img":"trip-korea.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-korea.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "seoul-food-map.html": {"region":"韓國","portal":"korea-travel.html","sb_link":"seoul-food.html","sb_img":"seoul-sidebar.webp","trip_img":"trip-korea.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-korea.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "singapore-3days.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"southeast-asia.html","sb_img":"singapore-sidebar.webp","trip_img":"trip-singapore.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-singapore.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "taipei-food.html": {"region":"台灣","portal":"taiwan-travel.html","sb_link":"taipei-food.html","sb_img":"taipei-sidebar.webp","trip_img":"trip-taiwan.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-taiwan.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "thailand-sim.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"chiang-mai.html","sb_img":"thailand-sidebar.webp","trip_img":"trip-thailand.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "tokyo-accommodation.html": {"region":"日本","portal":"japan-travel.html","sb_link":"tokyo-5days.html","sb_img":"tokyo-sidebar.webp","trip_img":"trip-japan.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-japan.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "vietnam-danang.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"southeast-asia.html","sb_img":"danang-sidebar.webp","trip_img":"trip-vietnam.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-vietnam.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
    "vietnam-hochiminh.html": {"region":"東南亞","portal":"southeast-asia.html","sb_link":"southeast-asia.html","sb_img":"hochiminh-sidebar.webp","trip_img":"trip-vietnam.webp","trip_url":"https://tw.trip.com/sale/w/26497/go-vietnam.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"},
}

# Klook ad IDs per region
KLOOK_ADS = {
    "日本": {"adid": "klook_jp_001", "title": "東京・大阪・京都 Klook必買", "url": "https://www.klook.com/zh-TW/?aff_id=26497&lang=zh-TW"},
    "韓國": {"adid": "klook_kr_001", "title": "首爾・釜山・濟州島 Klook優惠", "url": "https://www.klook.com/zh-TW/?aff_id=26497&lang=zh-TW"},
    "東南亞": {"adid": "klook_sea_001", "title": "泰國・越南・新加坡 Klook必玩", "url": "https://www.klook.com/zh-TW/?aff_id=26497&lang=zh-TW"},
    "台灣": {"adid": "klook_tw_001", "title": "台灣 Klook必玩優惠", "url": "https://www.klook.com/zh-TW/?aff_id=26497&lang=zh-TW"},
}

# Related posts per region
RELATED_POSTS = {
    "日本": [
        {"title":"東京5天4夜攻略","url":"tokyo-5days.html","img":"og/tokyo-sidebar.webp"},
        {"title":"沖繩自駕攻略","url":"okinawa.html","img":"og/okinawa-sidebar.webp"},
        {"title":"大阪美食攻略","url":"osaka-food.html","img":"og/osaka-sidebar.webp"},
    ],
    "韓國": [
        {"title":"首爾美食攻略","url":"seoul-food.html","img":"og/seoul-sidebar.webp"},
        {"title":"釜山膠囊列車","url":"busan-capsule.html","img":"og/busan-sidebar.webp"},
        {"title":"濟州島自駕","url":"jeju-island.html","img":"og/jeju-sidebar.webp"},
    ],
    "東南亞": [
        {"title":"清邁遊牧指南","url":"chiang-mai.html","img":"og/chiangmai-sidebar.webp"},
        {"title":"曼谷吃貨攻略","url":"bangkok-3days.html","img":"og/bangkok-sidebar.webp"},
        {"title":"越南峴港攻略","url":"vietnam-danang.html","img":"og/danang-sidebar.webp"},
    ],
    "台灣": [
        {"title":"花東三天兩夜","url":"hualien-taitung.html","img":"og/hualien-sidebar.webp"},
        {"title":"台南美食攻略","url":"tainan-food.html","img":"og/tainan-sidebar.webp"},
        {"title":"墾丁攻略","url":"kenting.html","img":"og/kenting-sidebar.webp"},
    ],
}

EXCLUDE = {'index.html','404.html','about.html','contact.html','privacy.html','terms.html','disclaimer.html',
           'japan-travel.html','korea-travel.html','taiwan-travel.html','southeast-asia.html',
           'travel-tools.html','monthly-review.html','budget-calculator.html','miles-calculator.html',
           'tax-refund-calculator.html','power-plug-guide.html','packing-list.html','packing-checklist.html',
           'budget-airline-guide.html','credit-card-miles-guide.html','notion-travel-template.html',
           'esim-comparison.html','seasia-budget-travel-guide.html'}

# ─── 區塊生成函數 ────────────────────────────────────────────

def make_trip_promo(cfg):
    """TRIP PROMO BANNER"""
    return f'''<!-- TRIP PROMO BANNER -->
<div style="position:relative;margin-bottom:24px;">
<a data-affiliate="trip-com" href="{cfg['trip_url']}" rel="nofollow sponsored" target="_blank"><img alt="Trip.com 熱門優惠" src="images/{cfg['trip_img']}" style="width:100%;border-radius:12px;display:block;"/></a>
<div style="position:absolute;bottom:12px;right:12px;background:rgba(0,0,0,0.75);color:#fff;padding:8px 18px;border-radius:20px;font-size:13px;font-weight:600;backdrop-filter:blur(4px);">🔥 点此查看最新優惠 →</div>
</div>'''

def make_sidebar(cfg, page_title):
    """Sidebar card with hero image"""
    return f'''<div class="sidebar-card">
<a href="{cfg['sb_link']}">
<img alt="{page_title}" class="sb-hero-img" loading="lazy" src="images/{cfg['sb_img']}"/>
</a>
</div>'''

def make_lead_inline():
    """Lead magnet inline form"""
    return '''<!-- LEAD MAGNET INLINE -->
<div class="lead-inline" style="margin:28px 0;padding:24px;background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border-radius:16px;text-align:center;">
<h3 style="margin:0 0 12px;font-size:18px;">📥 免費下載：旅遊打包清單 PDF</h3>
<p style="margin:0 0 16px;font-size:14px;color:#555;">輸入 Email 立即獲取完整版打包清單，適用所有目的地。</p>
<div style="display:flex;gap:8px;max-width:360px;margin:0 auto;">
<input id="leadEmail" placeholder="your@email.com" style="flex:1;padding:10px 14px;border:1px solid #a5d6a7;border-radius:8px;font-size:14px;" type="email"/>
<button id="leadSubmitBtn" onclick="submitLeadInline()" style="padding:10px 20px;background:#2e7d32;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap;">免費下載</button>
</div>
<div id="leadMsg" style="margin-top:10px;font-size:13px;"></div>
</div>'''

def make_klook_ad(cfg):
    """Klook affiliate ad"""
    region = cfg["region"]
    kl = KLOOK_ADS.get(region, KLOOK_ADS["日本"])
    return f'''<!-- KLOOK AD -->
<div class="klk-aff-widget" style="margin:24px 0;padding:20px;background:#fff3e0;border-radius:12px;border-left:4px solid #ff9800;">
<h3 style="margin:0 0 10px;font-size:16px;">🏷️ {kl['title']}</h3>
<p style="margin:0 0 14px;font-size:14px;color:#666;">交通票券、美食套餐、景點門票一站購買</p>
<a href="{kl['url']}" rel="nofollow sponsored" target="_blank" style="display:inline-block;padding:10px 24px;background:#ff9800;color:#fff;border-radius:8px;font-weight:600;text-decoration:none;font-size:14px;">前往 Klook 選購 →</a>
</div>'''

def make_related(cfg):
    """Related posts cards"""
    region = cfg["region"]
    posts = RELATED_POSTS.get(region, RELATED_POSTS["日本"])
    cards = ""
    for p in posts:
        cards += f'''<a href="{p['url']}" style="display:block;text-decoration:none;color:inherit;padding:12px;background:#f5f5f5;border-radius:10px;margin-bottom:8px;">
<span style="font-size:14px;font-weight:600;">📖 {p['title']}</span></a>\n'''
    return f'''<!-- RELATED POSTS -->
<div class="related-posts" style="margin:24px 0;">
<h3 style="margin:0 0 14px;font-size:18px;">📚 延伸閱讀</h3>
{cards.strip()}</div>'''

def make_trip_recommend(cfg):
    """Trip.com 住宿推薦"""
    region = cfg["region"]
    region_en = {"日本":"japan","韓國":"korea","東南亞":"southeast-asia","台灣":"taiwan"}.get(region,"japan")
    return f'''<!-- TRIP.COM 住宿推薦 -->
<div class="trip-recommend" style="margin:24px 0;padding:20px;background:#e3f2fd;border-radius:12px;border-left:4px solid #1976d2;">
<h3 style="margin:0 0 10px;font-size:16px;">🏨 住宿比價推薦</h3>
<p style="margin:0 0 14px;font-size:14px;color:#666;">Trip.com 比價找最便宜住宿，專屬優惠碼持續更新</p>
<a href="https://tw.trip.com/hotels/?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690" rel="nofollow sponsored" target="_blank" style="display:inline-block;padding:10px 24px;background:#1976d2;color:#fff;border-radius:8px;font-weight:600;text-decoration:none;font-size:14px;">Trip.com 住宿比價 →</a>
</div>'''

def make_lead_script():
    """Lead magnet JS"""
    return '''<script>
function submitLeadInline(){
  var email = document.getElementById('leadEmail').value.trim();
  if(!email || !email.includes('@')){
    document.getElementById('leadMsg').innerHTML = '請輸入有效的 Email';
    document.getElementById('leadMsg').style.color = '#c62828';
    return;
  }
  var btn = document.getElementById('leadSubmitBtn');
  var msg = document.getElementById('leadMsg');
  btn.textContent = '傳送中...';
  btn.disabled = true;
  msg.innerHTML = '';
  fetch(WORKER_URL + '?email=' + encodeURIComponent(email) + '&resource=' + encodeURIComponent(getResourceKey()) + '&page=' + encodeURIComponent(document.title))
    .then(function(r){ return r.json(); })
    .then(function(d){
      if(d.ok || d.success){
        btn.textContent = '✉️ 已寄出，請收Email';
        btn.style.background = '#a5d6a7';
        btn.disabled = true;
        msg.innerHTML = '📧 Email 已寄出！請檢查信箱（含垃圾郵件）';
        msg.style.color = '#2e7d32';
        localStorage.setItem('leadSent','1');
      } else {
        btn.textContent = '傳送失敗，再試一次';
        btn.disabled = false;
        btn.style.background = '';
        msg.innerHTML = '傳送失敗，請再試一次 🙏';
        msg.style.color = '#c62828';
      }
    })
    .catch(function(e){
      btn.textContent = '傳送失敗，再試一次';
      btn.disabled = false;
      btn.style.background = '';
      msg.innerHTML = '網路錯誤，請再試一次 🙏';
      msg.style.color = '#c62828';
    });
}
</script>'''

# ─── 核心處理 ────────────────────────────────────────────────

def find_topbar_end(content):
    """Find where topbar ends. Try multiple patterns."""
    body_idx = content.find("<body")
    if body_idx < 0:
        return -1

    # Pattern 1: standard topbar with tagline
    marker = "\u7528\u6700\u5c11\u9810\u7b97\uff0c\u8d70\u6700\u591a\u5730\u65b9"
    idx = content.find(marker, body_idx)
    if idx >= 0:
        pos = idx + len(marker)
        divs_found = 0
        while divs_found < 3:
            next_div = content.find("</div>", pos)
            if next_div < 0:
                return -1
            divs_found += 1
            pos = next_div + 6
        return pos

    # Pattern 2: any </nav> after <body>
    nav_end = content.find("</nav>", body_idx)
    if nav_end >= 0:
        return nav_end + 6

    # Pattern 3: pages with unclosed nav — find </div>\n    </div>\n<section or </div>\n      </div>\n<section
    hero_match = re.search(r'</div>\s*</div>\s*(<section class="hero)', content[body_idx:])
    if hero_match:
        # Find the two </div> positions
        start = body_idx
        # Find the first </div> before <section
        section_start = body_idx + hero_match.start(1)
        # Go back to find </div></div> before <section
        before_section = content[section_start-60:section_start]
        # Return position right after the last </div> before <section
        last_div_pos = content.rfind("</div>", body_idx, section_start)
        if last_div_pos >= 0:
            return last_div_pos + 6

    return -1


def find_existing_footer_start(content):
    """Find existing site-footer start"""
    for pat in ['<footer class="site-footer">', '<footer class="site-footer"']:
        idx = content.find(pat)
        if idx >= 0:
            return idx
    # Also check for <!-- site-footer -->
    idx = content.find("<!-- site-footer -->")
    if idx >= 0:
        return idx
    return -1

def extract_page_title(content):
    """Extract <title>...</title>"""
    m = re.search(r'<title>([^<]+)</title>', content)
    return m.group(1).replace('｜均在路上 Travel Lab','').strip() if m else ""

def restructure_page(filepath):
    """Restructure a single HTML page"""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    fname = os.path.basename(filepath)
    if fname not in PAGE_CONFIG:
        return False, "not in PAGE_CONFIG"
    
    cfg = PAGE_CONFIG[fname]
    page_title = extract_page_title(original)
    
    # 1. Find topbar end
    topbar_end = find_topbar_end(original)
    if topbar_end < 0:
        return False, "cannot find topbar end"
    
    # 2. Split: before topbar end (header) | after topbar end (body content)
    header_part = original[:topbar_end]
    
    # 3. Find existing footer start in body content
    footer_start = find_existing_footer_start(original)
    if footer_start >= 0:
        body_content = original[topbar_end:footer_start].strip()
    else:
        body_content = original[topbar_end:].strip()
    
    # 4. Check existing blocks in body_content
    has_trip_promo = "TRIP PROMO BANNER" in body_content
    has_faq = "faq-section" in body_content
    has_lead = "lead-inline" in body_content
    has_klook = "klk-aff-widget" in body_content
    has_related = "related-posts" in body_content
    has_trip_rec = "trip-recommend" in body_content
    
    # 5. Extract existing blocks that we want to keep in place
    # Extract FAQ section if exists
    faq_block = ""
    if has_faq:
        # Take from the first <div class="faq- to end of content
        faq_match = re.search(r'(<div class="faq-section".*?)(?=<div class="(?:lead-inline|klk-aff-widget|related-posts|trip-recommend)|$)', body_content, re.DOTALL)
        if faq_match:
            faq_block = faq_match.group(1).strip()
    
    # 6. Build new content: after topbar, before any existing content
    # Remove existing charter-banner if any
    body_clean = re.sub(r'<!--\s*CHARTER BANNER\s*-->.*?</div>\s*</div>', '', body_content, count=1, flags=re.DOTALL)
    # Remove existing TRIP PROMO if any
    body_clean = re.sub(r'<!--\s*TRIP PROMO BANNER\s*-->.*?</div>\s*</div>', '', body_clean, count=1, flags=re.DOTALL)
    # Remove existing sidebar-card if any  
    body_clean = re.sub(r'<div class="sidebar-card">.*?</div>\s*</div>\s*</a>', '', body_clean, count=1, flags=re.DOTALL)
    # Remove existing lead-inline if any
    body_clean = re.sub(r'<div class="lead-inline".*?</div>\s*</div>\s*</div>', '', body_clean, count=1, flags=re.DOTALL)
    # Remove existing klk-aff-widget if any
    body_clean = re.sub(r'<div class="klk-aff-widget".*?</div>', '', body_clean, count=1, flags=re.DOTALL)
    # Remove existing related-posts if any
    body_clean = re.sub(r'<div class="related-posts".*?</div>\s*</div>', '', body_clean, count=1, flags=re.DOTALL)
    # Remove existing trip-recommend if any
    body_clean = re.sub(r'<div class="trip-recommend".*?</div>\s*</div>', '', body_clean, count=1, flags=re.DOTALL)
    # Remove existing three-col-wrapper if any
    if 'three-col-wrapper' in body_clean:
        body_clean = re.sub(r'<div class="three-col-wrapper">.*?</div>\s*</div>\s*</div>\s*</div>', '', body_clean, count=1, flags=re.DOTALL)
    # Remove any article-container wrapper
    if '<div class="article-container">' in body_clean:
        body_clean = body_clean.replace('<div class="article-container">', '').replace('</div><!-- /article-container -->', '')
    
    body_clean = body_clean.strip()
    
    # 7. Collect all scripts at end of original file (between </body> and </html>)
    scripts = ""
    script_match = re.findall(r'<script>.*?</script>', original, re.DOTALL)
    # Keep only lead-related scripts
    for s in script_match:
        if 'submitLead' in s or 'WORKER_URL' in s or 'getResourceKey' in s:
            scripts += s + "\n"
    
    # 8. Assemble final page
    new_content = (
        header_part + "\n" +
        CHARTER_BANNER + "\n" +
        '<div class="three-col-wrapper">\n' +
        make_sidebar(cfg, page_title) + "\n" +
        '<div class="col-center">\n' +
        '<div class="article-container">\n' +
        make_trip_promo(cfg) + "\n" +
        body_clean + "\n" +
        make_trip_recommend(cfg) + "\n" +
        make_lead_inline() + "\n" +
        make_klook_ad(cfg) + "\n" +
        make_related(cfg) + "\n" +
        '</div><!-- /article-container -->\n' +
        '</div><!-- /col-center -->\n' +
        '</div><!-- /three-col-wrapper -->\n' +
        STD_FOOTER + "\n" +
        make_lead_script() + "\n" +
        '</body>\n</html>\n'
    )
    
    # Only write if changed
    if new_content.strip() != original.strip():
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True, "OK"
    else:
        return False, "No change"

# ─── Main ──────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("restructure_travel_v3.py")
    print("Travel Lab 文章頁統一14區塊排版")
    print("=" * 60)
    
    ok = 0
    skip = 0
    errors = []
    
    for fname in sorted(glob.glob("*.html")):
        if fname in EXCLUDE:
            skip += 1
            continue
        if fname not in PAGE_CONFIG:
            skip += 1
            continue
        cfg = PAGE_CONFIG[fname]
        success, msg = restructure_page(fname)
        if success:
            ok += 1
            print(f"  ✅ {fname}")
        else:
            errors.append((fname, msg))
            print(f"  ⏭️ {fname}: {msg}")
    
    print("=" * 60)
    print(f"結果: {ok} 成功重構, {skip} 跳過（非文章頁）")
    if errors:
        print(f"錯誤: {len(errors)}")
        for f, m in errors:
            print(f"  ❌ {f}: {m}")
    print("=" * 60)
