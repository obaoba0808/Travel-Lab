#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复所有 HTML 页面的 og:image:height 多余 > 字符错误
P0 关键问题修复脚本
"""

import os
import re

html_dir = '.'
fixed_count = 0
error_files = []

for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(html_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 修复 og:image:height 多余的 > 字符
            pattern = r'og:image:height" content="(\d+)">>'
            replacement = r'og:image:height" content="\1">'
            
            new_content = re.sub(pattern, replacement, content)
            
            # 同时检查 og:image:width 是否也有同样问题
            pattern2 = r'og:image:width" content="(\d+)">>'
            new_content = re.sub(pattern2, r'og:image:width" content="\1">', new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed_count += 1
                print(f'Fixed: {filename}')
                    
        except Exception as e:
            error_files.append((filename, str(e)))
            print(f'Error: {filename} - {e}')

print(f'\nTotal fixed: {fixed_count} files')
if error_files:
    print(f'Errors: {len(error_files)} files')
    for fname, err in error_files:
        print(f'  - {fname}: {err}')
