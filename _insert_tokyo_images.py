#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在 tokyo-5days.html 對應章節插入 4 張圖片
- 四角圓角（border-radius: 16px）
- 每張圖片下方加入「小編個人體驗感」小字
- UI 美化（陰影、置中、hover 效果）
"""

import re
import os

FILE = "tokyo-5days.html"

IMAGES = [
    {
        # Day 2: 澀谷十字路口 + Shibuya Sky
        "src": "images/shibuya-sky.webp",
        "alt": "澀谷十字路口與 Shibuya Sky 實戰心得",
        "insert_after": r'(<div class="tip-box">\s*<strong>💡 提示：</strong>Shibuya Sky 建議提前上 Klook 購票，現場常售罄。黃昏時段看夕陽最美！\s*</div>\s*</div>)',
        "experience": "小編個人體驗：澀谷十字路口下午 3-5 點人最多，想拍空景建議早上 9 點前！Shibuya Sky 黃昏時段（16:00-18:00）超難搶，我上次提前 2 週在 Klook 上買，現場很多人當場買不到。"
    },
    {
        # Day 3: 築地市場
        "src": "images/tsukiji-market.webp",
        "alt": "豊洲市場（築地市場搬遷後）壽司實戰心得",
        "insert_after": r'(<div class="tip-box">\s*<strong>💡 個人觀點：</strong>豊洲市場的壽司排隊真的久，但如果你不想排隊，可以改去市場內的 <strong>Uogashi Nihon-ichi</strong>，一樣新鮮但人少很多。另外，銀座的 <strong>Itoya 文具店</strong> 有7層樓，買明信片寄回台灣超有紀念價值！\s*</div>\s*</div>)',
        "experience": "小編個人體驗：築地（現在是豊洲）的壽司真的超新鮮！Sushi Dai 排隊 2 小時起跳，但吃第一口就覺得值得。如果你不想排隊，Uogashi Nihon-ichi 是人少很多的選擇，一樣是市場內的壽司店。"
    },
    {
        # Day 4: 鎌倉啤酒
        "src": "images/kamakura-beer.webp",
        "alt": "鎌倉一站買當地釀造啤酒實戰心得",
        "insert_after": r'(<div class="tip-box">\s*<strong>💡 個人觀點：</strong>鎌倉週末人超多，<strong>強烈建議平日去</strong>。如果只能週末去，早上7:00前就要從東京出發，才能避開人潮。另外，江之電是路面電車，沒有車門自動關閉，可以在行駛中把頭伸出車窗拍照（但注意安全）！這是我去過最chill的電車體驗。\s*</div>\s*</div>)',
        "experience": "小編個人體驗：鎌倉一站買的當地釀造啤酒超好喝！晚上在車站附近的小酒吧喝，配著鎌倉的夕陽回憶一整天，超有感的。推薦買「鎌倉啤酒 IPA」，苦味剛好不會太重。"
    },
    {
        # Day 5: 新宿歌舞伎町一蘭拉麵
        "src": "images/shinjuku-ramen.webp",
        "alt": "新宿歌舞伎町一蘭拉麵實戰心得（24小時營業）",
        "insert_after": r'(<div class="tip-box">\s*<strong>💡 個人觀點：</strong>最後一天不要安排太遠的地方，我上次因為去上野逛太久而錯過機場快車，差點沒趕上飛機。建議最後一天就待在飯店附近逛街，輕鬆一點。另外，如果你有剩餘的日圓（硬幣），可以在機場的 <strong>自動販賣機</strong> 買飲料喝完再安檢，日本安檢不能帶超過100ml液體上飛機。\s*</div>\s*</div>)',
        "experience": "小編個人體驗：一蘭拉麵被過度炒作了，但沒吃過還是可以試一次。我個人覺得口味偏鹹，湯頭沒有台灣的蘭拉麵店那麼濃郁。不過一蘭的體驗很特別——隔間式座位、自動點餐機，很有日本獨居文化的感覺。推薦半夜 1-2 點去，完全不用排隊！"
    }
]

def create_image_html(img):
    """生成圖片 HTML（圓角 + 陰影 + 小編體驗小字）"""
    return f'''
<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0; transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
  <img src="{img['src']}" alt="{img['alt']}" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);cursor:pointer;" loading="lazy">
  <p style="margin:10px 0 0 0;font-size:13px;color:#666;line-height:1.6;font-style:italic;">📝 {img['experience']}</p>
</div>
'''

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, FILE)
    
    print(f"[處理中] {FILE}...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    inserted_count = 0
    
    for img in IMAGES:
        pattern = img["insert_after"]
        img_html = create_image_html(img)
        replacement = r'\1' + img_html
        
        new_html, count = re.subn(pattern, replacement, html, count=1, flags=re.DOTALL)
        
        if count == 0:
            print(f"[FAIL] 找不到插入位置: {img['src']}")
        else:
            html = new_html
            inserted_count += 1
            print(f"[OK] 插入成功: {img['src']}")
    
    if inserted_count == 0:
        print("[FAIL] 沒有任何圖片插入成功，請檢查正則表達式")
        return
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"[完成] {FILE} 已更新（{inserted_count} 張圖片）")

if __name__ == "__main__":
    main()
