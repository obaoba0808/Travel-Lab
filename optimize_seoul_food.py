#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
优化 seoul-food.html 的关键词密度和内链结构
"""

import re

# 读取文件
with open('seoul-food.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在 H2 后添加引导段落 (包含内链)
old_h2 = '<h2>🦀 必吃美食 Top 5</h2>'
new_h2 = '''<h2>🦀 必吃美食 Top 5</h2>

<p style="margin-bottom:18px;">首爾美食多元又便宜，從街邊小吃到米其林推薦都有。如果規劃<span style="color:var(--tiffany-dark);font-weight:600;"><a href="busan-capsule.html" style="color:inherit;text-decoration:underline;">釜山膠囊列車行程</a></span>，或是想了解<span style="color:var(--tiffany-dark);font-weight:600;"><a href="korea-budget.html" style="color:inherit;text-decoration:underline;">韓國自由行預算</a></span>，我們也有完整攻略。</p>'''

if old_h2 in content:
    content = content.replace(old_h2, new_h2)
    print('✅ 成功添加 H2 引导段落')
else:
    print('❌ 找不到 H2 目标文本')

# 2. 在「醃蟹」段落添加内链
old_crab = '<p>生醃花蟹浸泡在特製醬油中，蟹黃拌飯一口入魂，韓國人稱它「偷飯賊」因為太下飯了！</p>'
new_crab = '<p>生醃花蟹浸泡在特製醬油中，蟹黃拌飯一口入魂，韓國人稱它「偷飯賊」因為太下飯了！如果搭配<span style="color:var(--tiffany-dark);font-weight:600;"><a href="jeju-island.html" style="color:inherit;text-decoration:underline;">濟州島自駕環島</a></span>，可以在濟州吃到最新鮮的醃蟹。</p>'

if old_crab in content:
    content = content.replace(old_crab, new_crab)
    print('✅ 成功添加醃蟹段落内链')
else:
    print('❌ 找不到醃蟹段落')

# 3. 修改「吃法」说明
old_eat = '<li><strong>吃法</strong>：蟹殼裡放白飯+蟹黃拌勻，是老饕吃法</li>'
new_eat = '<li><strong>吃法</strong>：蟹殼裡放白飯+蟹黃拌勻，是老饕吃法。參考我們的<span style="color:var(--tiffany-dark);font-weight:600;"><a href="seoul-food.html" style="color:inherit;text-decoration:underline;">首爾美食地圖</a></span>，可以找到更多隱藏版美食。</li>'

if old_eat in content:
    content = content.replace(old_eat, new_eat)
    print('✅ 成功添加吃法说明内链')
else:
    print('❌ 找不到吃法说明')

# 保存文件 (UTF-8 without BOM)
with open('seoul-food.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ seoul-food.html 已更新')
print('✅ 优化完成：添加了 3 个上下文内链')
