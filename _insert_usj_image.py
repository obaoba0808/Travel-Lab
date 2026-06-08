#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 osaka-usj.html 的「必玩設施Top 10」h2 標題後方插入圖片"""

import re

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\osaka-usj.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 要插入的圖片 HTML
image_html = """<h2>必玩設施Top 10</h2>

<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;">
  <img src="images/ollieyu-osaka-usj.webp" alt="大阪環球影城必玩設施實戰心得" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
</div>

<div class="highlight-box-beautify">"""

# 執行替換（取代原來的 <h2>...</h2>\n\n<div class="highlight-box-beautify">）
old_text = """<h2>必玩設施Top 10</h2>

<div class="highlight-box-beautify">"""

if old_text in content:
    content = content.replace(old_text, image_html)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Image inserted successfully!")
    print("  Location: After <h2>必玩設施Top 10</h2>")
    print("  Image: images/ollieyu-osaka-usj.webp")
else:
    print("[ERROR] Target location not found")
    # 除錯：顯示周邊內容
    idx = content.find("<h2>必玩設施Top 10</h2>")
    if idx != -1:
        print(f"  Found heading at position: {idx}")
        print(f"  Surrounding content: {repr(content[idx:idx+150])}")
    else:
        print("  Heading not found in file")
