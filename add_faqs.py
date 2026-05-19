import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

new_faqs = {
    'jiufen.html': [
        ('九份什麼時候去人最少？', '週二到週四的平日早上9點前抵達，人潮最少。暑假和連假絕對避開，國慶假期的九份幾乎無法移動。推薦1-3月淡季前往，淡季的九份寧靜又有氛圍。'),
    ],
    'korea-travel.html': [
        ('韓國自駕方便嗎？', '首爾不建議自駕（交通堵塞嚴重、停車費昂貴）。濟州島非常適合自駕，租車一天約NT$800-1,500，道路寬敞、景點分散。釜山可考慮自駕，但市區交通也較擁擠。持有國際駕照即可在韓國租車。'),
        ('韓國旅遊什麼季節最推薦？', '春天（3-5月）櫻花季和秋天（9-11月）紅葉季最美。夏天（6-8月）炎熱潮濕且有梅雨季，不推薦。冬天（12-2月）適合滑雪和泡溫泉，首爾聖誕市集很浪漫。若預算有限，冬季機票和住宿最便宜。'),
    ],
    'osaka-usj.html': [
        ('快速通關券值得買嗎？', '值得！尤其是超級任天堂樂園和哈利波特區域，不買快速通關可能要排2-3小時。Express Pass 7項NT$2,500-3,500，任天堂專屬通行證約¥5,000。建議官網提前購買，現場通常售完。'),
    ],
    'taipei-food.html': [
        ('台北有什麼隱藏版美食？', '① 永康街「永康15」芒果冰（非鼎泰豐那條巷子）② 大安區「段純貞」牛肉麵 ③ 中山區「喫飯食堂」定食 ④ 松山區「阜杭豆漿」（5點就要排）⑤ 萬華區「合江街」平價便當。這些本地人才知道的店，比觀光客區好吃又便宜。'),
    ],
    'vietnam-danang.html': [
        ('峴港安全嗎？女生可以獨旅嗎？', '峴港是越南最安全的旅遊城市之一，女生獨旅非常適合。注意事項：選擇評價好的住宿、夜晚避免偏僻小巷、搭 Grab（越南Uber）取代街邊攬客計程車、貴重物品放飯店保險箱。會安和峴港市區治安良好，放心玩！'),
    ],
}

for fname, faqs in new_faqs.items():
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    
    # Determine format by checking existing FAQ class
    has_arrow = 'class="faq-arrow"' in c or '<span class="arrow">' in c
    has_onclick = 'onclick="this.classList.toggle' in c
    
    new_html = ''
    for q, a in faqs:
        if has_onclick:
            new_html += f'''  <div class="faq-item" onclick="this.classList.toggle('open')">
    <div class="faq-q">{q}</div>
    <div class="faq-a">{a}</div>
  </div>
'''
        elif has_arrow:
            new_html += f'''      <div class="faq-item">
        <div class="faq-q">{q}<span class="arrow">▼</span></div>
        <div class="faq-a">{a}</div>
      </div>
'''
        else:
            new_html += f'''<div class="faq-item">
  <div class="faq-q">{q}</div>
  <div class="faq-a">{a}</div>
</div>
'''
    
    # Insert before the closing of FAQ section
    # For article pages with arrow format: find last faq-item closing, insert after it but before the section closing divs
    # Pattern: </div>\n  </div>\n</div> (faq-item > faq-section > col-center)
    
    # Find last faq-item
    items = list(re.finditer(r'class="faq-item"', c))
    if not items:
        print(f"SKIP {fname}: no faq-item found")
        continue
    
    last_item = items[-1]
    # Find the closing of this faq-item (</div></div>)
    after = c[last_item.start():]
    # Find the pattern: faq-a closing </div> then </div> for faq-item
    close_match = re.search(r'</div>\s*</div>', after)
    if not close_match:
        print(f"SKIP {fname}: can't find faq-item closing")
        continue
    
    insert_pos = last_item.start() + close_match.end()
    c = c[:insert_pos] + '\n' + new_html + c[insert_pos:]
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    
    print(f"DONE {fname}: added {len(faqs)} FAQ(s)")

print("\nAll done!")
