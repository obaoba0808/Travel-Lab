# batch-apply-layout-v2.ps1 - Apply layout-standard.css to all article pages
# Uses ASCII-safe identifiers, Chinese text in separate hashtable

$repoPath = "C:\Users\FH01\Travel-Lab"
$articles = @(
  "bangkok-3days.html","bangkok-4days.html","tokyo-5days.html","seoul-5days.html",
  "osaka-food.html","osaka-usj.html","chiang-mai.html","fukuoka-5days.html",
  "busan-4days.html","jeju-island.html","kyoto-temples.html","singapore-3days.html",
  "kualalumpur-3days.html","vietnam-danang.html","vietnam-hochiminh.html",
  "angkor-wat-2days.html","bangkok-massage.html","hokkaido-winter.html",
  "okinawa.html","hualien-taitung.html","tainan-food.html","kenting.html",
  "taipei-food.html","jiufen.html"
)

# City name mappings (ID -> Chinese name)
$cityNames = @{
  "bangkok-3days.html" = "曼谷"
  "bangkok-4days.html" = "曼谷"
  "tokyo-5days.html" = "東京"
  "seoul-5days.html" = "首爾"
  "osaka-food.html" = "大阪"
  "osaka-usj.html" = "大阪"
  "chiang-mai.html" = "清邁"
  "fukuoka-5days.html" = "福岡"
  "busan-4days.html" = "釜山"
  "jeju-island.html" = "濟州島"
  "kyoto-temples.html" = "京都"
  "singapore-3days.html" = "新加坡"
  "kualalumpur-3days.html" = "吉隆坡"
  "vietnam-danang.html" = "峴港"
  "vietnam-hochiminh.html" = "胡志明"
  "angkor-wat-2days.html" = "吳哥窟"
  "bangkok-massage.html" = "曼谷"
  "hokkaido-winter.html" = "北海道"
  "okinawa.html" = "沖繩"
  "hualien-taitung.html" = "花東"
  "tainan-food.html" = "台南"
  "kenting.html" = "墾丁"
  "taipei-food.html" = "台北"
  "jiufen.html" = "九份"
}

# Sidebar image mappings
$sidebarImages = @{
  "bangkok-3days.html" = "images/bangkok-sidebar.webp"
  "bangkok-4days.html" = "images/bangkok-sidebar.webp"
  "tokyo-5days.html" = "images/tokyo-sidebar.webp"
  "seoul-5days.html" = "images/seoul-sidebar.webp"
  "osaka-food.html" = "images/osaka-food-sidebar.webp"
  "osaka-usj.html" = "images/osaka-usj-sidebar.webp"
  "chiang-mai.html" = "images/chiang-mai-sidebar.webp"
  "fukuoka-5days.html" = "images/fukuoka-sidebar.webp"
  "busan-4days.html" = "images/busan-sidebar.webp"
  "jeju-island.html" = "images/jeju-sidebar.webp"
  "kyoto-temples.html" = "images/kyoto-sidebar.webp"
  "singapore-3days.html" = "images/singapore-sidebar.webp"
  "kualalumpur-3days.html" = "images/kualalumpur-sidebar.webp"
  "vietnam-danang.html" = "images/danang-sidebar.webp"
  "vietnam-hochiminh.html" = "images/hochiminh-sidebar.webp"
  "angkor-wat-2days.html" = "images/angkor-sidebar.webp"
  "bangkok-massage.html" = "images/bangkok-massage.webp"
  "hokkaido-winter.html" = "images/hokkaido-sidebar.webp"
  "okinawa.html" = "images/okinawa-sidebar.webp"
  "hualien-taitung.html" = "images/hualien-sidebar.webp"
  "tainan-food.html" = "images/tainan-food.webp"
  "kenting.html" = "images/kenting-sidebar.webp"
  "taipei-food.html" = "images/taipei-food.webp"
  "jiufen.html" = "images/jiufen-sidebar.webp"
}

# Nav items (label -> icon emoji)
$navItems = @(
  @{Label="景點"; Icon="🏛️"},
  @{Label="美食"; Icon="🍜"},
  @{Label="購物"; Icon="🛍️"},
  @{Label="交通"; Icon="🚆"},
  @{Label="住宿"; Icon="🏨"},
  @{Label="實用資訊"; Icon="💡"}
)

$count = 0
$errors = 0

