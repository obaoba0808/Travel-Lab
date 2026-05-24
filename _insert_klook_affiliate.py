#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
插入 Klook 聯盟推薦卡片到 Travel Lab 頁面
- osaka-usj.html: 2 個 Klook 卡片（USJ 普通票 + 快速通關）
- kansai-pass.html: 1 個 Klook 卡片（JR Pass）
- tokyo-5days.html: 1 個 Klook 卡片（Tokyo Subway Pass）
"""

import re
import os

PAGES = [
    {
        "file": "osaka-usj.html",
        "insert_after": r'(<div class="highlight-box-beautify"><div class="hb-title">⭐ 推薦（排隊30-60分鐘）</div><p>⑥ 迷你兵團鬧翻天 ⑦ 大白鯊 ⑧ 浴火赤子情 ⑨ 飛天史努比 ⑩ 小小兵樂園</p></div>)',
        "cards": [
            {
                "title": "門票推薦（Klook）",
                "subtitle": "我自己購買的電子票，QR Code 直接入場",
                "color": "#FF5722",
                "bg": "#FFF3E0",
                "emoji": "🎢",
                "text": "這次去 USJ 我直接在 Klook 上買 <strong>電子票（QR Code 直接入場）</strong>，不用換票、不用排隊，超方便！如果你想省時間，也可以加購 <strong>Express Pass（快速通關）</strong>，熱門設施可以直接跳過排隊。",
                "link": "https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry%2F",
                "cta": "🔗 立即查看 USJ 門票最新優惠",
                "note": "（我自己是預算旅行者，會優先選擇方便又不用排隊的票券，Klook 上購買真的很快！）",
                "hover": "#F4511E"
            },
            {
                "title": "快速通關推薦（Klook）",
                "subtitle": "熱門設施免排隊，節省 2-4 小時",
                "color": "#FF5722",
                "bg": "#FFF3E0",
                "emoji": "⚡",
                "text": "如果你只有一天時間，強烈推薦加購 <strong>Express Pass（快速通關券）</strong>！可以跳過飛天翼龍、咒術迴戰、哈利波特禁忌之旅的排隊人潮，省下至少 2-4 小時，一天玩完所有熱門設施不是夢！",
                "link": "https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F3407-universal-studios-japan-express-pass-osaka%2F",
                "cta": "🔗 立即查看快速通關最新優惠",
                "note": "（旺季週末建議提前一週購買，現場常常售完！）",
                "hover": "#F4511E"
            }
        ]
    },
    {
        "file": "kansai-pass.html",
        "insert_after": r'(<div style="text-align:center;margin:28px 0;">\s*<img src="images/ollieyu-kansai-pass\.webp"[^>]*>\s*</div>)',
        "cards": [
            {
                "title": "交通票券推薦（Klook）",
                "subtitle": "我自己購買的 JR Pass，關西機場直達京都/大阪",
                "color": "#007B43",
                "bg": "#E8F8F7",
                "emoji": "🚅",
                "text": "這次關西自由行我直接在 Klook 上買 <strong>JR Pass 關西寬廣區域券（5日）</strong>，成田/關西機場就能領票，直接搭 HARUKA 到京都/大阪，不用排隊買票、不用算車資，超方便！",
                "link": "https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-HK%2Factivity%2F3277-5-day-kansai-wide-area-jr-pass%2F",
                "cta": "🔗 立即查看 JR Pass 最新優惠",
                "note": "（我自己是預算旅行者，會優先選擇方便又不用算車資的票券，JR Pass 真的省超多！）",
                "hover": "#006637"
            }
        ]
    },
    {
        "file": "tokyo-5days.html",
        "insert_after": r'(<h2>東京都內交通</h2>)',
        "cards": [
            {
                "title": "交通票券推薦（Klook）",
                "subtitle": "我自己購買的 Tokyo Subway Ticket，新宿/澀谷/淺草隨便搭",
                "color": "#0078C8",
                "bg": "#E3F2FD",
                "emoji": "🚇",
                "text": "這次東京自由行我直接在 Klook 上買 <strong>Tokyo Subway Ticket（24/48/72小時）</strong>，成田/羽田機場就能領票，地鐵隨便搭，不用每次買票、不用算車資，超方便！推薦買 72 小時，CP 值最高。",
                "link": "https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283447&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1552-subway-ticket-tokyo%2F",
                "cta": "🔗 立即查看地鐵票券最新優惠",
                "note": "（我自己是預算旅行者，會優先選擇方便又不用算車資的票券，Tokyo Subway Ticket 真的省超多！）",
                "hover": "#01579B"
            }
        ]
    }
]

def create_card_html(card):
    """生成 Klook 推薦卡片 HTML"""
    return f'''
<!-- KLOOK 聯盟推薦 -->
<div class="klook-recommend-card" style="
    background: {card['bg']};
    border-radius: 16px;
    padding: 24px 28px;
    margin: 36px 0;
    border-left: 5px solid {card['color']};
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    transition: transform 0.2s, box-shadow 0.2s;
" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 24px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 16px rgba(0,0,0,0.06)'">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
    <span style="font-size:22px;">{card['emoji']}</span>
    <div>
      <div style="font-weight:700; color:{card['color']}; font-size:15px;">{card['title']}</div>
      <div style="font-size:12px; color:#666;">{card['subtitle']}</div>
    </div>
  </div>

  <p style="margin:0 0 14px 0; font-size:14px; line-height:1.8; color:#1a1a2e;">
    {card['text']}
  </p>

  <a href="{card['link']}" 
     target="_blank" rel="nofollow sponsored" data-affiliate="klook"
     style="
        display:inline-block;
        background:{card['color']};
        color:#fff;
        padding:10px 22px;
        border-radius:8px;
        text-decoration:none;
        font-weight:600;
        font-size:14px;
        transition:background 0.2s;
        border:none;
        cursor:pointer;
     " onmouseover="this.style.background='{card['hover']}'"
     onmouseout="this.style.background='{card['color']}'">
    {card['cta']}
  </a>

  <p style="margin:10px 0 0 0; font-size:12px; color:#666;">
    {card['note']}
  </p>
</div>
'''

def insert_cards(html, page_config):
    """在指定位置插入卡片"""
    cards_html = "\n".join(create_card_html(card) for card in page_config["cards"])
    pattern = page_config["insert_after"]
    
    # 使用 re.sub 在匹配處後方插入卡片
    replacement = r'\1' + cards_html
    new_html, count = re.subn(pattern, replacement, html, count=1, flags=re.DOTALL)
    
    if count == 0:
        print(f"[FAIL] 找不到插入位置: {page_config['file']}")
        return None
    
    print(f"[OK] 插入成功: {page_config['file']} ({len(page_config['cards'])} 個卡片)")
    return new_html

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for page in PAGES:
        file_path = os.path.join(base_dir, page["file"])
        
        if not os.path.exists(file_path):
            print(f"[SKIP] 檔案不存在: {file_path}")
            continue
        
        print(f"[處理中] {page['file']}...")
        
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
        
        new_html = insert_cards(html, page)
        
        if new_html is None:
            continue
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_html)
        
        print(f"[完成] {page['file']} 已更新")

if __name__ == "__main__":
    main()
