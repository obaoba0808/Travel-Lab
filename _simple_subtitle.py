import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# Subtitle mappings (what comes after "填Email立即收到" - note includes "PDF下載連結")
SUBTITLE_MAP = {
    'bangkok-3days.html': '3天2夜吃到飽PDF下載連結和',
    'bangkok-massage.html': '必去按摩店地圖PDF下載連結和',
    'busan-capsule.html': '住宿省錢攻略PDF下載連結和',
    'chiang-mai.html': '長期旅居指南PDF下載連結和',
    'esim-comparison.html': '日本eSIM比較PDF下載連結和',
    'hokkaido-winter.html': '冬季穿搭攻略PDF下載連結和',
    'hualien-taitung.html': '花東行程PDF下載連結和',
    'japan-budget-guide.html': '日本預算表PDF下載連結和',
    'japan-travel.html': '日本攻略PDF下載連結和',
    'jeju-island.html': '濟州島攻略PDF下載連結和',
    'jiufen.html': '九份攻略PDF下載連結和',
    'kansai-pass.html': '關西攻略PDF下載連結和',
    'kenting.html': '墾丁攻略PDF下載連結和',
    'korea-budget-travel-guide.html': '韓國預算表PDF下載連結和',
    'korea-budget.html': '韓國預算表PDF下載連結和',
    'korea-travel.html': '韓國攻略PDF下載連結和',
    'kyoto-temples.html': '京都楓葉攻略PDF下載連結和',
    'okinawa.html': '沖繩攻略PDF下載連結和',
    'osaka-food.html': '大阪美食PDF下載連結和',
    'osaka-usj.html': 'USJ攻略PDF下載連結和',
    'packing-list-online.html': '行李清單PDF下載連結和',
    'packing-list.html': '行李清單PDF下載連結和',
    'seasia-budget-travel-guide.html': '東南亞預算表PDF下載連結和',
    'seoul-food.html': '首爾美食PDF下載連結和',
    'southeast-asia.html': '東南亞攻略PDF下載連結和',
    'tainan-food.html': '台南美食PDF下載連結和',
    'taipei-food.html': '台北美食PDF下載連結和',
    'taiwan-travel.html': '台灣攻略PDF下載連結和',
    'tokyo-5days.html': '東京五天攻略PDF下載連結和',
    'vietnam-danang.html': '峴港攻略PDF下載連結和',
}

count = 0
for fname, new_middle in SUBTITLE_MAP.items():
    path = os.path.join(base, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    if 'lead-inline' not in html:
        continue
    
    # Replace the generic with new specific content
    old = '<p>填Email立即收到PDF下載連結和最新旅遊資訊</p>'
    new = f'<p>填Email立即收到{new_middle}最新旅遊資訊</p>'
    
    if old in html:
        html = html.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ {fname}')
        count += 1
    else:
        print(f'⏭️ {fname} (no match)')

print(f'\nTotal: {count} files updated')