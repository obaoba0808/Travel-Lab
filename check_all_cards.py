import sys; sys.stdout.reconfigure(encoding='utf-8')
import re

pages = {
    'korea-travel.html': ['首爾直版.png', '釜山直版.png', '濟州島直版.png'],
    'taiwan-travel.html': ['花東直版.png', '台南直版.png', '墾丁直版.png'],
    'southeast-asia.html': ['清邁直版.png', '曼谷直版.png'],
}

for page, expected in pages.items():
    c = open(page, 'r', encoding='utf-8').read()
    imgs = re.findall(r'src="images/([^"]+)"', c)
    print(f'\n=== {page} ===')
    for img in imgs:
        if any(x in img for x in ['hero', '直版', 'card']):
            mark = '✅' if img in expected or '直版' in img else '❌'
            print(f'  {mark} {img}')