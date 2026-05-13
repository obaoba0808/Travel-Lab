# -*- coding: utf-8 -*-
"""
Batch rebuild article pages - remove inline CSS, add style.css, update header
"""

import re
import os

# Read japan-travel.html for the header template
with open('japan-travel.html', 'r', encoding='utf-8') as f:
    japan_html = f.read()

# Extract head section (everything before </head>)
head_end = japan_html.find('</head>')
japan_head = japan_html[:head_end + len('</head>')]

# Extract body start section (topbar only - up to CATEGORY HERO)
body_start = japan_html.find('<body>')
hero_start = japan_html.find('<!-- CATEGORY HERO -->')
japan_body_header = japan_html[body_start:hero_start]

# Extract footer section
footer_start = japan_html.find('<!-- FOOTER -->')
body_end = japan_html.find('</body>')
japan_footer = japan_html[footer_start:body_end + len('</body>')]

# Article pages to rebuild
article_pages = [
    'tokyo-5days.html', 'kansai-pass.html', 'hokkaido-winter.html',
    'okinawa.html', 'kyoto-temples.html', 'seoul-food.html',
    'busan-capsule.html', 'jeju-island.html', 'hualien-taitung.html',
    'tainan-food.html', 'kenting.html', 'chiang-mai.html', 'bangkok-3days.html'
]

# Navigation active mapping (which nav item should be highlighted)
nav_active_map = {
    'tokyo-5days.html': 'japan-travel.html',
    'kansai-pass.html': 'japan-travel.html',
    'hokkaido-winter.html': 'japan-travel.html',
    'okinawa.html': 'japan-travel.html',
    'kyoto-temples.html': 'japan-travel.html',
    'seoul-food.html': 'korea-travel.html',
    'busan-capsule.html': 'korea-travel.html',
    'jeju-island.html': 'korea-travel.html',
    'hualien-taitung.html': 'taiwan-travel.html',
    'tainan-food.html': 'taiwan-travel.html',
    'kenting.html': 'taiwan-travel.html',
    'chiang-mai.html': 'southeast-asia.html',
    'bangkok-3days.html': 'southeast-asia.html',
}

def rebuild_article_page(filename):
    """Rebuild an article page with new header/footer"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract unique content from the article
    # 1. Meta tags (title, description, keywords, canonical, og:image)
    title_match = re.search(r'<title>([^<]+)</title>', content)
    desc_match = re.search(r'<meta name="description" content="([^"]+)">', content)
    keywords_match = re.search(r'<meta name="keywords" content="([^"]+)">', content)
    canonical_match = re.search(r'<link rel="canonical" href="([^"]+)">', content)
    og_image_match = re.search(r'<meta property="og:image" content="([^"]+)">', content)
    
    # 2. JSON-LD scripts
    jsonld_matches = re.findall(r'<script type="application/ld\+json">.*?</script>', content, re.DOTALL)
    
    # 3. Main content (hero + article-container)
    # Extract hero section
    hero_match = re.search(r'<div class="hero"[^>]*>.*?</div>\s*</div>', content, re.DOTALL)
    hero_content = hero_match.group(0) if hero_match else ''
    
    # Extract article-container (everything from <div class="article-container"> to the end)
    article_match = re.search(r'<div class="article-container">.*$', content, re.DOTALL)
    article_content = article_match.group(0) if article_match else ''
    
    # Remove trailing </body></html> if present
    if article_content:
        article_content = re.sub(r'</body>\s*</html>\s*$', '', article_content)
        # Also remove trailing footer if it got included
        article_content = re.sub(r'<footer>.*$', '', article_content, flags=re.DOTALL)
    
    main_content = hero_content + '\n' + article_content
    
    if not main_content:
        print(f'  WARNING: No main content found in {filename}')
        return None
    
    # Build new head section
    title = title_match.group(1) if title_match else '均在路上 Travel Lab'
    description = desc_match.group(1) if desc_match else ''
    keywords = keywords_match.group(1) if keywords_match else ''
    canonical = canonical_match.group(1) if canonical_match else f'https://obaoba0808.github.io/Travel-Lab/{filename}'
    og_image = og_image_match.group(1) if og_image_match else 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80'
    
    # Start building the new HTML
    new_html = f'''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<link rel="alternate" hreflang="zh-Hant" href="{canonical}">
<link rel="alternate" hreflang="zh-TW" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">

<!-- Open Graph -->
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:site_name" content="均在路上 Travel Lab">
<meta property="og:locale" content="zh_TW">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">

<!-- JSON-LD -->
'''
    # Add JSON-LD scripts
    for jsonld in jsonld_matches:
        new_html += jsonld + '\n'
    
    new_html += '''
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
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-S7KQGHSD2R');
</script>
</head>
<body>

'''
    
    # Add body header (topbar)
    # Need to highlight the correct nav item
    active_nav = nav_active_map.get(filename, '')
    body_header = japan_body_header
    
    # Replace the active nav item style
    if active_nav:
        # Find and highlight the correct dropdown
        pattern = f'href="{active_nav}"'
        replacement = f'href="{active_nav}" style="color:var(--tiffany);border-bottom-color:var(--tiffany);"'
        body_header = body_header.replace(f'<a {pattern}>', f'<a {replacement}>')
    
    new_html += body_header
    
    # Add main content
    new_html += '\n' + main_content + '\n'
    
    # Add footer
    new_html += japan_footer
    
    return new_html

# Main execution
if __name__ == '__main__':
    print('Starting article pages rebuild...')
    
    for filename in article_pages:
        if not os.path.exists(filename):
            print(f'{filename}: NOT FOUND')
            continue
        
        print(f'Rebuilding {filename}...')
        new_html = rebuild_article_page(filename)
        
        if new_html:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f'  OK {filename} written ({len(new_html)} bytes)')
        else:
            print(f'  FAILED to rebuild {filename}')
    
    print('\nArticle pages rebuild complete!')
