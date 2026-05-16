#!/usr/bin/env python3
"""
Wrap all unlinked images in <a> tags pointing to their destination page.
Skip self-links (image linking to its own page).
"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# Map image filename keywords to destination pages
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
}

total_changes = 0

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    original = content
    
    # Find unlinked <img> tags - not already wrapped in <a>
    # Pattern: <img ...> that is NOT preceded by <a href=...>
    # We use a negative lookbehind approach by finding img tags and checking context
    
    # Find all img tags
    img_pattern = re.compile(r'<img\s+([^>]*src=["\']([^"\']*)["\'][^>]*)>', re.IGNORECASE)
    
    # Process in reverse to maintain positions
    matches = list(img_pattern.finditer(content))
    
    changes_in_file = 0
    for m in reversed(matches):
        img_full = m.group(0)
        img_attrs = m.group(1)
        img_src = m.group(2)
        
        # Skip if already inside an <a> tag
        # Check if there's an opening <a> before this img without a closing </a> in between
        before = content[:m.start()]
        # Find last <a before this img
        last_a_open = before.rfind('<a ')
        last_a_close = before.rfind('</a>')
        if last_a_open > last_a_close and last_a_open != -1:
            # Inside an <a> tag already, skip
            continue
        
        # Find destination for this image
        dest = None
        img_filename = img_src.split('/')[-1].lower()
        for key, page in img_to_page.items():
            if key in img_filename:
                dest = page
                break
        
        if not dest:
            continue
        
        # Skip self-link (image on its own page)
        if dest == f:
            continue
        
        # Wrap the img in an <a> tag
        new_tag = f'<a href="{dest}">{img_full}</a>'
        content = content[:m.start()] + new_tag + content[m.end():]
        changes_in_file += 1
    
    if content != original:
        with open(f, 'w', encoding='utf-8', newline='\r\n') as fh:
            fh.write(content)
        print(f'{f}: {changes_in_file} images linked')
        total_changes += changes_in_file

print(f'\nTotal: {total_changes} images wrapped in links across all files')
