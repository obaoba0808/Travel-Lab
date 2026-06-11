import re, os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
files = ['tokyo-5days.html', 'thailand-sim.html', 'vietnam-hochiminh.html']

for fname in files:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    opens = c.count('<div')
    closes = c.count('</div>')
    balance = opens - closes

    fc = c.rfind('</form>')
    footer = c.find('<!-- FOOTER -->')
    if footer == -1:
        footer = c.find('<footer')
    between = c[fc:footer] if footer > fc else c[fc:fc+500]

    b_opens = between.count('<div')
    b_closes = between.count('</div>')

    print(f'=== {fname} ===')
    print(f'  整体: opens={opens}, closes={closes}, balance={balance}')
    print(f'  form->footer 区段长度: {len(between)} chars')
    print(f'  form->footer: <div>={b_opens}, </div>={b_closes}')
    print(f'  区段内容（前400字符）:')
    print(repr(between[:400]))
    print()
