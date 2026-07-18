# -*- coding: utf-8 -*-
import os, re

BASE = r'G:\aistudio-travel-lab'
os.chdir(BASE)

# All >= 80 chars
FIXES = {
    'bangkok-massage.html': '2026曼谷按摩SPA完整推薦攻略：臥佛寺泰式按摩、Divana Strings SPA、平價連鎖Let\'s Relax、Terminal 21商場按摩店完整評比，含預約教學與省錢技巧。',
    'budget-calculator.html': '出國旅遊預算試算器：輸入國家、天數與人數，自動幫你計算機票、住宿、餐飲、交通與購物等預算花費。內含日本、韓國、泰國、歐洲等多國參考價格，幫你精準抓預算！',
    'downloads.html': '均在路上 Travel Lab 免費旅遊資源下載中心｜打包清單模板、旅遊預算試算表、行程規劃表、機票比價技巧PDF等實用工具，下載即可使用，助你輕鬆規劃旅程。',
    'index.html': '均在路上 Travel Lab — 台港旅客省錢自由行攻略平台。日本、韓國、台灣、東南亞深度旅遊指南，含預算規劃、簽證、交通、住宿推薦與實際花費，讓你用最少預算走最多地方。',
    'japan-budget-guide.html': '2026最新日本自由行預算精算手冊！包含機票、住宿、交通、美食與藥妝購物花費明細，提供1人到多人的小資背包客、經典高CP值與奢華行程預算範本，附省錢15招。',
    'jeju-island.html': '濟州島自駕環島3天2夜攻略2026：城山日出峰日出、牛島花生冰淇淋、漢拏山登頂、涯月海邊咖啡街。附租車比價平台、必吃黑豬肉烤肉店、海鮮鍋名店推薦與自駕注意事項。',
    'jiufen.html': '九份老街2026完整攻略｜阿妹茶樓茶席、芋圓冰品排行、紅糟肉肉圓、昇平戲院懷舊。附火車+公車交通方式、平日避人潮最佳拍照時段、黃金瀑布順遊路線與住宿推薦。',
    'korea-budget.html': '最完整的首爾自由行預算規劃：機票、飯店、餐費、景點門票與購物花費完整拆解，附明洞換錢所比價、省錢15招與費用估算計算器，5天4夜小資行程總預算分析！',
    'kualalumpur-3days.html': '2026最新吉隆坡3天2夜自由行全攻略！深度探訪雙峰塔觀景台、茨廠街夜市、黑風洞彩虹階梯與武吉免登購物，附交通指南、小資住宿推薦、必吃美食與省錢交通卡使用教學。',
    'notion-travel-template.html': '免費下載 2026 Notion 旅遊規劃模板！一頁整合行程表、預算追蹤、行李打包清單與住宿筆記，支援手機同步、多人協作與離線編輯，讓你輕鬆管理每一次旅程。',
    'okinawa.html': '2026 沖繩自駕4天3夜攻略：美麗海水族館、古宇利島大橋、美國村、國際通與瀨長島。含獨家「沖繩自駕預算試算器」與「租車保險攻略」，幫你精準抓預算、避開隱藏費用。',
    'tainan-food.html': '台南美食牛肉湯地圖2026：文章牛肉湯、六千牛肉湯、阿村牛肉湯比較，國華街必吃碗粿、春捲、小卷米粉，與極具故事感的日式老屋咖啡店，附交通方式與營業時間整理。',
    'taipei-food.html': '台北美食地圖2026：鼎泰豐、永康街、寧夏夜市、饒河夜市、東區早午餐完整攻略，附12個行政區必吃推薦、交通方式與營業時間，讓你吃得像在地人一樣精準！',
    'tax-refund-calculator.html': '免稅店退稅試算器：輸入消費金額與國家，自動計算退稅金額。附韓國/日本/泰國/越南退稅流程、手續費、最低消費門檻、機場退稅櫃檯位置與常見問題解答。',
    'tokyo-accommodation.html': '東京住宿區域比較2026：新宿交通便利/上野平平價/淺草安靜/澀谷潮流/池袋家庭房。附每晚NT$800起平價飯店推薦、交通路線解析與選擇指南，幫你找到最適合的下榻地點。',
    'vietnam-hochiminh.html': '胡志明市3天2夜攻略2026：范老五街酒吧夜市、湄公河三角洲一日遊、戰爭遺跡博物館、10大必吃美食、3大住宿區推薦。含免簽證費教學、Grab叫車攻略與換錢技巧。',
}

changed = 0
for fname, new_desc in FIXES.items():
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'[SKIP] {fname}: not found')
        continue
    with open(path, encoding='utf-8', errors='replace') as f:
        html = f.read()
    pattern = re.compile(
        r'(<meta\s+[^>]*?(?:name|property)=["\']description["\'][^>]*?)content=["\']([^"\']*)["\']',
        re.IGNORECASE | re.DOTALL
    )
    def replacer(m):
        return f'{m.group(1)}content="{new_desc}"'
    new_html, count = pattern.subn(replacer, html)
    if count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        changed += 1
        print(f'[OK] {fname}: {len(new_desc)} chars')
    else:
        print(f'[SKIP] {fname}: no desc tag')

print(f'\nFixed {changed} files.')
