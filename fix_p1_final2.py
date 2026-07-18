# -*- coding: utf-8 -*-
"""Final fix for meta descriptions - handles corrupted bangkok-massage.html."""
import os, re

BASE = r'G:\aistudio-travel-lab'
os.chdir(BASE)

# Final batch - ALL >= 80 chars
FIXES = {
    'bangkok-massage.html': '2026曼谷按摩SPA完整推薦攻略：臥佛寺泰式按摩、Divana Strings SPA、平價連鎖Let\'s Relax、Terminal 21商場按摩店完整評比，含預約教學與省錢技巧，讓你放鬆不傷荷包！',
    'budget-calculator.html': '出國旅遊預算試算器：輸入國家、天數與人數，自動幫你計算機票、住宿、餐飲、交通與購物等預算花費。內含日本、韓國、泰國、歐洲多國參考價格，精準抓預算不求人超實用！',
    'tax-refund-calculator.html': '免稅店退稅試算器：輸入消費金額與國家，自動計算退稅金額。附韓國/日本/泰國/越南退稅流程、手續費、最低消費門檻、機場退稅櫃檯位置與常見問題解答完整攻略教學。',
}

changed = 0
for fname, new_desc in FIXES.items():
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8', errors='replace') as f:
        html = f.read()

    # Special handling for bangkok-massage.html - replace entire corrupted line
    if fname == 'bangkok-massage.html':
        old_line = re.search(r'<meta name="description" content="[^"]*"', html)
        if old_line:
            new_line = f'<meta name="description" content="{new_desc}"'
            html = html.replace(old_line.group(0), new_line)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            changed += 1
            print(f'[OK] {fname}: {len(new_desc)} chars (corrupted line replaced)')
        continue

    # Normal handling
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
