#!/usr/bin/env python3
"""
Replace category-hero overlay with full-bleed image + title below pattern
for about.html and travel-tools.html
"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# ── 1. Update about.html ──
with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_hero = """<div class="category-hero" style="background-image: url('images/about-hero.webp');">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>關於均在路上 Travel Lab</h1>
    <p>每篇攻略，都是實地走訪的驗證結果。</p>
  </div>
</div>"""

new_hero = """<div class="hero-full-bleed">
  <img src="images/about-hero.webp" alt="關於均在路上 Travel Lab" class="hero-full-img">
</div>
<div class="hero-title-block">
  <div class="hero-title-inner">
    <span class="hero-region-tag">About Us</span>
    <h1 class="hero-main-title">關於均在路上 Travel Lab</h1>
    <p class="hero-sub-title">每篇攻略，都是實地走訪的驗證結果。</p>
  </div>
</div>"""

html = html.replace(old_hero, new_hero)
with open('about.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('about.html: hero replaced')

# ── 2. Update travel-tools.html ──
with open('travel-tools.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_hero2 = """<div class="category-hero" style="background-image: url('images/travel-tools-hero.webp');">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>旅遊省錢工具包</h1>
    <p>機票、住宿、門票、網路，出國必備懶人包。</p>
  </div>
</div>"""

new_hero2 = """<div class="hero-full-bleed">
  <img src="images/travel-tools-hero.webp" alt="旅遊省錢工具包" class="hero-full-img">
</div>
<div class="hero-title-block">
  <div class="hero-title-inner">
    <span class="hero-region-tag">Travel Tools</span>
    <h1 class="hero-main-title">旅遊省錢工具包</h1>
    <p class="hero-sub-title">機票、住宿、門票、網路，出國必備懶人包。</p>
  </div>
</div>"""

html = html.replace(old_hero2, new_hero2)
with open('travel-tools.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html)
print('travel-tools.html: hero replaced')
