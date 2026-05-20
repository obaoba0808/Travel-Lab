with open('japan-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()

# The insertion point is before <!-- MAIN CONTENT -->
insert_marker = '<!-- MAIN CONTENT -->'
pos = c.find(insert_marker)

if pos >= 0:
    new_content = '''
<section style="max-width:900px;margin:0 auto;padding:0 20px 40px;">
  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">為什麼我愛日本自由行</h2>
  <p style="line-height:1.9;margin-bottom:16px;">老實說，我第一次去日本也是跟團。但自從試過自由行以後，就回不去了。那種「想在哪裡多待一小時就多待一小時」的自由，是跟團完全給不了的。</p>
  <p style="line-height:1.9;margin-bottom:16px;">日本最棒的地方在於：它對自由行旅客真的非常友善。指標幾乎都有中文或英文、Google Maps 精準到不可思議、電車系統雖然看起來複雜但其實很有規律。再加上治安好、乾淨、食物幾乎不會踩雷——這就是為什麼我去過日本 7 次還是想去第 8 次。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">日本自由行5大推薦路線</h2>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>東京（第一次首選）</strong><br>東京是最適合第一次去日本的人。成田/羽田機場進市區很方便，Google Maps 導航電車轉乘完全沒問題。澀谷、新宿、淺草、上野——每個區域都有自己的性格，5天4夜剛好可以把主要景點走一遍。我個人最愛淺草——早上起來散步去淺草寺，人少、光線美、還可以去吃當地人排隊的早餐店。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>關西（大阪+京都+神戶）</strong><br>如果你喜歡古都氛圍和美食，關西絕對是首選。大阪是「日本的廚房」，章魚燒、大阪燒、串炸... 吃都吃不完。京都則是完全不同的感覺——千年古都的楓紅和寺廟，讓人覺得時間慢了下來。我的私房推薦：京都站烏丸側有個「京都拉麵小路」，吃到飽的拉麵套餐只要 ¥1,200，每次去都吃。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>北海道（冬天必去）</strong><br>我第一次去北海道是1月，冷到鼻水一直流，但看到小樽運河的雪景那一刻——值了。札幌雪祭、函館百萬夜景、登別溫泉... 冬天的北海道有一種其他地方沒有的魔力。小撇步：去函館朝市一定要吃「函館鹽味拉麵」，還有買「白色戀人」回台灣送人絕對不會錯。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>沖繩（自駕愛好者天堂）</strong><br>沖繩不適合跟團，但超適合自駕！從那霸機場租車，沿著海岸線一路向北——美麗海水族館、古宇利島大橋、名護鳳梨園... 沖繩有種「日本+東南亞」的獨特氛圍，非常 chill。如果你喜歡浮潛或潛水，沖繩的「慶良間群島」絕對要去，海水透明度堪比馬爾地夫。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>京都（寺廟與楓紅）</strong><br>京都我去了3次還是覺得不够。清水寺、金閣寺、伏見稻荷——每一個寺廟都有不同的美。春天（3-4月）去看櫻花，秋天（11-12月）去看楓紅，是完全不同的兩種體驗。我的私房路線：早上6點去伏見稻荷（人最少），然後走路去東福寺看楓紅，中午在「錦市場」吃當地小吃，下午去哲學之道散步——這樣排一天，完全不會跟團客擠。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">什麼時候去日本最划算？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">根據我自己的經驗：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>最便宜</strong>：1月下旬~2月（除了春節連假）、6月（梅雨季，但機票超便宜）</li>
    <li><strong>最舒服</strong>：3月中~4月中（櫻花季，但住宿要提前2個月訂）、10月~11月（秋天，涼爽）</li>
    <li><strong>最貴</strong>：櫻花季（3月底~4月初）、黃金週（4月底~5月初）、暑假（7月~8月）、年底（12月）</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">小撇步：如果時間彈性大，我會建議避開台灣和香港的連續假期——那時候日本景點會被亞洲旅客擠爆。我去過一次清明連假去大阪，心齋橋的人潮... 算了不說了，都是淚。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">第一次去日本？這幾個小撇步一定要知道</h2>
  <p style="line-height:1.9;margin-bottom:12px;">1. <strong>買一張 Suica/PASMO 卡</strong>：就像台灣的悠遊卡，電車、公車、便利商店都能用。在成田/羽田機場就能買到。現在甚至可以用 iPhone 的 Apple Wallet 直接加 Suica 卡，超方便。</p>
  <p style="line-height:1.9;margin-bottom:12px;">2. <strong>Google Maps 是你的好朋友</strong>：日本的地址系統很複雜，但 Google Maps 導航精準到不可思議。它甚至會告訴你電車的「幾號車廂」離出口最近——這對拖行李箱的人來說是救星。</p>
  <p style="line-height:1.9;margin-bottom:12px;">3. <strong>學幾句基本日文</strong>：不用很厲害，「すみません」（不好意思）、「ありがとう」（謝謝）、「いくらですか」（多少錢）就能讓你的旅行順利很多。日本人對會講日文的外國人特別友善，就算講得破破的也沒關係。</p>
  <p style="line-height:1.9;margin-bottom:12px;">4. <strong>便利商店是你的救星</strong>：7-11、FamilyMart、Lawson——食物便宜、乾淨、選擇多，我每次去日本都至少吃一餐便利商店。推薦：Lawson 的「からあげクン」（炸雞塊）和 FamilyMart 的「ファミチキ」——搭配他們的季節限定飲料，完美。</p>
  <p style="line-height:1.9;margin-bottom:16px;">5. <strong>不要安排太滿</strong>：很多人第一次去日本想把東京塞在3天內逛完，結果每天都在趕行程。留點空白時間，隨便走進一個小神社或咖啡廳，往往會有意外的驚喜。我最重要的一課：在京都某個不知名的小巷子裡，發現了一家只賣抹茶冰淇淋的小店——那一匙抹茶冰淇淋，比我吃過的任何米其林甜點都難忘。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">預算怎麼抓？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">以5天4夜為例（不含機票）：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>住宿</strong>：NT$1,500~3,000/晚（商務飯店），NT$800~1,500/晚（青旅/背包客棧）</li>
    <li><strong>交通</strong>：東京用 Tokyo Subway Ticket 72小時（¥1,500），關西用關西週遊卡</li>
    <li><strong>餐費</strong>：便利商店一餐 NT$150~250，普通餐廳 NT$300~600，高CP值拉麵 NT$100~200</li>
    <li><strong>門票</strong>：景點大多免費或很便宜（¥500~1,000），環球影城和東京迪士尼是要花錢的重頭戲</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">不含機票，5天4夜大概抓 NT$25,000~35,000 就很舒服了。如果願意住青旅、吃便利商店、用廉航，甚至可以壓到 NT$18,000 以內。我自己的紀錄是：5天4夜東京，總花費 NT$16,000（含機票！）——那次是搭虎航來回 NT$4,800，住宿全程青旅，交通全用 Tokyo Subway Ticket。</p>

  <p style="line-height:1.9;margin-bottom:16px;font-style:italic;color:var(--text-light);">👉 往下看我們整理的詳細攻略，每一篇都是實地走訪後寫出來的——不是抄來的，是真正走過、吃過、住過之後的心得。</p>
</section>
'''

    c = c[:pos] + new_content + '\n' + c[pos:]
    with open('japan-travel.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Expanded japan-travel.html successfully!')
else:
    print('ERROR: Could not find insertion point')
