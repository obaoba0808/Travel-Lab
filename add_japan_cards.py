#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 japan-travel.html 的 card-grid 里添加缺失的 3 篇日本文章卡片"""

import re

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\japan-travel.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 检查是否已经有这3篇文章
has_osaka_food = 'osaka-food.html' in content
has_osaka_usj = 'osaka-usj.html' in content
has_japan_budget = 'japan-budget-guide.html' in content

if has_osaka_food and has_osaka_usj and has_japan_budget:
    print("[SKIP] 3 篇文章卡片已存在")
else:
    # 在最后一个 </article> 之后、</div> 之前插入新卡片
    # 找到 card-grid 里最后一个 </article> 的位置
    last_article_end = content.rfind('</article>', content.find('class="card-grid"'))
    
    if last_article_end == -1:
        print("[ERROR] 找不到 card-grid 里的 article")
    else:
        # 插入点：last_article_end + len('</article>')
        insert_pos = last_article_end + len('</article>')
        
        new_cards = """
    
    <article class="card">
      <a href="osaka-food.html"><img src="images/osaka-food-hero.webp" alt="大阪美食攻略" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="japan-travel.html" class="cat-tag">日本自由行</a>
        <h3><a href="osaka-food.html">【大阪美食】必吃美食地圖</a></h3>
        <p>章魚燒、大阪燒、串炸，大阪必吃美食全攻略。</p>
        <a href="osaka-food.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
    
    <article class="card">
      <a href="osaka-usj.html"><img src="images/osaka-usj-hero.webp" alt="大阪環球影城" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="japan-travel.html" class="cat-tag">日本自由行</a>
        <h3><a href="osaka-usj.html">【大阪USJ】環球影城全攻略</a></h3>
        <p>任天堂世界、哈利波特園區，大阪環球影城遊玩全指南。</p>
        <a href="osaka-usj.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
    
    <article class="card">
      <a href="japan-budget-guide.html"><img src="images/japan-budget-hero.webp" alt="日本預算指南" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="japan-travel.html" class="cat-tag">日本自由行</a>
        <h3><a href="japan-budget-guide.html">【日本預算】自由行費用全解析</a></h3>
        <p>機票、住宿、交通、餐飲，日本自由行預算完整指南。</p>
        <a href="japan-budget-guide.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
"""
        
        new_content = content[:insert_pos] + new_cards + content[insert_pos:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("[OK] 已添加 3 篇文章卡片到 japan-travel.html")
        print("  - 大阪美食攻略")
        print("  - 大阪環球影城")
        print("  - 日本預算指南")
