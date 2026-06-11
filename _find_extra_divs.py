import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

for fname in ['tokyo-5days.html', 'thailand-sim.html', 'vietnam-hochiminh.html']:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    balance = 0
    problems = []
    in_script = False
    for i, line in enumerate(lines, 1):
        # 跳过 <script> 内部
        if '<script' in line and '</script>' not in line:
            in_script = True
        if in_script:
            if '</script>' in line:
                in_script = False
            continue
        # 只统计当前行里的 div 开/关（简化：统计标签数）
        opens = line.count('<div')
        closes = line.count('</div>')
        balance += (opens - closes)
        if balance < 0:
            problems.append((i, balance, line.rstrip()))

    print(f'=== {fname} ===')
    print(f'  最终 balance: {balance}')
    if problems:
        print(f'  找到 {len(problems)} 处 balance<0 的位置：')
        for lineno, bal, content in problems[:10]:  # 显示前10个
            # 截断过长的内容
            short = content[:120] + ('...' if len(content) > 120 else '')
            print(f'    行 {lineno}: balance={bal}, 内容: {short}')
    else:
        print('  无 balance<0 的问题（结构正常）')
    print()
