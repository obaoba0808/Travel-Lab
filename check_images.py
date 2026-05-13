import os, re

workspace = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'

for fname in ['busan-capsule.html', 'hokkaido-winter.html', 'tainan-food.html']:
    path = os.path.join(workspace, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    imgs = re.findall(r'https://images\.unsplash\.com/photo-[^"\']+', content)
    print(fname + ':')
    for img in imgs:
        print('  ' + img[:120])
    print()
