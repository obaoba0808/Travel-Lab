# -*- coding: utf-8 -*-
"""刪除 footer 中「📋 關於我們」欄位（與新加的 footer-nav-row 重複）"""
import glob, re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配整個「關於我們」footer-col
    pattern = r'<div class="footer-col"><h4>📋 關於我們</h4>\s*<a href="about\.html">關於均在路上</a>\s*<a href="contact\.html">聯絡我們</a>\s*<a href="privacy\.html">隱私權政策</a>\s*<a href="terms\.html">使用條款</a>\s*<a href="disclaimer\.html">免責聲明</a>\s*</div>'
    
    new_content = re.sub(pattern, '', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

files = sorted(glob.glob('*.html'))
done = []
for f in files:
    if process_file(f):
        done.append(f)

print(f"已刪除「關於我們」欄: {len(done)} 頁")
for d in done:
    print(f"  - {d}")
