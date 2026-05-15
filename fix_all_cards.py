import sys; sys.stdout.reconfigure(encoding='utf-8')

fixes = {
    'korea-travel.html': {
        'seoul-hero.webp': '首爾直版.png',
        'busan-hero.webp': '釜山直版.png',
        'jeju-hero.webp': '濟州島直版.png',
    },
    'taiwan-travel.html': {
        'hualien-hero.webp': '花東直版.png',
        'tainan-hero.webp': '台南直版.png',
        'kenting-hero.webp': '墾丁直版.png',
    },
    'southeast-asia.html': {
        'chiangmai-hero.webp': '清邁直版.png',
        'bangkok-hero.webp': '曼谷直版.png',
    },
}

for page, mapping in fixes.items():
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    for old, new in mapping.items():
        if old in c:
            c = c.replace(f'images/{old}', f'images/{new}')
            print(f'  OK {page}: {old} -> {new}')
        else:
            print(f'  NOT FOUND {page}: {old}')
    with open(page, 'w', encoding='utf-8') as f:
        f.write(c)

print('\nDone!')