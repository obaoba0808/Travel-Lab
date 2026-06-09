# -*- coding: utf-8 -*-
"""修復 footer 結構：旅遊工具欄應在 footer-inner 內"""
import glob, re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找錯誤模式：footer-inner 被過早關閉，旅遊工具欄在外面
    # 模式：兩個 </div> 後面直接接 <div class="footer-col"><h4>🔧 旅遊工具
    pattern = r'(</div>\s*</div>)\s*(<div class="footer-col">\s*<h4>🔧 旅遊工具</h4>.*?</div>)\s*(</div>\s*<!-- 社群連結 -->)'
    
    def replacer(m):
        # 把旅遊工具欄移到 footer-inner 內（去掉多餘的 </div></div>）
        return '\n' + m.group(2) + '\n</div>\n<!-- 社群連結 -->'
    
    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

files = sorted(glob.glob('*.html'))
done = []
for f in files:
    if fix_file(f):
        done.append(f)

print(f"已修復: {len(done)} 頁")
for d in done:
    print(f"  - {d}")
