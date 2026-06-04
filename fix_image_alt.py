#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复所有 HTML 页面的图片 Alt 属性
P0 关键问题 #3 修复脚本
"""

import os
import re

html_dir = '.'
fixed_count = 0

def fix_alt_text(alt_text, src_text):
    """根据图片类型和 src 修复 alt 文本"""
    
    # 装饰性图片 (Trip.com / Agoda / Klook 等营销图片)
    if 'trip.com' in src_text.lower() or 'agoda' in src_text.lower() or 'klook' in src_text.lower():
        # 营销图片应该为空 alt (装饰性)
        return ''
    
    # 内容图片 - 检查是否过于营销化
    if '专属优惠' in alt_text or '促销' in alt_text or '优惠' in alt_text:
        # 移除营销词汇，保留描述性部分
        alt_text = alt_text.replace('专属优惠', '').replace('促销', '').replace('优惠', '')
        alt_text = alt_text.strip(' -_')
    
    # 如果 alt 为空或太短，根据文件名生成描述性 alt
    if len(alt_text) < 3:
        # 从文件名提取信息
        filename = os.path.basename(src_text)
        name_without_ext = os.path.splitext(filename)[0]
        
        # 将文件名转换为可读文本 (替换 - 为空格)
        readable_name = name_without_ext.replace('-', ' ').replace('_', ' ')
        
        # 添加适当的后缀
        if 'hero' in filename:
            alt_text = f"{readable_name} 主图"
        elif 'thumbnail' in filename or 'thumb' in filename:
            alt_text = f"{readable_name} 缩略图"
        else:
            alt_text = readable_name
    
    return alt_text

for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(html_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 找出所有图片标签
            img_pattern = r'<img[^>]*>'
            imgs = re.findall(img_pattern, content)
            
            if not imgs:
                continue
            
            new_content = content
            file_fixed = False
            
            for img in imgs:
                # 提取 src 和 alt
                src_match = re.search(r'src="([^"]*)"', img)
                alt_match = re.search(r'alt="([^"]*)"', img)
                
                src_text = src_match.group(1) if src_match else ''
                alt_text = alt_match.group(1) if alt_match else None
                
                # 判断是否需要修复
                need_fix = False
                
                if alt_text is None:
                    # 缺失 alt 属性
                    need_fix = True
                    new_alt = fix_alt_text('', src_text)
                elif len(alt_text) < 3:
                    # alt 太短
                    need_fix = True
                    new_alt = fix_alt_text(alt_text, src_text)
                elif '专属优惠' in alt_text or '促销' in alt_text:
                    # 过度营销
                    need_fix = True
                    new_alt = fix_alt_text(alt_text, src_text)
                
                if need_fix:
                    if alt_text is None:
                        # 添加 alt 属性
                        new_img = img.replace('>', f' alt="{new_alt}">', 1)
                    else:
                        # 替换 alt 属性
                        new_img = img.replace(f'alt="{alt_text}"', f'alt="{new_alt}"', 1)
                    
                    new_content = new_content.replace(img, new_img, 1)
                    file_fixed = True
            
            if file_fixed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed_count += 1
                print(f'Fixed: {filename}')
                
        except Exception as e:
            print(f'Error: {filename} - {e}')

print(f'\nTotal fixed: {fixed_count} files')
