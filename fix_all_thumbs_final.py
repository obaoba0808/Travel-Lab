#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fix ALL thumbnail images

import os

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
}

print('[START] Fixing ALL thumbnails...')

# Fix index.html homepage cards
idx_path = os.path.join(base, 'index.html')
with open(idx_path, 'rb') as f:
    content = f.read()

print('[Homepage] Fixing cards...')
for page, hero in hero_images.items():
    # Find: <a href="page"><img ... src="images/XXX.webp" ... class="post-thumb"></a>
    # Strategy: find 'href="page"' then find the <img> tag after it
    href_pos = content.find(('href="' + page + '"').encode())
    if href_pos == -1:
        print('  [SKIP] ' + page + ' (href not found)')
        continue
    
    # Find <img> after href position
    img_start = content.find(b'<img', href_pos)
    if img_start == -1:
        print('  [SKIP] ' + page + ' (img not found after href)')
        continue
    
    # Find src="..." in this img tag
    src_start = content.find(b'src="images/', img_start)
    img_end = content.find(b'>', img_start)
    
    if src_start == -1 or src_start > img_end:
        print('  [SKIP] ' + page + ' (src not found in img tag)')
        continue
    
    # Replace the src value
    old_src_end = content.find(b'"', src_start + 5)
    old_src = content[src_start:old_src_end]
    new_src = ('src="' + hero + '"').encode()
    
    if old_src != new_src:
        content = content[:src_start] + new_src + content[old_src_end:]
        print('  [FIXED] ' + page + ' -> ' + hero)
    else:
        print('  [SKIP] ' + page + ' (already correct)')

with open(idx_path, 'wb') as f:
    f.write(content)
print('[Homepage] Saved!')

# Fix ALL article pages - post-thumb img
print('\n[Articles] Fixing post-thumb...')
for page, hero in hero_images.items():
    page_path = os.path.join(base, page)
    if not os.path.exists(page_path):
        print('  [SKIP] ' + page + ' (file not found)')
        continue
    
    with open(page_path, 'rb') as f:
        c = f.read()
    
    # Find class="post-thumb" in an <img> tag
    # The structure: <img ... class="post-thumb" src="images/XXX.webp" ...>
    # Strategy: find 'class="post-thumb"' then find src="..." before or after it
    thumb_pos = c.find(b'class="post-thumb"')
    if thumb_pos == -1:
        print('  [SKIP] ' + page + ' (post-thumb class not found)')
        continue
    
    # Find src="images/..." near this position (before or after)
    # Try after first
    src_start = c.find(b'src="images/', thumb_pos)
    if src_start == -1 or src_start > c.find(b'>', thumb_pos):
        # Try before
        src_start = c.rfind(b'src="images/', 0, thumb_pos + 20)
    
    if src_start == -1:
        print('  [SKIP] ' + page + ' (src not found near post-thumb)')
        continue
    
    # Replace the src value
    src_end = c.find(b'"', src_start + 5)
    old_src = c[src_start:src_end]
    new_src = ('src="' + hero + '"').encode()
    
    if old_src != new_src:
        new_c = c[:src_start] + new_src + c[src_end:]
        with open(page_path, 'wb') as f:
            f.write(new_c)
        print('  [FIXED] ' + page + ' -> ' + hero)
        c = new_c  # Update for multiple replacements
    else:
        print('  [SKIP] ' + page + ' (already correct)')

print('\n[DONE] All thumbnails fixed!')
