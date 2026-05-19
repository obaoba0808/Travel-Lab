#!/usr/bin/env python3
"""修復所有 HTML 頁面的東南亞下拉選單，加入 hongkong-3days.html"""

import os
import re

# 工作目錄
work_dir = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"

# 要插入的香港連結 HTML
hongkong_link = '\n          <a href="hongkong-3days.html">香港3天2夜攻略</a>'

# 在 vietnam-danang.html 連結之後插入
target_pattern = r'(<a href="vietnam-danang.html">越南峴港攻略</a>)'

def fix_dropdown(content):
    """修復東南亞下拉選單"""
    replacement = r'\1' + hongkong_link
    new_content = re.sub(target_pattern, replacement, content)
    return new_content

# 處理所有 HTML 檔案
html_files = [f for f in os.listdir(work_dir) if f.endswith('.html') and not f.startswith('_')]

fixed_count = 0
for filename in html_files:
    filepath = os.path.join(work_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 檢查是否已經有 hongkong-3days.html 在東南亞下拉選單中
    if 'href="hongkong-3days.html"' in content and '東南亞自由行 ▾' in content:
        # 檢查是否在 dropdown-menu 中
        seasia_section = re.search(r'東南亞自由行 ▾.*?</div>\s*</div>', content, re.DOTALL)
        if seasia_section and 'hongkong-3days.html' in seasia_section.group(0):
            print(f"[OK] 已包含: {filename}")
            continue
    
    # 修復
    new_content = fix_dropdown(content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[Fix] 已修復: {filename}")
        fixed_count += 1
    else:
        print(f"[Skip] 未找到目標: {filename}")

print(f"\n完成！共修復 {fixed_count} 個檔案")
