# -*- coding: utf-8 -*-
import os, re

BASE = r'G:\aistudio-travel-lab'
os.chdir(BASE)

short = []
for fname in sorted(os.listdir(BASE)):
    if not fname.endswith('.html'): continue
    path = os.path.join(BASE, fname)
    with open(path, encoding='utf-8', errors='replace') as f:
        content = f.read()
    m = re.search(r'<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if m:
        desc = m.group(1)
        if len(desc) < 80:
            short.append((fname, len(desc), desc[:60]))

print(f'Found {len(short)} short meta descriptions (< 80 chars):')
for fname, length, preview in short:
    print(f'{fname}: {length} chars | {preview}')
