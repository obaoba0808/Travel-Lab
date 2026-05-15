import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

hero_fixes = {
    'kyoto-sidebar.png': 'kyoto-hero.webp',
    'kansai-sidebar.png': 'kansai-hero.webp',
    'hokkaido-sidebar.png': 'hokkaido-hero.webp',
    'okinawa-sidebar.png': 'okinawa-hero.webp',
    'seoul-sidebar.png': 'seoul-hero.webp',
    'busan-sidebar.png': 'busan-hero.webp',
    'jeju-sidebar.png': 'jeju-hero.webp',
    'hualien-sidebar.png': 'hualien-hero.webp',
    'tainan-sidebar.png': 'tainan-hero.webp',
    'kenting-sidebar.png': 'kenting-hero.webp',
    'chiangmai-sidebar.png': 'chiangmai-hero.webp',
    'bangkok-sidebar.png': 'bangkok-hero.webp',
}

article_pages = [
    'tokyo-5days.html', 'kansai-pass.html', 'hokkaido-winter.html', 'okinawa.html',
    'kyoto-temples.html', 'seoul-food.html', 'busan-capsule.html', 'jeju-island.html',
    'hualien-taitung.html', 'tainan-food.html', 'kenting.html', 'chiang-mai.html',
    'bangkok-3days.html'
]

for f in article_pages:
    c = open(f, 'r', encoding='utf-8').read()
    orig = c
    
    # Find the hero div and fix img src inside it
    def fix_hero_div(m):
        content = m.group(0)
        for old, new in hero_fixes.items():
            content = content.replace(old, new)
        return content
    
    c = re.sub(r'<div class="hero">[^<]*<img[^>]*>[^<]*</div>', fix_hero_div, c)
    
    # Fix related post-thumb (should be hero images)
    for old, new in hero_fixes.items():
        c = re.sub(
            r'(class="post-thumb"[^>]*>[\s]*<img[^>]*src=")' + re.escape(old) + r'(")',
            r'\1' + new + r'\2',
            c
        )
    
    if c != orig:
        open(f, 'w', encoding='utf-8').write(c)
        print(f'Fixed: {f}')
