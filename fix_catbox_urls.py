#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replace catbox.moe URLs with local image paths in HTML files."""

import os
import re

HTML_DIR = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"
IMAGE_DIR = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\images"

# Mapping: HTML file -> local image file (in images/ directory)
MAPPING = {
    'busan-capsule.html': 'ChatGPT Image 2026年5月13日 下午07_33_47.png',
    'chiang-mai.html': 'ChatGPT Image 2026年5月13日 下午07_35_21.png',
    'hualien-taitung.html': 'ChatGPT Image 2026年5月13日 下午07_46_00.png',
    'jeju-island.html': 'ChatGPT Image 2026年5月13日 下午07_49_19.png',
    'kansai-pass.html': 'ChatGPT Image 2026年5月13日 下午07_51_39.png',
    'kenting.html': 'ChatGPT Image 2026年5月13日 下午07_53_33.png',
    'kyoto-temples.html': 'ChatGPT Image 2026年5月13日 下午07_55_35.png',
    'seoul-food.html': 'ChatGPT Image 2026年5月13日 下午07_58_46.png',
    'tainan-food.html': 'ChatGPT Image 2026年5月13日 下午08_00_29.png',
}

def fix_html_file(html_path, img_filename):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace catbox.moe URL with local path
    # Pattern matches: <img src="https://files.catbox.moe/XXXXXX.png" alt="..." class="hero-img" ...>
    pattern = r'src="https://files\.catbox\.moe/[^"]+"'
    replacement = f'src="images/{img_filename}"'
    
    content = re.sub(pattern, replacement, content)
    
    # Also fix og:image and Twitter image meta tags if they reference catbox.moe
    content = re.sub(r'content="https://files\.catbox\.moe/[^"]+"', lambda m: m.group(0), content)  # Keep for now
    
    if content != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    fixed = []
    for html_file, img_file in MAPPING.items():
        html_path = os.path.join(HTML_DIR, html_file)
        if os.path.exists(html_path):
            if fix_html_file(html_path, img_file):
                fixed.append(html_file)
    
    if fixed:
        print("[OK] Fixed %d files - replaced catbox.moe URLs with local images:" % len(fixed))
        for f in fixed:
            print("  - %s" % f)
    else:
        print("[i] No files needed fixing.")

if __name__ == '__main__':
    main()
