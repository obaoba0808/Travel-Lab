#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 busan-capsule.html 的「🚃 膠囊列車基本資訊」h2 標題後方插入圖片"""

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\busan-capsule.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 要找到的 h2 標題
h2_heading = "<h2>🚃 膠囊列車基本資訊</h2>"

if h2_heading in content:
    # 要插入的圖片 HTML（圓角 16px + 陰影）
    image_html = """
    
<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;">
  <img src="images/ollieyu-busan.webp" alt="釜山膠囊列車實戰心得：海雲台、甘川文化村、海東龍宮寺" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
</div>

"""
    
    # 在 </h2> 後方插入圖片
    new_content = content.replace(h2_heading, h2_heading + image_html, 1)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("[OK] Image inserted successfully!")
    print("  Location: After <h2>🚃 膠囊列車基本資訊</h2>")
    print("  Image: images/ollieyu-busan.webp")
    print("  Style: border-radius:16px, box-shadow")
else:
    print("[ERROR] Target h2 heading not found!")
    # 除錯：顯示檔案中的 h2 標題
    import re
    h2_matches = re.findall(r'<h2>.*?</h2>', content)
    print(f"  Found {len(h2_matches)} h2 headings:")
    for i, match in enumerate(h2_matches[:10]):
        print(f"    {i+1}. {match}")
