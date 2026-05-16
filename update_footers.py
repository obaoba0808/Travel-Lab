#!/usr/bin/env python3
"""Add legal links to all page footers + update sitemap.xml"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# Add legal links to every page's footer bottom
legal_links = '''    <div style="margin-top:8px;font-size:12px;">
      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>
      <a href="privacy.html" style="color:inherit;margin-right:12px;">隱私權政策</a>
      <a href="terms.html" style="color:inherit;margin-right:12px;">使用條款</a>
      <a href="disclaimer.html" style="color:inherit;">免責聲明</a>
    </div>'''

pages = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['terms.html','disclaimer.html']]
count = 0

for f in pages:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Replace old footer bottom with new legal links
    old_pattern = r'<div style="margin-top:8px;font-size:12px;">\s*<a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>\s*<a href="contact.html" style="color:inherit;">聯絡我們</a>\s*</div>'
    new_str = legal_links
    
    content_new, n = re.subn(old_pattern, new_str, content)
    if n == 0:
        # Try different pattern
        old_pattern2 = r'<a href="contact.html" style="color:inherit;">聯絡我們</a>'
        if old_pattern2 in content:
            # Find the container div
            content_new = content.replace(old_pattern2, '<a href="disclaimer.html" style="color:inherit;">免責聲明</a>')
            n = 1
    
    if n > 0:
        with open(f, 'w', encoding='utf-8', newline='\r\n') as fh:
            fh.write(content_new)
        count += 1
        print(f'{f}: legal links added')
    else:
        # Check if already has terms/disclaimer
        if 'terms.html' in content:
            print(f'{f}: already has legal links')
        else:
            print(f'{f}: pattern not matched - manual check needed')

print(f'\nUpdated {count} pages')

# Update sitemap.xml
sitemap_pages = [
    'index.html', 'about.html', 'travel-tools.html',
    'japan-travel.html', 'korea-travel.html', 'taiwan-travel.html', 'southeast-asia.html',
    'tokyo-5days.html', 'kansai-pass.html', 'hokkaido-winter.html', 'okinawa.html', 'kyoto-temples.html',
    'seoul-food.html', 'busan-capsule.html', 'jeju-island.html',
    'hualien-taitung.html', 'tainan-food.html', 'kenting.html',
    'chiang-mai.html', 'bangkok-3days.html',
    'contact.html', 'privacy.html', 'terms.html', 'disclaimer.html'
]

sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
''' + ''.join(f'  <url><loc>https://golightly.fun/{p}</loc><lastmod>2026-05-16</lastmod><changefreq>monthly</changefreq></url>\n' for p in sitemap_pages) + '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(sitemap)
print('sitemap.xml updated with 24 pages')