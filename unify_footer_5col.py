# -*- coding: utf-8 -*-
"""全站 footer 統一為 5 欄（刪除「法律資訊」第6欄），比照 japan-drugstore-checklist.html"""
import glob, re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if filepath == 'japan-drugstore-checklist.html':
        return False
    
    # 匹配「法律資訊」footer-col — 用 <ul><li> 結構
    pattern = r'<div class="footer-col"><h4>[^<]*法律資訊[^<]*</h4>\s*<ul>\s*<li><a href="about\.html">關於我們</a></li>\s*<li><a href="contact\.html">聯絡我們</a></li>\s*<li><a href="privacy\.html">隱私權政策</a></li>\s*<li><a href="terms\.html">使用條款</a></li>\s*<li><a href="disclaimer\.html">免責聲明</a></li>\s*</ul>\s*</div>'
    
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

print(f"已刪除第6欄: {len(done)} 頁")
for d in done:
    print(f"  - {d}")
