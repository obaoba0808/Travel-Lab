import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

with open(os.path.join(BASE, 'tokyo-5days.html'), 'r', encoding='utf-8') as f:
    tokyo = f.read()

# 提取 <body> 到 </body> 的内容（不含 body 标签本身）
body_start = tokyo.find('<body') + 1
body_start = tokyo.find('>', body_start) + 1
body_end = tokyo.find('</body>')
body_content = tokyo[body_start:body_end]

print('=== tokyo-5days.html body 内容长度 ===')
print(len(body_content))
print()
print('前 500 字符：')
print(repr(body_content[:500]))
print()
print('后 500 字符：')
print(repr(body_content[-500:]))
