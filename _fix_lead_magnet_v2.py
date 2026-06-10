#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修復 tokyo-5days.html：將 Lead Magnet 從 footer 內部移到 article-container 內部
正確位置：FAQ 之後、Klook 推廣之前
"""

import re
import sys

filepath = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\tokyo-5days.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 找到 Lead Magnet 區塊（從 <!-- PDF Lead Magnet --> 到 </footer> 前的 </div>）
# 使用非貪婪匹配找到 Lead Magnet 整個 div
lm_pattern = r'(<!-- PDF Lead Magnet -->\n<div style="background:linear-gradient\(135deg,#667eea 0%,#764ba2 100%\);border-radius:16px;padding:40px 24px;margin:48px 0;text-align:center;color:#fff">.*?</div>\n)(?=\s*</footer>)'
lm_match = re.search(lm_pattern, content, re.DOTALL)

if not lm_match:
    print("ERROR: 找不到 Lead Magnet 區塊")
    sys.exit(1)

lead_magnet_block = lm_match.group(1)
print(f"找到 Lead Magnet 區塊（長度: {len(lead_magnet_block)} 字元）")

# 2. 從 footer 中移除 Lead Magnet
content = content.replace(lead_magnet_block, '')

# 3. 找到插入位置：</section> (FAQ 結尾) 之後，Klook 推廣之前
#    正確位置是在 </section> 後、<!-- KLOOK 動態橫幅：--> 之前
insert_marker = '</section>\n<!-- KLOOK 動態橫幅： -->'

if insert_marker not in content:
    print("ERROR: 找不到插入標記")
    sys.exit(1)

# 插入 Lead Magnet
content = content.replace(insert_marker, '</section>\n' + lead_magnet_block + '\n<!-- KLOOK 動態橫幅： -->')

# 4. 寫回檔案
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Lead Magnet 已移到正確位置（FAQ 之後、Klook 推廣之前）")
