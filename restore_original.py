#!/usr/bin/env python3
"""Restore japan-travel.html and style.css to original (overlay version)"""
import os

os.chdir(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab')

# === Restore japan-travel.html ===
html_path = 'japan-travel.html'
with open(html_path, 'rb') as f:
    raw = f.read()
norm = raw.replace(b'\r\r\n', b'\n').replace(b'\r\n', b'\n')
text = norm.decode('utf-8', errors='replace')

# Check current state - if has hero-title-block, replace back
if 'hero-title-block' in text:
    # Find and replace back to original overlay
    old_block = '''<div class="category-hero">
    <img src="images/japan-hero.webp" class="hero-img-full" alt="日本自由行" width="1536" height="1024">
  </div>

  <!-- HERO TITLE BLOCK - Magazine style, below image -->
  <div class="hero-title-block">
    <div class="hero-title-inner">
      <span class="hero-region-tag">&#x1F1EF;&#x1F1F5; 日本自由行</span>
      <h1 class="hero-main-title">日本自由行全攻略</h1>
      <p class="hero-sub-title">東京、京阪神 北海道 帶你用最划算的方式玩透日本，交通票券與必吃美食總整理。</p>
      <div class="hero-meta">
        <span> 5大目的地</span>
        <span class="hero-meta-dot"></span>
        <span> 18篇攻略文章</span>
        <span class="hero-meta-dot"></span>
        <span> 機票+住宿省錢密技</span>
      </div>
    </div>
  </div>'''

    new_block = '''<div class="category-hero">
  <img src="images/japan-hero.webp" style="width:100%;height:auto;display:block;" alt="日本自由行" width="1536" height="1024">
  <div class="overlay">
    <h1>日本自由行全攻略</h1>
    <p>東京、京阪神 北海道 帶你用最划算的方式玩透日本，交通票券與必吃美食總整理。</p>
  </div>
</div>'''
    
    text = text.replace(old_block, new_block)
    result = text.replace('\n', '\r\n').encode('utf-8')
    with open(html_path, 'wb') as f:
        f.write(result)
    print('HTML restored to overlay version')
else:
    print('hero-title-block not found in HTML')

# Verify the restore
with open(html_path, 'rb') as f:
    chk = f.read()
print('overlay in HTML:', b'class="overlay"' in chk)
print('hero-title-block removed:', b'hero-title-block' not in chk)

# === Restore style.css ===
css_path = 'style.css'
with open(css_path, 'rb') as f:
    raw = f.read()
norm = raw.replace(b'\r\r\n', b'\n').replace(b'\r\n', b'\n')
css = norm.decode('utf-8', errors='replace')

# If has hero-title-block styles, replace back to original
if 'hero-title-block {' in css:
    new_css = '''/* ========== CATEGORY HERO ========== */
.category-hero { position:relative; overflow:hidden; }
.category-hero img { width:100%; height:auto; object-fit:contain; display:block; }
.category-hero .overlay { position:absolute; inset:0; display:flex; align-items:flex-end; padding:40px; color:#fff; text-shadow:0 1px 4px rgba(0,0,0,0.6); }
.category-hero .overlay h2 { color:#fff; font-family:'Noto Serif TC',serif; font-size:32px; font-weight:700; }
.category-hero .overlay p { color:rgba(255,255,255,0.85); font-size:15px; margin-top:6px; }'''
    
    old_css_part = '''/* ========== CATEGORY HERO (full-bleed image) ========== */
.category-hero { position:relative; overflow:hidden; }
.category-hero img { width:100%; height:auto; display:block; }
.category-hero .overlay { display:none; }

/* ========== HERO TITLE BLOCK (magazine style, below image) ========== */
.hero-title-block {
  background: linear-gradient(180deg, #f9fcfc 0%, #ffffff 100%);
  border-bottom: 1px solid var(--border);
  padding: 50px 20px 45px;
}
.hero-title-inner {
  max-width: 820px;
  margin: 0 auto;
  text-align: center;
}
.hero-region-tag {
  display: inline-block;
  background: var(--tiffany);
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 14px;
  border-radius: 20px;
  letter-spacing: 0.5px;
  margin-bottom: 16px;
  text-transform: uppercase;
}
.hero-main-title {
  font-family: 'Noto Serif TC', serif;
  font-size: 38px;
  font-weight: 700;
  color: #1a1a2e;
  line-height: 1.35;
  margin-bottom: 14px;
  letter-spacing: -0.5px;
}
.hero-sub-title {
  font-size: 16px;
  color: var(--text-gray);
  line-height: 1.9;
  max-width: 640px;
  margin: 0 auto 18px;
}
.hero-meta {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--text-gray);
  flex-wrap: wrap;
}
.hero-meta-dot { color: var(--tiffany); font-weight: bold; }'''
    
    css = css.replace(old_css_part, new_css)
    result_css = css.replace('\n', '\r\n').encode('utf-8')
    with open(css_path, 'wb') as f:
        f.write(result_css)
    print('CSS restored to original')
else:
    print('hero-title-block not found in CSS')

# Verify
with open(css_path, 'rb') as f:
    chk = f.read()
print('.overlay styles in CSS:', b'.category-hero .overlay {' in chk)
print('hero-title-block removed from CSS:', b'hero-title-block {' not in chk)