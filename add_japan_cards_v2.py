#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 japan-travel.html 的 card-grid 里添加缺失的 3 篇日本文章卡片"""

import re

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\japan-travel.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 检查 card-grid 里是否已经有这3篇文章的卡片
has_osaka_food = 'osaka-food.html"' in content and 'osaka-food-hero.webp' in content
has_osaka_usj = 'osaka-usj.html"' in content and 'osaka-usj-hero.webp' in content
has_japan_budget = 'japan-budget-guide.html"' in content and 'japan-budget-hero.webp' in content

print("检查 card-grid 状态：")
print(f"  - 大阪美食卡片: {'✅ 已存在' if has_osaka_food else '❌ 缺失'}")
print(f"  - 大阪USJ卡片: {'✅ 已存在' if has_osaka_usj else '❌ 缺失'}")
print(f"  - 日本预算卡片: {'✅ 已存在' if has_japan_budget else '❌ 缺失'}")

if has_osaka_food and has_osaka_usj and has_japan_budget:
    print("\n[SKIP] 3 篇文章卡片已存在")
else:
    # 找到 card-grid 的结束标签位置
    # 找到最后一个 </article> 的位置
    last_article_end = content.rfind('</article>', content.find('<div class="card-grid">'))
    
    if last_article_end == -1:
        print("[ERROR] 找不到 card-grid 里的 article")
    else:
        # 插入点：最后一个 </article> 之后
        insert_pos = last_article_end + len('</article>')
        
        new_cards = """
    
    <article class="card">
      <a href="osaka-food.html"><img src="images/osaka-food-hero.webp" alt="大阪美食攻略" style="width:100%;height:auto;display:block;" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="japan-travel.html" class="cat-tag">日本自由行</a>
        <h3><a href="osaka-food.html">【大阪】必吃美食地圖</a></h3>
        <p>章魚燒、大阪燒、串炸，大阪必吃美食全攻略。</p>
        <a href="osaka-food.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
    
    <article class="card">
      <a href="osaka-usj.html"><img src="images/osaka-usj-hero.webp" alt="大阪USJ環球影城" style="width:100%;height:auto;display:block;" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="japan-travel.html" class="cat-tag">日本自由行</a>
        <h3><a href="osaka-usj.html">【大阪USJ】環球影城全攻略</a></h3>
        <p>任天堂世界、哈利波特園區，大阪環球影城遊玩全指南。</p>
        <a href="osaka-usj.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
    
    <article class="card">
      <a href="japan-budget-guide.html"><img src="images/japan-budget-hero.webp" alt="日本預算指南" style="width:100%;height:auto;display:block;" width="1536" height="1024"></a>
      <div class="card-body">
        <a href="japan-travel.html" class="cat-tag">日本自由行</a>
        <h3><a href="japan-budget-guide.html">【日本預算】自由行費用全解析</a></h3>
        <p>機票、住宿、交通、餐飲，日本自由行預算完整指南。</p>
        <a href="japan-budget-guide.html" class="read-more">閱讀文章 →</a>
      </div>
    </article>
"""
        
        # 在插入点之后，需要保留原来的 </div>（card-grid 结束标签）
        # 但我的 new_cards 已经包含了 3 个新卡片，需要在后面加上原来的 </div>
        # 让我重新构造
        
        # 找到 card-grid 的 </div> 结束标签
        card_grid_end = content.find('</div>', insert_pos)
        if card_grid_end == -1:
            print("[ERROR] 找不到 card-grid 的结束标签")
        else:
            # 在最后一个 </article> 之后插入新卡片
            new_content = content[:insert_pos] + new_cards + content[insert_pos:]
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            
            print("\n[OK] 已添加 3 篇文章卡片到 japan-travel.html")
            print("  - 大阪美食攻略")
            print("  - 大阪USJ環球影城")
            print("  - 日本預算指南")
