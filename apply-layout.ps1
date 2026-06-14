# apply-layout.ps1 - Apply layout-standard.css to all article pages
# Run from Travel-Lab directory

$articles = @(
  "bangkok-3days.html",
  "bangkok-4days.html",
  "tokyo-5days.html",
  "seoul-5days.html",
  "osaka-food.html",
  "osaka-usj.html",
  "chiang-mai.html",
  "fukuoka-5days.html",
  "busan-4days.html",
  "jeju-island.html",
  "kyoto-temples.html",
  "singapore-3days.html",
  "kualalumpur-3days.html",
  "vietnam-danang.html",
  "vietnam-hochiminh.html",
  "angkor-wat-2days.html",
  "bangkok-massage.html",
  "hokkaido-winter.html",
  "okinawa.html",
  "hualien-taitung.html",
  "tainan-food.html",
  "kenting.html",
  "taipei-food.html",
  "jiufen.html"
)

$cityData = @{
  "bangkok-3days.html" = @{
    City = "曼谷"
    Subtitle = "泰國自由行攻略"
    SidebarImg = "images/bangkok-sidebar.webp"
    HeroImg = "images/bangkok-hero.webp"
    NavItems = @(
      @{Icon="🏛️"; Label="景點"; Anchor="景點"},
      @{Icon="🍜"; Label="美食"; Anchor="美食"},
      @{Icon="🛍️"; Label="購物"; Anchor="購物"},
      @{Icon="🚆"; Label="交通"; Anchor="交通"},
      @{Icon="🏨"; Label="住宿"; Anchor="住宿"},
      @{Icon="💡"; Label="實用資訊"; Anchor="實用資訊"}
    )
    TripLink = "https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"
    TripBanner = "images/trip-thailand.webp"
    KlookSection = "bangkok"
    RelatedArticles = @(
      @{Title="曼谷4天3夜攻略"; Url="bangkok-4days.html"; Img="images/bangkok-sidebar.webp"},
      @{Title="曼谷按摩推薦"; Url="bangkok-massage.html"; Img="images/bangkok-massage.webp"},
      @{Title="清邁數位遊牧"; Url="chiang-mai.html"; Img="images/chiang-mai.webp"},
      @{Title="新加坡3天2夜"; Url="singapore-3days.html"; Img="images/singapore-hero.webp"}
    )
  }
  "bangkok-4days.html" = @{
    City = "曼谷"
    Subtitle = "泰國自由行攻略"
    SidebarImg = "images/bangkok-sidebar.webp"
    HeroImg = "images/bangkok-hero.webp"
    NavItems = @(
      @{Icon="🏛️"; Label="景點"; Anchor="景點"},
      @{Icon="🍜"; Label="美食"; Anchor="美食"},
      @{Icon="🛍️"; Label="購物"; Anchor="購物"},
      @{Icon="🚆"; Label="交通"; Anchor="交通"},
      @{Icon="🏨"; Label="住宿"; Anchor="住宿"},
      @{Icon="💡"; Label="實用資訊"; Anchor="實用資訊"}
    )
    TripLink = "https://tw.trip.com/sale/w/26497/go-thailand.html?locale=zh-tw&curr=twd&promo_referer=3952_26497_7&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078987"
    TripBanner = "images/trip-thailand.webp"
    KlookSection = "bangkok"
    RelatedArticles = @(
      @{Title="曼谷3天2夜吃貨攻略"; Url="bangkok-3days.html"; Img="images/bangkok-hero.webp"},
      @{Title="曼谷按摩推薦"; Url="bangkok-massage.html"; Img="images/bangkok-massage.webp"},
      @{Title="清邁數位遊牧"; Url="chiang-mai.html"; Img="images/chiang-mai.webp"},
      @{Title="吳哥窟2天1夜"; Url="angkor-wat-2days.html"; Img="images/angkor-wat.webp"}
    )
  }
  "tokyo-5days.html" = @{
    City = "東京"
    Subtitle = "日本自由行攻略"
    SidebarImg = "images/tokyo-sidebar.webp"
    HeroImg = "images/tokyo-hero.webp"
    NavItems = @(
      @{Icon="🏛️"; Label="景點"; Anchor="景點"},
      @{Icon="🍜"; Label="美食"; Anchor="美食"},
      @{Icon="🛍️"; Label="購物"; Anchor="購物"},
      @{Icon="🚆"; Label="交通"; Anchor="交通"},
      @{Icon="🏨"; Label="住宿"; Anchor="住宿"},
      @{Icon="💡"; Label="實用資訊"; Anchor="實用資訊"}
    )
    TripLink = "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"
    TripBanner = "images/trip-japan.webp"
    KlookSection = "tokyo"
    RelatedArticles = @(
      @{Title="大阪美食攻略"; Url="osaka-food.html"; Img="images/osaka-food.webp"},
      @{Title="京都寺廟地圖"; Url="kyoto-temples.html"; Img="images/kyoto-temples.webp"},
      @{Title="北海道賞雪"; Url="hokkaido-winter.html"; Img="images/hokkaido-winter.webp"},
      @{Title="東京住宿推薦"; Url="tokyo-accommodation.html"; Img="images/tokyo-hero.webp"}
    )
  }
  "seoul-5days.html" = @{
    City = "首爾"
    Subtitle = "韓國自由行攻略"
    SidebarImg = "images/seoul-sidebar.webp"
    HeroImg = "images/seoul-hero.webp"
    NavItems = @(
      @{Icon="🏛️"; Label="景點"; Anchor="景點"},
      @{Icon="🍜"; Label="美食"; Anchor="美食"},
      @{Icon="🛍️"; Label="購物"; Anchor="購物"},
      @{Icon="🚆"; Label="交通"; Anchor="交通"},
      @{Icon="🏨"; Label="住宿"; Anchor="住宿"},
      @{Icon="💡"; Label="實用資訊"; Anchor="實用資訊"}
    )
    TripLink = "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"
    TripBanner = "images/trip-japan.webp"
    KlookSection = "seoul"
    RelatedArticles = @(
      @{Title="釜山4天3夜"; Url="busan-4days.html"; Img="images/busan-hero.webp"},
      @{Title="首爾美食攻略"; Url="seoul-food.html"; Img="images/seoul-food.webp"},
      @{Title="濟州島自駕"; Url="jeju-island.html"; Img="images/jeju-island.webp"},
      @{Title="首爾美食地圖"; Url="seoul-food-map.html"; Img="images/seoul-food-map.webp"}
    )
  }
  "osaka-food.html" = @{
    City = "大阪"
    Subtitle = "日本美食攻略"
    SidebarImg = "images/osaka-food-sidebar.webp"
    HeroImg = "images/osaka-food-hero.webp"
    NavItems = @(
      @{Icon="🍜"; Label="道頓堀"; Anchor="道頓堀"},
      @{Icon="🍰"; Label="甜點"; Anchor="甜點"},
      @{Icon="🏛️"; Label="地下街"; Anchor="地下街"},
      @{Icon="🚆"; Label="交通"; Anchor="交通"},
      @{Icon="🏨"; Label="住宿"; Anchor="住宿"},
      @{Icon="💡"; Label="實用資訊"; Anchor="實用資訊"}
    )
    TripLink = "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"
    TripBanner = "images/trip-japan.webp"
    KlookSection = "osaka"
    RelatedArticles = @(
      @{Title="大阪環球影城"; Url="osaka-usj.html"; Img="images/osaka-usj.webp"},
      @{Title="東京5天4夜"; Url="tokyo-5days.html"; Img="images/tokyo-hero.webp"},
      @{Title="京都寺廟地圖"; Url="kyoto-temples.html"; Img="images/kyoto-temples.webp"},
      @{Title="神戶牛排推薦"; Url="japan-travel.html"; Img="images/japan-travel.webp"}
    )
  }
  "osaka-usj.html" = @{
    City = "大阪"
    Subtitle = "環球影城攻略"
    SidebarImg = "images/osaka-usj-sidebar.webp"
    HeroImg = "images/osaka-usj-hero.webp"
    NavItems = @(
      @{Icon="🎢"; Label="設施"; Anchor="設施"},
      @{Icon="🎫"; Label="門票"; Anchor="門票"},
      @{Icon="🏨"; Label="Express"; Anchor="Express"},
      @{Icon="🍜"; Label="美食"; Anchor="美食"},
      @{Icon="💡"; Label="實用資訊"; Anchor="實用資訊"},
      @{Icon="🚆"; Label="交通"; Anchor="交通"}
    )
    TripLink = "https://tw.trip.com/sale/w/4217/japan-travel.html?locale=zh_tw&promo_referer=3952_4217_9&Allianceid=8237671&SID=312406690&trip_sub1=&trip_sub3=P17078945n"
    TripBanner = "images/trip-japan.webp"
    KlookSection = "osaka"
    RelatedArticles = @(
      @{Title="大阪美食攻略"; Url="osaka-food.html"; Img="images/osaka-food.webp"},
      @{Title="東京5天4夜"; Url="tokyo-5days.html"; Img="images/tokyo-hero.webp"},
      @{Title="京都寺廟地圖"; Url="kyoto-temples.html"; Img="images/kyoto-temples.webp"},
      @{Title="神戶牛排推薦"; Url="japan-travel.html"; Img="images/japan-travel.webp"}
    )
  }
}

