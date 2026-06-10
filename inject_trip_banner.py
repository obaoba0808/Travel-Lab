#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在每篇文章 FAQ 後面插入對應城市的 Trip.com 動態橫幅廣告 (iframe)
插入位置：</section> (FAQ 結尾) 之後，<div class="related-posts"> 之前
支援 minified HTML（標籤間可能無換行）
"""

import re
import os

BASE_DIR = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"

# 文章檔案 → 橫幅 ID + 尺寸 + 城市名
BANNER_MAP = {
    # 日本 - 分城市
    "tokyo-5days.html":       ("DB17161314", 468, 60, "東京"),
    "kyoto-temples.html":      ("DB17161349", 468, 60, "大阪"),
    "kansai-pass.html":        ("DB17161349", 468, 60, "大阪"),
    "osaka-food.html":         ("DB17161349", 468, 60, "大阪"),
    "osaka-usj.html":          ("DB17161349", 468, 60, "大阪"),
    "japan-budget-guide.html": ("DB17161314", 468, 60, "東京"),
    "hokkaido-winter.html":   ("DB17161468", 468, 60, "札幌"),
    "okinawa.html":            ("DB17161314", 468, 60, "東京"),
    # 韓國 - 分城市
    "seoul-food.html":         ("DB17161370", 468, 60, "首爾"),
    "busan-capsule.html":     ("DB17161545", 468, 60, "釜山"),
    "jeju-island.html":        ("DB17161370", 468, 60, "首爾"),
    "korea-budget.html":       ("DB17161370", 468, 60, "首爾"),
    # 台灣
    "hualien-taitung.html":    ("DB17138130", 728, 90, "台北"),
    "tainan-food.html":        ("DB17138130", 728, 90, "台北"),
    "kenting.html":            ("DB17138130", 728, 90, "台北"),
    "taipei-food.html":        ("DB17138130", 728, 90, "台北"),
    "jiufen.html":             ("DB17138130", 728, 90, "台北"),
    # 東南亞
    "chiang-mai.html":         ("DB17161559", 468, 60, "清邁"),
    "bangkok-3days.html":      ("DB17161132", 468, 60, "曼谷"),
    "bangkok-massage.html":    ("DB17161132", 468, 60, "曼谷"),
    "vietnam-danang.html":     ("DB17165612", 468, 60, "胡志明市"),
    "hongkong-3days.html":    ("DB17165486", 468, 60, "香港"),
}

ALLIANCE_ID = "8237671"
SID = "312406690"

def make_iframe(banner_id, width, height, city_name):
    """生成動態橫幅 iframe HTML"""
    return (
        '\n<!-- TRIP 動態橫幅：' + city_name + ' -->\n'
        '<div class="trip-dynamic-banner" style="max-width:' + str(width) + 'px;margin:32px auto;text-align:center;">\n'
        '  <iframe border="0"\n'
        '    src="https://tw.trip.com/partners/ad/' + banner_id + '?Allianceid=' + ALLIANCE_ID + '&SID=' + SID + '&trip_sub1="\n'
        '    style="width:' + str(width) + 'px;height:' + str(height) + 'px;border:none;"\n'
        '    frameborder="0"\n'
        '    scrolling="no"\n'
        '    id="' + banner_id + '"></iframe>\n'
        '</div>\n'
    )

def process_file(filepath, banner_id, width, height, city_name):
    """處理單一檔案：在 FAQ </section> 後插入橫幅"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 檢查是否已經插入過（避免重複執行）
    if "trip-dynamic-banner" in content:
        print("  [SKIP] 已包含 trip-dynamic-banner，跳過：" + os.path.basename(filepath))
        return False

    iframe_html = make_iframe(banner_id, width, height, city_name)

    # 插入位置：</section> 之後，<div class="related-posts"> 之前
    # 支援 minified HTML（標籤間可能無換行或只有空白）
    pattern = r'(</section>\s*)(<div class="related-posts">)'
    replacement = r'\1' + iframe_html + r'\2'

    new_content, count = re.subn(pattern, replacement, content, count=1)

    if count == 0:
        # Debug：顯示 FAQ 區域尾部
        faq_section = re.search(r'<section class="faq-section">.*?</section>', content, re.DOTALL)
        if faq_section:
            end_snippet = faq_section.group()[-400:]
            print("  [DEBUG] FAQ section 尾部 400 字元：")
            print(repr(end_snippet))
        else:
            # 找不到 faq-section，嘗試找所有 </section>
            all_ends = re.findall(r'</section>', content)
            print("  [DEBUG] 找不到 faq-section，檔案中共有 " + str(len(all_ends)) + " 個 </section>")

        print("  [WARN] 找不到插入點（</section> + related-posts），跳過: " + os.path.basename(filepath))
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("  [OK] 已插入 " + city_name + " 橫幅 (" + banner_id + "): " + os.path.basename(filepath))
    return True

def main():
    print("=" * 60)
    print("Trip.com 動態橫幅插入腳本")
    print("插入位置: FAQ </section> 之後，related-posts 之前")
    print("=" * 60)

    success = 0
    skipped = 0
    failed = 0

    for filename, (banner_id, width, height, city_name) in BANNER_MAP.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print("  [ERROR] 檔案不存在：" + filename)
            failed += 1
            continue

        print("\n處理: " + filename + " -> " + city_name + " (" + banner_id + ")")
        try:
            result = process_file(filepath, banner_id, width, height, city_name)
            if result:
                success += 1
            else:
                skipped += 1
        except Exception as e:
            print("  [ERROR] " + str(e))
            failed += 1

    print("")
    print("=" * 60)
    print("完成: 成功 " + str(success) + " 個 | 跳過 " + str(skipped) + " 個 | 失敗 " + str(failed) + " 個")
    print("=" * 60)

if __name__ == "__main__":
    main()
