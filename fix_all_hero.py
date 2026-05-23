#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'
os.chdir(base)

# Check hero img src in southeast-asia.html
with open('southeast-asia.html', 'r', encoding='utf-8') as f:
    c = f.read()
m = re.search(r'hero-full-img[^>]*src="([^"]+)"', c)
print('southeast-asia.html hero src:', m.group(1) if m else 'NOT FOUND')

# Check card count in southeast-asia.html
cards = re.findall(r'<article class="card">', c)
print('southeast-asia.html card count:', len(cards))

# Fix hero img src for 5 pages
fixes = {
    'vietnam-danang.html': 'vietnam-danang-hero.webp',
    'bangkok-massage.html': 'bangkok-massage-hero.webp',
    'jiufen.html': 'jiufen-hero.webp',
    'taipei-food.html': 'taipei-food-hero.webp',
    'korea-budget.html': 'korea-budget-hero.webp',
}

for fname, correct_img in fixes.items():
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'(<img\s+class="hero-full-img"\s+src=")([^"]+)(")', c)
    if m:
        old_src = m.group(2)
        if old_src == 'images/' + correct_img:
            print('[SKIP]', fname, '- already correct')
        else:
            new_c = c.replace(m.group(0), m.group(1) + 'images/' + correct_img + m.group(3))
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(new_c)
            print('[OK]', fname, ':', old_src, '->', 'images/' + correct_img)
    else:
        print('[WARN]', fname, '- no hero-full-img tag found')
