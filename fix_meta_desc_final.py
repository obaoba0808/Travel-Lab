# -*- coding: utf-8 -*-
import os, re

BASE = r'G:\aistudio-travel-lab'
os.chdir(BASE)

# FINAL - all >= 80 chars, verified
FIXES = {
    'bangkok-massage.html': '2026曼谷按摩SPA完整推薦攻略：臥佛寺泰式按摩、Divana Strings SPA、平價連鎖Let\'s Relax、Terminal 21商場按摩店完整評比，含預約教學與省錢技巧。',
    'about.html': '關於均在路上 Travel Lab：我們的使命是幫助讀者用最合理的預算，走最深度的旅程。了解我們的故事、品牌願景、專業編輯團隊、合作夥伴與聯繫方式，以及常見問答。',
    'taiwan-travel.html': '台灣深度旅遊提案2026：花東縱谷3天2夜自然之旅、台南美食牛肉湯地圖、墾丁海景夜市攻略，由在地人帶路探索私房景點與季節限定體驗，附大眾交通與自駕路線建議指南。',
    'tokyo-5days.html': '東京5天4夜自由行攻略2026：淺草寺晴空塔、澀谷原宿逛街、築地場外市場美食、迪士尼門票優惠，附完整地鐵乘車教學與每日行程表，預算NT$15,000搞定遊客必讀。',
}

for fname, new_desc in FIXES.items():
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f'[SKIP] {fname}')
        continue
    with open(fpath, encoding='utf-8', errors='replace') as f:
        html = f.read()
    pattern = re.compile(
        r'(<meta\s+[^>]*?(?:name|property)=["\']description["\'][^>]*?)content=["\']([^"\']*)["\']',
        re.IGNORECASE | re.DOTALL
    )
    def replacer(m):
        return f'{m.group(1)}content="{new_desc}"'
    new_html, count = pattern.subn(replacer, html)
    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f'[OK] {fname}: {len(new_desc)} chars')
    else:
        print(f'[SKIP] {fname}: no desc tag')
