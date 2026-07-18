# -*- coding: utf-8 -*-
"""Fix render-blocking Google Fonts (Tailwind CDN kept sync for correct rendering)."""
import os, re

BASE = r'G:\aistudio-travel-lab'
os.chdir(BASE)

changed = 0
for fname in sorted(os.listdir(BASE)):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(BASE, fname)
    with open(path, encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    before = html

    # Make Google Fonts non-render-blocking: media="print" onload trick
    def defer_fonts(m):
        tag = m.group(0)
        if 'media=' in tag:
            return tag  # already modified
        return tag.replace(
            'rel="stylesheet"',
            'rel="stylesheet" media="print" onload="this.media=\'all\'"'
        )
    html = re.sub(
        r'<link\s+href="https://fonts\.googleapis\.com/css2\?[^"]*"\s+rel="stylesheet">',
        defer_fonts,
        html
    )

    # Add noscript fallback for Google Fonts
    if 'fonts.googleapis.com' in html and '<noscript>' not in html:
        m = re.search(r'<link\s+href="(https://fonts\.googleapis\.com/css2\?[^"\']+)"[^>]*>', html)
        if m:
            noscript_tag = '<noscript><link href="' + m.group(1) + '" rel="stylesheet"></noscript>'
            html = html + '\n    ' + noscript_tag

    if html != before:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        changed += 1
        print(f'[OK] {fname}')

print(f'\nFixed {changed} files.')
