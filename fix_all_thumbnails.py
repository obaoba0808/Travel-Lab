#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fix ALL thumbnail images:
# 1. index.html homepage cards -> use each article's HERO image
# 2. Article pages post-thumb -> use that article's HERO image

import re

# Mapping: page -> its HERO image
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
    'chiang-mai.html': 'images/chiangmai-hero.webp',
    'bangkok-3days.html': 'images/bangkok-hero.webp',
    'bangkok-massage.html': 'images/bangkok-massage-hero.webp',
    'vietnam-danang.html': 'images/vietnam-danang-hero.webp',
    'esim-comparison.html': 'esim-comparison-hero.webp',
    'hongkong-3days.html': 'hongkong-3days-hero.webp',
}

# Step 1: Fix index.html homepage cards
index_path = 'index.html'
with open(index_path, 'rb') as f:
    content = f.read()

print('[Homepage] Fixing card thumbnails...')
for page, hero_img in hero_images.items():
    # Pattern: <img ... src="images/XXX.webp" ...> inside a card linking to 'page'
    # Replace ANY img src inside a card that links to this page
    pattern = rb'(<a href="' + re.escape(page).encode() + rb'">\s*<img [^>]*src=")images/[^"]+(")([^>]*></a>)'
    replacement = rb'\1' + hero_img.encode() + rb'\2'
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        print('  [FIXED] ' + page)
        content = new_content
    else:
        print('  [SKIP] ' + page + ' (not found or already correct)')

with open(index_path, 'wb') as f:
    f.write(content)
print('[Homepage] Done!')

# Step 2: Fix ALL article pages - post-thumb -> hero image
import os
for page, hero_img in hero_images.items():
    if not os.path.exists(page):
        print('[SKIP] ' + page + ' (file not found)')
        continue
    with open(page, 'rb') as f:
        content = f.read()
    # Fix post-thumb img src
    pattern = rb'(<img [^>]*class="post-thumb"[^>]*src=")images/[^"]+(")'
    replacement = rb'\1' + hero_img.encode() + rb'\2'
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        with open(page, 'wb') as f:
            f.write(new_content)
        print('[FIXED] ' + page + ' post-thumb -> ' + hero_img)
    else:
        print('[SKIP] ' + page + ' (post-thumb already correct)')

print('\\n[DONE] All thumbnails fixed!')
