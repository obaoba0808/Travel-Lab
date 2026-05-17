#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# Read in text mode
with open('southeast-asia.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the 2 missing article cards
new_cards = """

    <article class="card">
      <a href="bangkok-massage.html"><img src="images/bangkok-massage-hero.webp" alt="曼谷按摩推薦" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="southeast-asia.html" class="cat-tag">東南亞自由行</a>
        <h3><a href="bangkok-massage.html">【曼谷按摩】必試泰式按摩</a></h3>
        <p>曼谷最佳按摩店推薦，從平價到豪華，幫你消除旅途疲勞。</p>
        <a href="bangkok-massage.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>

    <article class="card">
      <a href="vietnam-danang.html"><img src="images/vietnam-danang-hero.webp" alt="越南峴港3天2夜全攻略" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="southeast-asia.html" class="cat-tag">東南亞自由行</a>
        <h3><a href="vietnam-danang.html">【越南峴港】3天2夜全攻略</a></h3>
        <p>峴港海灘、會安古鎮、巴拿山金橋，越南中部精華路線。</p>
        <a href="vietnam-danang.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
"""

# Find the position after the second card (bangkok-3days.html)
pattern = r'(<article class="card">\s*<a href="bangkok-3days.html">.*?</article>)'
match = re.search(pattern, content, flags=re.DOTALL)

if match:
    # Insert new cards after the matched card
    pos = match.end()
    new_content = content[:pos] + new_cards + content[pos:]
    
    with open('southeast-asia.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('[OK] southeast-asia.html updated with 2 missing article cards')
else:
    print('[ERROR] Pattern not found in southeast-asia.html')
