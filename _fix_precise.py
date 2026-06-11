import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

def fix_html_divs(html):
    """
    精确栈式修复：逐字符找 <div> / </div> 标签，
    用栈配对，把多余的 </div> 替换成注释。
    返回 (修复后HTML, 移除数量)
    """
    # 先用正则找出所有 div 开/闭标签的位置和类型
    # 用非贪婪匹配避免跨标签匹配
    pattern = re.compile(r'<(/?)div\b[^>]*>', re.I)
    
    tags = []  # [(pos, is_close, tag_text), ...]
    for m in pattern.finditer(html):
        is_close = m.group(1) == '/'
        tags.append((m.start(), is_close, m.group()))
    
    # 栈式配对，记录需要移除的 </div> 位置
    stack = []  # [(pos, tag_text), ...] 开标签的位置
    remove_positions = set()
    
    for pos, is_close, tag_text in tags:
        if not is_close:
            # 开标签，入栈
            stack.append((pos, tag_text))
        else:
            # 闭标签
            if stack:
                stack.pop()  # 正常配对，不做操作
            else:
                # 多余闭标签，记录位置（移除整个 </div> 标签）
                remove_positions.add(pos)
    
    if not remove_positions:
        return html, 0
    
    # 从后往前移除，避免位置偏移
    result = html
    removed = 0
    for pos in sorted(remove_positions, reverse=True):
        # 找到这个标签的结束位置
        end = result.find('>', pos)
        if end != -1:
            # 移除整个标签
            result = result[:pos] + '<!-- FIXED EXTRA ' + result[pos:end+1] + ' -->' + result[end+1:]
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
    print(f'  修复后: opens={o2}, closes={c2}, diff={o2-c2}')
    print(f'  移除/注释了 {n} 个多余 </div>')
    
    if o2 == c2:
        print('  ✅ 平衡!')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f'  已写入 {fname}')
    else:
        print(f'  ⚠ 仍不平衡 (diff={o2-c2})，需要进一步检查')
        # 写入备份供检查
        backup = path + '.bak'
        with open(backup, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f'  修复版本已写入 {backup}')
    print()
