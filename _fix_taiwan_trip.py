#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""處理 taiwan-travel.html：在有 style 屬性的 faq-section 前插入 Trip.com 推薦卡片"""

import re, os

BASE = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"
FILE = "taiwan-travel.html"
TASK = {
    "url": "https://www.trip.com/t/FeyjyxPZpU2",
    "city": "台北",
    "area": "西門町",
    "spot": "西門紅樓、北車站、西門町步行街",
    "experience": "台北強烈推薦住西門町，交通超方便，機場巴士直達，晚上還能逛夜市吃宵夜",
}

TIFFANY = "#0ABAB5"
TIFFANY_LIGHT = "#E8F8F7"
TEXT_DARK = "#1a1a2e"
TEXT_GRAY = "#666"

CARD = ("""
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
     " onmouseover="this.style.background='#089E9b'"
     onmouseout="this.style.background='{tiffany}'">
    🔗 立即查看最新價格與空房
  </a>

  <p style="margin:10px 0 0 0; font-size:12px; color:{gray};">
    （{experience}）
  </p>
</div>
""").format(
    tiffany=TIFFANY,
    light=TIFFANY_LIGHT,
    dark=TEXT_DARK,
    gray=TEXT_GRAY,
    url=TASK["url"],
    city=TASK["city"],
    area=TASK["area"],
    spot=TASK["spot"],
    experience=TASK["experience"],
)

fp = os.path.join(BASE, FILE)
with open(fp, "r", encoding="utf-8") as f:
    content = f.read()

if "trip-recommend-card" in content:
    print(f"SKIP {FILE} — 已存在推薦卡片")
else:
    # 匹配帶有 style 屬性的 faq-section
    pattern = r'(<section class="faq-section"[^>]*>)'
    match = re.search(pattern, content)
    if not match:
        print(f"FAIL {FILE} — 找不到 FAQ 插入點")
    else:
        insert_point = match.group(1)
        new_content = content.replace(insert_point, CARD + "\n\n" + insert_point, 1)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"OK {FILE}")
