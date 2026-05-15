import sys, glob
sys.stdout.reconfigure(encoding='utf-8')

# For article pages: sb-hero-img lines must use SIDEBAR images
# These 4 pages incorrectly have hero in sb-hero-img
sb_fixes = [
    ('hokkaido-winter.html', 'hokkaido-hero.webp', 'hokkaido-sidebar.png'),
    ('kansai-pass.html', 'kansai-hero.webp', 'kansai-sidebar.png'),
    ('okinawa.html', 'okinawa-hero.webp', 'okinawa-sidebar.png'),
    ('tokyo-5days.html', 'tokyo-hero.png', 'tokyo-hero.png'),  # tokyo special - user provided
]

for fname, old, new in sb_fixes:
    c = open(fname, 'r', encoding='utf-8').read()
    if old in c:
        c = c.replace(old, new)
        open(fname, 'w', encoding='utf-8').write(c)
        print(f'  sidebar fix: {fname} {old} -> {new}')

# post-thumb related posts must use HERO images
pt_fixes = [
    ('bangkok-3days.html', 'chiangmai-sidebar.png', 'chiangmai-hero.webp'),
    ('busan-capsule.html', 'seoul-sidebar.png', 'seoul-hero.webp'),
    ('busan-capsule.html', 'jeju-sidebar.png', 'jeju-hero.webp'),
    ('chiang-mai.html', 'bangkok-sidebar.png', 'bangkok-hero.webp'),
    ('hualien-taitung.html', 'tainan-sidebar.png', 'tainan-hero.webp'),
    ('hualien-taitung.html', 'kenting-sidebar.png', 'kenting-hero.webp'),
    ('jeju-island.html', 'seoul-sidebar.png', 'seoul-hero.webp'),
    ('jeju-island.html', 'busan-sidebar.png', 'busan-hero.webp'),
    ('kenting.html', 'hualien-sidebar.png', 'hualien-hero.webp'),
    ('kenting.html', 'tainan-sidebar.png', 'tainan-hero.webp'),
    ('seoul-food.html', 'busan-sidebar.png', 'busan-hero.webp'),
    ('seoul-food.html', 'jeju-sidebar.png', 'jeju-hero.webp'),
    ('tainan-food.html', 'hualien-sidebar.png', 'hualien-hero.webp'),
    ('tainan-food.html', 'kenting-sidebar.png', 'kenting-hero.webp'),
]

for fname, old, new in pt_fixes:
    c = open(fname, 'r', encoding='utf-8').read()
    if old in c:
        c = c.replace(old, new)
        open(fname, 'w', encoding='utf-8').write(c)
        print(f'  post-thumb fix: {fname} {old} -> {new}')

print('Done.')
