#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在文章頁面 FAQ 前插入自然 Trip.com 住宿推薦（Tiffany 藍配色）"""

import re
import os

BASE = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"

# 頁面 → (Trip.com 連結, 城市名稱, 住宿區域推薦)
TASKS = [
    {
        "file": "tokyo-5days.html",
        "url": "https://www.trip.com/t/DPuJzZWZpU2",
        "city": "東京",
        "area": "上野",
        "spot": "淺草寺、上野公園",
        "experience": "我自己是預算旅行者，會優先選擇乾淨舒服又不會太貴的住宿，這間目前我還是很推薦的",
    },
    {
        "file": "osaka-food.html",
        "url": "https://www.trip.com/t/MjoWgCaZpU2",
        "city": "大阪",
        "area": "心齋橋",
        "spot": "道頓堀、心齋橋筋商店街",
        "experience": "我自己是美食優先的旅行者，住心齋橋真的超方便，早上起床就能衝道頓堀吃早餐",
    },
    {
        "file": "osaka-usj.html",
        "url": "https://www.trip.com/t/MjoWgCaZpU2",
        "city": "大阪",
        "area": "環球影城（USJ）附近",
        "spot": "環球影城、天保山摩天輪",
        "experience": "如果想節省交通時間，強烈建議住 USJ 附近，早上可以提早進園避開人潮",
    },
    {
        "file": "hokkaido-winter.html",
        "url": "https://www.trip.com/t/iP461veZpU2",
        "city": "札幌",
        "area": "大通公園附近",
        "spot": "札幌雪祭會場、薄野",
        "experience": "冬天去札幌強烈建議住大通附近，雪祭期間走路就能到會場，不用擔心末班車",
    },
    {
        "file": "seoul-food.html",
        "url": "https://www.trip.com/t/7Ri6hsdZpU2",
        "city": "首爾",
        "area": "明洞",
        "spot": "明洞、南大門市場",
        "experience": "第一次去首爾強烈推薦住明洞，交通超方便，機場巴士直達，晚上還能逛街吃宵夜",
    },
    {
        "file": "busan-capsule.html",
        "url": "https://www.trip.com/t/bZhtHKgZpU2",
        "city": "釜山",
        "area": "海雲台",
        "spot": "海雲台海水浴場、釜山膠囊列車",
        "experience": "釜山強烈推薦住海雲台，早上起床就能看到海，傍晚還能在海邊散步超浪漫",
    },
    {
        "file": "bangkok-3days.html",
        "url": "https://www.trip.com/t/Vdq2kzTZpU2",
        "city": "曼谷",
        "area": "暹羅（Siam）",
        "spot": "暹羅百貨、MBK 購物中心",
        "experience": "曼谷強烈推薦住暹羅區，BTS 直達，去哪裡都方便，而且百貨超多超好逛",
    },
    {
        "file": "bangkok-massage.html",
        "url": "https://www.trip.com/t/Vdq2kzTZpU2",
        "city": "曼谷",
        "area": "素坤逸（Sukhumvit）",
        "spot": "娜娜廣場、阿斯寇商圈",
        "experience": "如果想體驗曼谷夜生活，強烈建議住素坤逸區，按摩店、酒吧、夜市全部步行就到",
    },
    {
        "file": "chiang-mai.html",
        "url": "https://www.trip.com/t/3Cp8JljZpU2",
        "city": "清邁",
        "area": "塔佩門（Tha Pae Gate）附近",
        "spot": "塔佩門、週日夜市、清邁古城",
        "experience": "清邁強烈推薦住塔佩門附近，週末夜市走出來就到，古城區散步也超方便",
    },
    {
        "file": "vietnam-danang.html",
        "url": "https://www.trip.com/t/RWHD5HiZpU2",
        "city": "峴港",
        "area": "美溪海灘（My Khe Beach）附近",
        "spot": "美溪海灘、巴拿山、會安古鎮",
        "experience": "峴港強烈推薦住美溪海灘附近，早上起床就能去海邊跑步，傍晚還能在海邊看夕陽",
    },
    {
        "file": "taiwan-travel.html",
        "url": "https://www.trip.com/t/FeyjyxPZpU2",
        "city": "台北",
        "area": "西門町",
        "spot": "西門紅樓、北車站、西門町步行街",
        "experience": "台北強烈推薦住西門町，交通超方便，機場巴士直達，晚上還能逛夜市吃宵夜",
    },
]

