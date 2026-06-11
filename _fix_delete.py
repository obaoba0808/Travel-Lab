import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

def fix_html_divs(html):
    """
    栈式解析，真正删除多余的 </div> 标签。
    返回 (修复后HTML, 删除数量)
    """
    pattern = re.compile(r'<(/?)div\b[^>]*>', re.I)
    
    tags = list(pattern.finditer(html))
    
    stack = []  # 存储开标签的 position
    remove_positions = set()
    
    for m in tags:
        is_close = m.group(1) == '/'
        if not is_close:
            # 开标签，入栈
            stack.append(m.start())
        else:
            # 闭标签
            if stack:
                stack.pop()  # 正常配对
            else:
                # 多余闭标签，记录位置
                remove_positions.add(m.start())
    
    if not remove_positions:
        return html, 0
    
    # 从后往前删除，避免位置偏移
    result = html
    removed = 0
    for pos in sorted(remove_positions, reverse=True):
        # 找到这个 </div> 的完整起止位置
        end = result.find('>', pos)
        if end != -1:
            # 真正删除这个标签
            result = result[:pos] + result[end+1:]
            removed += 1
    
    return result, removed

# 修复两个文件
for fname in ['thailand-sim.html', 'vietnam-hochiminh.html']:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    
    o = original.count('<div')
    c = original.count('</div>')
    
    fixed, n = fix_html_divs(original)
    
    o2 = fixed.count('<div')
    c2 = fixed.count('</div>')
    
    print(f'=== {fname} ===')
    print(f'  修复前: opens={o}, closes={c}, diff={o-c}')
    print(f'  删除了 {n} 个多余 </div>')
    print(f'  修复后: opens={o2}, closes={c2}, diff={o2-c2}')
    
    if o2 == c2:
        print('  ✅ 平衡!')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f'  已写入 {fname}')
    else:
        print(f'  ❌ 仍不平衡 (diff={o2-c2})')
        # 写入备份供检查
        backup = path + '.bak2'
        with open(backup, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f'  修复版本已写入 {backup}')
    print()
