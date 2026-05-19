#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
优化图片 ALT 标签，提高图片搜索可见度
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

def optimize_alt_tags(filepath):
    """优化单个文件的图片 ALT 标签"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 1. 修复空的 ALT 标签
        content = re.sub(r'alt=""', r'alt="旅游图片"', content)
        
        # 2. 修复无意义的 ALT 标签
        content = re.sub(r'alt="image"', r'alt="旅游图片"', content)
        content = re.sub(r'alt="img"', r'alt="旅游图片"', content)
        content = re.sub(r'alt="photo"', r'alt="旅游图片"', content)
        
        # 3. 为特定页面的图片添加更具描述性的 ALT 标签
        # 这需要根据每个页面的内容来定制，这里只是示例
        if 'japan-travel.html' in filepath:
            content = re.sub(r'alt="旅游图片"', r'alt="日本旅游风景"', content)
        elif 'korea-travel.html' in filepath:
            content = re.sub(r'alt="旅游图片"', r'alt="韩国旅游风景"', content)
        elif 'taiwan-travel.html' in filepath:
            content = re.sub(r'alt="旅游图片"', r'alt="台湾旅游风景"', content)
        elif 'southeast-asia.html' in filepath:
            content = re.sub(r'alt="旅游图片"', r'alt="东南亚旅游风景"', content)
        
        # 检查是否有修改
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Updated"
        else:
            return False, "No change"
            
    except Exception as e:
        return False, str(e)

def main():
    """主函数"""
    # 获取所有 HTML 文件
    html_files = []
    for f in os.listdir(BASE):
        if f.endswith('.html'):
            html_files.append(os.path.join(BASE, f))
    
    print(f"Found {len(html_files)} HTML files to process")
    
    updated = 0
    skipped = 0
    
    for filepath in html_files:
        success, msg = optimize_alt_tags(filepath)
        if success:
            updated += 1
            print(f"[UPDATED] {os.path.basename(filepath)}")
        else:
            skipped += 1
            if msg != "No change":
                print(f"[ERROR] {os.path.basename(filepath)}: {msg}")
    
    print(f"\nDone: {updated} files updated, {skipped} skipped")

if __name__ == '__main__':
    main()
