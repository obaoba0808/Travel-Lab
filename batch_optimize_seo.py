#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量优化 Travel-Lab 文章页的 SEO（内链 + 关键词）
给每个文章页添加 2-3 个上下文内链
"""

import re
import os

# 定义分类和对应的文章页
CATEGORIES = {
    'japan': [
        'japan-travel.html',
        'tokyo-5days.html',
        'kansai-pass.html',
        'hokkaido-winter.html',
        'okinawa.html',
        'kyoto-temples.html',
        'osaka-food.html',
        'osaka-usj.html',
        'japan-budget-guide.html'
    ],
    'korea': [
        'korea-travel.html',
        'seoul-food.html',
        'busan-capsule.html',
        'jeju-island.html',
        'korea-budget.html'
    ],
    'taiwan': [
        'taiwan-travel.html',
        'hualien-taitung.html',
        'tainan-food.html',
        'kenting.html',
        'taipei-food.html',
        'jiufen.html'
    ],
    'southeast_asia': [
        'southeast-asia.html',
        'chiang-mai.html',
        'bangkok-3days.html',
        'bangkok-massage.html',
        'vietnam-danang.html'
    ],
    'other': [
        'esim-comparison.html'
    ]
}

# 已优化的页面（跳过）
OPTIMIZED = {
    'japan-budget-guide.html',
    'kyoto-temples.html',
    'seoul-food.html',
    'bangkok-3days.html'
}

def get_category(file_name):
    """获取文件所属分类"""
    for cat, files in CATEGORIES.items():
        if file_name in files:
            return cat
    return 'other'

def get_related_links(file_name, category, max_links=3):
    """获取同分类的其他文章链接"""
    if category not in CATEGORIES:
        return []
    
    related = [f for f in CATEGORIES[category] if f != file_name]
    return related[:max_links]

def add_internal_links(content, file_name, category):
    """给文章内容添加内链"""
    related = get_related_links(file_name, category, max_links=3)
    
    if not related:
        return content, False
    
    # 1. 在第一个 <h2> 后添加引导段落
    h2_pattern = r'(<h2>[^<]+</h2>)'
    h2_match = re.search(h2_pattern, content)
    
    if h2_match and len(related) >= 2:
        h2_tag = h2_match.group(1)
        link1 = related[0]
        link2 = related[1]
        
        # 提取页面标题作为锚文本
        link1_name = link1.replace('.html', '').replace('-', ' ')
        link2_name = link2.replace('.html', '').replace('-', ' ')
        
        intro_para = f'''
<p style="margin-bottom:18px;">這篇攻略幫你掌握實用技巧。如果你也計劃'''
        intro_para += f'''<span style="color:var(--tiffany-dark);font-weight:600;"><a href="{link1}" style="color:inherit;text-decoration:underline;">{link1_name}</a></span>'''
        intro_para += f'''或是研究<span style="color:var(--tiffany-dark);font-weight:600;"><a href="{link2}" style="color:inherit;text-decoration:underline;">{link2_name}</a></span>，我們也有完整攻略。</p>'''
        
        # 插入在 H2 后
        old_text = h2_tag + '\n\n'
        new_text = h2_tag + '\n' + intro_para + '\n\n'
        
        if old_text in content:
            content = content.replace(old_text, new_text, 1)
            print(f'  ✅ 添加 H2 后引导段落（2个内链）')
    
    # 2. 在第一个 <div class="day-card"> 前添加内链
    if len(related) >= 3:
        link3 = related[2]
        link3_name = link3.replace('.html', '').replace('-', ' ')
        
        day_card_pattern = r'(<div class="day-card">)'
        day_card_match = re.search(day_card_pattern, content)
        
        if day_card_match:
            old_day = day_card_match.group(1)
            new_day = f'''<p style="margin:16px 0;">延伸參考：<span style="color:var(--tiffany-dark);font-weight:600;"><a href="{link3}" style="color:inherit;text-decoration:underline;">{link3_name}</a></span></p>

<div class="day-card">'''
            
            if old_day in content:
                content = content.replace(old_day, new_day, 1)
                print(f'  ✅ 添加 day-card 前内链（1个内链）')
    
    return content, True

def optimize_file(file_path):
    """优化单个文件"""
    file_name = os.path.basename(file_path)
    
    # 跳过已优化的
    if file_name in OPTIMIZED:
        print(f'⏭️  跳过（已优化）: {file_name}')
        return False
    
    # 跳过非文章页
    if file_name.startswith('_') or file_name in ['index.html', 'about.html', 'contact.html', '404.html', 'privacy.html', 'terms.html', 'disclaimer.html', 'travel-tools.html']:
        print(f'⏭️  跳过（非文章页）: {file_name}')
        return False
    
    print(f'\n🔍 优化: {file_name}')
    
    # 读取文件
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f'  ❌ 读取失败: {e}')
        return False
    
    # 获取分类
    category = get_category(file_name)
    print(f'  分类: {category}')
    
    # 添加内链
    new_content, modified = add_internal_links(content, file_name, category)
    
    if not modified:
        print(f'  ⚠️  未修改（可能已优化或无法确定位置）')
        return False
    
    # 保存文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  ✅ 保存成功: {file_name}')
        return True
    except Exception as e:
        print(f'  ❌ 保存失败: {e}')
        return False

def main():
    """主函数"""
    print('=' * 60)
    print('批量优化 Travel-Lab SEO（内链 + 关键词）')
    print('=' * 60)
    
    # 获取所有 HTML 文件
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]
    
    print(f'\n找到 {len(html_files)} 个 HTML 文件')
    print(f'已优化（跳过）: {len(OPTIMIZED)} 个')
    print(f'待优化: {len(html_files) - len(OPTIMIZED)} 个\n')
    
    # 优化每个文件
    optimized_count = 0
    for html_file in sorted(html_files):
        if optimize_file(html_file):
            optimized_count += 1
    
    print('\n' + '=' * 60)
    print(f'优化完成！共优化 {optimized_count} 个页面')
    print('=' * 60)

if __name__ == '__main__':
    main()
