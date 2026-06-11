import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

with open(os.path.join(BASE, 'tokyo-5days.html'), 'r', encoding='utf-8') as f:
    c = f.read()

start = c.find('<div class="related-posts"')
end = c.find('<!-- FOOTER -->')
print('=== tokyo-5days.html 正确模板（related-posts 到 three-col-wrapper 关闭）===')
print(repr(c[start:end]))
print()
print('长度:', len(c[start:end]))
