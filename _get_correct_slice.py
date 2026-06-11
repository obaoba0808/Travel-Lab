import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# 读取 tokyo-5days.html 的正确片段（form close 到 FOOTER）
with open(os.path.join(BASE, 'tokyo-5days.html'), 'r', encoding='utf-8') as f:
    tokyo = f.read()

fc_t = tokyo.rfind('</form>')
footer_t = tokyo.find('<!-- FOOTER -->')
correct_slice = tokyo[fc_t:footer_t]

print('=== tokyo-5days.html 正确片段（前500字符）===')
print(repr(correct_slice[:500]))
print()
print(f'正确片段长度: {len(correct_slice)}')
print(f'正确片段 opens: {correct_slice.count("<div")}')
print(f'正确片段 closes: {correct_slice.count("</div>")}')
