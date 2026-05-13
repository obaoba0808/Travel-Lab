# -*- coding: utf-8 -*-
"""
Batch rebuild script for Travel Lab website
Removes inline CSS, adds style.css link, updates HTML structure
"""

import re
import os

# Page configurations
PAGES = {
    'korea-travel.html': {
        'title': '韓國自由行攻略｜均在路上 Travel Lab',
        'description': '韓國自由行吃貨指南：首爾明洞弘大美食攻略、釜山海雲台膠囊列車預約教學，最划算換錢與交通卡推薦。',
        'keywords': '韓國自由行,首爾攻略,釜山旅遊,韓國美食,明洞弘大,海雲台膠囊列車,韓國換錢,T-money卡',
        'hero_title': '韓國自由行吃貨指南',
        'hero_subtitle': '首爾、釜山、濟州島必吃烤肉、打卡咖啡廳與最新流行服飾逛街地圖。',
        'hero_image': 'https://images.unsplash.com/photo-1517154421773-0529f29ea451?auto=format&fit=crop&w=1920&q=80',
        'nav_active': 'korea-travel.html',
        'articles': [
            ('seoul-food.html', '【首爾必吃美食】明洞、弘大攻略', '醬蟹、烤五花肉、人參雞湯！首爾必吃清單懶人包與換錢所推薦。', 'https://images.unsplash.com/photo-1538681105587-85640961bf8b?auto=format&fit=crop&w=600&q=80'),
            ('busan-capsule.html', '【釜山膠囊列車】海雲台預約教學', '釜山海雲台膠囊列車預約流程、最佳搭乘時間與周邊景點推薦。', 'https://images.unsplash.com/photo-1517154421773-0529f29ea451?auto=format&fit=crop&w=600&q=80'),
            ('jeju-island.html', '【濟州島自駕】環島3天2夜攻略', '濟州島自駕環島路線、必去景點與美食推薦，機車租車教學。', 'https://images.unsplash.com/photo-1559128010-7c1ad6e1b6a5?auto=format&fit=crop&w=600&q=80'),
        ]
    },
    'taiwan-travel.html': {
        'title': '台灣旅遊攻略｜均在路上 Travel Lab',
        'description': '台灣深度旅遊提案：花東縱谷三天兩夜、台南美食牛肉湯、墾丁海景夜市，本地人帶路私房景點。',
        'keywords': '台灣旅遊,花東旅遊,台南美食,墾丁旅遊,台灣自由行,花蓮台東,台南牛肉湯',
        'hero_title': '台灣深度旅遊提案',
        'hero_subtitle': '花東縱谷、台南古城、墾丁海景，本地人帶路私房景點。',
        'hero_image': 'https://images.unsplash.com/photo-1470004914212-05527e49370b?auto=format&fit=crop&w=1920&q=80',
        'nav_active': 'taiwan-travel.html',
        'articles': [
            ('hualien-taitung.html', '【花東三天兩夜】縱谷慢旅行', '花蓮台東縱谷線、海岸線景點推薦，住宿與交通攻略。', 'https://images.unsplash.com/photo-1470004914212-05527e49370b?auto=format&fit=crop&w=600&q=80'),
            ('tainan-food.html', '【台南美食】牛肉湯與國華街', '台南必吃牛肉湯、國華街小吃、老屋咖啡廳推薦。', 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80'),
            ('kenting.html', '【墾丁三天兩夜】海景與夜市', '墾丁必去沙灘、龍磐公園、鵝鑾鼻與夜市美食推薦。', 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80'),
        ]
    },
    'southeast-asia.html': {
        'title': '東南亞自由行攻略｜均在路上 Travel Lab',
        'description': '東南亞自由行：泰國曼谷吃貨攻略、清邁數位遊牧、越南、柬埔寨簽證與交通完整指南。',
        'keywords': '東南亞自由行,泰國旅遊,曼谷攻略,清邁數位遊牧,越南旅遊,柬埔寨簽證',
        'hero_title': '東南亞自由行',
        'hero_subtitle': '泰國、越南、柬埔寨，簽證、交通、美食一次搞定。',
        'hero_image': 'https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1920&q=80',
        'nav_active': 'southeast-asia.html',
        'articles': [
            ('chiang-mai.html', '【清邁數位遊牧】7天生活指南', '清邁咖啡廳、長租公寓、簽證與網路推薦，數位遊牧必備攻略。', 'https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=600&q=80'),
            ('bangkok-3days.html', '【曼谷3天2夜】吃貨攻略', '洽圖洽週末市集、唐人街、10大必吃美食推薦。', 'https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=600&q=80'),
        ]
    },
    'travel-tools.html': {
        'title': '旅遊工具推薦｜均在路上 Travel Lab',
        'description': '旅遊省錢工具包：Agoda訂房、Klook景點門票、Skyscanner機票比價、Airalo eSIM，出國必備懶人包。',
        'keywords': '旅遊工具,Agoda,Klook,Skyscanner,eSIM,旅遊保險,機票比價,訂房優惠',
        'hero_title': '旅遊省錢工具包',
        'hero_subtitle': '機票、住宿、門票、網路，出國必備懶人包。',
        'hero_image': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1920&q=80',
        'nav_active': 'travel-tools.html',
        'articles': []
    },
}

def build_category_page(config, filename):
    """Build a category page HTML"""
    
    html = f'''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="UTF-8">
<title>{config['title']}</title>
<meta name="description" content="{config['description']}">
<meta name="keywords" content="{config['keywords']}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="https://obaoba0808.github.io/Travel-Lab/{filename}">
<meta name="robots" content="index, follow">
<link rel="alternate" hreflang="zh-Hant" href="https://obaoba0808.github.io/Travel-Lab/{filename}">
<link rel="alternate" hreflang="zh-TW" href="https://obaoba0808.github.io/Travel-Lab/{filename}">
<link rel="alternate" hreflang="x-default" href="https://obaoba0808.github.io/Travel-Lab/{filename}">

<!-- Open Graph -->
<meta property="og:title" content="{config['hero_title']}｜均在路上 Travel Lab">
<meta property="og:description" content="{config['description']}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://obaoba0808.github.io/Travel-Lab/{filename}">
<meta property="og:image" content="{config['hero_image']}">
<meta property="og:site_name" content="均在路上 Travel Lab">
<meta property="og:locale" content="zh_TW">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{config['hero_title']}｜均在路上 Travel Lab">
<meta name="twitter:description" content="{config['description']}">
<meta name="twitter:image" content="{config['hero_image']}">

<!-- JSON-LD -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "{config['hero_title']}",
  "description": "{config['description']}",
  "url": "https://obaoba0808.github.io/Travel-Lab/{filename}",
  "isPartOf": {{
    "@type": "WebSite",
    "name": "均在路上 Travel Lab",
    "url": "https://obaoba0808.github.io/Travel-Lab/"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://obaoba0808.github.io/Travel-Lab/"}},
    {{"@type": "ListItem", "position": 2, "name": "{config['hero_title']}", "item": "https://obaoba0808.github.io/Travel-Lab/{filename}"}}
  ]
}}
</script>

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">

<!-- Stylesheet -->
<link rel="stylesheet" href="style.css">

<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S7KQGHSD2R"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-S7KQGHSD2R');
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
      <a href="travel-tools.html">旅遊工具</a>
    </nav>
  </div>
</div>

<!-- SITE BRANDING -->
<div class="site-branding">
  <h1>均在路上 <span>Travel Lab</span></h1>
  <p>用最少預算，走最多地方的實戰旅遊攻略</p>
</div>

<!-- CATEGORY HERO -->
<div class="category-hero" style="background-image: url('{config['hero_image']}');">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>{config['hero_title']}</h1>
    <p>{config['hero_subtitle']}</p>
  </div>
</div>

<!-- MAIN CONTENT -->
<div class="site-content">
  <main class="content-area">
    <h2 class="section-title">最新文章</h2>
    <div class="posts-grid">'''

    # Add article cards
    for article in config['articles']:
        html += f'''
      <article class="card">
        <div class="card-image">
          <img src="{article[3]}" alt="{article[1]}">
        </div>
        <div class="card-content">
          <h3><a href="{article[0]}">{article[1]}</a></h3>
          <p>{article[2]}</p>
          <a href="{article[0]}" class="btn btn-primary">閱讀文章</a>
        </div>
      </article>'''

    html += '''
    </div>
  </main>

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sidebar-widget">
      <h3>分類導覽</h3>
      <ul>
        <li><a href="japan-travel.html">日本自由行</a></li>
        <li><a href="korea-travel.html">韓國自由行</a></li>
        <li><a href="taiwan-travel.html">台灣旅遊</a></li>
        <li><a href="southeast-asia.html">東南亞自由行</a></li>
        <li><a href="travel-tools.html">旅遊工具推薦</a></li>
      </ul>
    </div>

    <div class="sidebar-widget">
      <h3>熱門文章</h3>
      <ul>
        <li><a href="tokyo-5days.html">東京5天4夜行程攻略</a></li>
        <li><a href="seoul-food.html">首爾必吃美食清單</a></li>
        <li><a href="okinawa.html">沖繩自駕攻略</a></li>
      </ul>
    </div>

    <div class="sidebar-widget">
      <h3>優惠工具</h3>
      <ul>
        <li><a href="https://www.agoda.com/zh-tw" target="_blank" rel="noopener noreferrer">Agoda 訂房優惠</a></li>
        <li><a href="https://www.klook.com/zh-TW/" target="_blank" rel="noopener noreferrer">Klook 門票折扣</a></li>
        <li><a href="https://www.skyscanner.com.tw/" target="_blank" rel="noopener noreferrer">Skyscanner 機票比價</a></li>
        <li><a href="https://www.airalo.com/" target="_blank" rel="noopener noreferrer">Airalo eSIM</a></li>
      </ul>
    </div>
  </aside>
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
    <p>© 2026 均在路上 Travel Lab. All Rights Reserved.</p>
  </div>
</footer>

</body>
</html>'''
    
    return html

# Main execution
if __name__ == '__main__':
    print('Starting batch rebuild...')
    
    for filename, config in PAGES.items():
        print(f'Building {filename}...')
        html = build_category_page(config, filename)
        
        # Write using the proper method
        output_path = filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f'  OK {filename} written ({len(html)} bytes)')
    
    print('\\nCategory pages rebuilt successfully!')
    print('Now need to rebuild article pages...')
