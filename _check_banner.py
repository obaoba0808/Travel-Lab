import os

pages = [f for f in os.listdir('.') if f.endswith('.html')]
outside = []
for f in sorted(pages):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        lines = fh.readlines()
    cb_line = tcw_line = -1
    for i, line in enumerate(lines):
        if 'charter-banner' in line:
            cb_line = i + 1
        if 'three-col-wrapper' in line and 'class=' in line:
            tcw_line = i + 1
    if cb_line > 0 and tcw_line > 0:
        pos = 'OUTSIDE' if cb_line < tcw_line else 'INSIDE'
        print(f'{pos}: {f} (banner@{cb_line}, wrapper@{tcw_line})')
        if pos == 'OUTSIDE':
            outside.append(f)
print(f'\nTotal OUTSIDE: {len(outside)}')