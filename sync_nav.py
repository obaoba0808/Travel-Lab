#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
同步所有子页面的导航下拉菜单，使其与 index.html 一致
用法: python sync_nav.py
"""
import re
import os
import sys

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_canonical_nav(html):
    """从 index.html 提取完整的导航区块"""
    pattern = r'(<nav class="main-nav">)(.*?</nav>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        return match.group(0)
    return None

def get_active_region(filepath):
    """判断当前页面应该高亮哪个导航项"""
    filename = os.path.basename(filepath)
    if filename == 'index.html':
        return 'index'
    if (filename.startswith('tokyo') or 
        filename.startswith('kansai') or 
        filename.startswith('hokkaido') or 
        filename.startswith('okinawa') or 
        filename.startswith('kyoto') or
        filename.startswith('osaka') or
        filename.startswith('japan')):
        return 'japan'
    if (filename.startswith('seoul') or 
        filename.startswith('busan') or 
        filename.startswith('jeju') or 
        filename.startswith('korea')):
        return 'korea'
    if (filename.startswith('hualien') or 
        filename.startswith('tainan') or 
        filename.startswith('kenting') or 
        filename.startswith('taipei') or 
        filename.startswith('jiufen') or
        filename.startswith('taiwan')):
        return 'taiwan'
    if (filename.startswith('chiang') or 
        filename.startswith('bangkok') or 
        filename.startswith('vietnam') or 
        filename.startswith('southeast')):
        return 'southeast'
    return 'index'  # 默认

def adjust_active_nav(nav_html, region):
    """调整导航的 active 状态"""
    # 移除所有 style="color:var(--tiffany);border-bottom-color:var(--tiffany);"
    nav_html = re.sub(r' style="color:var\(--tiffany\);border-bottom-color:var\(--tiffany\);"', '', nav_html)
    nav_html = nav_html.replace(' class="active"', ' "')
    
    if region == 'index':
        nav_html = nav_html.replace('<a href="index.html">首頁</a>', '<a href="index.html" class="active">首頁</a>')
    elif region == 'japan':
        nav_html = nav_html.replace('<a href="japan-travel.html">日本自由行 ▾</a>', '<a href="japan-travel.html" style="color:var(--tiffany);border-bottom-color:var(--tiffany);">日本自由行 ▾</a>')
    elif region == 'korea':
        nav_html = nav_html.replace('<a href="korea-travel.html">韓国自由行 ▾</a>', '<a href="korea-travel.html" style="color:var(--tiffany);border-bottom-color:var(--tiffany);">韓国自由行 ▾</a>')
    elif region == 'taiwan':
        nav_html = nav_html.replace('<a href="taiwan-travel.html">台湾旅游 ▾</a>', '<a href="taiwan-travel.html" style="color:var(--tiffany);border-bottom-color:var(--tiffany);">台湾旅游 ▾</a>')
    elif region == 'southeast':
        nav_html = nav_html.replace('<a href="southeast-asia.html">东南亚自由行 ▾</a>', '<a href="southeast-asia.html" style="color:var(--tiffany);border-bottom-color:var(--tiffany);">东南亚自由行 ▾</a>')
    
    return nav_html

def main():
    travel_lab_dir = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'
    
    # 读取 index.html 的导航
    index_path = os.path.join(travel_lab_dir, 'index.html')
    index_html = read_file(index_path)
    canonical_nav = extract_canonical_nav(index_html)
    
    if not canonical_nav:
        print("[ERROR] Cannot extract nav from index.html")
        sys.exit(1)
    
    print("[OK] Extracted canonical navigation from index.html")
    
    # 遍历所有 HTML 文件（排除 index.html）
    for filename in os.listdir(travel_lab_dir):
        if not filename.endswith('.html') or filename == 'index.html' or filename == '404.html':
            continue
        
        filepath = os.path.join(travel_lab_dir, filename)
        file_html = read_file(filepath)
        
        # 找出当前页面应该高亮哪个区域
        region = get_active_region(filepath)
        
        if not region:
            print("[SKIP] Cannot determine region for: " + filename)
            continue
        
        # 用 canonical nav 替换
        new_nav = adjust_active_nav(canonical_nav, region)
        
        # 替换文件中的导航区块
        pattern = r'<nav class="main-nav">.*?</nav>'
        new_html = re.sub(pattern, new_nav, file_html, flags=re.DOTALL)
        
        if new_html != file_html:
            write_file(filepath, new_html)
            print("[OK] Updated: " + filename + " (active: " + region + ")")
        else:
            print("[SKIP] No change: " + filename)
    
    print("\n[OK] All pages updated!")

if __name__ == '__main__':
    main()
