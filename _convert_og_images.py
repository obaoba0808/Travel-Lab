# -*- coding: utf-8 -*-
"""
Convert WebP OG images to JPG format
Get image dimensions (width × height)
"""
from PIL import Image
import os
import json

# 1. Find all WebP images in images/og/
og_dir = 'images/og'
webp_files = [f for f in os.listdir(og_dir) if f.endswith('.webp')]
print(f'[INFO] Found {len(webp_files)} WebP images')

# 2. Convert each WebP to JPG
converted = 0
image_info = {}

for webp_file in webp_files:
    webp_path = os.path.join(og_dir, webp_file)
    jpg_file = webp_file.replace('.webp', '.jpg')
    jpg_path = os.path.join(og_dir, jpg_file)
    
    # 3. Open WebP, convert to RGB (for JPG), save as JPG
    try:
        with Image.open(webp_path) as img:
            # Get dimensions
            width, height = img.size
            image_info[webp_file] = {'width': width, 'height': height}
            
            # Convert to RGB (JPG doesn't support transparency)
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save as JPG (quality=90)
            img.save(jpg_path, 'JPEG', quality=90, optimize=True)
            converted += 1
            print(f'[SUCCESS] {webp_file} → {jpg_file} ({width}x{height})')
    except Exception as e:
        print(f'[ERROR] Failed to convert {webp_file}: {e}')

print(f'\n[RESULTS] Converted {converted}/{len(webp_files)} images')
print('[INFO] Image info saved to image_info.json')

# 4. Save image info to JSON
with open('image_info.json', 'w', encoding='utf-8') as f:
    json.dump(image_info, f, indent=2, ensure_ascii=False)

print('[INFO] Ready to update HTML files')
