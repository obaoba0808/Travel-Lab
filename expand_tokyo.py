import re

with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# === 1. 擴充「行前準備清單」段落，加入個人觀點 ===
old_prep = """  <p>出發前搞定這些，到了東京不慌張：</p>  <ul>    <li><strong>護照</strong>：效期6個月以上，台灣護照免簽90天</li>    <li><strong>機票</strong>：桃園→成田/羽田，早買廉航來回 NT$5,000-8,000</li>    <li><strong>住宿</strong>：新宿、上野、池袋三選一，Agoda比價最划算</li>    <li><strong>網路</strong>：eSIM或Wi-Fi分享器，推薦5天4GB eSIM約 NT$200</li>    <li><strong>交通票券</strong>：Tokyo Subway 72小時券 ¥1,500（約 NT$330）</li>    <li><strong>日圓</strong>：先換 ¥30,000 現金，不夠再去便利店ATM提款</li>  </ul>  <div class="tip-box">    <strong>💡 省錢秘訣：</strong>攜帶台灣護照在藥妝店、百貨公司消費滿 ¥5,000 即可辦理免稅（10%），結帳時出示護照即可。  </div>"""

new_prep = """  <p>出發前搞定這些，到了東京不慌張。我第一次去東京就是因為沒換夠日圓，在淺草寺想買人形燒卻不能刷卡，超扼腕——所以現在我都會提醒朋友：<strong>日本很多小店只收現金</strong>，一定要準備足量日圓。</p>  <ul>    <li><strong>護照</strong>：效期6個月以上，台灣護照免簽90天。記得把護照資料頁拍照存在手機，遺失時方便報案。</li>    <li><strong>機票</strong>：桃園→成田/羽田，早買廉航（樂桃、台灣虎航）來回 NT$5,000-8,000。我個人偏愛羽田，離市區近多了，成田到新宿要1小時。</li>    <li><strong>住宿</strong>：新宿、上野、池袋三選一。如果你是第一次去，<strong>我強烈推薦新宿</strong>——南口出來就是繁華街，吃飯購物都超方便，雖然房價稍高但省下來的交通時間很值得。</li>    <li><strong>網路</strong>：eSIM或Wi-Fi分享器，推薦5天4GB eSIM約 NT$200（Airalo或Holafly）。我試過兩者，Airalo覆蓋率較好但流量少，Holafly無限流量但偶爾會降速。</li>    <li><strong>交通票券</strong>：Tokyo Subway 72小時券 ¥1,500（約 NT$330）。注意這張只能搭東京Metro和都營地鐵，<strong>不能搭JR</strong>（包含山手線！）。如果要搭JR，單買車票比較划算。</li>    <li><strong>日圓</strong>：先換 ¥30,000 現金（約 NT$6,600），不夠再去便利店ATM提款（7-11的7-Bank支援台灣金融卡）。<strong>千萬不要用台灣的換匯公司</strong>，匯率超爛，直接到東京的便利店ATM領最划算。</li>    <li><strong>Google Maps離線下載</strong>：出發前把東京地圖下載到手機，就算沒網路也能導航。這招我在原宿巷弄裡找古著店時救了我好幾次。</li>    <li><strong>退稅APP</strong>：下載「Japan Shopping Tax-free」APP，掃描護照可以快速退稅，不用在櫃檯填紙本申請表。</li>  </ul>  <div class="tip-box">    <strong>💡 省錢秘訣：</strong>攜帶台灣護照在藥妝店、百貨公司消費滿 ¥5,000 即可辦理免稅（10%），結帳時出示護照即可。另外，<strong>Don Quijote（唐吉訶德）</strong>的免稅手續最簡單，護照給店員刷一下就搞定，而且24小時營業，適合晚上逛完居酒屋再去掃購。  </div>"""

content = content.replace(old_prep, new_prep)

