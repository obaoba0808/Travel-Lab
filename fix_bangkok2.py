# -*- coding: utf-8 -*-
"""Fix bangkok-massage.html by replacing entire corrupted meta tag."""
import re

path = r'G:\aistudio-travel-lab\bangkok-massage.html'

with open(path, encoding='utf-8', errors='replace') as f:
    html = f.read()

# Find the corrupted meta description line (contains repeated text)
lines = html.split('\n')
for i, line in enumerate(lines):
    if 'name="description"' in line and 'Let\'s Relax' in line:
        print(f'Line {i}: {line[:150]}...')
        # Replace entire line
        new_desc = '2026曼谷按摩SPA完整推薦攻略：臥佛寺泰式按摩、Divana Strings SPA、平價連鎖Let\'s Relax、Terminal 21商場按摩店完整評比，含預約教學與省錢技巧，讓你放鬆不傷荷包！'
        lines[i] = f'  <meta name="description" content="{new_desc}"/>'
        print(f'Fixed: {len(new_desc)} chars')
        break

html = '\n'.join(lines)
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Done')
