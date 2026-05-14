#!/usr/bin/env python
"""Create 404.html for Travel Lab"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_match = re.search(r'(.+?</head>)', content, re.DOTALL)
footer_match = re.search(r'(<footer class=.site-footer.>.+?</footer>)', content, re.DOTALL)

head = head_match.group(1) if head_match else ''
footer = footer_match.group(1) if footer_match else ''

# Update title in head
head = head.replace('均在路上 Travel Lab｜用最少預算走最多地方的實戰旅遊攻略', '頁面未找到｜均在路上 Travel Lab')
# Remove canonical for 404
head = re.sub(r'<link rel="canonical"[^>]+>', '', head)

# Read nav from index
nav_section = ''
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()
nav_match = re.search(r'(<div class="site-topbar">.+?</div>\s*</div>)', idx, re.DOTALL)
if nav_match:
    nav_section = nav_match.group(1)

html = f'''<!DOCTYPE html>
<html lang="zh-Hant-TW">
{head}
<body>
{nav_section}
<div style="max-width:800px;margin:80px auto;padding:40px 20px;text-align:center;">
  <h1 style="font-size:64px;color:#0ABAB5;margin-bottom:16px;">404</h1>
  <h2 style="font-size:24px;margin-bottom:16px;">哎呀，這個頁面不在地圖上 🗺️</h2>
  <p style="color:#777;margin-bottom:32px;">你尋找的頁面可能已經移動或不存在了。</p>
  <a href="index.html" style="display:inline-block;background:#0ABAB5;color:#fff;padding:12px 32px;border-radius:8px;font-weight:500;">回到首頁</a>
</div>
{footer}
</body>
</html>'''

with open('404.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Created 404.html')
