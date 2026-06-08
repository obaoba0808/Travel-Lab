import glob
for f in sorted(glob.glob('*.html')):
    if f in ('index.html','404.html'): continue
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    has_hero_section = 'hero-' in c and '<section' in c
    has_charter = 'charter-banner' in c
    has_three_col = 'three-col-wrapper' in c
    print(f'{f}: charter={has_charter} three_col={has_three_col}')
