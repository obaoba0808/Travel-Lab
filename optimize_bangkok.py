#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
优化 bangkok-3days.html 的关键词密度和内链结构
"""

import re

# 读取文件
with open('bangkok-3days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在 H2「曼谷交通」后添加引导段落 (包含内链)
old_traffic = '<h2>🚇 曼谷交通：BTS + MRT 最省心</h2>'
new_traffic = '''<h2>🚇 曼谷交通：BTS + MRT 最省心</h2>

<p style="margin-bottom:18px;">曼谷塞车世界有名，善用空铁和地铁是最聪明的选择。如果规划<span style="color:var(--tiffany-dark);font-weight:600;"><a href="chiang-mai.html" style="color:inherit;text-decoration:underline;">清邁數位遊牧行程</a></span>，或是想了解<span style="color:var(--tiffany-dark);font-weight:600;"><a href="bangkok-massage.html" style="color:inherit;text-decoration:underline;">曼谷按摩推薦</a></span>，我們也有完整攻略。</p>'''

if old_traffic in content:
    content = content.replace(old_traffic, new_traffic)
    print('✅ 成功添加交通段落引导内链')
else:
    print('❌ 找不到交通段落 H2')

# 2. 在 Day 1 段落添加内链
old_day1 = '<div class="day-card">\n    <span class="day-tag">Day 1</span>\n    <h3>老城區：大皇宮 → 臥佛寺 → 唐人街美食</h3>'
new_day1 = '''<div class="day-card">
    <span class="day-tag">Day 1</span>
    <h3>老城區：大皇宮 → 臥佛寺 → 唐人街美食</h3>
    
    <p style="margin-bottom:12px;">第一天建議走老城區精華路線，如果時間充裕，也可以安排<span style="color:var(--tiffany-dark);font-weight:600;"><a href="vietnam-danang.html" style="color:inherit;text-decoration:underline;">越南峴港海灘行程</a></span>作為延伸旅行。</p>'''

if old_day1 in content:
    content = content.replace(old_day1, new_day1)
    print('✅ 成功添加 Day 1 内链')
else:
    print('❌ 找不到 Day 1 段落')

# 3. 在「必吃10大美食」列表前添加引导
old_food = '<h2>🍜 曼谷必吃10大美食</h2>'
new_food = '''<h2>🍜 曼谷必吃10大美食</h2>

<p style="margin-bottom:18px;">曼谷美食便宜又多样，从路边摊到米其林推荐都有。如果比较<span style="color:var(--tiffany-dark);font-weight:600;"><a href="taipei-food.html" style="color:inherit;text-decoration:underline;">台北美食地圖</a></span>和曼谷美食，你會發現兩者的夜市文化非常相似。</p>'''

if old_food in content:
    content = content.replace(old_food, new_food)
    print('✅ 成功添加美食段落引导内链')
else:
    print('❌ 找不到美食段落 H2')

# 保存文件 (UTF-8 without BOM)
with open('bangkok-3days.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ bangkok-3days.html 已更新')
print('✅ 优化完成：添加了 3 个上下文内链')
