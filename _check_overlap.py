import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
path = os.path.join(BASE, 'tokyo-accommodation.html')

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# 找 three-col-wrapper 区域
idx = c.find('three-col-wrapper')
if idx == -1:
    print('❌ 未找到 three-col-wrapper')
else:
    print(f'=== three-col-wrapper 位置: {idx} ===')
    # 提取到 article-container 结束
    end = c.find('<!-- /article-container -->', idx)
    if end == -1:
        end = min(idx + 2000, len(c))
    else:
        end += 30
    snippet = c[idx:end]
    print(snippet[:1500])
    print(f'\n... (共 {len(snippet)} 字符)')

# 检查 col-left 和 sidebar-card
print('\n=== 检查 sidebar-card ===')
sidx = c.find('sidebar-card')
if sidx != -1:
    print(c[max(0,sidx-100):sidx+300])

# 检查 CSS 中相关样式
print('\n=== 检查 .three-col-wrapper 样式 ===')
css_path = os.path.join(BASE, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
for pattern in ['three-col-wrapper', 'col-left', 'col-center', 'col-right', 'sidebar-card']:
    m = css.find(pattern)
    if m != -1:
        print(f'\n--- {pattern} (pos {m}) ---')
        print(css[m:m+400])
