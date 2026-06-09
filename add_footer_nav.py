# -*- coding: utf-8 -*-
"""在 footer-bottom 區域加入橫向導航連結列（關於均在路上/聯絡我們/隱私權政策/使用條款/免責聲明）"""
import glob, re, os

NAV_HTML = '''<div class="footer-nav-row">
  <a href="about.html">關於均在路上</a>
  <span class="footer-nav-sep">·</span>
  <a href="contact.html">聯絡我們</a>
  <span class="footer-nav-sep">·</span>
  <a href="privacy.html">隱私權政策</a>
  <span class="footer-nav-sep">·</span>
  <a href="terms.html">使用條款</a>
  <span class="footer-nav-sep">·</span>
  <a href="disclaimer.html">免責聲明</a>
</div>'''

CSS_RULE = '''
/* Footer Nav Row - 橫向連結列 */
.footer-nav-row {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px 16px;
  padding: 14px 0;
  border-top: 1px solid rgba(255,255,255,0.1);
  margin-top: 16px;
}
.footer-nav-row a {
  color: rgba(255,255,255,0.75);
  text-decoration: none;
  font-size: 13px;
  transition: color 0.2s;
}
.footer-nav-row a:hover {
  color: #4ecdc4;
}
.footer-nav-sep {
  color: rgba(255,255,255,0.3);
  font-size: 12px;
}'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 跳過沒有 footer 的檔案
    if 'site-footer' not in content and 'class="footer"' not in content and 'footer-bottom' not in content:
        return False
    
    # 如果已經有 footer-nav-row 就跳過
    if 'footer-nav-row' in content:
        return False
    
    # 找到 footer-bottom 或版權行，在它前面插入
    patterns = [
        (r'(<div class="footer-bottom">)', r'\1' + NAV_HTML),
        (r'(© \d+ 均在路上)', NAV_HTML + r'\1'),
    ]
    
    modified = False
    for pattern, replacement in patterns:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modified = True
            break
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 處理所有 HTML 檔案
files = sorted(glob.glob('*.html'))
done = []
for f in files:
    if process_file(f):
        done.append(f)

print(f"已處理 {len(done)} 個檔案:")
for d in done:
    print(f"  + {d}")

# 加入 CSS 到 style.css
css_path = 'style.css'
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    if 'footer-nav-row' not in css:
        # 加在 /* Footer */ 區塊之前或檔案末尾
        if '/* Footer */' in css:
            css = css.replace('/* Footer */', CSS_RULE + '\n\n/* Footer */')
        else:
            css += '\n' + CSS_RULE
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css)
        print(f"\n已更新 style.css (加入 .footer-nav-row 樣式)")
