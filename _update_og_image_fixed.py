# -*- coding: utf-8 -*-
"""
Update og:image tags in all HTML files
FIXED: Correctly detect if file needs update
"""
import os
import re
import json

# 1. Load image dimensions
with open('image_info.json', 'r', encoding='utf-8') as f:
    image_info = json.load(f)

# 2. Find all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f'[INFO] Found {len(html_files)} HTML files')

updated_count = 0

# 3. Process each file
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 4. Check if already updated (has og:image:width tag)
    if 'og:image:width' in content:
        print(f'[SKIP ] {filename} (already has og:image:width)')
        continue
    
    # 5. Find og:image tag
    og_image_pattern = r'<meta\s+property\s*=\s*["\']og:image["\']\s+content\s*=\s*["\']([^"\']+)["\']'
    match = re.search(og_image_pattern, content)
    
    if not match:
        print(f'[WARN ] {filename}: No og:image tag found')
        continue
    
    og_image_url = match.group(1)
    og_image_tag = match.group(0)
    
    # 6. Extract filename from URL
    og_image_filename = os.path.basename(og_image_url)
    
    # 7. Determine JPG and WebP filenames
    jpg_filename = og_image_filename.replace('.webp', '.jpg')
    webp_filename = og_image_filename  # already .webp
    
    # 8. Get image dimensions
    if og_image_filename in image_info:
        width = image_info[og_image_filename]['width']
        height = image_info[og_image_filename]['height']
    else:
        # Default to 1200x630 if not found
        width = 1200
        height = 630
        print(f'[WARN] {filename}: No dimensions for {og_image_filename}, using default')
    
    # 9. Create new OG image tags
    base_url = og_image_url.rsplit('/', 1)[0]
    
    new_og_tags = f'''<meta property="og:image" content="{base_url}/{jpg_filename}">
<meta property="og:image:secure_url" content="{og_image_url}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="{width}">
<meta property="og:image:height" content="{height}">'''
    
    # 10. Replace old og:image tag with new tags
    new_content = content.replace(og_image_tag, new_og_tags)
    
    # 11. Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    updated_count += 1
    print(f'[UPDATED] {filename}')

print(f'\n[SUCCESS] Updated {updated_count} files')
print('[INFO] Ready to commit and push')
