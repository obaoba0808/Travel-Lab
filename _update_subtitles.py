import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# Subtitle mappings (what comes after "填Email立即收到" and before "PDF和最新旅遊資訊")
SUBTITLE_MAP = {
    'bangkok-3days.html': '3天2夜吃到飽',
    'bangkok-massage.html': '必去按摩店地圖',
    'busan-capsule.html': '住宿省錢攻略',
    'chiang-mai.html': '長期旅居指南',
    'esim-comparison.html': '上網方案推薦',
    'hokkaido-winter.html': '衣物裝備清單',
    'hualien-taitung.html': '行程規劃攻略',
    'japan-budget-guide.html': '費用規劃表',
    'japan-travel.html': '新手入門攻略',
    'jeju-island.html': '環島路線地圖',
    'jiufen.html': '美食景點推薦',
    'kansai-pass.html': '省錢必備攻略',
    'kenting.html': '必吃美食攻略',
    'korea-budget-travel-guide.html': '費用明細表',
    'korea-budget.html': '費用明細表',
    'korea-travel.html': '新手必看攻略',
    'kyoto-temples.html': '最佳觀賞日程',
    'live-japan-budget.html': '即時費用表',
    'okinawa.html': '環島必備地圖',
    'osaka-food.html': '道地小吃推薦',
    'osaka-usj.html': '遊玩攻略秘笈',
    'packing-list-online.html': '必備物品檢查',
    'packing-list.html': '必備物品檢查',
    'seasia-budget-travel-guide.html': '各國費用比較',
    'seoul-food.html': '米其林推薦',
    'southeast-asia.html': '跨國攻略',
    'tainan-food.html': '牛肉湯小吃',
    'taipei-food.html': '必吃餐廳推薦',
    'taiwan-travel-guide.html': '全台攻略',
    'taiwan-travel.html': '秘境推薦',
    'tokyo-5days.html': '行程規劃',
    'vietnam-danang.html': '海灘美食推薦',
}

def encode(s):
    return ''.join(f'&#{ord(c)};' for c in s)

count = 0
for fname, subtitle in SUBTITLE_MAP.items():
    path = os.path.join(base, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    if 'lead-inline' not in html:
        continue
    
    # Replace the generic "PDF和最新旅遊資訊" part with specific subtitle
    # The P tag pattern is: <p>填Email立即收到[subtitle]PDF和最新旅遊資訊</p>
    
    old_p_plain = '<p>填Email立即收到PDF和最新旅遊資訊</p>'
    old_p_encoded = f'<p>{encode("填Email立即收到PDF和最新旅遊資訊")}</p>'
    
    new_p_plain = f'<p>填Email立即收到{subtitle}PDF和最新旅遊資訊</p>'
    new_p_encoded = f'<p>{encode("填Email立即收到" + subtitle + "PDF和最新旅遊資訊")}</p>'
    
    replaced = False
    
    if old_p_plain in html:
        html = html.replace(old_p_plain, new_p_plain)
        replaced = True
    elif old_p_encoded in html:
        html = html.replace(old_p_encoded, new_p_encoded)
        replaced = True
    
    if replaced:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ {fname} → {subtitle}')
        count += 1

print(f'\nTotal: {count} files updated')