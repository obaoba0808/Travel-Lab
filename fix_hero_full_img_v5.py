#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次更新 Hero 區塊：從 background-image 改為 <img class="hero-full-img">
所有非首頁頁面（排除 index.html）
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
    """處理單個 HTML 檔案"""
    with open(filepath, 'rb') as f:
        content = f.read()
    
    original = content
    
    # 1. 修改 Hero 區塊的 style="background-image:url(...)"
    # 改為 <img class="hero-full-img" src="images/xxx-hero.webp" alt="...">
    # 先找到 hero-beautify 區塊
    hero_pattern = rb'<section class="hero-beautify"[^>]*>'
    hero_match = re.search(hero_pattern, content)
    
    if hero_match:
        # 檢查是否已經有 <img class="hero-full-img">
        if b'hero-full-img' not in content:
            # 需要修改：移除 style="background-image:url(...)"，添加 img 標籤
            # 先處理 style 屬性
            style_pattern = rb'style="background-image:url\([^"]*"\)"'
            content = re.sub(style_pattern, b'', content)
            
            # 在 <section> 後添加 <img>
            # 讀取 alt 文字（從 h1 或 title）
            h1_pattern = rb'<h1[^>]*>(.*?)</h1>'
            h1_match = re.search(h1_pattern, content)
            if h1_match:
                # 移除 HTML 標籤
                alt_text = re.sub(rb'<[^>]+>', b'', h1_match.group(1)).decode('utf-8', errors='replace').strip()
            else:
                alt_text = hero_img.replace('-hero.webp', '').replace('-', ' ').title()
            
            img_tag = f'<img class="hero-full-img" src="images/{hero_img}" alt="{alt_text}">'.encode('utf-8')
            
            # 在 <section class="hero-beautify"> 後插入 <img>
            insert_pos = hero_match.end()
            content = content[:insert_pos] + b'\n  ' + img_tag + b'\n' + content[insert_pos:]
            print(f'  [OK] Added <img> tag')
        else:
            print(f'  [SKIP] Already has hero-full-img')
    else:
        print(f'  [WARN] No hero-beautify section found')
    
    # 2. 更新 og:image
    og_pattern = rb'<meta property="og:image" content="[^"]*">'
    og_new = f'<meta property="og:image" content="https://golightly.fun/images/{hero_img}">'.encode('utf-8')
    content = re.sub(og_pattern, og_new, content)
    
    # 3. 更新 JSON-LD 中的 image
    # 找到 "image": ["..."] 或 "image": "..."
    json_pattern = rb'"image"\s*:\s*"(https://golightly\.fun/images/[^"]+)"'
    json_new = f'"image": "https://golightly.fun/images/{hero_img}"'.encode('utf-8')
    content = re.sub(json_pattern, json_new, content)
    
    # 4. 確認沒有 style="background-image:url()" 殘留
    if b'background-image:url(' in content:
        print(f'  [WARN] Still has background-image in file!')
    
    # 只有當內容有變更時才寫入
    if content != original:
        with open(filepath, 'wb') as f:
            f.write(content)
        return True
    else:
        return False

# 主程式
print('=== Hero Full Image Batch Fix ===')
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
print(f'=== Done ===')
print(f'Updated: {updated}')
print(f'Skipped: {skipped}')
