#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fix ALL post-thumb img src for 17 article pages
# Each article should use ITS OWN hero image

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
    'busan-capsule.html': 'images/busan-capsule-hero.webp',
    'jeju-island.html': 'images/jeju-island-hero.webp',
    'korea-budget.html': 'images/korea-budget-hero.webp',
    'hualien-taitung.html': 'images/hualien-taitung-hero.webp',
    'tainan-food.html': 'images/tainan-food-hero.webp',
    'kenting.html': 'images/kenting-hero.webp',
    'taipei-food.html': 'images/taipei-food-hero.webp',
    'jiufen.html': 'images/jiufen-hero.webp',
    'chiang-mai.html': 'images/chiang-mai-hero.webp',
    'bangkok-3days.html': 'images/bangkok-3days-hero.webp',
    'bangkok-massage.html': 'images/bangkok-massage-hero.webp',
    'vietnam-danang.html': 'images/vietnam-danang-hero.webp',
}

print('[START] Fixing post-thumb for ALL article pages...')

for page, hero in hero_images.items():
    page_path = os.path.join(base, page)
    if not os.path.exists(page_path):
        print('  [SKIP] ' + page + ' (file not found)')
        continue
    
    with open(page_path, 'rb') as f:
        content = f.read()
    
    # Method: Find <img ... class="post-thumb" ...>
    # The img tag might have attributes in any order
    # Strategy: find 'class="post-thumb"', then find the <img> tag containing it
    
    # Find position of 'class="post-thumb"'
    idx = content.find(b'class="post-thumb"')
    if idx == -1:
        print('  [SKIP] ' + page + ' (post-thumb not found)')
        continue
    
    # Find the <img> tag that contains this class
    # Search backwards for '<img' and forwards for '>'
    img_start = content.rfind(b'<img', 0, idx)
    if img_start == -1:
        print('  [SKIP] ' + page + ' (img start not found)')
        continue
    
    img_end = content.find(b'>', idx)
    if img_end == -1:
        print('  [SKIP] ' + page + ' (img end not found)')
        continue
    
    img_tag = content[img_start:img_end+1]
    
    # Replace the src attribute in this img_tag
    # Pattern: src="XXX" -> src="hero_image"
    new_img_tag = re.sub(rb'src="[^"]*"', b'src="' + hero.encode() + b'"', img_tag)
    
    if new_img_tag != img_tag:
        new_content = content[:img_start] + new_img_tag + content[img_end+1:]
        with open(page_path, 'wb') as f:
            f.write(new_content)
        print('  [FIXED] ' + page + ' -> ' + hero)
    else:
        print('  [SKIP] ' + page + ' (src not found in tag)')

print('\n[DONE] All post-thumb fixed!')
