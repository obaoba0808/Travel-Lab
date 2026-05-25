#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch insert images into 4 HTML pages after specific headings."""

import os

base = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"

tasks = [
    {
        "file": "bangkok-3days.html",
        "target": "<h3>老城區：大皇宮 → 臥佛寺 → 唐人街美食</h3>",
        "img": "ollieyu-bangkok-3days.webp",
        "alt": "曼谷3天2夜實戰心得：大皇宮、臥佛寺、唐人街美食"
    },
    {
        "file": "bangkok-massage.html",
        "target": "<h2>平價連鎖店推薦（฿200-900）</h2>",
        "img": "ollieyu-bangkok-massage.webp",
        "alt": "曼谷按摩實戰心得：平價連鎖按摩店推薦"
    },
    {
        "file": "chiang-mai.html",
        "target": "<h3>老城區寺廟 + 週日夜市</h3>",
        "img": "ollieyu-chiang-mai.webp",
        "alt": "清邁旅遊實戰心得：老城區寺廟、週日夜市"
    },
    {
        "file": "vietnam-danang.html",
        "target": "<h2>Day 1：巴拿山（Ba Na Hills）</h2>",
        "img": "ollieyu-vietnam.webp",
        "alt": "越南峴港實戰心得：巴拿山纜車、佛手橋"
    },
]

image_html_template = """

<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0;">
  <img src="images/{img}" alt="{alt}" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);">
</div>
"""

results = []
for t in tasks:
    fp = os.path.join(base, t["file"])
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    if t["target"] in content:
        html = image_html_template.format(img=t["img"], alt=t["alt"])
        new_content = content.replace(t["target"], t["target"] + html, 1)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_content)
        results.append(f"OK {t['file']}")
    else:
        results.append(f"FAIL {t['file']} - target not found")

for r in results:
    print(r)
