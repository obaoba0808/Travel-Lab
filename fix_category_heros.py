#!/usr/bin/env python3
"""Move hero title below image for 4 category pages"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

pages = {
    'japan-travel.html': {
        'bg': 'images/japan-hero.png',
        'alt': '日本自由行',
        'tag': 'Japan',
        'h1': '日本自由行攻略',
        'p': '東京、關西、北海道、沖繩、京都，五大路線實戰攻略。',
    },
    'korea-travel.html': {
        'bg': 'images/korea-hero.png',
        'alt': '韓國自由行',
        'tag': 'Korea',
        'h1': '韓國自由行攻略',
        'p': '首爾美食、釜山膠囊列車、濟州島自駕，三大路線全收錄。',
    },
    'taiwan-travel.html': {
        'bg': 'images/taiwan-hero.png',
        'alt': '台灣旅遊',
        'tag': 'Taiwan',
        'h1': '台灣深度旅遊',
        'p': '花東縱谷、台南古都、墾丁海景，在地人帶路攻略。',
    },
    'southeast-asia.html': {
        'bg': 'images/southeast-asia-hero.png',
        'alt': '東南亞自由行',
        'tag': 'Southeast Asia',
        'h1': '東南亞自由行',
        'p': '清邁數位遊牧、曼谷吃貨攻略，低成本長旅行首選。',
    },
}

for f, cfg in pages.items():
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Find and replace category-hero section
    pattern = re.compile(
        r'<!--\s*CATEGORY HERO\s*-->.*?</div>\s*</div>',
        re.DOTALL
    )
    m = pattern.search(content)
    if not m:
        print(f'{f}: CATEGORY HERO not found!')
        continue
    
    old = m.group(0)
    new = f'''<!-- FULL-BLEED HERO -->
<div class="hero-full-bleed">
  <img src="{cfg['bg']}" alt="{cfg['alt']}" class="hero-full-img">
</div>
<div class="hero-title-block">
  <div class="hero-title-inner">
    <span class="hero-region-tag">{cfg['tag']}</span>
    <h1 class="hero-main-title">{cfg['h1']}</h1>
    <p class="hero-sub-title">{cfg['p']}</p>
  </div>
</div>'''
    
    content = content[:m.start()] + new + content[m.end():]
    
    with open(f, 'w', encoding='utf-8', newline='\r\n') as fh:
        fh.write(content)
    print(f'{f}: done')

print('\nAll 4 pages updated')
