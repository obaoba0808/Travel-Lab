import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

def fix_extra_divs(html):
    """栈式解析，移除多余的 </div> 并返回修复后的 HTML"""
    # 用正则提取所有 div 开标签和闭标签（按出现顺序）
    pattern = re.compile(r'<(/?)div[\s>]')
    # 但这样不够精确，改用逐字符解析 div 标签
    # 简化：先把所有标签提出来，再栈式校验
    tags = re.findall(r'</?div[\s>][^>]*>', html, re.I)
    
    stack = []  # 存储 (tag_text, position) 
    extra_positions = []
    
    for m in re.finditer(r'</?div[\s>][^>]*>', html, re.I):
        tag = m.group()
        if tag.startswith('</div'):
            if stack:
                stack.pop()
            else:
                # 多余闭标签
                extra_positions.append(m.start())
        else:
            stack.append((tag, m.start()))
    
    # 从后往前移除，避免位置偏移
    html_fixed = html
    for pos in sorted(extra_positions, reverse=True):
        # 找到这个 </div> 的完整起止位置
        end = html_fixed.find('>', pos)
        if end != -1:
            html_fixed = html_fixed[:pos] + html_fixed[end+1:]
    
    return html_fixed, len(extra_positions)

for fname in ['thailand-sim.html', 'vietnam-hochiminh.html']:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    o = c.count('<div')
    cl = c.count('</div>')
    print(f'=== {fname}（修复前）===')
    print(f'  opens={o}, closes={cl}, diff={o-cl}')
    
    fixed, n_removed = fix_extra_divs(c)
    
    o2 = fixed.count('<div')
    cl2 = fixed.count('</div>')
    print(f'  移除了 {n_removed} 个多余 </div>')
    print(f'  修复后: opens={o2}, closes={cl2}, diff={o2-cl2}')
    
    if o2 == cl2:
        print('  ✅ 平衡!')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f'  已写入 {fname}')
    else:
        print(f'  ❌ 仍不平衡 (diff={o2-cl2})')
    print()
