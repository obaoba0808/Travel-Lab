#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在每篇文章 FAQ 後面插入對應城市的 Trip.com 動態橫幅廣告 (iframe)
插入位置：</section> (FAQ 結尾) 之後，<div class="related-posts"> 之前
使用「位置搜尋法」代替 regex，處理各種 HTML 格式（含 minified）
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

    # 方法：找 </section> 和 <div class="related-posts"> 的位置
    # 在兩者之間插入 iframe
    
    # 先找 FAQ 的 </section>（最後一個 </section> 通常就是 FAQ 結尾）
    # 但更準確的做法是找 <section class="faq-section"> 後面的 </section>
    
    faq_start = content.find('<section class="faq-section">')
    
    if faq_start >= 0:
        # 從 faq 開頭往後找第一個 </section>
        faq_end_tag = '</section>'
        end_pos = content.find(faq_end_tag, faq_start)
        if end_pos < 0:
            print("  [WARN] 找不到 FAQ 的 </section>，跳過: " + os.path.basename(filepath))
            return False
        # end_pos 指向 </section> 的 '<'
        insert_pos = end_pos + len(faq_end_tag)  # 插入點 = </section> 之後
    else:
        # 沒有 faq-section 標籤，嘗試找最後一個 </section>
        last_end = content.rfind('</section>')
        if last_end < 0:
            print("  [WARN] 找不到任何 </section>，跳過: " + os.path.basename(filepath))
            return False
        insert_pos = last_end + len('</section>')
    
    # 檢查插入點後面是否有 <div class="related-posts">
    related_tag = '<div class="related-posts">'
    related_pos = content.find(related_tag, insert_pos)
    
    if related_pos < 0:
        # 可能 related-posts 在插入點前面，嘗試從檔案開頭找
        related_pos = content.find(related_tag)
        if related_pos < 0:
            print("  [WARN] 找不到 related-posts，跳過: " + os.path.basename(filepath))
            return False
    
    # 在 insert_pos 處插入（</section> 結尾處）
    # 但更準確的做法是：在 </section> 和 related-posts 之間插入
    # 即在 insert_pos 和 related_pos 之間插入
    
    # 在 </section> 標籤後面插入橫幅 HTML
    new_content = content[:insert_pos] + '\n' + iframe_html + content[insert_pos:]
    
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
