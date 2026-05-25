"""Fix short alt tags - replace with descriptive SEO-friendly alt text."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

# Map image filename patterns to descriptive alt text
ALT_MAP = {
    "bangkok-hero.webp": "曼谷大皇宮與昭披耶河夜景｜泰國曼谷自由行必訪景點",
    "chiangmai-hero.webp": "清邁古城雙龍寺山景｜泰國清邁數位遊牧推薦",
    "bangkok-massage-hero.webp": "曼谷傳統泰式按摩體驗｜平價SPA與街邊按摩店推薦",
    "bangkok-sidebar.webp": "曼谷水上市場美食｜泰國旅遊必吃推薦",
    "vietnam-danang-hero.webp": "峴港美溪海灘日落｜越南峴港自由行攻略",
    "busan-hero.webp": "釜山海雲台膠囊列車海岸線｜韓國釜山必玩景點",
    "seoul-hero.webp": "首爾景福宮夜景｜韓國首爾自由行必去景點",
    "hokkaido-hero.webp": "北海道小樽運河雪景｜日本北海道冬季賞雪攻略",
    "okinawa-hero.webp": "沖繩美麗海水族館｜沖繩自駕必訪景點",
    "hualien-hero.webp": "花蓮太魯閣國家公園峽谷｜台灣花東自駕推薦",
    "tainan-hero.webp": "台南赤崁樓古蹟｜台南美食旅遊推薦",
    "kenting-hero.webp": "墾丁白沙灣海灘｜台灣墾丁三天兩夜攻略",
    "japan-budget-hero.webp": "日本廉航機票比價攻略｜東京大阪首爾便宜機票推薦",
    "japan-budget-guide-sidebar.webp": "日本旅遊預算解析｜省錢自由行完整指南",
    "tokyo-hero.webp": "東京鐵塔與澀谷十字路口｜東京5天4夜自由行",
    "kansai-hero.webp": "關西機場至大阪京都交通｜關西周遊券使用攻略",
    "osaka-food-hero.webp": "大阪道頓堀章魚燒與拉麵｜大阪必吃美食推薦",
    "jeju-hero.webp": "濟州島城山日出峰｜韓國濟州島自由行攻略",
    "jiufen-hero.webp": "九份老街紅燈籠夜景｜九份一日遊私房路線",
    "jiufen-sidebar.webp": "九份茶館與山城海景｜瑞芳九份必吃必逛推薦",
    "taipei-food-hero.webp": "台北士林夜市小吃｜台北必吃美食地圖推薦",
    "taipei-food-sidebar.webp": "台北鼎泰豐與牛肉麵｜台北旅遊美食推薦",
    "kyoto-hero.webp": "京都伏見稻荷大社千本鳥居｜京都寺廟巡禮攻略",
    "osaka-usj-sidebar.webp": "大阪環球影城哈利波特園區｜USJ門票與快速通關攻略",
    "taiwan-hero.webp": "台灣日月潭與太魯閣｜台灣環島自由行攻略",
    "vietnam-danang-sidebar.webp": "峴港巴拿山金色橋｜越南旅遊必去景點",
    "travel-tools-hero.webp": "旅遊工具比較｜eSIM、交通票券、保險推薦",
    "korea-budget-hero.webp": "韓國首爾明洞街景｜韓國5天4夜預算攻略",
    "korea-budget-sidebar.webp": "釜山甘川文化村｜韓國自由行省錢推薦",
    "seoul-food-hero.webp": "首爾廣藏市場綠豆煎餅｜首爾必吃美食推薦",
}

fixed_count = 0

for f in sorted(os.listdir(".")):
    if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
        continue
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()

    modified = False
    for img_name, new_alt in ALT_MAP.items():
        # Pattern: alt="short_text" ... src="...img_name"
        # Or: src="...img_name" ... alt="short_text"
        # We need to match img tags containing this src and replace their alt

        # Match img tags with this source file
        pattern = r'(<img\s[^>]*?)src="[^"]*' + re.escape(img_name) + r'([^>]*?>)'
        matches = list(re.finditer(pattern, c))
        for m in matches:
            tag = m.group(0)
            # Check if alt is short
            alt_m = re.search(r'alt="([^"]*)"', tag)
            if alt_m and len(alt_m.group(1).strip()) < 5:
                new_tag = re.sub(r'alt="[^"]*"', f'alt="{new_alt}"', tag, count=1)
                c = c.replace(tag, new_tag, 1)
                modified = True
                fixed_count += 1

    if modified:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(c)

print(f"Fixed {fixed_count} short alt tags across all files.")