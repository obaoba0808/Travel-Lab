import re

with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The insertion point: before FAQ section
# The file is minified, so look for the exact string
insertion_point = '  <section class="faq-section">'

day3_5_content = """
  <div class="day-card">
    <span class="day-tag">Day 3</span>
    <h3>築地市場 → 銀座 → 秋葉原</h3>
    <ul>
      <li>早上前往 <strong>豊洲市場</strong>（築地已搬遷！別跑錯地方），5:00-6:00 看金槍魚拍賣（需提前網路預約）</li>
      <li>市場內 <strong>Sushi Dai</strong> 吃新鮮壽司（排隊1-2小時，但超值！），我覺得比築地本通的壽司大眾店好吃10倍</li>
      <li>中午搭地鐵到 <strong>銀座</strong>，逛 Ginza Six 百貨，地下一樓食品區可以試吃超多零食</li>
      <li>下午搭 <strong>銀座線</strong> 到 <strong>秋葉原</strong>，逛電器店、動漫周邊，推薦 <strong>Super Potato</strong> retro 遊戲店</li>
      <li>晚上在秋葉原吃 <strong>女僕咖啡廳</strong>（如果你敢的話），或去 <strong>筑土神防</strong> 看夜景</li>
    </ul>
    <div class="tip-box">
      <strong>💡 個人觀點：</strong>豊洲市場的壽司排隊真的久，但如果你不想排隊，可以改去市場內的 <strong>Uogashi Nihon-ichi</strong>，一樣新鮮但人少很多。另外，銀座的 <strong>Itoya 文具店</strong> 有7層樓，買明信片寄回台灣超有紀念價值！
    </div>
  </div>

  <div class="day-card">
    <span class="day-tag">Day 4</span>
    <h3>鎌倉一日遊 → 江之島 → 小町通</h3>
    <ul>
      <li>早上從新宿搭 <strong>JR 湘南新宿線</strong> 到鎌倉（約1小時，¥940）</li>
      <li>鎌倉站下車後，搭 <strong>江之電</strong>（一日券 ¥800）到 <strong>鎌倉高校前站</strong> ——《灌籃高手》片頭曲的平交道就在這！</li>
      <li>步行到 <strong>長谷寺</strong> 看鎌倉大佛（¥300），我覺得比奈良大佛更有親切感，可以近距離參觀</li>
      <li>中午在 <strong>小町通</strong> 吃鎌倉名物「鎌倉包」（¥150/個），還有 <strong>鳩サブレー</strong> 餅乾必買當伴手禮</li>
      <li>下午走到 <strong>江之島</strong>，參觀嚴島神社，黃昏時在島上看出海夕陽超級美</li>
      <li>回程在鎌倉站買 <strong>鎌倉啤酒</strong>（當地釀造，超好喝）</li>
    </ul>
    <div class="tip-box">
      <strong>💡 個人觀點：</strong>鎌倉週末人超多，<strong>強烈建議平日去</strong>。如果只能週末去，早上7:00前就要從東京出發，才能避開人潮。另外，江之電是路面電車，沒有車門自動關閉，可以在行駛中把頭伸出車窗拍照（但注意安全）！這是我去過最chill的電車體驗。
    </div>
  </div>

  <div class="day-card">
    <span class="day-tag">Day 5</span>
    <h3>最後採購 → 最後一刻的東京</h3>
    <ul>
      <li>早上 <strong>新宿御苑</strong> 散步（¥500），如果剛好是櫻花季或紅葉季，這裡比上野公園人少很多</li>
      <li>中午在 <strong>新宿歌舞伎町</strong> 吃 <strong>一蘭拉麵</strong>（新宿店24小時營業！），個人覺得一蘭被過度炒作，但沒吃過還是可以試一次</li>
      <li>下午 <strong>Don Quijote（唐吉訶德）</strong> 新宿本店瘋狂採購：藥妝、零食、電器用品，全部免稅</li>
      <li>16:00 前回到飯店拿行李，搭 <strong>Narita Express</strong> 或 <strong>Skyliner</strong> 到機場</li>
      <li>在成田/羽田機場最後領 <strong>Last call</strong>：用剩餘日圓買 <strong>Royce生巧克力</strong>（只有機場有賣）和 <strong>東京Banana</strong></li>
    </ul>
    <div class="tip-box">
      <strong>💡 個人觀點：</strong>最後一天不要安排太遠的地方，我上次因為去上野逛太久而錯過機場快車，差點沒趕上飛機。建議最後一天就待在飯店附近逛街，輕鬆一點。另外，如果你有剩餘的硬幣（日圓硬幣），可以在機場的 <strong>自動販賣機</strong> 買飲料喝完再安檢，日本安檢不能帶超過100ml液體上飛機。
    </div>
  </div>
"""

if insertion_point in content:
    idx = content.find(insertion_point)
    new_content = content[:idx] + day3_5_content + '\n' + content[idx:]
    
    with open('tokyo-5days.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ Day 3-5 插入成功！")
    print(f"   插入位置：第 {content[:idx].count(chr(10))+1} 行")
else:
    print("❌ 找不到插入點！")
    # Debug: show what's around the FAQ section
    idx = content.find('faq-section')
    if idx >= 0:
        print(f"   找到 faq-section 在位置 {idx}")
        print(f"   前50字：{content[max(0,idx-50):idx+50]}")
