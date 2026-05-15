import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

fixes = {
    'hokkaido-sidebar.png': 'hokkaido-hero.webp',
    'okinawa-sidebar.png': 'okinawa-hero.webp',
    'kansai-sidebar.png': 'kansai-hero.webp',
}

for f in glob.glob('*.html'):
    c = open(f, 'r', encoding='utf-8').read()
    orig = c
    for old, new in fixes.items():
        # post-thumb > img src pattern
        pat = r'(class="post-thumb"><img[^>]*src=")' + re.escape(old) + r'(")'
        c = re.sub(pat, r'\1' + new + r'\2', c)
    if c != orig:
        open(f, 'w', encoding='utf-8').write(c)
        print(f'Fixed: {f}')
