import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# 1. 读取 tokyo-5days.html 的正确片段
with open(os.path.join(BASE, 'tokyo-5days.html'), 'r', encoding='utf-8') as f:
    tokyo = f.read()
fc_t = tokyo.rfind('</form>')
footer_t = tokyo.find('<!-- FOOTER -->')
correct = tokyo[fc_t:footer_t]  # 正确片段（不含 FOOTER 注释）

print(f'正确片段长度: {len(correct)}')
print(f'正确片段前100字符: {repr(correct[:100])}')
print()

# 2. 对每个错误文件进行替换
for fname in ['thailand-sim.html', 'vietnam-hochiminh.html']:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    fc = c.rfind('</form>')
    footer = c.find('<!-- FOOTER -->')

    # 取出错误的旧区段
    old_slice = c[fc:footer]
    print(f'=== {fname} ===')
    print(f'  旧区段长度: {len(old_slice)}')
    print(f'  旧区段前150字符: {repr(old_slice[:150])}')

    # 替换
    new_c = c[:fc] + correct + c[footer:]

    # 验证整体平衡
    o = new_c.count('<div')
    cl = new_c.count('</div>')
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
