#!/usr/bin/env python3
"""Scan all HTML files for images and check if they're wrapped in links"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# Map image filenames to destination pages
img_to_page = {
    'tokyo': 'tokyo-5days.html',
    'kansai': 'kansai-pass.html',
    'hokkaido': 'hokkaido-winter.html',
    'okinawa': 'okinawa.html',
    'kyoto': 'kyoto-temples.html',
    'seoul': 'seoul-food.html',
    'busan': 'busan-capsule.html',
    'jeju': 'jeju-island.html',
    'hualien': 'hualien-taitung.html',
    'tainan': 'tainan-food.html',
    'kenting': 'kenting.html',
    'chiang-mai': 'chiang-mai.html',
    'bangkok': 'bangkok-3days.html',
    'japan': 'japan-travel.html',
    'korea': 'korea-travel.html',
    'taiwan': 'taiwan-travel.html',
    'southeast': 'southeast-asia.html',
    'travel-tools': 'travel-tools.html',
    'about-hero': 'about.html',
}

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Find all img tags with their context
    pattern = re.compile(r'(<a[^>]*href=["\']([^"\']*)["\'][^>]*>)?\s*(<img[^>]*src=["\']([^"\']*)["\'][^>]*>)(\s*</a>)?', re.IGNORECASE)
    
    needs_link = []
    for m in pattern.finditer(content):
        a_open = m.group(1)
        a_href = m.group(2)
        img_tag = m.group(3)
        img_src = m.group(4)
        a_close = m.group(5)
        
        # Skip if already linked
        if a_open and a_close:
            continue
        
        # Skip tiny icons/logos
        if 'logo' in img_src.lower() or 'icon' in img_src.lower():
            continue
            
        # Find matching destination
        dest = None
        for key, page in img_to_page.items():
            if key in img_src.lower():
                dest = page
                break
        
        if dest:
            needs_link.append((img_src, dest, img_tag[:100]))
    
    if needs_link:
        print(f'\n{f}:')
        for src, dest, preview in needs_link:
            print(f'  {src} -> {dest}')

print('\n--- Done ---')
