import sys
sys.stdout.reconfigure(encoding='utf-8')

fixes = [
    ('hokkaido-winter.html', 'hokkaido-sidebar.png', 'hokkaido-hero.webp'),
    ('okinawa.html', 'okinawa-sidebar.png', 'okinawa-hero.webp'),
]

for fname, old, new in fixes:
    c = open(fname, 'r', encoding='utf-8').read()
    if old in c:
        c = c.replace(old, new)
        open(fname, 'w', encoding='utf-8').write(c)
        print(f'Fixed: {fname} hero {old} -> {new}')
