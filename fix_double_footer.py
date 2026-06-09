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
    
    # 匹配舊 footer 區塊：從 <!-- Footer --> 到 </footer>（下一個 footer 之前）
    # 使用非貪婪匹配，只匹配第一個 footer
    pattern = r'(\s*)<!-- Footer -->\s*<footer class="footer">.*?</footer>\s*(<script src="script\.js"></script>)?'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        print(f"  找到舊 footer，刪除中...")
        # 刪除舊 footer，保留 script.js（如果有的話）
        new_content = re.sub(pattern, r'\n    <script src="script.js"></script>', content)
        
        # 寫回檔案
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ 已修復")
    else:
        print(f"  ⚠️ 未找到舊 footer 模式")

print("\n完成！")
