#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 japan-travel.html 的 card-grid 里添加缺失的 3 篇日本文章卡片（無 Unicode 輸出）"""

import os

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\japan-travel.html"

# 以二進制模式讀取（保留 CRLF）
with open(file_path, "rb") as f:
    raw = f.read()

# 解碼為字串（保留 \r\n）
content = raw.decode("utf-8")

# 檢查是否已有這 3 篇文章的卡片
has_food = '<article class="card">' in content and 'osaka-food.html' in content and 'osaka-food-hero.webp' in content
has_usj = '<article class="card">' in content and 'osaka-usj.html' in content and 'osaka-usj-hero.webp' in content
has_budget = '<article class="card">' in content and 'japan-budget-guide.html' in content and 'japan-budget-hero.webp' in content

# 輸出狀態（只用 ASCII）
status = []
status.append("Check status:")
status.append("  - Osaka food card: " + ("EXISTS" if has_food else "MISSING"))
status.append("  - Osaka USJ card: " + ("EXISTS" if has_usj else "MISSING"))
status.append("  - Japan budget card: " + ("EXISTS" if has_budget else "MISSING"))

for line in status:
    print(line)

if has_food and has_usj and has_budget:
    print("\n[SKIP] 3 articles already exist")
else:
    # 找到最後一個 </article> 的位置（在 card-grid 內）
    card_grid_start = content.find('<div class="card-grid">')
    
    if card_grid_start == -1:
        print("[ERROR] Cannot find card-grid")
    else:
        # 在 card-grid 區域內找最後一個 </article>
        search_pos = card_grid_start
        last_article_end = -1
        while True:
            pos = content.find('</article>', search_pos)
            if pos == -1 or pos > content.find('</div>', card_grid_start + 1000):
                break
            last_article_end = pos
            search_pos = pos + len('</article>')
        
        if last_article_end == -1:
            print("[ERROR] Cannot find last article in card-grid")
        else:
            # 插入點：最後一個 </article> 之後
            insert_pos = last_article_end + len('</article>')
            
            # 3 個新卡片的 HTML（遵循 CRLF \r\n）
            new_cards = "\r\n    <article class=\"card\">\r\n      <a href=\"osaka-food.html\"><img src=\"images/osaka-food-hero.webp\" alt=\"Osaka Food\" style=\"width:100%;height:auto;display:block;\" width=\"1536\" height=\"1024\"></a>\r\n      <div class=\"card-body\">\r\n        <a href=\"japan-travel.html\" class=\"cat-tag\">日本自由行</a>\r\n        <h3><a href=\"osaka-food.html\">【大阪美食】必吃美食地圖</a></h3>\r\n        <p>章魚燒、大阪燒、串炸，大阪必吃美食全攻略。</p>\r\n        <a href=\"osaka-food.html\" class=\"read-more\">閱讀文章 →</a>\r\n      </div>\r\n    </article>\r\n    \r\n    <article class=\"card\">\r\n      <a href=\"osaka-usj.html\"><img src=\"images/osaka-usj-hero.webp\" alt=\"Osaka USJ\" style=\"width:100%;height:auto;display:block;\" width=\"1536\" height=\"1024\"></a>\r\n      <div class=\"card-body\">\r\n        <a href=\"japan-travel.html\" class=\"cat-tag\">日本自由行</a>\r\n        <h3><a href=\"osaka-usj.html\">【大阪USJ】環球影城全攻略</a></h3>\r\n        <p>超級瑪莉世界、哈利波特園區，大阪環球影城遊玩全指南。</p>\r\n        <a href=\"osaka-usj.html\" class=\"read-more\">閱讀文章 →</a>\r\n      </div>\r\n    </article>\r\n    \r\n    <article class=\"card\">\r\n      <a href=\"japan-budget-guide.html\"><img src=\"images/japan-budget-hero.webp\" alt=\"Japan Budget\" style=\"width:100%;height:auto;display:block;\" width=\"1536\" height=\"1024\"></a>\r\n      <div class=\"card-body\">\r\n        <a href=\"japan-travel.html\" class=\"cat-tag\">日本自由行</a>\r\n        <h3><a href=\"japan-budget-guide.html\">【日本預算】自由行費用全解析</a></h3>\r\n        <p>機票、住宿、交通、餐飲，日本自由行預算完整指南。</p>\r\n        <a href=\"japan-budget-guide.html\" class=\"read-more\">閱讀文章 →</a>\r\n      </div>\r\n    </article>\r\n    "
            
            # 插入新卡片
            new_content = content[:insert_pos] + new_cards + content[insert_pos:]
            
            # 以二進制模式寫入（保留 CRLF）
            with open(file_path, "wb") as f:
                f.write(new_content.encode("utf-8"))
            
            print("\n[OK] Added 3 article cards to japan-travel.html")
            if not has_food:
                print("  - Osaka food guide")
            if not has_usj:
                print("  - Osaka USJ guide")
            if not has_budget:
                print("  - Japan budget guide")
