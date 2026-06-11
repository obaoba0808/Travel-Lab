import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
fname = 'tokyo-5days.html'
with open(os.path.join(BASE, fname), 'r', encoding='utf-8') as f:
    c = f.read()

# 找到 form 开始和结束位置
fs = c.find('<form action="https://formspree.io/f/xredjjgb"')
fc = c.rfind('</form>')
footer = c.find('<!-- FOOTER -->')

print(f'form start: {fs}')
print(f'form close: {fc}')
print(f'footer: {footer}')
print()

# 追踪从 form start 到 footer 的 div 深度
depth = 0
events = []
for m in re.finditer(r'<div|</div', c):
    pos = m.start()
    if pos < fs:
        # 在 form 之前，追踪深度
        if m.group() == '<div':
            depth += 1
        else:
            depth -= 1
        continue
    if pos > footer + 500:
        break
    tag = m.group()
    if tag == '<div':
        depth += 1
    else:
        depth -= 1
    offset = pos - fc
    events.append((offset, tag, depth))

print('Div events from form start to footer+500:')
for offset, tag, d in events:
    marker = ''
    if offset == 0:
        marker = '  <-- FORM CLOSE'
    if offset > 0 and offset < 50:
        marker = f'  (offset +{offset})'
    print(f'  offset={offset:+d}: {tag[:40]!r}  depth={d}{marker}')