# Fallback data for articles not in cityData
$defaultCity = @{
  City = "旅遊攻略"
  Subtitle = "自由行攻略"
  SidebarImg = "images/placeholder.webp"
  HeroImg = "images/placeholder-hero.webp"
  NavItems = @(
    @{Icon="🏛️"; Label="景點"; Anchor="景點"},
    @{Icon="🍜"; Label="美食"; Anchor="美食"},
    @{Icon="🛍️"; Label="購物"; Anchor="購物"},
    @{Icon="🚆"; Label="交通"; Anchor="交通"},
    @{Icon="🏨"; Label="住宿"; Anchor="住宿"},
    @{Icon="💡"; Label="實用資訊"; Anchor="實用資訊"}
  )
  TripLink = "https://tw.trip.com"
  TripBanner = "images/trip-thailand.webp"
  KlookSection = "travel"
  RelatedArticles = @(
    @{Title="相關文章"; Url="index.html"; Img="images/placeholder.webp"},
    @{Title="相關文章"; Url="index.html"; Img="images/placeholder.webp"},
    @{Title="相關文章"; Url="index.html"; Img="images/placeholder.webp"},
    @{Title="相關文章"; Url="index.html"; Img="images/placeholder.webp"}
  )
}

# Function to build sidebar HTML
function Build-SidebarHTML($data) {
  $navItems = ""
  foreach ($item in $data.NavItems) {
    $navItems += @"
    <a class="ls-sidebar-nav-item" href="#$($item.Anchor)">
      <span class="ls-sidebar-nav-icon">$($item.Icon)</span>
      <span class="ls-sidebar-nav-label">$($item.Label)</span>
    </a>
"@
  }
  
  $sidebar = @"
<aside class="ls-sidebar">
<div class="ls-sidebar-card">
<a href="travel-tools.html">
<img alt="$($data.City)攻略" class="ls-sidebar-hero" loading="lazy" src="$($data.SidebarImg)"/>
</a>
<div class="ls-sidebar-header">
<div class="ls-sidebar-city">$($data.City)</div>
<div class="ls-sidebar-sub">$($data.Subtitle)</div>
</div>
<nav class="ls-sidebar-nav">
$navItems
</nav>
<div class="ls-sidebar-qr">
<div class="ls-sidebar-qr-title">📱 追蹤我們</div>
<img alt="LINE QR" src="images/line-qr.webp"/>
<div class="ls-sidebar-qr-desc">掃描 LINE 取得最新旅遊資訊</div>
</div>
<a class="ls-sidebar-cta" href="travel-tools.html">📂 下載攻略 PDF</a>
</div>
</aside>
"@
  return $sidebar
}

