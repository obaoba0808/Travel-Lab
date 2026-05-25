#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在 okinawa.html 的「Day 2」day-card 後方插入圖片"""

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\okinawa.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 要找到的 Day 2 區塊結尾（tip-box 的 </div> 之後）
# 插入在 </div> 後方（Day 2 區塊結束後）
target_pattern = """    </ul>
    <div class="tip-box">
      <strong>💡 建議：</strong>北部路程較遠，建議早上8點前出發。水族館上午人少，下午1點後旅遊團湧入會很擠。
    </div>
  </div>"""

if target_pattern in content:
    # 要插入的圖片 HTML（圓角 16px + 陰影）
    image_html = """
    
<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;">
  <img src="images/ollieyu-okinawa.webp" alt="沖繩自駕實戰心得：美麗海水族館、古宇利島、心形岩" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
</div>

"""
    
    # 在 Day 2 區塊結尾後方插入圖片
    replacement = target_pattern + image_html
    new_content = content.replace(target_pattern, replacement, 1)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("[OK] Image inserted successfully!")
    print("  Location: After Day 2 section (tip-box)")
    print("  Image: images/ollieyu-okinawa.webp")
    print("  Style: border-radius:16px, box-shadow")
else:
    print("[ERROR] Target pattern not found!")
    # 除錯：顯示檔案中的 Day 相關內容
    import re
    day_matches = re.findall(r'<span class="day-tag">Day \d+</span>', content)
    print(f"  Found {len(day_matches)} Day entries:")
    for i, match in enumerate(day_matches[:10]):
        print(f"    {i+1}. {match}")
