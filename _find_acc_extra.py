import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
path = os.path.join(BASE, 'tokyo-accommodation.html')

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# 找 article-container 区域
ac_start = c.find('class="article-container"')
ac_end = c.find('<!-- /article-container -->') + len('<!-- /article-container -->')
ac_content = c[ac_start:ac_end]

# 栈式解析找多余 </div>
pattern = re.compile(r'<(/?)div\b[^>]*>', re.I)
stack = []
extra_pos = []

for m in pattern.finditer(ac_content):
    is_close = m.group(1) == '/'
    if not is_close:
        stack.append(m.start())
    else:
        if stack:
            stack.pop()
        else:
            extra_pos.append(m.start())

print(f'article-container 内部:')
print(f'  多余 </div> 数量: {len(extra_pos)}')
for pos in extra_pos:
    # 计算在原文中的绝对位置
    abs_pos = ac_start + pos
    lines = c[:abs_pos].count('\n')
    line_content = c[c.rfind('\n', 0, abs_pos)+1:c.find('\n', abs_pos)].strip()[:120]
    print(f'  绝对位置: {abs_pos}, 行号: {lines+1}')
    print(f'    内容: {line_content}')
    print()
