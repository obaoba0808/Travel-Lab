import sys, glob
sys.stdout.reconfigure(encoding='utf-8')

mapping = {
    'seoul-hero.webp': 'seoul-sidebar.png',
    'busan-hero.webp': 'busan-sidebar.png',
    'jeju-hero.webp': 'jeju-sidebar.png',
    'kansai-hero.webp': 'kansai-sidebar.png',
    'okinawa-hero.webp': 'okinawa-sidebar.png',
    'kyoto-hero.webp': 'kyoto-sidebar.png',
    'hokkaido-hero.webp': 'hokkaido-sidebar.png',
    'hualien-hero.webp': 'hualien-sidebar.png',
    'tainan-hero.webp': 'tainan-sidebar.png',
    'kenting-hero.webp': 'kenting-sidebar.png',
    'chiangmai-hero.webp': 'chiangmai-sidebar.png',
    'bangkok-hero.webp': 'bangkok-sidebar.png',
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
    for old, new in mapping.items():
        if old in c:
            c = c.replace(old, new)
            print(f'  {f}: {old} -> {new}')
    if c != orig:
        open(f, 'w', encoding='utf-8').write(c)
        print(f'Saved: {f}')
