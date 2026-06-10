#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修復 5 個檔案的 Hero <img src> 指向正確圖片
"""
import os
import re

base_dir = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'

pages = {
    'vietnam-danang.html': 'vietnam-danang-hero.webp',
    'bangkok-massage.html': 'bangkok-massage-hero.webp',
    'jiufen.html': 'jiufen-hero.webp',
    'taipei-food.html': 'taipei-food-hero.webp',
    'korea-budget.html': 'korea-budget-hero.webp',
}

print('=== Fix Hero <img src> ===')
print()

for page, img in pages.items():
    filepath = os.path.join(base_dir, page)
    print(f'Processing: {page}')
    
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # 找 <img class="hero-full-img" src="images/...">
    pattern = rb'<img class="hero-full-img"\s+src="images/[^"]+"'
    matches = re.findall(pattern, content)
    
    if matches:
        old_src = matches[0]
        new_src = f'<img class="hero-full-img" src="images/{img}"'.encode('utf-8')
        content = content.replace(old_src, new_src)
        print(f'  [OK] Fixed: {old_src.decode("utf-8", errors="replace")} -> {new_src.decode("utf-8")}')
        
        with open(filepath, 'wb') as f:
            f.write(content)
    else:
        print(f'  [WARN] No <img class="hero-full-img"> found!')

print()
print('=== Done ===')
