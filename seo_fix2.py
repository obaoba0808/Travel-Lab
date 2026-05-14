#!/usr/bin/env python
"""Add width/height to all <img> tags and delete old PNG/JPG files"""

import os, re, glob
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE, "images")

# 1. Build dimension map
dim_map = {}
for f in os.listdir(IMG_DIR):
    if f.endswith(('.webp', '.png', '.jpg', '.jpeg')):
        try:
            img = Image.open(os.path.join(IMG_DIR, f))
            dim_map[f] = img.size  # (w, h)
            img.close()
        except:
            pass

print("Image dimensions:")
for k, v in sorted(dim_map.items()):
    if k.endswith('.webp'):
        print(f"  {k}: {v[0]}x{v[1]}")

# 2. Add width/height to <img> tags in HTML
html_files = glob.glob(os.path.join(BASE, "*.html"))
print(f"\nFixing {len(html_files)} HTML files...")

for html_path in html_files:
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Find all <img src="images/xxx"> without width/height
    def add_dims(match):
        full_tag = match.group(0)
        if 'width=' in full_tag and 'height=' in full_tag:
            return full_tag  # already has dimensions
        
        # Extract src filename
        src_match = re.search(r'src="images/([^"]+)"', full_tag)
        if not src_match:
            return full_tag
        fname = src_match.group(1)
        
        if fname in dim_map:
            w, h = dim_map[fname]
            # Insert before the closing >
            tag = full_tag.rstrip('>')
            tag = tag + f' width="{w}" height="{h}">'
            return tag
        return full_tag
    
    content = re.sub(r'<img\s[^>]+>', add_dims, content)
    
    if content != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  FIXED: {os.path.basename(html_path)}")
    else:
        print(f"  OK: {os.path.basename(html_path)}")

# 3. Delete old PNG files that have been replaced by WebP
print("\nDeleting old image files...")
webp_files = {f for f in os.listdir(IMG_DIR) if f.endswith('.webp')}
deleted = 0
for f in os.listdir(IMG_DIR):
    if f.endswith(('.png', '.jpg', '.jpeg')):
        # Check if WebP version exists
        webp_name = os.path.splitext(f)[0] + '.webp'
        if webp_name in webp_files:
            os.remove(os.path.join(IMG_DIR, f))
            print(f"  DEL: {f}")
            deleted += 1
        else:
            print(f"  KEEP: {f} (no WebP replacement)")
print(f"Deleted {deleted} old image files")

# 4. Summary
total_webp = sum(os.path.getsize(os.path.join(IMG_DIR, f)) for f in os.listdir(IMG_DIR) if f.endswith('.webp'))
print(f"\nTotal images size now: {total_webp/1024/1024:.1f} MB (was ~64 MB)")