# Tiffany 藍配色
TIFFANY = "#0ABAB5"
TIFFANY_LIGHT = "#E8F8F7"
TEXT_DARK = "#1a1a2e"
TEXT_GRAY = "#666"
BORDER = "#e0e0e0"

CARD_HTML = """
<!-- 住宿推薦（Trip.com 聯盟） -->
<div class="trip-recommend-card" style="
    background: {light};
    border-radius: 16px;
    padding: 24px 28px;
    margin: 36px 0;
    border-left: 5px solid {tiffany};
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    transition: transform 0.2s, box-shadow 0.2s;
">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
    <span style="font-size:22px;">🏨</span>
    <div>
      <div style="font-weight:700; color:{tiffany}; font-size:15px;">住宿推薦（Trip.com）</div>
      <div style="font-size:12px; color:{gray};">我實際住過的區域，CP 值高</div>
    </div>
  </div>

  <p style="margin:0 0 14px 0; font-size:14px; line-height:1.8; color:{dark};">
    這次在<strong>{city}</strong>我住在<strong>{area}</strong>這間飯店，位置超方便，走路就能到{spot}。房間乾淨、CP 值很高，目前在 Trip.com 上還有不錯的優惠：
  </p>

  <a href="{url}" target="_blank" rel="nofollow sponsored" data-affiliate="trip-com"
     style="
        display:inline-block;
        background:{tiffany};
        color:#fff;
        padding:10px 22px;
        border-radius:8px;
        text-decoration:none;
        font-weight:600;
        font-size:14px;
        transition:background 0.2s;
        border:none;
        cursor:pointer;
     " onmouseover="this.style.background='#089E9E'"
     onmouseout="this.style.background='{tiffany}'">
    🔗 立即查看最新價格與空房
  </a>

  <p style="margin:10px 0 0 0; font-size:12px; color:{gray};">
    （{experience}）
  </p>
</div>
""".format(
    tiffany=TIFFANY,
    light=TIFFANY_LIGHT,
    dark=TEXT_DARK,
    gray=TEXT_GRAY,
    url="{url}",
    city="{city}",
    area="{area}",
    spot="{spot}",
    experience="{experience}",
)

def insert_recommendation(filepath, task):
    """在 FAQ 區塊前插入住宿推薦卡片"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 檢查是否已插入（避免重複）
    if "trip-recommend-card" in content:
        return f"SKIP {os.path.basename(filepath)} — 已存在推薦卡片"

    # 找插入點：<section class="faq-section"> 或 「常見問題」
    # 優先找 <section class="faq-section">
    faq_pattern = r'(<section class="faq-section">)'
    match = re.search(faq_pattern, content)

    if not match:
        # 找不到 FAQ，嘗試找「常見問題」h2
        faq_pattern = r'(<h2>[^<]*常見問題[^<]*</h2>)'
        match = re.search(faq_pattern, content)

    if not match:
        return f"FAIL {os.path.basename(filepath)} — 找不到 FAQ 插入點"

    insert_point = match.group(1)

    # 組裝 HTML
    html = CARD_HTML.format(
        url=task["url"],
        city=task["city"],
        area=task["area"],
        spot=task["spot"],
        experience=task["experience"],
    )

    # 插入
    new_content = content.replace(insert_point, html + "\n\n" + insert_point, 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return f"OK {os.path.basename(filepath)}"


# 執行
results = []
for task in TASKS:
    fp = os.path.join(BASE, task["file"])
    if not os.path.exists(fp):
        results.append(f"MISSING {task['file']}")
        continue
    result = insert_recommendation(fp, task)
    results.append(result)

# PowerShell cp950 不支援 emoji，改用純文字輸出
print("=== 執行結果 ===")
for r in results:
    status = r.split()[0]
    if status == "OK":
        print(f"  [OK] {r}")
    elif status == "SKIP":
        print(f"  [SKIP] {r}")
    else:
        print(f"  [FAIL] {r}")
