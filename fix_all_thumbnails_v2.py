#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fix ALL thumbnail images across all pages

import re, os

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'

hero_images = {
    'tokyo-5days.html': 'images/tokyo-hero.webp',
    'kansai-pass.html': 'images/kansai-pass-hero.webp',
    'hokkaido-winter.html': 'images/hokkaido-hero.webp',
    'okinawa.html': 'images/okinawa-hero.webp',
    'kyoto-temples.html': 'images/kyoto-hero.webp',
    'osaka-food.html': 'images/osaka-food-hero.webp',
    'osaka-usj.html': 'images/osaka-usj-hero.webp',
    'japan-budget-guide.html': 'images/japan-budget-hero.webp',
    'seoul-food.html': 'images/seoul-food-hero.webp',
    'busan-capsule.html': 'images/busan-hero.webp',
    'jeju-island.html': 'images/jeju-hero.webp',
    'korea-budget.html': 'images/korea-budget-hero.webp',
    'hualien-taitung.html': 'images/hualien-hero.webp',
    'tainan-food.html': 'images/tainan-food-hero.webp',
    'kenting.html': 'images/kenting-hero.webp',
    'taipei-food.html': 'images/taipei-food-hero.webp',
    'jiufen.html': 'images/jiufen-hero.webp',
    'chiang-mai.html': 'images/chiang-mai-hero.webp',
    'bangkok-3days.html': 'images/bangkok-hero.webp',
    'bangkok-massage.html': 'images/bangkok-massage-hero.webp',
    'vietnam-danang.html': 'images/vietnam-danang-hero.webp',
    'esim-comparison.html': 'images/esim-comparison-hero.webp',
    'hongkong-3days.html': 'images/hongkong-3days-hero.webp',
}

print('[Step 1] Fixing index.html homepage cards...')
idx_path = os.path.join(base, 'index.html')
with open(idx_path, 'rb') as f:
    content = f.read()

for page, hero in hero_images.items():
    pattern = rb'<a href="' + re.escape(page).encode() + rb'">\s*<img [^>]*src="images/[^"]*\.webp"'
    replacement = b'<a href="' + page.encode() + b'">\n        <img loading="lazy" src="' + hero.encode() + b'"'
    new_c = re.sub(pattern, replacement, content)
    if new_c != content:
        print('  [FIXED] ' + page)
        content = new_c
    else:
        print('  [SKIP] ' + page + ' (not found)')

with open(idx_path, 'wb') as f:
    f.write(content)
print('  [OK] index.html saved!')

print('\n[Step 2] Fixing ALL article pages post-thumb...')
for page, hero in hero_images.items():
    page_path = os.path.join(base, page)
    if not os.path.exists(page_path):
        print('  [SKIP] ' + page + ' (file not found)')
        continue
    with open(page_path, 'rb') as f:
        c = f.read()
    pattern = rb'<img [^>]*class="post-thumb"[^>]*src="images/[^"]*\.webp"'
    replacement = b'<img loading="lazy" class="post-thumb" src="' + hero.encode() + b'"'
    new_c = re.sub(pattern, replacement, c)
    if new_c != c:
        with open(page_path, 'wb') as f:
            f.write(new_c)
        print('  [FIXED] ' + page)
    else:
        print('  [SKIP] ' + page + ' (post-thumb not found or already correct)')

print('\n[DONE] All thumbnails fixed!')
