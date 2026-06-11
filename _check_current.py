import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

for fname in ['thailand-sim.html', 'vietnam-hochiminh.html']:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    start = c.find('<div class="related-posts"')
    end = c.find('<!-- FOOTER -->')
    print(f'=== {fname} 当前 related-posts 到 FOOTER ===')
    print(repr(c[start:end]))
    print()
