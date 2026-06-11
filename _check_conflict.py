import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
css_path = os.path.join(BASE, 'style.css')
html_path = os.path.join(BASE, 'tokyo-accommodation.html')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 找所有 .three-col-wrapper 的定义
print('=== CSS 中所有 three-col-wrapper 定义 ===')
for m in re.finditer(r'\.three-col-wrapper[^{]*\{[^}]+\}', css):
    print(m.group())
    print()

# 检查 HTML 中的使用
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

count = html.count('three-col-wrapper')
print(f'HTML 中 three-col-wrapper 出现次数: {count}')

# 找每个出现位置
idx = 0
for i in range(count):
    idx = html.find('three-col-wrapper', idx)
    # 往前找上下文
    start = max(0, idx - 80)
    end = min(len(html), idx + 80)
    context = html[start:end].replace('\n', ' ')
    print(f'\n--- 出现 #{i+1} (pos {idx}) ---')
    print(context)
    idx += len('three-col-wrapper')
