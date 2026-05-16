#!/usr/bin/env python3
"""
Round 2: Link remaining unlinked images in article & index pages.
- charter-banner -> about.html (car service contact)
- index.html card images -> destination pages
- Skip hero images (self-link to own page)
- Skip sidebar.png (already linked)
"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

img_to_page = {
    'tokyo-hero': 'tokyo-5days.html',
    'kansai-hero': 'kansai-pass.html',
    'hokkaido-hero': 'hokkaido-winter.html',
    'okinawa-hero': 'okinawa.html',
    'kyoto-hero': 'kyoto-temples.html',
    'seoul-hero': 'seoul-food.html',
    'busan-hero': 'busan-capsule.html',
    'jeju-hero': 'jeju-island.html',
    'hualien-hero': 'hualien-taitung.html',
    'tainan-hero': 'tainan-food.html',
    'kenting-hero': 'kenting.html',
    'chiang-mai-hero': 'chiang-mai.html',
    'bangkok-hero': 'bangkok-3days.html',
    'japan-hero': 'japan-travel.html',
    'korea-hero': 'korea-travel.html',
    'taiwan-hero': 'taiwan-travel.html',
    'southeast-asia-hero': 'southeast-asia.html',
    'about-hero': 'about.html',
    'travel-tools-hero': 'travel-tools.html',
    'charter-banner': 'about.html',
    'sidebar': None,  # skip
}

total_changes = 0

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    original = content
    
    for m in reversed(list(re.finditer(r'<img[^>]*>', content))):
        tag = m.group(0)
        pos = m.start()
        
        # Check if already inside <a>
        before = content[max(0, pos-200):pos]
        last_a_open = before.rfind('<a ')
        last_a_close = before.rfind('</a>')
        if last_a_open > last_a_close and last_a_open != -1:
            continue
        
        # Find src
        src_match = re.search(r'src=["\']([^"\']*)["\']', tag)
        if not src_match:
            continue
        img_src = src_match.group(1)
        img_filename = img_src.split('/')[-1].lower()
        
        # Find destination
        dest = None
        for key, page in img_to_page.items():
            if key is None:
                continue
            if key in img_filename:
                dest = page
                break
        
        if not dest:
            continue
        
        # Skip self-link
        if dest == f:
            continue
        
        # Wrap in <a>
        new_tag = f'<a href="{dest}">{tag}</a>'
        content = content[:pos] + new_tag + content[pos + len(tag):]
        total_changes += 1
    
    if content != original:
        with open(f, 'w', encoding='utf-8', newline='\r\n') as fh:
            fh.write(content)
        changes = content.count('<a href=') - original.count('<a href=')
        print(f'{f}: +{changes} links added')

print(f'\nTotal: {total_changes} images linked')
