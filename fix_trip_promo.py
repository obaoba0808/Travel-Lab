import os, re

files = [
    'bangkok-3days.html', 'bangkok-massage.html', 'busan-capsule.html',
    'chiang-mai.html', 'hokkaido-winter.html', 'hongkong-3days.html',
    'hualien-taitung.html', 'japan-budget-guide.html', 'jeju-island.html',
    'kansai-pass.html', 'kenting.html', 'korea-budget.html',
    'kyoto-temples.html', 'okinawa.html', 'osaka-food.html',
    'osaka-usj.html', 'seoul-food.html', 'tainan-food.html',
    'taipei-food.html', 'tokyo-5days.html', 'vietnam-danang.html'
]

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'

# Pattern to remove: trip-promo-inline div block (FAQ前靜態圖片)
pattern = re.compile(r'\n\s*<div class="trip-promo-inline">\s*<a[^>]*>.*?</a>\s*</div>\n', re.DOTALL)

for f in files:
    path = os.path.join(base, f)
    with open(path, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    new_c = pattern.sub('\n', c)
    
    if new_c != c:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_c)
        print(f'[OK] {f}')
    else:
        print(f'[WARN] {f} - no match')
