import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# 读取 tokyo-5days.html 的正确片段（form close 到 FOOTER）
with open(os.path.join(BASE, 'tokyo-5days.html'), 'r', encoding='utf-8') as f:
    tokyo = f.read()

# 找到 form close 和 FOOTER 的位置
fc_t = tokyo.rfind('</form>')
footer_t = tokyo.find('<!-- FOOTER -->')
correct_slice = tokyo[fc_t:footer_t]

print('=== tokyo-5days.html 正确片段（最后500字符）===')
print(repr(correct_slice[-500:]))
print()

# 修复两个文件
for fname in ['thailand-sim.html', 'vietnam-hochiminh.html']:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 找到 form close 和 FOOTER
    fc = c.rfind('</form>')
    footer = c.find('<!-- FOOTER -->')

    # 替换错误片段为正确片段
    old_slice = c[fc:footer]
    new_c = c[:fc] + correct_slice + c[footer:]

    # 验证
    o = new_c.count('<div')
    cl = new_c.count('</div>')
    print(f'=== {fname} ===')
    print(f'  旧片段长度: {len(old_slice)}')
    print(f'  新片段长度: {len(correct_slice)}')
    print(f'  修复后: opens={o}, closes={cl}, diff={o-cl}')
    if o == cl:
        print('  ✅ 平衡!')
    else:
        print(f'  ❌ 仍不平衡 (diff={o-cl})')

    # 写回
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f'  已写入 {fname}')
    print()
