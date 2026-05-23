#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LATEST fix: Correct <img src="images/xxx-hero.webp"> for all 5 pages
"""
import os
import re

base_dir = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'
images_dir = os.path.join(base_dir, 'images')

# Correct mapping
pages = {
    'vietnam-danang.html': 'vietnam-danang-hero.webp',
    'bangkok-massage.html': 'bangkok-massage-hero.webp',
    'jiufen.html': 'jiufen-hero.webp',
    'taipei-food.html': 'taipei-food-hero.webp',
    'korea-budget.html': 'korea-budget-hero.webp',
}

def process_file(filepath, hero_img):
    """Fix <img src> tag"""
    with open(filepath, 'rb') as f:
        content = f.read()
    
    original = content
    modified = False
    
    # Fix <img class="hero-full-img" src="images/xxx.webp">
    img_pattern = rb'<img class="hero-full-img"\s+src="images/[^"]+"'
    img_match = re.search(img_pattern, content)
    
    if img_match:
        old_img_tag = img_match.group(0)
        new_img_tag = f'<img class="hero-full-img" src="images/{hero_img}"'.encode('utf-8')
        
        # Also fix alt attribute
        alt_pattern = rb'alt="[^"]*"'
        alt_match = re.search(alt_pattern, content[img_match.start():img_match.end()+200])
        if alt_match:
            # Extract alt text from hero img filename
            alt_text = hero_img.replace('-hero.webp', '').replace('-', ' ')
            new_alt = f'alt="{alt_text}"'.encode('utf-8')
            # Remove old alt, add new alt
            old_alt = alt_match.group(0)
            content = content.replace(old_alt, new_alt, 1)
        
        content = content.replace(old_img_tag, new_img_tag, 1)
        print(f'  [OK] Fixed <img src> to {hero_img}')
        modified = True
    else:
        print(f'  [WARN] No <img class="hero-full-img"> found!')
    
    # Ensure og:image is correct
    og_pattern = rb'<meta property="og:image" content="[^"]*">'
    og_new = f'<meta property="og:image" content="https://golightly.fun/images/{hero_img}">'.encode('utf-8')
    content = re.sub(og_pattern, og_new, content)
    print(f'  [OK] og:image updated')
    
    # Ensure JSON-LD image is correct
    json_pattern = rb'"image":\s*"https://golightly\.fun/images/[^"]*"'
    json_new = f'"image": "https://golightly.fun/images/{hero_img}"'.encode('utf-8')
    content = re.sub(json_pattern, json_new, content)
    print(f'  [OK] JSON-LD image updated')
    
    # Only write if content changed
    if content != original:
        with open(filepath, 'wb') as f:
            f.write(content)
        return True
    else:
        return False

# Main
print('=== FINAL Fix <img src> ===')
print(f'Base dir: {base_dir}')
print()

updated = 0
skipped = 0

for page, img in pages.items():
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath):
        print(f'[SKIP] File not found: {page}')
        skipped += 1
        continue
    
    print(f'Processing: {page} -> {img}')
    try:
        if process_file(filepath, img):
            print(f'  [OK] Updated: {page}')
            updated += 1
        else:
            print(f'  [SKIP] No change: {page}')
            skipped += 1
    except Exception as e:
        print(f'  [ERROR] {e}')
        skipped += 1

print()
print('=== Done ===')
print(f'Updated: {updated}')
print(f'Skipped: {skipped}')
