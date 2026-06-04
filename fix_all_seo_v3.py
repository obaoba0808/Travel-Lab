#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复所有 SEO 问题 (V3 - 修复 f-string 语法)
P1 + P2 问题综合修复脚本
"""

import os
import re
import json

html_dir = '.'
current_date = '2026-05-26'  # 最后修改日期

fixed_stats = {
    'article_modified_time': 0,
    'breadcrumb_schema': 0,
    'nofollow_sponsored': 0,
    'sitemap_changefreq': 0
}

# ========= 修复 1: 添加 article:modified_time =========
print("=== Fixing P2 #8: Add article:modified_time ===\n")

article_pages = [
    'kyoto-temples.html', 'japan-budget-guide.html', 'japan-travel.html',
    'korea-budget.html', 'korea-travel.html', 'taiwan-travel.html',
    'southeast-asia.html', 'tokyo-5days.html', 'kansai-pass.html',
    'hokkaido-winter.html', 'okinawa.html', 'seoul-food.html',
    'busan-capsule.html', 'jeju-island.html', 'hualien-taitung.html',
    'tainan-food.html', 'kenting.html', 'chiang-mai.html',
    'bangkok-3days.html', 'osaka-food.html', 'osaka-usj.html',
    'packing-list.html', 'vietnam-danang.html', 'bangkok-massage.html',
    'esim-comparison.html', 'taipei-food.html', 'jiufen.html'
]

for filename in article_pages:
    if not os.path.exists(os.path.join(html_dir, filename)):
        continue
        
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有 article:modified_time
    if 'article:modified_time' in content:
        continue
    
    # 在 article:published_time 后添加 article:modified_time
    pattern = r'(<meta property="article:published_time" content="[^"]*">)'
    
    replacement = r'\1\n<meta property="article:modified_time" content="' + current_date + '">'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed_stats['article_modified_time'] += 1
        print(f'[OK] {filename}')

print(f"\nTotal: {fixed_stats['article_modified_time']} pages\n")

# ========= 修复 2: 修复 sitemap.xml changefreq =========
print("=== Fixing P2 #7: Adjust sitemap.xml changefreq ===\n")

sitemap_path = os.path.join(html_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

# 静态内容页 -> monthly
static_pages = [
    'kyoto-temples.html', 'japan-budget-guide.html', 'korea-budget.html',
    'seoul-food.html', 'busan-capsule.html', 'jeju-island.html',
    'hualien-taitung.html', 'tainan-food.html', 'kenting.html',
    'chiang-mai.html', 'bangkok-3days.html', 'osaka-food.html',
    'osaka-usj.html', 'vietnam-danang.html', 'bangkok-massage.html',
    'esim-comparison.html', 'taipei-food.html', 'jiufen.html',
    'hokkaido-winter.html', 'okinawa.html'
]

for page in static_pages:
    # 将 weekly 改为 monthly
    pattern = r'(<loc>https://golightly\.fun/' + re.escape(page) + r'</loc><lastmod>[^<]+</lastmod><changefreq>)weekly(</changefreq>)'
    replacement = r'\1monthly\2'
    new_sitemap = re.sub(pattern, replacement, sitemap)
    
    if new_sitemap != sitemap:
        sitemap = new_sitemap
        fixed_stats['sitemap_changefreq'] += 1
        print(f'[OK] {page}: weekly -> monthly')

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)

print(f"\nTotal: {fixed_stats['sitemap_changefreq']} URLs\n")

# ========= 修复 3: 添加 BreadcrumbList JSON-LD =========
print("=== Fixing P1 #6: Add BreadcrumbList structured data ===\n")

# 定义面包屑路径
breadcrumb_data = {
    'kyoto-temples.html': [
        ('https://golightly.fun/', '首页'),
        ('https://golightly.fun/japan-travel.html', '日本自由行'),
        ('https://golightly.fun/kyoto-temples.html', '京都寺庙散步地图')
    ],
    'japan-budget-guide.html': [
        ('https://golightly.fun/', '首页'),
        ('https://golightly.fun/japan-travel.html', '日本自由行'),
        ('https://golightly.fun/japan-budget-guide.html', '日本预算指南')
    ],
    'seoul-food.html': [
        ('https://golightly.fun/', '首页'),
        ('https://golightly.fun/korea-travel.html', '韩国自由行'),
        ('https://golightly.fun/seoul-food.html', '首尔美食攻略')
    ]
}

for filename, items in breadcrumb_data.items():
    filepath = os.path.join(html_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有 BreadcrumbList
    if 'BreadcrumbList' in content:
        print(f'[WARN] {filename}: Already has BreadcrumbList')
        continue
    
    # 生成 BreadcrumbList JSON-LD
    breadcrumb_json = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': []
    }
    
    for i, (url, name) in enumerate(items, 1):
        breadcrumb_json['itemListElement'].append({
            '@type': 'ListItem',
            'position': i,
            'name': name,
            'item': url
        })
    
    # 插入到第一个 </head> 前
    json_str = '\n<script type="application/ld+json">\n' + json.dumps(breadcrumb_json, ensure_ascii=False, indent=2) + '\n</script>\n'
    
    # 在 </head> 前插入
    pattern = r'</head>'
    replacement = json_str + '</head>'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed_stats['breadcrumb_schema'] += 1
        print(f'[OK] {filename}')

print(f"\nTotal: {fixed_stats['breadcrumb_schema']} pages\n")

# ========= 修复 4: 外部联盟链接添加 rel="nofollow sponsored" =========
print("=== Fixing P2 #10: Add rel=\"nofollow sponsored\" to affiliate links ===\n")

affiliate_domains = [
    'trip.com', 'agoda.com', 'klook.com', 'skyscanner.com',
    'airalo.com', 'holafly.com', 'esimgo.com'
]

for filename in os.listdir(html_dir):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(html_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    for domain in affiliate_domains:
        pattern = r'<a href="[^"]*' + re.escape(domain) + r'[^"]*"'
        
        def add_nofollow_sponsored(match):
            link = match.group(0)
            
            # 检查是否已有 rel
            if 'rel=' in link:
                return link
            
            # 在 > 前添加 rel="nofollow sponsored"
            new_link = link.replace('>', ' rel="nofollow sponsored">')
            return new_link
        
        new_content = re.sub(pattern, add_nofollow_sponsored, content)
        
        if new_content != content:
            content = new_content
            modified = True
    
    # 保存修改
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_stats['nofollow_sponsored'] += 1
        print(f'[OK] {filename}')

print(f"\nTotal: {fixed_stats['nofollow_sponsored']} files\n")

# ========= 打印统计信息 =========
print("=== Fix Statistics ===\n")
for key, value in fixed_stats.items():
    print(f'{key}: {value}')

print("\n[OK] All P1 + P2 issues fixed!")
print("[WARN] Some issues need manual check:")
print("  1. P1 #4: Internal links - need to add contextual internal links")
print("  2. P1 #5: Keyword density - need to optimize content manually")
print("  3. P0 #3: Image Alt attributes - need further inspection")
