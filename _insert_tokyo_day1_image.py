#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 tokyo-5days.html 的「抵達東京 → 淺草 → 東京晴空塔」h3 標題後方插入圖片"""

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\tokyo-5days.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 要找到的 h3 標題
h3_heading = "<h3>抵達東京 → 淺草 → 東京晴空塔</h3>"

if h3_heading in content:
    # 要插入的圖片 HTML（圓角 16px + 陰影）
    image_html = """
    
<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;">
  <img src="images/ollieyu-tokyo.webp" alt="東京5天4夜實戰心得：抵達東京、淺草寺、東京晴空塔" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
</div>

"""
    
    # 在 </h3> 後方插入圖片
    new_content = content.replace(h3_heading, h3_heading + image_html, 1)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("[OK] Image inserted successfully!")
    print("  Location: After <h3>抵達東京 → 淺草 → 東京晴空塔</h3>")
    print("  Image: images/ollieyu-tokyo.webp")
    print("  Style: border-radius:16px, box-shadow")
else:
    print("[ERROR] Target h3 heading not found!")
    # 除錯：顯示檔案中的 h3 標題
    import re
    h3_matches = re.findall(r'<h3>.*?</h3>', content)
    print(f"  Found {len(h3_matches)} h3 headings:")
    for i, match in enumerate(h3_matches[:10]):
        print(f"    {i+1}. {match}")
