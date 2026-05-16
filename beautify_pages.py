#!/usr/bin/env python3
"""Beautify about.html and travel-tools.html with Tiffany green styling"""
import os

os.chdir(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')

# ============================================================
# BEAUTIFY about.html
# ============================================================
about_new = '''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="UTF-8">
<title>關於我們｜均在路上 Travel Lab</title>
<meta name="description" content="均在路上 Travel Lab 的品牌故事與編輯理念，一個用實際走訪驗證的旅遊攻略網站，幫你用最少預算走最多地方。">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="https://golightly.fun/about.html">
<meta name="robots" content="index, follow">
<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/about.html">
<link rel="alternate" hreflang="zh-TW" href="https://golightly.fun/about.html">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/about.html">

<!-- Open Graph -->
<meta property="og:title" content="關於我們｜均在路上 Travel Lab">
<meta property="og:description" content="均在路上 Travel Lab 的品牌故事與編輯理念，一個用實際走訪驗證的旅遊攻略網站，幫你用最少預算走最多地方。">
<meta property="og:type" content="website">
<meta property="og:url" content="https://golightly.fun/about.html">
<meta property="og:image" content="https://golightly.fun/images/tokyo-hero.webp">
<meta property="og:site_name" content="均在路上 Travel Lab">
<meta property="og:locale" content="zh_TW">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="關於我們｜均在路上 Travel Lab">
<meta name="twitter:description" content="均在路上 Travel Lab 的品牌故事與編輯理念，一個用實際走訪驗證的旅遊攻略網站，幫你用最少預算走最多地方。">
<meta name="twitter:image" content="https://golightly.fun/images/tokyo-hero.webp">

<!-- JSON-LD: AboutPage -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "關於均在路上 Travel Lab",
  "description": "均在路上 Travel Lab 的品牌故事與編輯理念，一個用實際走訪驗證的旅遊攻略網站。",
  "url": "https://golightly.fun/about.html",
  "mainEntity": {
    "@type": "Organization",
    "name": "均在路上 Travel Lab",
    "url": "https://golightly.fun/",
    "description": "實戰旅遊攻略網站，用最少預算走最多地方。"
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "均在路上 Travel Lab",
  "url": "https://golightly.fun/",
  "description": "實戰旅遊攻略網站，用最少預算走最多地方。",
  "sameAs": []
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://golightly.fun/"},
    {"@type": "ListItem", "position": 2, "name": "關於我們", "item": "https://golightly.fun/about.html"}
  ]
}
</script>

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">

<!-- Stylesheet -->
<link rel="stylesheet" href="style.css">

<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S7KQGHSD2R"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-S7KQGHSD2R');
</script>
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✈️</text></svg>">
</head>
<body>

<!-- TOP BAR NAVIGATION -->
<div class="site-topbar">
  <div class="topbar-inner">
    <button class="mobile-toggle" onclick="document.querySelector('.main-nav').classList.toggle('active')">☰</button>
    <nav class="main-nav">
      <a href="index.html">首頁</a>
      <div class="nav-dropdown">
        <a href="japan-travel.html" class="dropdown-toggle">日本自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="tokyo-5days.html">東京5天4夜行程</a>
          <a href="kansai-pass.html">關西交通票券指南</a>
          <a href="hokkaido-winter.html">北海道冬季賞雪</a>
          <a href="okinawa.html">沖繩自駕4天3夜</a>
          <a href="kyoto-temples.html">京都寺廟楓紅散步</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="korea-travel.html" class="dropdown-toggle">韓國自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="seoul-food.html">首爾必吃美食攻略</a>
          <a href="busan-capsule.html">釜山膠囊列車預約</a>
          <a href="jeju-island.html">濟州島自駕環島</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="taiwan-travel.html" class="dropdown-toggle">台灣旅遊 ▾</a>
        <div class="dropdown-menu">
          <a href="hualien-taitung.html">花東三天兩夜</a>
          <a href="tainan-food.html">台南美食牛肉湯</a>
          <a href="kenting.html">墾丁海景夜市攻略</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="southeast-asia.html" class="dropdown-toggle">東南亞自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="chiang-mai.html">清邁數位遊牧指南</a>
          <a href="bangkok-3days.html">曼谷吃貨攻略</a>
        </div>
      </div>
      <a href="travel-tools.html">旅遊工具</a>
      <a href="about.html" class="active">關於我們</a>
    </nav>
  </div>
</div>

<!-- SITE BRANDING -->
<div class="site-branding">
  <span class="site-title">均在路上 <span>Travel Lab</span></span>
  <p>用最少預算，走最多地方的實戰旅遊攻略</p>
</div>

<!-- CATEGORY HERO -->
<div class="category-hero" style="background-image: url('images/tokyo-hero.webp');">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>關於均在路上 Travel Lab</h1>
    <p>每篇攻略，都是實地走訪的驗證結果。</p>
  </div>
</div>

<!-- MAIN CONTENT -->
<div class="site-content">
  <main class="content-area" style="max-width:900px;">

    <!-- Story Section with Tiffany styling -->
    <div style="background:linear-gradient(135deg, var(--tiffany-light) 0%, #fff 100%); border-radius:16px; padding:40px; margin-bottom:40px; border-left:5px solid var(--tiffany);">
      <h2 style="color:var(--tiffany-dark); margin-bottom:20px; font-size:26px;">我們的故事</h2>
      <p style="font-size:16px; line-height:2; margin-bottom:16px;">均在路上 Travel Lab 誕生於一個簡單的信念：<strong style="color:var(--tiffany-dark);">旅行不必花大錢</strong>。我們相信，最好的旅行攻略不是坐在辦公室裡拼湊出來的，而是用雙腳走出來的。網站上的每一篇文章，都是我們實際走訪、親身體驗後寫下的紀錄。</p>
      <p style="font-size:16px; line-height:2;">從東京巷弄的平價拉麵到清邁的數位遊牧咖啡廳，從沖繩的自駕路線到釜山膠囊列車的預約流程——我們不只告訴你哪裡好玩，更告訴你怎麼玩最省、怎麼避開地雷。</p>
    </div>

    <!-- Editorial Principles Cards -->
    <h2 style="color:var(--tiffany-dark); margin:40px 0 24px; padding-left:15px; border-left:5px solid var(--tiffany);">編輯理念</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:20px; margin-bottom:40px;">
      <div style="background:#fff; border-radius:14px; padding:28px; box-shadow:0 4px 20px rgba(10,186,181,0.1); border:1px solid var(--tiffany-light); transition:0.3s;">
        <div style="font-size:36px; margin-bottom:12px;">🎯</div>
        <h3 style="color:var(--tiffany-dark); font-size:18px; margin-bottom:10px;">實用 > 漂亮</h3>
        <p style="color:var(--text-gray); font-size:14px; line-height:1.8;">我們追求的是讓你真的能用上的資訊，不是華而不實的旅遊美文。</p>
      </div>
      <div style="background:#fff; border-radius:14px; padding:28px; box-shadow:0 4px 20px rgba(10,186,181,0.1); border:1px solid var(--tiffany-light); transition:0.3s;">
        <div style="font-size:36px; margin-bottom:12px;">📊</div>
        <h3 style="color:var(--tiffany-dark); font-size:18px; margin-bottom:10px;">具體數據 > 模糊描述</h3>
        <p style="color:var(--text-gray); font-size:14px; line-height:1.8;">「大概很便宜」不如「交通券省了 2,400 日圓」，所有建議都附上具體價格和時間。</p>
      </div>
      <div style="background:#fff; border-radius:14px; padding:28px; box-shadow:0 4px 20px rgba(10,186,181,0.1); border:1px solid var(--tiffany-light); transition:0.3s;">
        <div style="font-size:36px; margin-bottom:12px;">🔄</div>
        <h3 style="color:var(--tiffany-dark); font-size:18px; margin-bottom:10px;">定期更新</h3>
        <p style="color:var(--text-gray); font-size:14px; line-height:1.8;">票價會變、店家會倒、路線會改，我們持續回訪更新，確保資訊的準確性。</p>
      </div>
    </div>

    <!-- Destination Coverage Grid -->
    <h2 style="color:var(--tiffany-dark); margin:40px 0 24px; padding-left:15px; border-left:5px solid var(--tiffany);">涵蓋目的地</h2>
    <p style="margin-bottom:20px;">目前網站共收錄 <strong style="color:var(--tiffany-dark);">13 篇實戰攻略</strong>，涵蓋四大區域：</p>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:16px; margin-bottom:40px;">
      <div style="background:linear-gradient(135deg, #e8f4f8 0%, #f0f9f9 100%); border-radius:12px; padding:24px; border:2px solid var(--tiffany-light);">
        <span style="display:inline-block; background:var(--tiffany); color:#fff; font-size:12px; padding:4px 12px; border-radius:20px; margin-bottom:12px;">5 篇</span>
        <h4 style="color:var(--tiffany-dark); font-size:16px; margin-bottom:8px;">🇯🇵 日本自由行</h4>
        <p style="font-size:13px; color:var(--text-gray);">東京、關西、北海道、沖繩、京都</p>
      </div>
      <div style="background:linear-gradient(135deg, #f8f0f4 0%, #fcf5f8 100%); border-radius:12px; padding:24px; border:2px solid #f0d0e0;">
        <span style="display:inline-block; background:#e84a7f; color:#fff; font-size:12px; padding:4px 12px; border-radius:20px; margin-bottom:12px;">3 篇</span>
        <h4 style="color:#c73a6a; font-size:16px; margin-bottom:8px;">🇰🇷 韓國自由行</h4>
        <p style="font-size:13px; color:var(--text-gray);">首爾、釜山、濟州島</p>
      </div>
      <div style="background:linear-gradient(135deg, #f0f8f0 0%, #f5fcf5 100%); border-radius:12px; padding:24px; border:2px solid #d0e8d0;">
        <span style="display:inline-block; background:#4a9f4a; color:#fff; font-size:12px; padding:4px 12px; border-radius:20px; margin-bottom:12px;">3 篇</span>
        <h4 style="color:#3a8a3a; font-size:16px; margin-bottom:8px;">🇹🇼 台灣旅遊</h4>
        <p style="font-size:13px; color:var(--text-gray);">花東、台南、墾丁</p>
      </div>
      <div style="background:linear-gradient(135deg, #f8f4e8 0%, #fcf8f0 100%); border-radius:12px; padding:24px; border:2px solid #e8d8a0;">
        <span style="display:inline-block; background:#c9a227; color:#fff; font-size:12px; padding:4px 12px; border-radius:20px; margin-bottom:12px;">2 篇</span>
        <h4 style="color:#a08020; font-size:16px; margin-bottom:8px;">🌏 東南亞自由行</h4>
        <p style="font-size:13px; color:var(--text-gray);">清邁、曼谷</p>
      </div>
    </div>

    <!-- Taiwan Car Service CTA -->
    <div style="background:linear-gradient(135deg, var(--tiffany) 0%, var(--tiffany-dark) 100%); border-radius:16px; padding:40px; text-align:center; color:#fff; margin-bottom:40px;">
      <h2 style="font-size:24px; margin-bottom:12px;">🚐 台灣包車服務</h2>
      <p style="font-size:15px; opacity:0.95; margin-bottom:24px; max-width:500px; margin-left:auto; margin-right:auto;">我們也提供台灣包車旅遊服務，適合不想自己開車、希望輕鬆遊覽花東、墾丁等路線的旅人。</p>
      <div style="display:flex; flex-wrap:wrap; gap:16px; justify-content:center; margin-bottom:20px;">
        <div style="background:rgba(255,255,255,0.2); padding:12px 24px; border-radius:30px; font-size:14px;">
          <strong>LINE：</strong> @938nzmjr
        </div>
        <div style="background:rgba(255,255,255,0.2); padding:12px 24px; border-radius:30px; font-size:14px;">
          <strong>電話：</strong> 0926-656666
        </div>
      </div>
      <p style="font-size:13px; opacity:0.85;">歡迎透過 LINE 洽詢行程與報價，我們會盡快回覆。</p>
    </div>

  </main>
</div>

<!-- FOOTER -->
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col">
      <h4>日本自由行</h4>
      <ul>
        <li><a href="tokyo-5days.html">東京5天4夜</a></li>
        <li><a href="kansai-pass.html">關西交通票券</a></li>
        <li><a href="hokkaido-winter.html">北海道冬季</a></li>
        <li><a href="okinawa.html">沖繩自駕</a></li>
        <li><a href="kyoto-temples.html">京都寺廟</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>韓國自由行</h4>
      <ul>
        <li><a href="seoul-food.html">首爾美食</a></li>
        <li><a href="busan-capsule.html">釜山膠囊列車</a></li>
        <li><a href="jeju-island.html">濟州島自駕</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>台灣旅遊</h4>
      <ul>
        <li><a href="hualien-taitung.html">花東三天兩夜</a></li>
        <li><a href="tainan-food.html">台南美食</a></li>
        <li><a href="kenting.html">墾丁海景</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>東南亞自由行</h4>
      <ul>
        <li><a href="chiang-mai.html">清邁數位遊牧</a></li>
        <li><a href="bangkok-3days.html">曼谷吃貨攻略</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 均在路上 Travel Lab. All Rights Reserved.</p>
    <div style="margin-top:8px;font-size:12px;">
      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>
      <a href="contact.html" style="color:inherit;margin-right:12px;">聯絡我們</a>
      <a href="privacy.html" style="color:inherit;">隱私權政策</a>
    </div>
  </div>
</footer>

</body>
</html>'''

# ============================================================
# BEAUTIFY travel-tools.html
# ============================================================
tools_new = '''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="UTF-8">
<title>旅遊工具推薦｜均在路上 Travel Lab</title>
<meta name="description" content="旅遊省錢工具包：Agoda訂房、Klook景點門票、Skyscanner機票比價、Airalo eSIM，出國必備懶人包。">
<meta name="keywords" content="旅遊工具,Agoda,Klook,Skyscanner,eSIM,旅遊保險,機票比價,訂房優惠">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="https://golightly.fun/travel-tools.html">
<meta name="robots" content="index, follow">
<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/travel-tools.html">
<link rel="alternate" hreflang="zh-TW" href="https://golightly.fun/travel-tools.html">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/travel-tools.html">

<!-- Open Graph -->
<meta property="og:title" content="旅遊省錢工具包｜均在路上 Travel Lab">
<meta property="og:description" content="旅遊省錢工具包：Agoda訂房、Klook景點門票、Skyscanner機票比價、Airalo eSIM，出國必備懶人包。">
<meta property="og:type" content="website">
<meta property="og:url" content="https://golightly.fun/travel-tools.html">
<meta property="og:image" content="https://golightly.fun/images/tokyo-hero.webp">
<meta property="og:site_name" content="均在路上 Travel Lab">
<meta property="og:locale" content="zh_TW">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="旅遊省錢工具包｜均在路上 Travel Lab">
<meta name="twitter:description" content="旅遊省錢工具包：Agoda訂房、Klook景點門票、Skyscanner機票比價、Airalo eSIM，出國必備懶人包。">
<meta name="twitter:image" content="https://golightly.fun/images/tokyo-hero.webp">

<!-- JSON-LD -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "旅遊省錢工具包",
  "description": "旅遊省錢工具包：Agoda訂房、Klook景點門票、Skyscanner機票比價、Airalo eSIM，出國必備懶人包。",
  "url": "https://golightly.fun/travel-tools.html",
  "isPartOf": {
    "@type": "WebSite",
    "name": "均在路上 Travel Lab",
    "url": "https://golightly.fun/"
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://golightly.fun/"},
    {"@type": "ListItem", "position": 2, "name": "旅遊省錢工具包", "item": "https://golightly.fun/travel-tools.html"}
  ]
}
</script>

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap" rel="stylesheet">

<!-- Stylesheet -->
<link rel="stylesheet" href="style.css">

<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S7KQGHSD2R"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-S7KQGHSD2R');
</script>
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✈️</text></svg>">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"出國旅行必備哪些 APP？","acceptedAnswer":{"@type":"Answer","text":"Google Maps（導航）、Google Translate（翻譯）、Klook（門票預約）、Agoda（訂房）、Skyscanner（機票比價）是五大必裝 APP。"}},{"@type":"Question","name":"eSIM 和 Wi-Fi 分享器哪個好？","acceptedAnswer":{"@type":"Answer","text":"短期旅行（3-5天）推薦 Airalo eSIM，免租借、即買即用、約 NT$200-400。長期或多人同行用 Wi-Fi 分享器更划算。"}},{"@type":"Question","name":"旅遊保險一定要買嗎？","acceptedAnswer":{"@type":"Answer","text":"強烈建議購買。醫療費用、班機延誤、行李遺失都能理賠。富邦、國泰等保險公司有專門的旅遊險，一天約 NT$100-200。"}}]}
</script>
</head>
<body>

<!-- TOP BAR NAVIGATION -->
<div class="site-topbar">
  <div class="topbar-inner">
    <button class="mobile-toggle" onclick="document.querySelector('.main-nav').classList.toggle('active')">☰</button>
    <nav class="main-nav">
      <a href="index.html">首頁</a>
      <div class="nav-dropdown">
        <a href="japan-travel.html" class="dropdown-toggle">日本自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="tokyo-5days.html">東京5天4夜行程</a>
          <a href="kansai-pass.html">關西交通票券指南</a>
          <a href="hokkaido-winter.html">北海道冬季賞雪</a>
          <a href="okinawa.html">沖繩自駕4天3夜</a>
          <a href="kyoto-temples.html">京都寺廟楓紅散步</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="korea-travel.html" class="dropdown-toggle">韓國自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="seoul-food.html">首爾必吃美食攻略</a>
          <a href="busan-capsule.html">釜山膠囊列車預約</a>
          <a href="jeju-island.html">濟州島自駕環島</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="taiwan-travel.html" class="dropdown-toggle">台灣旅遊 ▾</a>
        <div class="dropdown-menu">
          <a href="hualien-taitung.html">花東三天兩夜</a>
          <a href="tainan-food.html">台南美食牛肉湯</a>
          <a href="kenting.html">墾丁海景夜市攻略</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="southeast-asia.html" class="dropdown-toggle">東南亞自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="chiang-mai.html">清邁數位遊牧指南</a>
          <a href="bangkok-3days.html">曼谷吃貨攻略</a>
        </div>
      </div>
      <a href="travel-tools.html" class="active">旅遊工具</a>
    </nav>
  </div>
</div>

<!-- SITE BRANDING -->
<div class="site-branding">
  <span class="site-title">均在路上 <span>Travel Lab</span></span>
  <p>用最少預算，走最多地方的實戰旅遊攻略</p>
</div>

<!-- CATEGORY HERO -->
<div class="category-hero" style="background-image: url('images/tokyo-hero.webp');">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>旅遊省錢工具包</h1>
    <p>機票、住宿、門票、網路，出國必備懶人包。</p>
  </div>
</div>

<!-- MAIN CONTENT -->
<div class="site-content" style="max-width:1100px;">
  <main class="content-area" style="max-width:100%;">

    <!-- Tools Grid with Tiffany styling -->
    <h2 style="color:var(--tiffany-dark); margin:40px 0 24px; padding-left:15px; border-left:5px solid var(--tiffany);">訂房與住宿</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px; margin-bottom:40px;">
      <div style="background:#fff; border-radius:16px; padding:30px; box-shadow:0 4px 24px rgba(10,186,181,0.12); border:2px solid var(--tiffany-light); transition:0.3s;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <div style="background:linear-gradient(135deg, #f5a623 0%, #e8941c 100%); width:50px; height:50px; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px;">🏨</div>
          <h3 style="color:#e8941c; font-size:20px;">Agoda</h3>
        </div>
        <p style="color:var(--text-gray); font-size:14px; line-height:1.8; margin-bottom:20px;">全球訂房平台，常態折扣 10-20%，會員累積點數可折抵現金。</p>
        <a href="https://www.agoda.com/zh-tw" target="_blank" rel="noopener noreferrer sponsored" style="display:inline-block; background:linear-gradient(135deg, #f5a623 0%, #e8941c 100%); color:#fff; padding:10px 24px; border-radius:30px; font-size:14px; font-weight:500;">前往 Agoda →</a>
      </div>
    </div>

    <h2 style="color:var(--tiffany-dark); margin:40px 0 24px; padding-left:15px; border-left:5px solid var(--tiffany);">景點門票與活動</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px; margin-bottom:40px;">
      <div style="background:#fff; border-radius:16px; padding:30px; box-shadow:0 4px 24px rgba(10,186,181,0.12); border:2px solid var(--tiffany-light); transition:0.3s;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <div style="background:linear-gradient(135deg, #FF5A5F 0%, #e04a4f 100%); width:50px; height:50px; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px;">🎫</div>
          <h3 style="color:#e04a4f; font-size:20px;">Klook</h3>
        </div>
        <p style="color:var(--text-gray); font-size:14px; line-height:1.8; margin-bottom:20px;">亞洲最大旅遊體驗平台，門票、一日遊、交通票券一站購足。</p>
        <a href="https://www.klook.com/zh-TW/" target="_blank" rel="noopener noreferrer sponsored" style="display:inline-block; background:linear-gradient(135deg, #FF5A5F 0%, #e04a4f 100%); color:#fff; padding:10px 24px; border-radius:30px; font-size:14px; font-weight:500;">前往 Klook →</a>
      </div>
    </div>

    <h2 style="color:var(--tiffany-dark); margin:40px 0 24px; padding-left:15px; border-left:5px solid var(--tiffany);">機票比價</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px; margin-bottom:40px;">
      <div style="background:#fff; border-radius:16px; padding:30px; box-shadow:0 4px 24px rgba(10,186,181,0.12); border:2px solid var(--tiffany-light); transition:0.3s;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <div style="background:linear-gradient(135deg, #00A2DF 0%, #0090c8 100%); width:50px; height:50px; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px;">✈️</div>
          <h3 style="color:#0090c8; font-size:20px;">Skyscanner</h3>
        </div>
        <p style="color:var(--text-gray); font-size:14px; line-height:1.8; margin-bottom:20px;">全球機票比價引擎，一次比較數百家航空，找出最便宜組合。</p>
        <a href="https://www.skyscanner.com.tw/" target="_blank" rel="noopener noreferrer sponsored" style="display:inline-block; background:linear-gradient(135deg, #00A2DF 0%, #0090c8 100%); color:#fff; padding:10px 24px; border-radius:30px; font-size:14px; font-weight:500;">前往 Skyscanner →</a>
      </div>
    </div>

    <h2 style="color:var(--tiffany-dark); margin:40px 0 24px; padding-left:15px; border-left:5px solid var(--tiffany);">出國網路</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:24px; margin-bottom:40px;">
      <div style="background:#fff; border-radius:16px; padding:30px; box-shadow:0 4px 24px rgba(10,186,181,0.12); border:2px solid var(--tiffany-light); transition:0.3s;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
          <div style="background:linear-gradient(135deg, #333 0%, #222 100%); width:50px; height:50px; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px;">📱</div>
          <h3 style="color:#333; font-size:20px;">Airalo eSIM</h3>
        </div>
        <p style="color:var(--text-gray); font-size:14px; line-height:1.8; margin-bottom:20px;">全球 eSIM 平台，免換卡、即買即用，日韓泰 eSIM 只要 NT$200 起。</p>
        <a href="https://www.airalo.com/" target="_blank" rel="noopener noreferrer sponsored" style="display:inline-block; background:linear-gradient(135deg, #333 0%, #222 100%); color:#fff; padding:10px 24px; border-radius:30px; font-size:14px; font-weight:500;">前往 Airalo →</a>
      </div>
    </div>

  </main>
</div>

<!-- FAQ Section with Tiffany styling -->
<section style="max-width:900px; margin:40px auto; padding:0 40px;">
  <h2 style="color:var(--tiffany-dark); margin-bottom:24px; padding-left:15px; border-left:5px solid var(--tiffany);">常見問題</h2>
  
  <div style="background:var(--tiffany-light); border-radius:14px; margin-bottom:16px; overflow:hidden; border:1px solid var(--tiffany-light);">
    <h3 style="padding:20px 24px; font-weight:600; cursor:pointer; display:flex; justify-content:space-between; align-items:center; background:#fff; margin:0;">
      <span style="color:var(--tiffany-dark);">Q: 出國旅行必備哪些 APP？</span>
      <span style="color:var(--tiffany); font-size:18px;">▼</span>
    </h3>
    <p style="padding:0 24px 20px; color:var(--text-gray); line-height:1.9; background:#fff;">Google Maps（導航）、Google Translate（翻譯）、Klook（門票預約）、Agoda（訂房）、Skyscanner（機票比價）是五大必裝 APP。</p>
  </div>
  
  <div style="background:var(--tiffany-light); border-radius:14px; margin-bottom:16px; overflow:hidden; border:1px solid var(--tiffany-light);">
    <h3 style="padding:20px 24px; font-weight:600; cursor:pointer; display:flex; justify-content:space-between; align-items:center; background:#fff; margin:0;">
      <span style="color:var(--tiffany-dark);">Q: eSIM 和 Wi-Fi 分享器哪個好？</span>
      <span style="color:var(--tiffany); font-size:18px;">▼</span>
    </h3>
    <p style="padding:0 24px 20px; color:var(--text-gray); line-height:1.9; background:#fff;">短期旅行（3-5天）推薦 Airalo eSIM，免租借、即買即用、約 NT$200-400。長期或多人同行用 Wi-Fi 分享器更划算。</p>
  </div>
  
  <div style="background:var(--tiffany-light); border-radius:14px; margin-bottom:16px; overflow:hidden; border:1px solid var(--tiffany-light);">
    <h3 style="padding:20px 24px; font-weight:600; cursor:pointer; display:flex; justify-content:space-between; align-items:center; background:#fff; margin:0;">
      <span style="color:var(--tiffany-dark);">Q: 旅遊保險一定要買嗎？</span>
      <span style="color:var(--tiffany); font-size:18px;">▼</span>
    </h3>
    <p style="padding:0 24px 20px; color:var(--text-gray); line-height:1.9; background:#fff;">強烈建議購買。醫療費用、班機延誤、行李遺失都能理賠。富邦、國泰等保險公司有專門的旅遊險，一天約 NT$100-200。</p>
  </div>
</section>

<!-- FOOTER -->
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col">
      <h4>日本自由行</h4>
      <ul>
        <li><a href="tokyo-5days.html">東京5天4夜</a></li>
        <li><a href="kansai-pass.html">關西交通票券</a></li>
        <li><a href="hokkaido-winter.html">北海道冬季</a></li>
        <li><a href="okinawa.html">沖繩自駕</a></li>
        <li><a href="kyoto-temples.html">京都寺廟</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>韓國自由行</h4>
      <ul>
        <li><a href="seoul-food.html">首爾美食</a></li>
        <li><a href="busan-capsule.html">釜山膠囊列車</a></li>
        <li><a href="jeju-island.html">濟州島自駕</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>台灣旅遊</h4>
      <ul>
        <li><a href="hualien-taitung.html">花東三天兩夜</a></li>
        <li><a href="tainan-food.html">台南美食</a></li>
        <li><a href="kenting.html">墾丁海景</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>東南亞自由行</h4>
      <ul>
        <li><a href="chiang-mai.html">清邁數位遊牧</a></li>
        <li><a href="bangkok-3days.html">曼谷吃貨攻略</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 均在路上 Travel Lab. All Rights Reserved.</p>
  </div>
    <div style="margin-top:8px;font-size:12px;">
      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>
      <a href="contact.html" style="color:inherit;margin-right:12px;">聯絡我們</a>
      <a href="privacy.html" style="color:inherit;">隱私權政策</a>
    </div>
  </div>
</footer>

</body>
</html>'''

# Write files
with open('about.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(about_new)
print('about.html updated')

with open('travel-tools.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(tools_new)
print('travel-tools.html updated')

print('Done!')
