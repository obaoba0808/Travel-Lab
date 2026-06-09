# -*- coding: utf-8 -*-
import glob, re

variants = {}
for f in sorted(glob.glob('*.html')):
    c = open(f,'r',encoding='utf-8').read()
    if 'site-footer' not in c:
        continue
    cols = len(re.findall(r'<div class="footer-col">', c))
    has_legal = '法律資訊' in c or '關於我們' in c  # 舊欄位名
    has_nav_row = 'footer-nav-row' in c
    key = f'{cols}col_legal={has_legal}_navrow={has_nav_row}'
    if key not in variants:
        variants[key] = []
    variants[key].append(f)

for k, v in sorted(variants.items()):
    print(f'{k}: {len(v)} pages')
    for name in v[:5]:
        print(f'  - {name}')
    if len(v) > 5:
        print(f'  ... and {len(v)-5} more')
    print()
