#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 osaka-usj.html 的「必玩設施Top 10」h2 標題後方插入圖片"""

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\osaka-usj.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 找標題位置
heading = "<h2>必玩設施Top 10</h2>"
idx = content.find(heading)

if idx == -1:
    import sys
    sys.exit("ERROR: Heading not found")

# 找到 </h2> 結尾位置
heading_end = idx + len(heading)

# 要插入的圖片 HTML（圓角 16px + 陰影）
image_html = """

<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;">
  <img src="images/ollieyu-osaka-usj.webp" alt="大阪環球影城必玩設施實戰心得" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
</div>

"""

# 在 </h2> 後方插入圖片
new_content = content[:heading_end] + image_html + content[heading_end:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("SUCCESS: Image inserted after heading")
print("Image: images/ollieyu-osaka-usj.webp")
print("Style: border-radius:16px, box-shadow")
