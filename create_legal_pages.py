#!/usr/bin/env python3
"""Create terms.html and disclaimer.html legal pages"""
import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# ── Terms of Use ──
terms_html = '''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="UTF-8">
<title>使用條款｜均在路上 Travel Lab</title>
<meta name="description" content="均在路上 Travel Lab 使用條款。請在使用本網站前仔細閱讀，了解您的權利與義務。">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://golightly.fun/terms.html">
<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/terms.html">
<link rel="alternate" hreflang="zh-TW" href="https://golactly.fun/terms.html">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/terms.html">
<meta property="og:title" content="使用條款｜均在路上 Travel Lab">
<meta property="og:description" content="均在路上 Travel Lab 使用條款。">
<meta property="og:type" content="website">
<meta property="og:url" content="https://golightly.fun/terms.html">
<meta property="og:site_name" content="均在路上 Travel Lab">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebPage","name":"使用條款","url":"https://golightly.fun/terms.html"}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✈️</text></svg>">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S7KQGHSD2R"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-S7KQGHSD2R');
</script>
</head>
<body>

<!-- TOP BAR -->
<div class="site-topbar">
  <div class="topbar-inner">
    <button class="mobile-toggle" onclick="document.querySelector('.main-nav').classList.toggle('open')">☰</button>
    <nav class="main-nav">
      <a href="index.html">首頁</a>
      <div class="nav-dropdown">
        <a href="japan-travel.html">日本自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="tokyo-5days.html">東京5天4夜行程</a>
          <a href="kansai-pass.html">關西交通票券指南</a>
          <a href="hokkaido-winter.html">北海道冬季賞雪</a>
          <a href="okinawa.html">沖繩自駕攻略</a>
          <a href="kyoto-temples.html">京都寺廟散步地圖</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="korea-travel.html">韓國自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="seoul-food.html">首爾必吃美食攻略</a>
          <a href="busan-capsule.html">釜山膠囊列車預約</a>
          <a href="jeju-island.html">濟州島自駕環島</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="taiwan-travel.html">台灣旅遊 ▾</a>
        <div class="dropdown-menu">
          <a href="hualien-taitung.html">花東三天兩夜</a>
          <a href="tainan-food.html">台南美食牛肉湯</a>
          <a href="kenting.html">墾丁海景夜市攻略</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="southeast-asia.html">東南亞自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="chiang-mai.html">清邁數位遊牧指南</a>
          <a href="bangkok-3days.html">曼谷吃貨攻略</a>
        </div>
      </div>
      <a href="travel-tools.html">旅遊工具</a>
      <a href="about.html">關於我們</a>
    </nav>
    <div style="font-size:13px;color:var(--text-light);">✈ 用最少預算，走最多地方</div>
  </div>
</div>

<!-- PAGE HEADER -->
<div style="background:linear-gradient(135deg, #e8f4f8 0%, #f9fcfb 100%); border-bottom:3px solid var(--tiffany); padding:40px 20px; text-align:center;">
  <h1 style="font-family:'Noto Serif TC',serif; font-size:32px; color:#1a1a2e; margin-bottom:8px;">使用條款</h1>
  <p style="color:var(--text-gray); font-size:14px;">Terms of Service · 最後更新：2026年5月</p>
</div>

<!-- CONTENT -->
<div style="max-width:800px; margin:0 auto; padding:40px 20px;">
  <div style="background:#fff; border-radius:12px; padding:40px; box-shadow:0 2px 15px rgba(0,0,0,0.06);">

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">一、服務說明</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      均在路上 Travel Lab（以下簡稱「本網站」）為旅遊資訊內容平台，提供日本、韓國、台灣、東南亞等地的自由行攻略、行程建議與工具推薦。本網站所有內容僅供參考，不構成任何形式的旅遊建議或契約。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">二、智慧財產權</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站所有文章、圖片、圖表、程式碼及設計，均為均在路上 Travel Lab 原創或經合法授權，版權歸本網站所有。未经明确授权，任何人不得以任何形式复制、转载、改编或用于商业目的。如需引用或分享，请注明出处并保留原文链接。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">三、資訊準確性</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站致力於提供準確、最新的旅遊資訊，但無法保證所有內容（價格、時間、路線、店家資訊）皆為最新或完全準確。旅遊資訊可能因季節、政策或店家變動而改變，讀者應在出發前自行向相關單位確認。本網站不對任何因資訊過時所导致的损失承担责任。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">四、第三方連結</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站可能包含通往第三方網站（機票比價、訂房平台、預約系統等）的連結。這些連結僅為便利讀者，本網站不對第三方網站的內容、服務或隱私政策負責。建議在使用第三方服務前詳閱其使用條款與隱私權政策。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">五、免責聲明</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站不對以下情形承擔任何責任：（一）因使用本網站資訊而导致的任何損失或傷害；（二）第三方廣告或推廣內容的準確性；（三）任何因不可抗力（如天災、罷工、疫情等）導致的行程變更或取消；（四）讀者自行做出的旅遊決策所產生的後果。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">六、隱私保護</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站重視您的隱私。我們僅透過 Google Analytics 收集匿名流量數據，以改善網站體驗。本網站不使用Cookie進行追蹤。如需了解更多，請參閱我們的<a href="privacy.html" style="color:var(--tiffany-dark); font-weight:600;">隱私權政策</a>。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">七、修改權利</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站保留隨時修改本使用條款的權利，修改後的條款於公告時生效。建議您定期查閱本頁面，以了解最新條款。如您繼續使用本網站，即表示您接受修改後的條款。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">八、聯絡方式</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9;">
      如對本使用條款有任何疑問，歡迎<a href="about.html" style="color:var(--tiffany-dark); font-weight:600;">透過關於我們頁面</a>與我們聯絡。
    </p>

  </div>
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
      <h4>法律資訊</h4>
      <ul>
        <li><a href="privacy.html">隱私權政策</a></li>
        <li><a href="terms.html">使用條款</a></li>
        <li><a href="disclaimer.html">免責聲明</a></li>
        <li><a href="about.html">關於我們</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 均在路上 Travel Lab. All Rights Reserved.</p>
    <div style="margin-top:8px;font-size:12px;">
      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>
      <a href="privacy.html" style="color:inherit;margin-right:12px;">隱私權政策</a>
      <a href="terms.html" style="color:inherit;margin-right:12px;">使用條款</a>
      <a href="disclaimer.html" style="color:inherit;">免責聲明</a>
    </div>
  </div>
</footer>

</body>
</html>'''

