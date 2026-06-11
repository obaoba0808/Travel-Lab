#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修復 downloads.html：為每個卡片加入正確的 PDF 下載連結
"""

import re

# 讀取檔案
with open('downloads.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 標題到 PDF 檔案的對應表
pdf_mapping = {
    '曼谷美食地圖': 'bangkok-food-map.pdf',
    '首爾美食地圖': 'seoul-food-map.pdf',
    '大阪美食地圖': 'osaka-food-map.pdf',
    '台北美食地圖': 'taipei-food-map.pdf',
    '台南美食地圖': 'tainan-food-map.pdf',
    '東京Metro攻略': 'tokyo-metro-map.pdf',
    '行李清單': 'packing-checklist.pdf',
    '日本預算表': 'japan-budget-sheet.pdf',
    '韓國預算表': 'korea-budget-sheet.pdf',
    '東南亞預算表': 'sea-budget-sheet.pdf',
    '清邁數位遊牧攻略': 'chiang-mai-guide.pdf',
    '釜山膠囊旅館指南': 'busan-capsule-guide.pdf',
    '峴港攻略地圖': 'danang-map.pdf',
    '濟州島自駕路線': 'jeju-driving-route.pdf',
    '北海道行李清單': 'hokkaido-packing-list.pdf',
    '花蓮三日行程': 'hualien-itinerary.pdf',
    '九份旅遊攻略': 'jiufen-guide.pdf',
    '墾丁夜市攻略': 'kenting-night-market.pdf',
    '關西周遊券攻略': 'kansai-pass-calculator.pdf',
    '京都賞楓schedule': 'kyoto-momiji-schedule.pdf',
    '沖繩自駕地圖': 'okinawa-driving-map.pdf',
    'USJ快速通關攻略': 'usj-quick-pass.pdf',
    '緊急聯絡卡': 'emergency-contact-card.pdf',
    '台灣旅遊攻略': 'taipei-food-map.pdf',  # 暫時對應到台北美食地圖
}

# 找到所有 card 並加入下載按鈕
def process_cards(html):
    import re
    
    # 匹配每個 card div
    card_pattern = r'(<div class="card">[\s\S]*?</div>\n      </div>)'
    
    def add_download_btn(match):
        card = match.group(1)
        
        # 取得標題
        title_match = re.search(r'<h3>(.*?)</h3>', card)
        if not title_match:
            return card
        
        title = title_match.group(1)
        pdf_file = pdf_mapping.get(title)
        
        if not pdf_file:
            print(f"⚠️ 找不到對應 PDF: {title}")
            return card
        
        # 在倒數第二個 </div> 前插入下載按鈕
        # 找到 card 內最後一個 </div> (這是 card 的結束標籤)
        # 我們要在它之前插入按鈕
        download_btn = f'\n        <a href="/downloads/{pdf_file}" download class="download-btn">📥 下載 PDF</a>'
        
        # 在最後一個 </div> 前插入
        card = card.rstrip().replace('</div>', download_btn + '\n      </div>', 1)
        
        return card
    
    # 處理所有 cards
    html = re.sub(card_pattern, add_download_btn, html)
    return html

# 更新 CSS：加入 .download-btn 樣式，並讓 card 可以點擊
new_styles = """
    .card {
      background: #fff;
      border-radius: 14px;
      padding: 24px 20px;
      border: 1px solid #e8ecf0;
      transition: transform 0.2s, box-shadow 0.2s;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.1); }
    .download-btn {
      display: inline-block;
      background: linear-gradient(135deg, #0ABAB5, #764ba2);
      color: #fff;
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 8px;
      text-align: center;
      margin-top: 4px;
      transition: opacity 0.2s;
      cursor: pointer;
    }
    .download-btn:hover { opacity: 0.85; }
    .back {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #0ABAB5;
      text-decoration: none;
      font-weight: 600;
      margin-bottom: 24px;
    }
    .back:hover { text-decoration: underline; }
  </style>"""

# 執行處理
content = process_cards(content)

# 取代 CSS（把舊的 </style> 前的內容換成新的）
old_css_end = content.find('  </style>')
if old_css_end > 0:
    # 找到 <style> 開始位置
    style_start = content.find('<style>')
    # 取代整個 style 區塊
    content = content[:style_start] + '<style>' + new_styles

# 寫入檔案
with open('downloads.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ downloads.html 已更新：所有卡片加入下載按鈕")
print(f"✅ 處理了 {len([k for k in pdf_mapping.keys() if k in content])} 個 PDF 對應")
