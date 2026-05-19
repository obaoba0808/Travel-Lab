import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

need_fix = {
    'bangkok-massage.html': '曼谷按摩',
    'esim-comparison.html': 'eSIM比較',
    'japan-budget-guide.html': '日本窮遊',
    'jiufen.html': '九份',
    'korea-travel.html': '韓國旅遊',
    'osaka-food.html': '大阪美食',
    'osaka-usj.html': '大阪USJ',
    'packing-list.html': '行李清單',
    'southeast-asia.html': '東南亞旅遊',
    'taipei-food.html': '台北美食',
    'vietnam-danang.html': '峴港旅遊',
}

for fname, topic in need_fix.items():
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    
    # Count existing FAQ items
    count = len(re.findall(r'class="faq-item"', c))
    print(f'{fname}: {count} FAQs')
    
    # Show last 3 FAQ questions to understand format
    faq_items = re.findall(r'class="faq-q">(.+?)</div>', c)
    for q in faq_items:
        q_clean = re.sub(r'<span[^>]*>.*?</span>', '', q).strip()
        print(f'  Q: {q_clean}')
    print()
