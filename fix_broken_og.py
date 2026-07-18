# -*- coding: utf-8 -*-
import os, re

BASE = r"G:\aistudio-travel-lab"
os.chdir(BASE)

# 1. Fix &amp; in Unsplash URLs in physical HTML files
files_with_amp = [
    'angkor-wat-2days.html',
    'kualalumpur-3days.html',
    'singapore-3days.html',
]

fixed = 0
for fname in files_with_amp:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"NOT FOUND: {fname}")
        continue
    with open(fpath, encoding='utf-8', errors='replace') as f:
        html = f.read()
    before = html
    # Fix og:image URLs: decode &amp; to &
    def fix_og_url(m):
        url = m.group(2)
        if '&amp;' in url:
            return m.group(1) + url.replace('&amp;', '&') + m.group(3)
        return m.group(0)
    new_html = re.sub(
        r'(<meta\s+property="og:image"\s+content=")([^"]+)("\s*/?>)',
        fix_og_url,
        html, flags=re.IGNORECASE
    )
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        fixed += 1
        print(f"Fixed &amp; in: {fname}")
    else:
        print(f"No &amp; found: {fname}")

# 2. Fix customPages.ts - busan-capsule coverImage
cp_path = os.path.join(BASE, 'data', 'customPages.ts')
if os.path.exists(cp_path):
    with open(cp_path, encoding='utf-8', errors='replace') as f:
        content = f.read()
    before = content
    changed = False
    if 'busan-capsule-train.webp' in content:
        content = content.replace('busan-capsule-train.webp', 'busan-hero.webp')
        changed = True
        print('Replaced busan-capsule-train.webp → busan-hero.webp in customPages.ts')
    if changed:
        with open(cp_path, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print('No changes needed in customPages.ts')

print(f"\nDone. Fixed {fixed} HTML files.")
