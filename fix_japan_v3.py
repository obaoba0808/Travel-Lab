#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 japan-travel.html 的 card-grid 里添加缺失的 3 篇日本文章卡片（修正版）"""

import re

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\japan-travel.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到 card-grid 的结束位置（</div> 之前）
in_card_grid = False
insert_pos = -1
for i, line in enumerate(lines):
    if '<div class="card-grid">' in line:
        in_card_grid = True
    if in_card_grid and '</div>' in line and i > 0:
        # 检查这个 </div> 是否在 card-grid 内（通过缩进判断）
        if lines[i].strip() == '</div>':
            # 可能是 card-grid 的结束标签
            # 检查下一行是否包含 <!-- CTA --> 或 <section class="faq-section">
            if i + 1 < len(lines) and ('<!-- CTA -->' in lines[i+1] or '<section class="faq-section"' in lines[i+1]):
                insert_pos = i  # 在 </div> 之前插入
                break

if insert_pos == -1:
    print("[ERROR] 找不到 card-grid 的结束位置")
else:
    # 检查是否已经有这 3 篇文章的卡片
    content = ''.join(lines)
    has_food = '<article class="card">' in content and 'osaka-food.html' in content and 'osaka-food-hero.webp' in content
    has_usj = '<article class="card">' in content and 'osaka-usj.html' in content and 'osaka-usj-hero.webp' in content
    has_budget = '<article class="card">' in content and 'japan-budget-guide.html' in content and 'japan-budget-hero.webp' in content
    
    if has_food and has_usj and has_budget:
        print("[SKIP] 3 篇文章卡片已存在")
    else:
        # 创建 3 个新卡片
        new_cards = [
            '\n    <article class="card">\n',
            '      <a href="osaka-food.html"><img src="images/osaka-food-hero.webp" alt="大阪美食攻略" style="width:100%;height:auto;display:block;" width="1536" height="1024"></a>\n',
            '      <div class="card-body">\n',
            '        <a href="japan-travel.html" class="cat-tag">日本自由行</a>\n',
            '        <h3><a href="osaka-food.html">【大阪美食】必吃美食地圖</a></h3>\n',
            '        <p>章鱼烧、大阪烧、串炸，大阪必吃美食全攻略。</p>\n',
            '        <a href="osaka-food.html" class="read-more">閱讀文章 →</a>\n',
            '      </div>\n',
            '    </article>\n',
            '\n    <article class="card">\n',
            '      <a href="osaka-usj.html"><img src="images/osaka-usj-hero.webp" alt="大阪USJ環球影城" style="width:100%;height:auto;display:block;" width="1536" height="1024"></a>\n',
            '      <div class="card-body">\n',
            '        <a href="japan-travel.html" class="cat-tag">日本自由行</a>\n',
            '        <h3><a href="osaka-usj.html">【大阪USJ】環球影城全攻略</a></h3>\n',
            '        <p>任天堂世界、哈利波特園區，大阪環球影城遊玩全指南。</p>\n',
            '        <a href="osaka-usj.html" class="read-more">閱讀文章 →</a>\n',
            '      </div>\n',
            '    </article>\n',
            '\n    <article class="card">\n',
            '      <a href="japan-budget-guide.html"><img src="images/japan-budget-hero.webp" alt="日本預算指南" style="width:100%;height:auto;display:block;" width="1536" height="1024"></a>\n',
            '      <div class="card-body">\n',
            '        <a href="japan-travel.html" class="cat-tag">日本自由行</a>\n',
            '        <h3><a href="japan-budget-guide.html">【日本預算】自由行費用全解析</a></h3>\n',
            '        <p>機票、住宿、交通、餐飲，日本自由行預算完整指南。</p>\n',
            '        <a href="japan-budget-guide.html" class="read-more">閱讀文章 →</a>\n',
            '      </div>\n',
            '    </article>\n'
        ]
        
        # 在 </div> 之前插入新卡片
        new_lines = lines[:insert_pos] + new_cards + lines[insert_pos:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        
        print("[OK] 已添加 3 篇文章卡片到 japan-travel.html")
        if not has_food:
            print("  - 大阪美食攻略")
        if not has_usj:
            print("  - 大阪USJ環球影城")
        if not has_budget:
            print("  - 日本預算指南")
