#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修復所有 HTML 檔案的 <title> 標籤
從 og:title 提取正確標題，替換損壞的 <title> 標籤
"""

import os
import re

def fix_html_file(filepath):
    """修復單個 HTML 檔案的 title 標籤"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 從 og:title 提取正確標題
    og_match = re.search(r'<meta property="og:title" content="(.*?)"', content)
    if not og_match:
        print(f'  SKIP (no og:title): {os.path.basename(filepath)}')
        return False
    
    correct_title = og_match.group(1)
    
    # 替換整個損壞的 title 標籤
    # 模式：<title>任意內容</title> → <title>正確標題</title>
    new_content = re.sub(
        r'<title>.*?</title>',
        f'<title>{correct_title}</title>',
        content,
        flags=re.DOTALL
    )
    
    # 同時修復可能損壞的 meta description 和 keywords
    # 檢查是否有 ><meta 這種損壞模式
    new_content = re.sub(r'">><meta', '"><meta', new_content)
    new_content = re.sub(r'">><title>', '"><title>', new_content)
    
    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    # 切換到腳本所在目錄
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print('HTML Title Tag Repair Tool')
    print('=' * 60)
    
    fixed_count = 0
    error_count = 0
    skipped_count = 0
    
    # 處理所有 HTML 檔案
    for filename in os.listdir('.'):
        if not filename.endswith('.html'):
            continue
        
        filepath = os.path.join('.', filename)
        
        try:
            if fix_html_file(filepath):
                print(f'✓ FIXED: {filename}')
                fixed_count += 1
            else:
                print(f'  OK:    {filename}')
                skipped_count += 1
        except Exception as e:
            print(f'✗ ERROR: {filename} - {str(e)}')
            error_count += 1
    
    print('=' * 60)
    print(f'Repair complete!')
    print(f'Fixed:   {fixed_count} files')
    print(f'Skipped: {skipped_count} files')
    print(f'Errors:  {error_count} files')
    
    # 顯示幾個修復後的標題示例
    print(f'\nSample fixed titles:')
    for filename in ['tokyo-5days.html', 'osaka-food.html', 'kyoto-temples.html', 'index.html']:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read(3000)
            title_match = re.search(r'<title>(.*?)</title>', content)
            if title_match:
                print(f'  {filename}: {title_match.group(1)[:60]}')

if __name__ == '__main__':
    main()
