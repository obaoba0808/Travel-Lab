# -*- coding: utf-8 -*-
"""
修復雙 footer 問題：刪除舊的 <footer class="footer"> 區塊
"""
import os
import re

# 需要修復的檔案
files_to_fix = [
    "angkor-wat-2days.html",
    "kualalumpur-3days.html",
    "monthly-review.html",
    "singapore-3days.html",
    "southeast-asia.html"
]

base_dir = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"

for filename in files_to_fix:
    filepath = os.path.join(base_dir, filename)
    print(f"處理: {filename}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到舊 footer 的開始和結束
    # 從 <footer class="footer"> 到 </footer>（第一個）
    old_footer_start = content.find('<footer class="footer">')
    if old_footer_start == -1:
        print(f"  ⚠️ 未找到舊 footer")
        continue
    
    # 找到對應的 </footer>
    # 需要計算嵌套，但這裡 footer 內部沒有其他 footer，所以可以直接找
    old_footer_end = content.find('</footer>', old_footer_start)
    if old_footer_end == -1:
        print(f"  ⚠️ 未找到舊 footer 結束標籤")
        continue
    
    # 找到新的 site-footer 開始位置
    new_footer_start = content.find('<footer class="site-footer">', old_footer_end)
    if new_footer_start == -1:
        print(f"  ⚠️ 未找到新 footer")
        continue
    
    # 刪除從舊 footer 開始到新 footer 之前的所有內容
    before_old = content[:old_footer_start]
    after_new = content[new_footer_start:]
    
    # 保留一個換行
    new_content = before_old.rstrip() + "\n\n    " + after_new
    
    # 寫回檔案
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  ✅ 已刪除舊 footer")

print("\n完成！")