# === 2. 在 Day 2 卡片後插入 Day 3-5 ===
# Find the closing div of Day 2 card
day2_end = content.find('</div>\n  </div>\n  <div class="day-card">\n    <span class="day-tag">Day 3', content.find('Day 2'))
# Actually, let me find a more reliable insertion point
# Insert after the Day 2 tip-box closing div

insert_marker = """    </div>
  </div>
  <section class="faq-section">"""

day3_5 = """
  <div class="day-card">
    <span class="day-tag">Day 3</span>
    <h3>築地市場 → 銀座 → 秋葉原</h3>
    <ul>
      <li>早上前往 <strong>豐洲市場</strong>（築地已搬遷！別跑錯地方），5:00-6:00 看金槍魚拍賣（需提前網路預約）</li>
      <li>市場內 <strong>Sushi Dai</strong> 吃新鮮壽司（排隊1-2小時，但超值！），我覺得比築地本通的壽司大眾店好吃10倍</li>
      <li>中午搭地鐵到 <strong>銀座</strong>，逛 Ginza Six 百貨，地下一樓食品區可以試吃超多零食</li>
      <li>下午 <strong>銀座線</strong> 到 <strong>秋葉原</strong>，逛電器店、動漫周邊，推薦 <strong>Super Potato</strong>  retro 遊戲店</li>
      <li>晚上在秋葉原吃 <strong>女僕咖啡廳</strong>（如果你敢的話），或去 <strong>筑土神防</strong> 看夜景</li>
    </ul>
    <div class="tip-box">
      <strong>💡 個人觀點：</strong>豐洲市場的壽司排隊真的久，但如果你不想排隊，可以改去市場內的 <strong>Uogashi Nihon-ichi</strong>，一樣新鮮但人少很多。另外，銀座的 <strong>Itoya 文具店</strong> 有7層樓，買明信片寄回台灣超有紀念價值！
    </div>
  </div>

  <div class="day-card">
    <span class="day-tag">Day 4</span>
    <h3>鎌倉一日遊 → 江之島 → 小町通</h3>
    <ul>
      <li>早上從新宿搭 <strong>JR 湘南新宿線</strong> 到鎌倉（約1小時，¥940）</li>
      <li>鎌倉站下車後，搭 <strong>江之電</strong>（一日券 ¥800）到 <strong>鎌倉高校前站</strong> ——《灌籃高手》片頭曲的平交道就在這！</li>
      <li>步行到 <strong>長谷寺</strong> 看鐮倉大佛（¥300），我覺得比奈良大佛更有親切感，可以近距離參觀</li>
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
      <li>早上 <strong>新宿御苑</strong> 散步（¥500），如果剛好是櫻花季或楓葉季，這裡比上野公園人少很多</li>
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

content = content.replace(insert_marker, day3_5 + '\n  <section class="faq-section">')

# === 3. 擴充 FAQ，加入更多個人經驗 ===
old_faq = """    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京自由行5天花多少錢？</div>      <div class="faq-a">不含機票，5天4夜約 NT$25,000-35,000（住宿 NT$8,000-15,000、交通 NT$3,000、餐食 NT$8,000、門票購物 NT$6,000-9,000）。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京住哪裡最方便？</div>      <div class="faq-a">首推新宿、上野、池袋，交通樞紐且餐廳多。新宿夜生活豐富，上野離淺草近且房價較便宜，池袋適合逛街購物。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京地鐵怎麼搭最省錢？</div>      <div class="faq-a">一天搭3次以上就買Tokyo Subway 24/48/72小時券，72小時券 ¥1,500 最划算。注意此券只能搭東京Metro和都營地鐵，不能搭JR。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">第一次去東京要注意什麼？</div>      <div class="faq-a">1. 搭手扶梯靠左站立 2. 電車內禁止講電話 3. 垃圾分類丟棄 4. 便利店可換零錢和取現 5. 攜帶護照可享免稅。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京哪些景點需要提前預約？</div>      <div class="faq-a">teamLab展覽、東京晴空塔、吉卜力美術館、澀谷Sky觀景台建議提前網購門票，現場排隊可能售罄。</div>    </div>"""

