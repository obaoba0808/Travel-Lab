import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# New mappings - just replace any old style directly
PDF_MAP = {
    'bangkok-3days.html': '曼谷吃貨攻略',
    'bangkok-massage.html': '曼谷按摩推薦',
    'busan-capsule.html': '釜山膠囊旅館',
    'chiang-mai.html': '清邁數位遊牧',
    'esim-comparison.html': '日本eSIM比較',
    'hokkaido-winter.html': '北海道冬季打包',
    'hualien-taitung.html': '花東三天兩夜',
    'japan-budget-guide.html': '日本旅遊預算',
    'japan-travel.html': '日本自由行',
    'jeju-island.html': '濟州島自駕',
    'jiufen.html': '九份老街攻略',
    'kansai-pass.html': '關西交通票券',
    'kenting.html': '墾丁海景夜市',
    'korea-budget-travel-guide.html': '韓國旅遊預算',
    'korea-budget.html': '韓國旅遊預算',
    'korea-travel.html': '韓國自由行',
    'kyoto-temples.html': '京都賞楓時間',
    'live-japan-budget.html': '日本旅遊預算',
    'okinawa.html': '沖繩自駕遊',
    'osaka-food.html': '大阪美食地圖',
    'osaka-usj.html': 'USJ快速通關',
    'packing-list-online.html': '旅遊行李清單',
    'packing-list.html': '旅遊行李清單',
    'seasia-budget-travel-guide.html': '東南亞旅遊預算',
    'seoul-food.html': '首爾美食地圖',
    'southeast-asia.html': '東南亞自由行',
    'tainan-food.html': '台南美食攻略',
    'taipei-food.html': '台北美食地圖',
    'taiwan-travel-guide.html': '台灣自由行',
    'taiwan-travel.html': '台灣旅遊攻略',
    'tokyo-5days.html': '東京五天四夜',
    'vietnam-danang.html': '越南峴港攻略',
}

def encode(s):
    return ''.join(f'&#{ord(c)};' for c in s)

count = 0
for fname, title in PDF_MAP.items():
    path = os.path.join(base, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    if 'lead-inline' not in html:
        continue
    
    # Simple direct replace for common patterns - any "小編獨家攻略，限時免費送" in any encoding becomes title
    old_patterns = [
        '<h3>小編獨家攻略，限時免費送</h3>',
        f'<h3>{encode("小編獨家攻略，限時免費送")}</h3>',
    ]
    
    new_h3 = f'<h3>{title}，限時免費送</h3>'
    
    replaced = False
    for old in old_patterns:
        if old in html:
            html = html.replace(old, new_h3)
            replaced = True
            break
    
    if replaced:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ {fname} → {title}')
        count += 1

print(f'\nTotal: {count} files updated')