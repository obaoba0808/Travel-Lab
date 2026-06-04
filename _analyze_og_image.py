# -*- coding: utf-8 -*-
"""
Analyze og:image tags in all HTML files
Check: format, missing width/height/type
"""
import os
import re

# 1. Find all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f'[INFO] Found {len(html_files)} HTML files')

og_image_data = []
missing_width = 0
missing_height = 0
missing_type = 0
webp_count = 0
jpg_count = 0
png_count = 0
other_count = 0

# 2. Analyze each file
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 3. Find all og:image tags
    og_image_pattern = r'<meta\s+property\s*=\s*["\']og:image["\']\s+content\s*=\s*["\']([^"\']+)["\']'
    matches = re.findall(og_image_pattern, content)
    
    for og_image_url in matches:
        og_image_data.append({
            'file': filename,
            'og:image': og_image_url
        })
        
        # 4. Check image format
        if og_image_url.lower().endswith('.webp'):
            webp_count += 1
        elif og_image_url.lower().endswith(('.jpg', '.jpeg')):
            jpg_count += 1
        elif og_image_url.lower().endswith('.png'):
            png_count += 1
        else:
            other_count += 1
    
    # 5. Check missing tags
    if not re.search(r'og:image:width', content, re.IGNORECASE):
        missing_width += 1
    if not re.search(r'og:image:height', content, re.IGNORECASE):
        missing_height += 1
    if not re.search(r'og:image:type', content, re.IGNORECASE):
        missing_type += 1

# 6. Print report
print(f'\n[RESULTS] Found {len(og_image_data)} og:image tags')
print(f'\n[IMAGE FORMAT]')
print(f'  WebP: {webp_count}')
print(f'  JPG:  {jpg_count}')
print(f'  PNG:  {png_count}')
print(f'  Other: {other_count}')

print(f'\n[MISSING TAGS]')
print(f'  Missing og:image:width  : {missing_width} files')
print(f'  Missing og:image:height : {missing_height} files')
print(f'  Missing og:image:type   : {missing_type} files')

print(f'\n[OG:IMAGE LIST] (first 10)')
for i, item in enumerate(og_image_data[:10], 1):
    print(f"  [{item['file']}] {item['og:image']}")

print(f'\n[INFO] Analysis complete')
