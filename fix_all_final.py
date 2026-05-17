#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fix ALL thumbnail images across ALL pages

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

print('[START] Fixing ALL thumbnails...')

# Fix article pages - post-thumb -> hero image
for page, hero in hero_images.items():
    page_path = os.path.join(base, page)
    if not os.path.exists(page_path):
        print('  [SKIP] ' + page + ' (file not found)')
        continue
    
    with open(page_path, 'rb') as f:
        content = f.read()
    
    # Find img with class="post-thumb", replace its src
    # Pattern: catch the src="..." that belongs to the post-thumb img
    pattern = rb'(<img [^>]*class="post-thumb"[^>]*src=")[^"]*("[^>]*>)'
    replacement = rb'\1' + hero.encode() + rb'\2'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(page_path, 'wb') as f:
            f.write(new_content)
        print('  [FIXED] ' + page + ' -> ' + hero)
    else:
        print('  [SKIP] ' + page + ' (post-thumb not found or already correct)')

# Fix index.html homepage cards
idx_path = os.path.join(base, 'index.html')
with open(idx_path, 'rb') as f:
    content = f.read()

print('\n[Homepage] Fixing cards...')
for page, hero in hero_images.items():
    # Pattern: <a href="page"> ... <img src="..."> ... </a>
    # We need to find the img inside the a tag for this page
    # Simple approach: find 'href="page"' then find the img src after it
    href_pos = content.find(('href="' + page + '"').encode())
    if href_pos == -1:
        print('  [SKIP] ' + page + ' (href not found in index)')
        continue
    
    # Find img tag after this position
    img_start = content.find(rb'<img', href_pos)
    if img_start == -1:
        print('  [SKIP] ' + page + ' (img not found after href)')
        continue
    
    img_end = content.find(rb'>', img_start)
    if img_end == -1:
        print('  [SKIP] ' + page + ' (img end not found)')
        continue
    
    img_tag = content[img_start:img_end+1]
    
    # Replace src in this img tag
    new_img_tag = re.sub(rb'src="[^"]*"', b'src="' + hero.encode() + b'"', img_tag)
    
    if new_img_tag != img_tag:
        new_content = content[:img_start] + new_img_tag + content[img_end+1:]
        with open(idx_path, 'wb') as f:
            f.write(new_content)
        content = new_content  # Update for next iteration
        print('  [FIXED] index card: ' + page + ' -> ' + hero)
    else:
        print('  [SKIP] index card: ' + page + ' (already correct)')

print('\n[DONE] All thumbnails fixed!')
