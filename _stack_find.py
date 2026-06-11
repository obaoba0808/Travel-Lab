import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

def find_extra_divs(html):
    """返回多余 </div> 的行号列表"""
    lines = html.split('\n')
    balance = 0
    extra = []
    in_script = False
    for i, line in enumerate(lines, 1):
        if '<script' in line and '</script>' not in line:
            in_script = True
        if in_script:
            if '</script>' in line:
                in_script = False
            continue
        opens = len(re.findall(r'<div[\s>]', line))
        closes = line.count('</div>')
        for _ in range(closes):
            balance -= 1
            if balance < 0:
                extra.append(i)
        balance += opens
    return extra

for fname in ['thailand-sim.html', 'vietnam-hochiminh.html']:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    extra = find_extra_divs(c)
    print(f'=== {fname} ===')
    print(f'  多余 </div> 行号: {extra}')
    print(f'  共 {len(extra)} 处')
    if extra:
        lines = c.split('\n')
        for lineno in extra:
            print(f'    行 {lineno}: {lines[lineno-1].strip()[:100]}')
    print()
