#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查所有 HTML 页面的图片 Alt 属性
P0 关键问题 #3 检查脚本
"""

import os
import re

html_dir = '.'
issues = []

print("=== 图片 Alt 属性检查 ===\n")

for filename in sorted(os.listdir(html_dir)):
    if filename.endswith('.html'):
        filepath = os.path.join(html_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 找出所有图片标签
        img_tags = re.findall(r'<img[^>]*>', content)
        
        if not img_tags:
            continue
        
        file_issues = []
        for img in img_tags:
            # 检查 alt 属性
            alt_match = re.search(r'alt="([^"]*)"', img)
            src_match = re.search(r'src="([^"]*)"', img)
            
            if not alt_match:
                # 缺失 alt 属性
                file_issues.append({
                    'type': 'missing',
                    'img': img[:80]
                })
            else:
                alt_text = alt_match.group(1)
                if len(alt_text) < 3:
                    # alt 文本太短
                    file_issues.append({
                        'type': 'too_short',
                        'alt': alt_text,
                        'img': img[:80]
                    })
                elif 'Trip.com' in alt_text or '优惠' in alt_text:
                    # 过度营销的 alt 文本
                    file_issues.append({
                        'type': 'overly_promotional',
                        'alt': alt_text,
                        'img': img[:80]
                    })
        
        if file_issues:
            issues.append({
                'file': filename,
                'issues': file_issues
            })
            print(f"⚠️  {filename}: {len(file_issues)} 个问题")
            for issue in file_issues[:3]:  # 只显示前3个
                if issue['type'] == 'missing':
                    print(f"    - 缺失 alt: {issue['img']}...")
                elif issue['type'] == 'too_short':
                    print(f"    - alt 太短: \"{issue['alt']}\"")
                elif issue['type'] == 'overly_promotional':
                    print(f"    - 过度营销: \"{issue['alt'][:30]}...\"")

print(f"\n总计: {len(issues)} 个文件需要修复")
print("\n建议操作:")
print("1. 装饰性图片: alt=\"\" (空 alt)")
print("2. 内容图片: 描述性 alt (包含关键词但不过度)")
print("3. 营销图片: 移除品牌名称，改为描述性文本")
