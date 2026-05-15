import sys
sys.stdout.reconfigure(encoding='utf-8')

fixes = [
    ('hokkaido-winter.html', 'hokkaido-hero.webp', 'hokkaido-sidebar.png'),
    ('okinawa.html', 'okinawa-hero.webp', 'okinawa-sidebar.png'),
]

for fname, old, new in fixes:
    c = open(fname, 'r', encoding='utf-8').read()
    if old in c:
        # only replace in sb-hero-img line
        import re
        c = re.sub(r'(sb-hero-img[^>]*src=")' + re.escape(old) + r'(")', r'\1' + new + r'\2', c)
        open(fname, 'w', encoding='utf-8').write(c)
        print(f'Fixed: {fname} sidebar {old} -> {new}')
