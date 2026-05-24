#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正 tokyo-5days.html 的 shinjuku-ramen.webp 插入
正則表達式修正：匹配實際 HTML 文字
"""

import re
import os

FILE = "tokyo-5days.html"

IMAGE_HTML = '''
<!-- 實戰推薦配圖 -->
<div style="text-align:center;margin:28px 0; transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
  <img src="images/shinjuku-ramen.webp" alt="新宿歌舞伎町一蘭拉麵實戰心得（24小時營業）" style="width:100%;max-width:600px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,0.1);cursor:pointer;" loading="lazy">
  <p style="margin:10px 0 0 0;font-size:13px;color:#666;line-height:1.6;font-style:italic;">📝 小編個人體驗：一蘭拉麵被過度炒作了，但沒吃過還是可以試一次。我個人覺得口味偏鹹，湯頭沒有台灣的蘭拉麵店那麼濃郁。不過一蘭的體驗很特別——隔間式座位、自動點餐機，很有日本獨居文化的感覺。推薦半夜 1-2 點去，完全不用排隊！</p>
</div>
'''

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, FILE)
    
    print(f"[處理中] {FILE}...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # 修正正則：匹配實際 HTML（硬幣（日圓硬幣））
    pattern = r'(    <div class="tip-box">\s*<strong>💡 個人觀點：</strong>最後一天不要安排太遠的地方，我上次因為去上野逛太久而錯過機場快車，差點沒趕上飛機。建議最後一天就待在飯店附近逛街，輕鬆一點。另外，如果你有剩餘的硬幣（日圓硬幣），可以在機場的 <strong>自動販賣機</strong> 買飲料喝完再安檢，日本安檢不能帶超過100ml液體上飛機。\s*</div>\s*</div>)'
    
    replacement = r'\1' + IMAGE_HTML
    
    new_html, count = re.subn(pattern, replacement, html, count=1, flags=re.DOTALL)
    
    if count == 0:
        print(f"[FAIL] 找不到插入位置: shinjuku-ramen.webp")
        # 除錯：印出前 2000 個字元，檢查 tip-box 內容
        idx = html.find("最後一天不要安排太遠")
        if idx != -1:
            print("找到「最後一天」關鍵字，上下文：")
            print(html[idx-50:idx+200])
        else:
            print("找不到「最後一天」關鍵字")
        return
    
    print(f"[OK] 插入成功: images/shinjuku-ramen.webp")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    
    print(f"[完成] {FILE} 已更新（shinjuku-ramen.webp）")

if __name__ == "__main__":
    main()
