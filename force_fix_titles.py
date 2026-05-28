#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
強制修復所有 HTML 檔案的 <title> 標籤
從 og:title 提取正確標題，直接覆寫檔案
"""

import os
import re
import sys

def fix_html_file(filepath):
    """修復單個 HTML 檔案的 title 標籤"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f'  ERROR reading {os.path.basename(filepath)}: {e}')
        return False
    
    original_content = content
    
    # 從 og:title 提取正確標題
    og_match = re.search(r'<meta property="og:title" content="(.*?)"', content)
    if not og_match:
        print(f'  SKIP (no og:title): {os.path.basename(filepath)}')
        return False
    
    correct_title = og_match.group(1)
    
    # 方法：直接找到 <title> 和 </title> 的位置，替換中間的內容
    title_start = content.find('<title>')
    title_end = content.find('</title>')
    
    if title_start == -1 or title_end == -1:
        print(f'  SKIP (no title tag): {os.path.basename(filepath)}')
        return False
    
    # 重建 content
    new_content = content[:title_start + 7] + correct_title + content[title_end:]
    
    # 同時修復 Worker URL
    wrong_patterns = [
        'https://https://golightly-email.8107e1de.workers.dev.workers.dev',
        'https://golightly-email.8107e1de.workers.dev.workers.dev',
        'YOUR-WORKER-URL',
    ]
    correct_url = 'https://golightly-email.8107e1de.workers.dev'
    
    for wrong in wrong_patterns:
        if wrong in new_content:
            new_content = new_content.replace(wrong, correct_url)
    
    if new_content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)
            return True
        except Exception as e:
            print(f'  ERROR writing {os.path.basename(filepath)}: {e}')
            return False
    
    return False

def main():
    # 切換到腳本所在目錄
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print('=' * 60)
    print('HTML Title Tag Force Repair Tool')
    print('=' * 60)
    print()
    
    fixed_count = 0
    skipped_count = 0
    error_count = 0
    
    # 處理所有 HTML 檔案
    for filename in sorted(os.listdir('.')):
        if not filename.endswith('.html'):
            continue
        
        filepath = os.path.join('.', filename)
        
        try:
            if fix_html_file(filepath):
                print(f'✓ FIXED: {filename}')
                fixed_count += 1
            else:
                skipped_count += 1
        except Exception as e:
            print(f'✗ ERROR: {filename} - {str(e)}')
            error_count += 1
    
    print()
    print('=' * 60)
    print(f'Repair complete!')
    print(f'Fixed:   {fixed_count} files')
    print(f'Skipped: {skipped_count} files')
    print(f'Errors:  {error_count} files')
    print('=' * 60)
    
    # 顯示幾個修復後的標題示例
    if fixed_count > 0:
        print()
        print('Sample fixed titles:')
        for filename in ['index.html', 'tokyo-5days.html', 'osaka-food.html']:
            if os.path.exists(filename):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read(3000)
                    title_match = re.search(r'<title>(.*?)</title>', content)
                    if title_match:
                        print(f'  {filename}: {title_match.group(1)[:60]}')
                except:
                    pass

if __name__ == '__main__':
    main()
