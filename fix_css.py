#!/usr/bin/env python3
"""Update style.css for hero title block"""
import re

css_path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\style.css'

with open(css_path, 'rb') as f:
    raw = f.read()
norm = raw.replace(b'\r\r\n', b'\n').replace(b'\r\n', b'\n')
css = norm.decode('utf-8', errors='replace')

old_css = '''/* ========== CATEGORY HERO ========== */
.category-hero { position:relative; overflow:hidden; }
.category-hero img { width:100%; height:auto; object-fit:contain; display:block; }
.category-hero .overlay { position:absolute; inset:0; display:flex; align-items:flex-end; padding:40px; color:#fff; text-shadow:0 1px 4px rgba(0,0,0,0.6); }
.category-hero .overlay h2 { color:#fff; font-family:'Noto Serif TC',serif; font-size:32px; font-weight:700; }
.category-hero .overlay p { color:rgba(255,255,255,0.85); font-size:15px; margin-top:6px; }'''

new_css = '''/* ========== CATEGORY HERO (full-bleed image) ========== */
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

if old_css in css:
    css = css.replace(old_css, new_css)
    print('CSS replaced OK')
else:
    # Find it and print what we have
    idx = css.find('CATEGORY HERO')
    snippet = css[idx:idx+500]
    print('NOT FOUND. Current:')
    print(repr(snippet[:500]))

css_bytes = css.replace('\n', '\r\n').encode('utf-8')
with open(css_path, 'wb') as f:
    f.write(css_bytes)

# Verify
with open(css_path, 'rb') as f:
    chk = f.read()
print('hero-title-block in CSS:', b'hero-title-block' in chk)
print('hero-main-title in CSS:', b'hero-main-title' in chk)
print('overlay display:none in CSS:', b'.overlay { display:none; }' in chk)