# Function to build Trip promo HTML
function Build-TripPromo($link, $banner) {
  return @"
<!-- BLOCK 6: Trip.com Promo -->
<div class="ls-trip-promo">
<div class="ls-trip-promo-title">✈️ 機票搜尋比價</div>
<div class="ls-trip-promo-desc">早鳥優惠，搶先預訂省更多</div>
<a class="ls-trip-promo-btn" href="$link" target="_blank" rel="noopener nofollow sponsored">立即搜尋 →</a>
</div>
"@
}

# Process each article
foreach ($article in $articles) {
  $path = ".\$article"
  if (Test-Path $path) {
    Write-Host "Processing $article..."
    $content = Get-Content $path -Raw -Encoding UTF8
    
    # Check if layout-standard.css is already linked
    if ($content -notmatch 'layout-standard\.css') {
      # Add CSS link after existing CSS links
      $content = $content -replace '(</head>)', '<link href="layout-standard.css" rel="stylesheet"/>`n$1'
    }
    
    # Update sidebar structure if old sidebar exists
    if ($content -match '<div class="sidebar-card">') {
      $data = if ($cityData.ContainsKey($article)) { $cityData[$article] } else { $defaultCity }
      $newSidebar = Build-SidebarHTML $data
      
      # Replace old sidebar with new one
      $pattern = '<div class="sidebar-card">[\s\S]*?</div>\s*</div>\s*<div class="col-center">'
      $replacement = "$newSidebar`n<div class=""col-center"">"
      $content = $content -replace $pattern, $replacement
    }
    
    # Add ls- classes to article content
    $content = $content -replace '<div class="article-container">', '<div class="article-container ls-article-content">'
    $content = $content -replace '<div class="day-card">', '<div class="day-card ls-day-card">'
    $content = $content -replace '<div class="tip-box">', '<div class="tip-box ls-tip-box">'
    
    # Update charter banner with ls- class
    $content = $content -replace '<div style="max-width:900px;margin:0 auto 30px;padding:0 20px;">', '<div class="ls-charter-banner">'
    $content = $content -replace '(?s)<div class="ls-charter-banner">.*?</div>\s*<div', "$newSidebar`n<div"
    
    Set-Content -Path $path -Value $content -Encoding UTF8
    Write-Host "  ✓ Updated $article"
  } else {
    Write-Host "  ✗ Not found: $article"
  }
}

Write-Host "`nDone! All article pages updated."