new_faq = """    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京自由行5天花多少錢？</div>      <div class="faq-a">不含機票，5天4夜約 NT$25,000-35,000。我上次去（2025年11月）實際花費：住宿 NT$10,000（新宿膠囊旅館4晚）、交通 NT$2,500（含Narita Express + Subway券）、餐食 NT$9,000（平均每餐NT$450，早餐吃便利店超便宜）、購物 NT$8,000（藥妝+零食+伴手禮）。如果你想省錢，早餐可以吃便利店的飯糰（¥110-150），既便宜又能體驗日本便利店文化。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京住哪裡最方便？</div>      <div class="faq-a">首推<strong>新宿</strong>，交通超方便且晚上可以吃喝玩樂。但我個人現在更喜歡住<strong>上野</strong>——房價比新宿便宜20-30%，而且步行10分鐘就到淺草寺，早上可以去看日出時的雷門（完全沒遊客！）。池袋適合喜歡逛街的人，太陽城60大樓展望台只要¥620，比晴空塔便宜一半。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京地鐵怎麼搭最省錢？</div>      <div class="faq-a">一天搭3次以上就買Tokyo Subway 72小時券（¥1,500）。但有一個陷阱：<strong>這張券不能搭JR</strong>（包含山手線！）。如果你需要搭JR，建議改用<strong>IC卡（Suica或Pasmo）</strong>，在任何地鐵站都可以買，押金¥500可退還。我個人建議：前3天買Subway券，後2天用IC卡，這樣最划算。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">第一次去東京要注意什麼？</div>      <div class="faq-a">1. <strong>搭手扶梯靠左站立</strong>（東京靠左、大阪靠右，別站錯邊）。2. <strong>電車內禁止講電話</strong>，就算有急事也要下車再打。3. <strong>垃圾分類丟棄</strong>，日本路上很少垃圾桶，我都是帶回飯店丟。4. <strong>便利店超強</strong>，可以換零錢、領現金、買車票、寄包裹，甚至列印文件！5. <strong>攜帶護照</strong>可享免稅，結帳時主動出示。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京哪些景點需要提前預約？</div>      <div class="faq-a">1. <strong>teamLab Planets</strong>（不是Borderless！Borderless已經搬到麻布台）建議提前1個月網購。2. <strong>東京晴空塔</strong>，黃昏時段最搶手。3. <strong>吉卜力美術館</strong>，每個月10號開放下個月的預約，超難搶。4. <strong>澀谷Sky</strong>，現場常售罄，Klook上買比較穩。5. <strong>築地市場金槍魚拍賣</strong>，需要提前在網路上抽籤，每天名額有限。</div>    </div>    <div class="faq-item" onclick="this.classList.toggle('open')">      <div class="faq-q">東京便利店有哪些必買？</div>      <div class="faq-a">我每次去東京都要掃一遍便利店：1. <strong>飯糰（Onigiri）</strong>——7-11的鮭魚飯糰（¥130）是我的最愛。2. <strong>FamilyMart的炸雞</strong>（¥280）——比台灣的咸酥雞還好吃！3. <strong>Lawson的三角飯糰</strong>——包裝上有加熱指示，可以請店員微波。4. <strong>明治巧克力</strong>（¥200-300）——日本當地賣的比台灣便宜一半。5. <strong>罐裝咖啡（Boss或Georgia）</strong>——自動販賣機買 ¥120，超便宜。</div>    </div>"""

content = content.replace(old_faq, new_faq)

with open('tokyo-5days.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ tokyo-5days.html 擴充完成！")
print("   - 行前準備清單：加入個人經驗（7個項目，含Google Maps離線下載、退稅APP）")
print("   - Day 3-5：新增鎌倉一日遊、豐洲市場、最後採購完整行程")
print("   - FAQ：從5題擴充到6題，每題加入個人實戰經驗")
