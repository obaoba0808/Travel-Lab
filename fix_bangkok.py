# -*- coding: utf-8 -*-
"""Fix corrupted bangkok-massage.html meta description."""
import re

BASE = r'G:\aistudio-travel-lab'
path = f'{BASE}\\bangkok-massage.html'

with open(path, encoding='utf-8', errors='replace') as f:
    html = f.read()

# Find and replace the corrupted line
old_line = re.search(r'<meta name="description" content="[^"]*"/>', html)
if old_line:
    print(f'Found corrupted line: {old_line.group(0)[:100]}...')
    new_desc = '2026曼谷按摩SPA完整推薦攻略：臥佛寺泰式按摩、Divana Strings SPA、平價連鎖Let\'s Relax、Terminal 21商場按摩店完整評比，含預約教學與省錢技巧，讓你放鬆不傷荷包！'
    new_line = f'<meta name="description" content="{new_desc}"/>'
    html = html.replace(old_line.group(0), new_line)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Fixed: {len(new_desc)} chars')
else:
    print('No corrupted line found')
