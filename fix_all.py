import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

# === RULES ===
# 1. .hero-img (page top banner) -> HERO image
# 2. .sb-hero-img (sidebar card) -> SIDEBAR image  
# 3. .post-thumb (related posts) -> HERO image
# 4. Category cards (img src + width=1536) -> HERO image

sidebar_files = {
    'seoul': 'seoul-sidebar.png', 'busan': 'busan-sidebar.png', 'jeju': 'jeju-sidebar.png',
    'kansai': 'kansai-sidebar.png', 'kyoto': 'kyoto-sidebar.png',
    'hokkaido': 'hokkaido-sidebar.png', 'okinawa': 'okinawa-sidebar.png',
    'hualien': 'hualien-sidebar.png', 'tainan': 'tainan-sidebar.png',
    'kenting': 'kenting-sidebar.png', 'chiangmai': 'chiangmai-sidebar.png',
    'bangkok': 'bangkok-sidebar.png',
}

hero_files = {
    'seoul': 'seoul-hero.webp', 'busan': 'busan-hero.webp', 'jeju': 'jeju-hero.webp',
    'kansai': 'kansai-hero.webp', 'kyoto': 'kyoto-hero.webp',
    'hokkaido': 'hokkaido-hero.webp', 'okinawa': 'okinawa-hero.webp',
    'hualien': 'hualien-hero.webp', 'tainan': 'tainan-hero.webp',
    'kenting': 'kenting-hero.webp', 'chiangmai': 'chiangmai-hero.webp',
    'bangkok': 'bangkok-hero.webp',
}

all_names = list(sidebar_files.keys())

article_pages = [
    'tokyo-5days.html', 'kansai-pass.html', 'hokkaido-winter.html', 'okinawa.html',
    'kyoto-temples.html', 'seoul-food.html', 'busan-capsule.html', 'jeju-island.html',
    'hualien-taitung.html', 'tainan-food.html', 'kenting.html', 'chiang-mai.html',
    'bangkok-3days.html'
]

for f in article_pages:
    c = open(f, 'r', encoding='utf-8').read()
    orig = c
    
    # Fix 1: hero-img -> use hero for ALL destinations in this page's hero
    for name in all_names:
        sb = sidebar_files[name]
        hr = hero_files[name]
        if sb in c:
            # only replace if inside a hero-img context
            # match: <div class="hero"><img ... src="sb" ... class="hero-img"
            c = re.sub(
                r'(<div class="hero"><img[^>]*src=")' + re.escape(sb) + r'(")',
                r'\1' + hr + r'\2',
                c
            )
    
    # Fix 2: sb-hero-img -> ensure sidebar
    for name in all_names:
        hr = hero_files[name]
        sb = sidebar_files[name]
        # replace hero with sidebar in sb-hero-img lines
        c = re.sub(
            r'(sb-hero-img[^>]*src=")' + re.escape(hr) + r'(")',
            r'\1' + sb + r'\2',
            c
        )
    
    # Fix 3: post-thumb -> ensure hero
    for name in all_names:
        sb = sidebar_files[name]
        hr = hero_files[name]
        c = re.sub(
            r'(post-thumb[^>]*><img[^>]*src=")' + re.escape(sb) + r'(")',
            r'\1' + hr + r'\2',
            c
        )
    
    if c != orig:
        open(f, 'w', encoding='utf-8').write(c)
        print(f'Updated: {f}')
