#!/usr/bin/env python3
"""Check article pages for unlinked images"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

for f in ['tokyo-5days.html', 'seoul-food.html', 'hualien-taitung.html']:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    print(f'\n=== {f} ===')
    for m in re.finditer(r'<img[^>]*>', content):
        tag = m.group(0)
        pos = m.start()
        before = content[max(0, pos-200):pos]
        last_a_open = before.rfind('<a ')
        last_a_close = before.rfind('</a>')
        linked = last_a_open > last_a_close and last_a_open != -1
        
        src_match = re.search(r'src=["\']([^"\']*)["\']', tag)
        src = src_match.group(1) if src_match else '?'
        print(f'  linked={linked} | {src}')
