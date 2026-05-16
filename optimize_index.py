#!/usr/bin/env python3
"""Optimize index.html based on Klook/Vialife reference sites"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add search box after site-branding
old_branding = '''<div class="site-branding">
  <h1>均在路上 <span>Travel Lab</span></h1>
  <p>用最少预算，走最多地方的实战旅游攻略</p>
</div>'''

new_branding = '''<div class="site-branding">
  <h1>均在路上 <span>Travel Lab</span></h1>
  <p>用最少预算，走最多地方的实战旅游攻略</p>
</div>

<!-- SEARCH BOX -->
<div class="search-box-wrap">
  <form class="search-form" action="https://www.google.com/search" method="get" target="_blank">
    <input type="hidden" name="as_sitesearch" value="golightly.fun">
    <div class="search-input-wrap">
      <span class="search-icon">&#128269;</span>
      <input type="text" name="q" placeholder="搜索攻略、目的地、交通方式..." class="search-input" required>
      <button type="submit" class="search-btn">搜索</button>
    </div>
  </form>
</div>'''

html = html.replace(old_branding, new_branding)

# 2. Add reading time + last updated + budget to article cards
# Pattern: find each post-item and add metadata
def upgrade_post_item(m):
    block = m.group(0)
    # Skip if already upgraded
    if 'reading-time' in block:
        return block
    
    # Extract date
    date_m = re.search(r'class="date">(\d{4}-\d{2}-\d{2})', block)
    date_str = date_m.group(1) if date_m else '2026-05-13'
    
    # Estimate reading time (500 words/min)
    excerpt_m = re.search(r'class="post-excerpt">(.*?)</p>', block, re.DOTALL)
    excerpt = excerpt_m.group(1) if excerpt_m else ''
    word_count = len(re.sub(r'<[^>]+>', '', excerpt))
    reading_min = max(3, word_count // 200 + 2)
    
    # Add metadata after post-meta
    old_meta = r'<div class="post-meta"><span class="author">Travel Lab</span><span class="date">\d{4}-\d{2}-\d{2}</span></div>'
    def replace_meta(mm):
        return mm.group(0) + f'\n        <div class="post-meta-extra"><span class="reading-time">&#128336; 约{reading_min}分钟</span><span class="last-updated">&#128197; 最后更新：{date_str}</span></div>'
    
    block_new = re.sub(old_meta, replace_meta, block)
    return block_new

html = re.sub(r'<article class="post-item">.*?</article>', upgrade_post_item, html, flags=re.DOTALL)

# 3. Upgrade sidebar "关于我们" section
old_about = '''<div class="widget">
      <div class="widget-title">💌 關於我們</div>
      <p style="font-size:13px;color:var(--text-gray);line-height:1.8;">均在路上 Travel Lab 是一個實戰旅遊攻略網站，我們相信旅行不必花大錢。每篇攻略都經過實地走訪驗證，從交通教學到美食推薦，幫你用最少預算走最多地方。</p>
    </div>'''

new_about = '''<div class="widget">
      <div class="widget-title">💌 關於 Travel Lab</div>
      <p style="font-size:13px;color:var(--text-gray);line-height:1.8;margin-bottom:12px;">均在路上 Travel Lab 是一個實戰旅遊攻略網站，我們相信旅行不必花大錢。</p>
      <div style="background:var(--tiffany-light);border-radius:8px;padding:12px;font-size:12px;line-height:1.8;">
        <div style="margin-bottom:6px;">✅ 每篇攻略實地驗證</div>
        <div style="margin-bottom:6px;">✅ 具體價格與時間資訊</div>
        <div style="margin-bottom:6px;">✅ 定期更新確保準確性</div>
        <div>✅ 附路線圖與預算表</div>
      </div>
    </div>'''

html = html.replace(old_about, new_about)

with open('index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)

print('index.html optimized')
print('- Search box added')
print('- Reading time + last updated added to article cards')
print('- Sidebar "About" section upgraded')
