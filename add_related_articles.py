#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为所有文章页添加「相关文章」区块 (P1 #4 内链结构优化)
"""

import os
import re

html_dir = '.'

# 定义相关文章映射 (根据地区和主题)
related_articles = {
    'kyoto-temples.html': [
        ('tokyo-5days.html', '东京5天4夜行程攻略'),
        ('kansai-pass.html', '关西交通票券指南'),
        ('japan-budget-guide.html', '日本旅游预算指南')
    ],
    'japan-budget-guide.html': [
        ('tokyo-5days.html', '东京5天4夜行程攻略'),
        ('kansai-pass.html', '关西交通票券指南'),
        ('osaka-usj.html', '大阪环球影城攻略')
    ],
    'tokyo-5days.html': [
        ('japan-budget-guide.html', '日本旅游预算指南'),
        ('kansai-pass.html', '关西交通票券指南'),
        ('okinawa.html', '冲绳自驾攻略')
    ],
    'kansai-pass.html': [
        ('kyoto-temples.html', '京都寺庙散步地图'),
        ('osaka-food.html', '大阪美食攻略'),
        ('japan-budget-guide.html', '日本旅游预算指南')
    ],
    'osaka-food.html': [
        ('kansai-pass.html', '关西交通票券指南'),
        ('osaka-usj.html', '大阪环球影城攻略'),
        ('japan-budget-guide.html', '日本旅游预算指南')
    ],
    'osaka-usj.html': [
        ('osaka-food.html', '大阪美食攻略'),
        ('kansai-pass.html', '关西交通票券指南'),
        ('japan-budget-guide.html', '日本旅游预算指南')
    ],
    'seoul-food.html': [
        ('busan-capsule.html', '釜山胶囊列车预约'),
        ('jeju-island.html', '济州岛自驾环岛'),
        ('korea-budget.html', '韩国自由行预算')
    ],
    'busan-capsule.html': [
        ('seoul-food.html', '首尔必吃美食攻略'),
        ('jeju-island.html', '济州岛自驾环岛'),
        ('korea-budget.html', '韩国自由行预算')
    ],
    'jeju-island.html': [
        ('seoul-food.html', '首尔必吃美食攻略'),
        ('busan-capsule.html', '釜山胶囊列车预约'),
        ('korea-budget.html', '韩国自由行预算')
    ],
    'korea-budget.html': [
        ('seoul-food.html', '首尔必吃美食攻略'),
        ('busan-capsule.html', '釜山胶囊列车预约'),
        ('jeju-island.html', '济州岛自驾环岛')
    ],
    'hualien-taitung.html': [
        ('tainan-food.html', '台南美食牛肉汤'),
        ('kenting.html', '垦丁海景夜市攻略'),
        ('taipei-food.html', '台北美食地图')
    ],
    'tainan-food.html': [
        ('hualien-taitung.html', '花东三天两夜'),
        ('kenting.html', '垦丁海景夜市攻略'),
        ('taipei-food.html', '台北美食地图')
    ],
    'kenting.html': [
        ('hualien-taitung.html', '花东三天两夜'),
        ('tainan-food.html', '台南美食牛肉汤'),
        ('taipei-food.html', '台北美食地图')
    ],
    'taipei-food.html': [
        ('hualien-taitung.html', '花东三天两夜'),
        ('tainan-food.html', '台南美食牛肉汤'),
        ('kenting.html', '垦丁海景夜市攻略')
    ],
    'chiang-mai.html': [
        ('bangkok-3days.html', '曼谷吃货攻略'),
        ('bangkok-massage.html', '曼谷按摩推荐'),
        ('vietnam-danang.html', '越南岘港攻略')
    ],
    'bangkok-3days.html': [
        ('chiang-mai.html', '清迈数位游牧指南'),
        ('bangkok-massage.html', '曼谷按摩推荐'),
        ('vietnam-danang.html', '越南岘港攻略')
    ],
    'bangkok-massage.html': [
        ('bangkok-3days.html', '曼谷吃货攻略'),
        ('chiang-mai.html', '清迈数位游牧指南'),
        ('vietnam-danang.html', '越南岘港攻略')
    ],
    'vietnam-danang.html': [
        ('chiang-mai.html', '清迈数位游牧指南'),
        ('bangkok-3days.html', '曼谷吃货攻略'),
        ('bangkok-massage.html', '曼谷按摩推荐')
    ]
}

print("=== 添加相关文章区块 (P1 #4) ===\n")

fixed_count = 0

for filename, related in related_articles.items():
    filepath = os.path.join(html_dir, filename)
    
    if not os.path.exists(filepath):
        print(f'[WARN] File not found: {filename}')
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有相关文章区块
    if '延伸阅读' in content or '相关文章' in content or 'related-articles' in content:
        print(f'[SKIP] {filename}: Already has related articles')
        continue
    
    # 生成相关文章 HTML
    related_html = '\n<!-- RELATED ARTICLES -->\n<div class="related-articles">\n  <h2 class="section-title">📖 延伸阅读</h2>\n  <ul class="related-list">\n'
    
    for link, title in related:
        related_html += f'    <li><a href="{link}">{title}</a></li>\n'
    
    related_html += '  </ul>\n</div>\n'
    
    # 在 </article> 或 </main> 前插入
    if '</article>' in content:
        new_content = content.replace('</article>', related_html + '</article>', 1)
    elif '</main>' in content:
        new_content = content.replace('</main>', related_html + '</main>', 1)
    else:
        # 在最后一个 </div> 前插入 (fallback)
        last_div = content.rfind('</div>')
        if last_div != -1:
            new_content = content[:last_div] + related_html + content[last_div:]
        else:
            print(f'[ERROR] {filename}: Cannot find insertion point')
            continue
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    fixed_count += 1
    print(f'[OK] {filename}: Added related articles')

print(f"\n=== 完成 ===")
print(f"总计添加: {fixed_count} 个页面")
print("\n[WARN] 需要手动添加 CSS 样式:")
print("  在 style.css 中添加 .related-articles 和 .related-list 样式")
