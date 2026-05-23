#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'
os.chdir(base)

# === Fix taiwan-travel.html: add 2 missing cards ===
taiwan_cards = """

    <article class="card">
      <a href="taipei-food.html"><img src="images/taipei-food-hero.webp" alt="台北美食地圖精選" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="taiwan-travel.html" class="cat-tag">台灣旅遊</a>
        <h3><a href="taipei-food.html">【台北美食地圖】精選推薦</a></h3>
        <p>台北必吃餐廳、夜市小吃、隱藏版美食推薦，在地人帶你吃遍台北。</p>
        <a href="taipei-food.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>

    <article class="card">
      <a href="jiufen.html"><img src="images/jiufen-hero.webp" alt="九份老街攻略" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="taiwan-travel.html" class="cat-tag">台灣旅遊</a>
        <h3><a href="jiufen.html">【九份老街】一日遊攻略</a></h3>
        <p>九份老街美食、茶館推薦、最佳拍照時間，從台北出發的交通指南。</p>
        <a href="jiufen.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
"""

with open('taiwan-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'(<article class="card">\s*<a href="kenting.html">.*?</article>)'
match = re.search(pattern, c, flags=re.DOTALL)
if match:
    new_c = c[:match.end()] + taiwan_cards + c[match.end():]
    with open('taiwan-travel.html', 'w', encoding='utf-8') as f:
        f.write(new_c)
    print('[OK] taiwan-travel.html updated with 2 missing cards (taipei-food, jiufen)')
else:
    print('[ERROR] taiwan-travel.html pattern not found')

# === Fix korea-travel.html: add 1 missing card ===
korea_card = """

    <article class="card">
      <a href="korea-budget.html"><img src="images/korea-budget-hero.webp" alt="韓國預算解析2026" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="korea-travel.html" class="cat-tag">韓國自由行</a>
        <h3><a href="korea-budget.html">【韓國預算解析】2026最新</a></h3>
        <p>韓國自由行費用全解析，機票、住宿、交通、餐飲預算一次看懂。</p>
        <a href="korea-budget.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
"""

with open('korea-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'(<article class="card">\s*<a href="jeju-island.html">.*?</article>)'
match = re.search(pattern, c, flags=re.DOTALL)
if match:
    new_c = c[:match.end()] + korea_card + c[match.end():]
    with open('korea-travel.html', 'w', encoding='utf-8') as f:
        f.write(new_c)
    print('[OK] korea-travel.html updated with 1 missing card (korea-budget)')
else:
    print('[ERROR] korea-travel.html pattern not found')