foreach ($article in $articles) {
  $path = Join-Path $repoPath $article
  if (Test-Path $path) {
    try {
      $content = Get-Content $path -Raw -Encoding UTF8
      
      # 1. Add CSS link if not present
      if ($content -notmatch 'layout-standard\.css') {
        $content = $content -replace '(<link href="beautify\.css"[^>]*>)', '$1' + "`n<link href=""layout-standard.css"" rel=""stylesheet""/>"
      }
      
      # 2. Add ls- classes to article content container
      $content = $content -replace '<div class="article-container">', '<div class="article-container ls-article-content">'
      
      # 3. Add ls- classes to day cards
      $content = $content -replace '<div class="day-card">', '<div class="day-card ls-day-card">'
      
      # 4. Add ls- classes to tip boxes
      $content = $content -replace '<div class="tip-box">', '<div class="tip-box ls-tip-box">'
      
      # 5. Add ls- classes to FAQ section
      $content = $content -replace '<div class="faq-section">', '<div class="faq-section ls-faq">'
      $content = $content -replace '<div class="faq-item">', '<div class="faq-item ls-faq-item">'
      $content = $content -replace '<div class="faq-q">', '<div class="faq-q ls-faq-q">'
      $content = $content -replace '<div class="faq-a">', '<div class="faq-a ls-faq-a">'
      
      # 6. Add ls- classes to related section
      $content = $content -replace '<div class="related-posts">', '<div class="related-posts ls-related">'
      $content = $content -replace '<div class="related-list">', '<div class="related-list ls-related-grid">'
      $content = $content -replace '<div class="related-card">', '<div class="related-card ls-related-card">'
      
      # 7. Update sidebar structure if old sidebar exists
      if ($content -match '<div class="sidebar-card">') {
        $cityName = if ($cityNames.ContainsKey($article)) { $cityNames[$article] } else { "旅遊" }
        $sidebarImg = if ($sidebarImages.ContainsKey($article)) { $sidebarImages[$article] } else { "images/placeholder.webp" }
        
        # Build nav items HTML
        $navHTML = ""
        foreach ($item in $navItems) {
          $navHTML += "`n    <a class=""ls-sidebar-nav-item"" href=""#$($item.Label)"">"
          $navHTML += "`n      <span class=""ls-sidebar-nav-icon"">$($item.Icon)</span>"
          $navHTML += "`n      <span class=""ls-sidebar-nav-label"">$($item.Label)</span>"
          $navHTML += "`n    </a>"
        }
        
        # Build new ls-sidebar HTML
        $newSidebar = @"
<aside class="ls-sidebar">
<div class="ls-sidebar-card">
<a href="$article">
<img alt="$cityName 攻略" class="ls-sidebar-hero" loading="lazy" src="$sidebarImg"/>
</a>
<div class="ls-sidebar-header">
<div class="ls-sidebar-city">$cityName</div>
<div class="ls-sidebar-sub">自由行攻略</div>
</div>
<nav class="ls-sidebar-nav">$navHTML
</nav>
<div class="ls-sidebar-qr">
<div class="ls-sidebar-qr-title">📱 追蹤我們</div>
<img alt="LINE QR" src="images/line-qr.webp"/>
<div class="ls-sidebar-qr-desc">掃描 LINE 取得最新旅遊資訊</div>
</div>
<a class="ls-sidebar-cta" href="travel-tools.html">📂 下載攻略 PDF</a>
</div>
</aside>
<div class="col-center">
"@
        
        # Pattern to match old sidebar
        $oldPattern = '<div class="sidebar-card">\s*<a[^>]*>\s*<img[^>]*class="sb-hero-img"[^>]*/>\s*</a>\s*</div>\s*<div class="col-center">'
        $content = $content -replace $oldPattern, $newSidebar
      }
      
      # Save
      Set-Content -Path $path -Value $content -Encoding UTF8 -NoNewline
      $count++
      Write-Host ("[OK] " + $article) -ForegroundColor Green
    } catch {
      $errors++
      Write-Host ("[ERR] " + $article + " - " + $_.Exception.Message) -ForegroundColor Red
    }
  } else {
    Write-Host ("[SKIP] " + $article + " not found") -ForegroundColor Yellow
  }
}

Write-Host ""
Write-Host ("Done: $count processed, $errors errors") -ForegroundColor Cyan