#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次更新 Hero 區域：確保 <img class="hero-full-img"> 標籤存在
更新 og:image 和 JSON-LD（已在 fix_hero_full_img_v5.py 處理）
"""
import os
import re

base_dir = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'
images_dir = os.path.join(base_dir, 'images')

# 需要處理的頁面對應
pages = {
    'vietnam-danang.html': 'vietnam-danang-hero.webp',
    'bangkok-massage.html': 'bangkok-massage-hero.webp',
    'jiufen.html': 'jiufen-hero.webp',
    'taipei-food.html': 'taipei-food-hero.webp',
    'korea-budget.html': 'korea-budget-hero.webp',
}

def process_file(filepath, hero_img):
    """處理單個 HTML 檔案：確保使用 <img class="hero-full-img"> 結構"""
    with open(filepath, 'rb') as f:
        content = f.read()
    
    original = content
    modified = False
    
    # 1. 檢查是否已經有 <img class="hero-full-img">
    img_pattern = rb'<img class="hero-full-img"'
    if img_pattern in content:
        print(f'  [OK] Already has <img class="hero-full-img>')
    else:
        print(f'  [FIX] Need to add <img class="hero-full-img>')
        # 嘗試從 style="background-image:url(...)" 轉換
        bg_pattern = rb'style="background-image:url\([^"]*"\)"'
        match = re.search(bg_pattern, content)
        if match:
            # 移除 style 屬性
            content = re.sub(bg_pattern, b'', content)
            print(f'  [OK] Removed background-image style')
            modified = True
    
    # 2. 檢查 <section class="hero-beautify"> 後是否有 <img>
    section_pattern = rb'<section class="hero-beautify"[^>]*>'
    section_match = re.search(section_pattern, content)
    if section_match and img_pattern not in content[section_match.end():section_match.end()+200]:
        # 需要在 section 後添加 img
        insert_pos = section_match.end()
        # 擷取 alt 文字（從 h1 或 title）
        h1_pattern = rb'<h1[^>]*>(.*?)</h1>'
        h1_match = re.search(h1_pattern, content)
        if h1_match:
            alt_text = re.sub(rb'<[^>]+>', b'', h1_match.group(1)).decode('utf-8', errors='replace').strip()
        else:
            alt_text = hero_img.replace('-hero.webp', '').replace('-', ' ')
        
        img_tag = f'<img class="hero-full-img" src="images/{hero_img}" alt="{alt_text}">'.encode('utf-8')
        
        content = content[:insert_pos] + b'\n  ' + img_tag + b'\n' + content[insert_pos:]
        print(f'  [OK] Added <img class="hero-full-img"> tag')
        modified = True
    
    # 3. 確認 og:image 正確
    og_pattern = rb'<meta property="og:image" content="[^"]*">'
    og_new = f'<meta property="og:image" content="https://golightly.fun/images/{hero_img}">'.encode('utf-8')
    content = re.sub(og_pattern, og_new, content)
    
    # 4. 確認 JSON-LD 中的 image
    json_pattern = rb'"image":\s*"https://golightly\.fun/images/[^"]*"'
    json_new = f'"image": "https://golightly.fun/images/{hero_img}"'.encode('utf-8')
    content = re.sub(json_pattern, json_new, content)
    
    # 只有當內容有變更時才寫入
    if content != original:
        with open(filepath, 'wb') as f:
            f.write(content)
        return True
    else:
        return False

# 主程式
print('=== Ensuring Hero Full Image Structure ===')
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
