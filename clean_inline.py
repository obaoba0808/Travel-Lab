import sys; sys.stdout.reconfigure(encoding='utf-8')

fixes = {
    'japan-travel.html': {
        'old': 'src="images/japan-hero.png" style="width:100%;height:auto;max-height:420px;object-fit:contain;display:block;"',
        'new': 'src="images/japan-hero.png" style="width:100%;height:auto;display:block;"'
    },
    'taiwan-travel.html': {
        'old': 'src="images/taiwan-hero.png" style="width:100%;height:auto;max-height:420px;object-fit:contain;display:block;"',
        'new': 'src="images/taiwan-hero.png" style="width:100%;height:auto;display:block;"'
    },
    'korea-travel.html': {
        'old': 'src="images/korea-hero.png" alt="韓國自由行吃貨指南" style="width:100%;height:auto;max-height:none;object-fit:contain;display:block;"',
        'new': 'src="images/korea-hero.png" alt="韓國自由行吃貨指南" style="width:100%;height:auto;display:block;"'
    },
    'southeast-asia.html': {
        'old': 'src="images/southeast-asia-hero.png" alt="東南亞自由行提案" style="width:100%;height:auto;max-height:none;object-fit:contain;display:block;"',
        'new': 'src="images/southeast-asia-hero.png" alt="東南亞自由行提案" style="width:100%;height:auto;display:block;"'
    },
}

for path, fix in fixes.items():
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    if fix['old'] in c:
        c = c.replace(fix['old'], fix['new'])
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'OK - {path}')
    else:
        print(f'Pattern not found - {path}')
        # show what IS there
        idx = c.find('hero.png')
        print('  Found:', repr(c[max(0,idx-50):idx+30]))