# ── Disclaimer ──
disclaimer_html = '''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="UTF-8">
<title>免責聲明｜均在路上 Travel Lab</title>
<meta name="description" content="均在路上 Travel Lab 免責聲明。本網站所有內容僅供參考，不構成旅遊建議，使用者請自行承擔使用風險。">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://golightly.fun/disclaimer.html">
<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/disclaimer.html">
<link rel="alternate" hreflang="zh-TW" href="https://golightly.fun/disclaimer.html">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/disclaimer.html">
<meta property="og:title" content="免責聲明｜均在路上 Travel Lab">
<meta property="og:description" content="均在路上 Travel Lab 免責聲明。">
<meta property="og:type" content="website">
<meta property="og:url" content="https://golightly.fun/disclaimer.html">
<meta property="og:site_name" content="均在路上 Travel Lab">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebPage","name":"免責聲明","url":"https://golightly.fun/disclaimer.html"}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✈️</text></svg>">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S7KQGHSD2R"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-S7KQGHSD2R');
</script>
</head>
<body>

<!-- TOP BAR -->
<div class="site-topbar">
  <div class="topbar-inner">
    <button class="mobile-toggle" onclick="document.querySelector('.main-nav').classList.toggle('open')">☰</button>
    <nav class="main-nav">
      <a href="index.html">首頁</a>
      <div class="nav-dropdown">
        <a href="japan-travel.html">日本自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="tokyo-5days.html">東京5天4夜行程</a>
          <a href="kansai-pass.html">關西交通票券指南</a>
          <a href="hokkaido-winter.html">北海道冬季賞雪</a>
          <a href="okinawa.html">沖繩自駕攻略</a>
          <a href="kyoto-temples.html">京都寺廟散步地圖</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="korea-travel.html">韓國自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="seoul-food.html">首爾必吃美食攻略</a>
          <a href="busan-capsule.html">釜山膠囊列車預約</a>
          <a href="jeju-island.html">濟州島自駕環島</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="taiwan-travel.html">台灣旅遊 ▾</a>
        <div class="dropdown-menu">
          <a href="hualien-taitung.html">花東三天兩夜</a>
          <a href="tainan-food.html">台南美食牛肉湯</a>
          <a href="kenting.html">墾丁海景夜市攻略</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="southeast-asia.html">東南亞自由行 ▾</a>
        <div class="dropdown-menu">
          <a href="chiang-mai.html">清邁數位遊牧指南</a>
          <a href="bangkok-3days.html">曼谷吃貨攻略</a>
        </div>
      </div>
      <a href="travel-tools.html">旅遊工具</a>
      <a href="about.html">關於我們</a>
    </nav>
    <div style="font-size:13px;color:var(--text-light);">✈ 用最少預算，走最多地方</div>
  </div>
</div>

<!-- PAGE HEADER -->
<div style="background:linear-gradient(135deg, #e8f4f8 0%, #f9fcfb 100%); border-bottom:3px solid var(--tiffany); padding:40px 20px; text-align:center;">
  <h1 style="font-family:'Noto Serif TC',serif; font-size:32px; color:#1a1a2e; margin-bottom:8px;">免責聲明</h1>
  <p style="color:var(--text-gray); font-size:14px;">Disclaimer · 最後更新：2026年5月</p>
</div>

<!-- CONTENT -->
<div style="max-width:800px; margin:0 auto; padding:40px 20px;">
  <div style="background:#fff; border-radius:12px; padding:40px; box-shadow:0 2px 15px rgba(0,0,0,0.06);">

    <div style="background:#fff3cd; border:1px solid #ffeeba; border-radius:8px; padding:16px 20px; margin-bottom:30px; font-size:14px; color:#856404; line-height:1.7;">
      <strong>⚠️ 重要提醒：</strong>本網站所有內容僅為個人旅遊經驗分享，不構成專業旅遊建議。使用本網站資訊前，請自行評估風險並向相關單位確認最新資訊。
    </div>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">一、資訊變動風險</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      旅遊資訊具有時效性。本網站所提及的門票價格、開放時間、交通路線、店家营业状态等，均為我們上次造訪時的記錄，可能已有變動。我們會尽可能定期更新，但不保證資訊的即時準確性。如有疑問，請直接聯繫相關單位或查詢官方網站。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">二、行程決策責任</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站不對使用者因參考本網站資訊所做的任何旅遊決策承擔責任。包括但不限於：機票與住宿的預訂取消或變更費用、簽證申請結果、簽證費用的任何損失、因路線變動而產生的額外交通費用、以及任何因行程變更而导致的損失。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">三、第三方服務</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站推薦的第三方服務（機票比價平台、訂房網站、景點門票預約等）均由各該第三方運營，我們不對其服務品質、價格變動、用戶體驗或任何糾紛負責。使用第三方服務前，請詳閱其條款與條件。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">四、安全與意外</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站不對任何在旅遊過程中發生的意外、傷害、財產損失或延誤負責。建議讀者在出發前購買適合的旅遊保險，並隨時關注外交部及相關單位的旅遊警示訊息。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">五、不可抗力</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      如因天災（颱風、地震、火山噴發等）、戰爭、罷工、疫情、政府政策、航班取消或其他不可抗力因素導致行程無法執行，本網站不對此承擔任何責任。建議旅客預留彈性緩冲時間，並购买相關旅遊不便險。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">六、廣告與贊助</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9; margin-bottom:20px;">
      本網站側邊欄及工具頁可能包含聯盟行銷連結與贊助內容。我們會明確標記「讀者專屬優惠」或「Sponsored」標示，但無法對第三方廣主的商品或服務質量負責。所有廣告內容不代表本網站立場。
    </p>

    <h2 style="color:var(--tiffany-dark); font-size:20px; margin-bottom:16px; padding-bottom:10px; border-bottom:2px solid var(--tiffany-light);">七、意見與建議</h2>
    <p style="color:var(--text-gray); font-size:15px; line-height:1.9;">
      如您發現本網站有任何資訊需要更新或有建議，歡迎透過<a href="https://line.me/ti/g/NbNGnW4Eh6" target="_blank" rel="noopener" style="color:var(--tiffany-dark); font-weight:600;">LINE 群組</a>與我們聯絡，我們會盡快核實並更新。
    </p>

  </div>
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
      <h4>法律資訊</h4>
      <ul>
        <li><a href="privacy.html">隱私權政策</a></li>
        <li><a href="terms.html">使用條款</a></li>
        <li><a href="disclaimer.html">免責聲明</a></li>
        <li><a href="about.html">關於我們</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 均在路上 Travel Lab. All Rights Reserved.</p>
    <div style="margin-top:8px;font-size:12px;">
      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>
      <a href="privacy.html" style="color:inherit;margin-right:12px;">隱私權政策</a>
      <a href="terms.html" style="color:inherit;margin-right:12px;">使用條款</a>
      <a href="disclaimer.html" style="color:inherit;">免責聲明</a>
    </div>
  </div>
</footer>

</body>
</html>'''

with open('terms.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(terms_html)
print('terms.html created')

with open('disclaimer.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(disclaimer_html)
print('disclaimer.html created')