# -*- coding: utf-8 -*-
import os, re

BASE = r'G:\aistudio-travel-lab'
os.chdir(BASE)

# Precise expansion - all >= 80 chars
FIXES = {
    'budget-calculator.html': '出國旅遊預算試算器：輸入國家、天數與人數，自動幫你計算機票、住宿、餐飲、交通與購物等預算花費。內含日本、韓國、泰國、歐洲等多國參考價格，幫你精準抓預算！',
    'downloads.html': '均在路上 Travel Lab 免費旅遊資源下載中心｜打包清單模板、旅遊預算試算表、行程規劃表、機票比價技巧PDF等實用工具，下載即可使用，助你輕鬆規劃旅程不求人。',
    'japan-budget-guide.html': '2026最新日本自由行預算精算手冊！包含機票、住宿、交通、美食與藥妝購物花費明細，提供1人到多人的小資背包客、經典高CP值與奢華行程預算範本，附省錢15招實戰技巧。',
    'jiufen.html': '九份老街2026完整攻略｜阿妹茶樓茶席、芋圓冰品排行、紅糟肉圓、昇平戲院懷舊。附火車+公車交通方式、平日避人潮最佳拍照時段、黃金瀑布順遊路線與住宿推薦清單。',
    'korea-budget.html': '最完整的首爾自由行預算規劃：機票、飯店、餐費、景點門票與購物花費完整拆解，附明洞換錢所比價、省錢15招與費用估算計算器，5天4夜小資行程總預算詳細分析！',
    'notion-travel-template.html': '免費下載 2026 Notion 旅遊規劃模板！一頁整合行程表、預算追蹤、行李打包清單與住宿筆記，支援手機同步、多人協作與離線編輯，讓你輕鬆管理每一次旅程不漏接。',
    'tainan-food.html': '台南美食牛肉湯地圖2026：文章牛肉湯、六千牛肉湯、阿村牛肉湯比較，國華街必吃碗粿、春捲、小卷米粉，與極具故事感的日式老屋咖啡店，附交通方式與營業時間完整整理。',
    'taipei-food.html': '台北美食地圖2026：鼎泰豐、永康街、寧夏夜市、饒河夜市、東區早午餐完整攻略，附12個行政區必吃推薦、交通方式與營業時間，讓你吃得像在地人一樣精準不踩雷！',
    'tax-refund-calculator.html': '免稅店退稅試算器：輸入消費金額與國家，自動計算退稅金額。附韓國/日本/泰國/越南退稅流程、手續費、最低消費門檻、機場退稅櫃檯位置與常見問題解答完整攻略。',
    'kualalumpur-3days.html': '2026最新吉隆坡3天2夜自由行全攻略！深度探訪雙峰塔觀景台、茨廠街夜市、黑風洞彩虹階梯與武吉免登購物，附交通指南、小資住宿推薦、必吃美食與省錢交通卡使用教學。',
}

changed = 0
for fname, new_desc in FIXES.items():
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
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

print(f'\nFixed {changed} files.')
