#!/usr/bin/env python3
"""Re-apply UI changes to japan-travel.html"""
import re

html_path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\japan-travel.html'

with open(html_path, 'rb') as f:
    raw = f.read()
norm = raw.replace(b'\r\r\n', b'\n').replace(b'\r\n', b'\n')
text = norm.decode('utf-8', errors='replace')

# Find the full category-hero block from its opening to its closing
# Strategy: locate <div class="category-hero"> and then search forward to find
# the matching </div> before section-divider

start = text.find('<div class="category-hero">')
if start == -1:
    start = text.find('class="category-hero"')
print('category-hero start:', start)

# Find where category-hero ends (the </div> just before section-divider)
section_divider_pos = text.find('section-divider')
print('section-divider pos:', section_divider_pos)

# Search backwards from section-divider for the </div> of category-hero
# We want to find the last </div> before <div class="section-divider">
search_area = text[start:section_divider_pos]
print('search area length:', len(search_area))
# Find the last occurrence of </div>
last_div = search_area.rfind('</div>')
print('last </div> in search area at offset:', last_div)

# End of category-hero block (exclusive - we want to replace up to and including the </div>)
end = start + last_div + len('</div>')
print('block to replace: start=%d, end=%d, len=%d' % (start, end, end-start))

old_block = text[start:end]
print('Old block found:', len(old_block), 'chars')
print('Has overlay:', 'class="overlay"' in old_block)
print('Has category-hero close:', '</div>' in old_block)

# New block
new_block = '''<div class="category-hero">
    <img src="images/japan-hero.webp" class="hero-img-full" alt="日本自由行" width="1536" height="1024">
  </div>

  <!-- HERO TITLE BLOCK - Magazine style, below image -->
  <div class="hero-title-block">
    <div class="hero-title-inner">
      <span class="hero-region-tag">&#x1F1EF;&#x1F1F5; 日本自由行</span>
      <h1 class="hero-main-title">日本自由行全攻略</h1>
      <p class="hero-sub-title">東京、京阪神、北海道&hellip;&hellip; 帶你用最划算的方式玩透日本，交通票券與必吃美食總整理。</p>
      <div class="hero-meta">
        <span>&#x2708; 5大目的地</span>
        <span class="hero-meta-dot">&bull;</span>
        <span>&#x1F4DD; 18篇攻略文章</span>
        <span class="hero-meta-dot">&bull;</span>
        <span>&#x1F4B0; 機票+住宿省錢密技</span>
      </div>
    </div>
  </div>

'''

if old_block in text:
    new_text = text.replace(old_block, new_block, 1)
    print('Replacement done!')
else:
    print('Old block NOT FOUND - showing it:')
    # Show the old block as bytes
    print(repr(old_block[:300]))

result_bytes = new_text.replace('\n', '\r\n').encode('utf-8')
with open(html_path, 'wb') as f:
    f.write(result_bytes)
print('Written.')

# Quick verify
with open(html_path, 'rb') as f:
    chk = f.read()
print('hero-title-block in result:', b'hero-title-block' in chk)
print('hero-main-title in result:', b'hero-main-title' in chk)
print('overlay in result:', b'class="overlay"' in chk)