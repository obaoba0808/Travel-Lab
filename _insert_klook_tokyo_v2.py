#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修正 tokyo-5days.html 的 Klook 聯盟卡片插入
插入在 tip-box 之後、每日行程詳解之前
"""

import re
import os

FILE = "tokyo-5days.html"

KLOOK_CARD = '''
<!-- KLOOK 聯盟推薦 -->
<div class="klook-recommend-card" style="
    background: #E3F2FD;
    border-radius: 16px;
    padding: 24px 28px;
    margin: 36px 0;
    border-left: 5px solid #0078C8;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    transition: transform 0.2s, box-shadow 0.2s;
" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 24px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 16px rgba(0,0,0,0.06)'">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
    <span style="font-size:22px;">🚇</span>
    <div>
      <div style="font-weight:700; color:#0078C8; font-size:15px;">交通票券推薦（Klook）</div>
      <div style="font-size:12px; color:#666;">我自己購買的 Tokyo Subway Ticket，新宿/澀谷/淺草隨便搭</div>
    </div>
  </div>

  <p style="margin:0 0 14px 0; font-size:14px; line-height:1.8; color:#1a1a2e;">
    這次東京自由行我直接在 Klook 上買 <strong>Tokyo Subway Ticket（24/48/72小時）</strong>，成田/羽田機場就能領票，地鐵隨便搭，不用每次買票、不用算車資，超方便！推薦買 72 小時，CP 值最高。
  </p>

  <a href="https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283447&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1552-subway-ticket-tokyo%2F" 
     target="_blank" rel="nofollow sponsored" data-affiliate="klook"
     style="
        display:inline-block;
        background:#0078C8;
        color:#fff;
        padding:10px 22px;
        border-radius:8px;
        text-decoration:none;
        font-weight:600;
        font-size:14px;
        transition:background 0.2s;
        border:none;
        cursor:pointer;
     " onmouseover="this.style.background='#01579B'"
     onmouseout="this.style.background='#0078C8'">
    🔗 立即查看地鐵票券最新優惠
  </a>

  <p style="margin:10px 0 0 0; font-size:12px; color:#666;">
    （我自己是預算旅行者，會優先選擇方便又不用算車資的票券，Tokyo Subway Ticket 真的省超多！）
  </p>
</div>
'''

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, FILE)
    
    print(f"[處理中] {FILE}...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # 插入在 tip-box 的 </div> 之後、每日行程詳解之前
    pattern = r'(  </div>  <h2>🗓️ 每日行程詳解</h2>)'
    
    replacement = r'\1' + KLOOK_CARD
    
    new_html, count = re.subn(pattern, replacement, html, count=1)
    
    if count == 0:
        print(f"[FAIL] 找不到插入位置: {FILE}")
        # 除錯：印出前 500 個字元
        print("檔案開頭:")
        print(html[:500])
        return
    
    print(f"[OK] 插入成功: {FILE} (1 個卡片)")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    
    print(f"[完成] {FILE} 已更新")

if __name__ == "__main__":
    main()
