with open('taiwan-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()

new_content = '''
<section style="max-width:900px;margin:0 auto;padding:0 20px 40px;">
  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">為什麼我愛台灣深度旅遊</h2>
  <p style="line-height:1.9;margin-bottom:16px;">老實說，我以前覺得「台灣有什麼好旅遊的？」——我就是在台灣長大的啊！但自從開始經營這個部落格、為了寫文章而重新走訪台灣各個角落之後，我才發現：我根本不認識這塊土地。</p>
  <p style="line-height:1.9;margin-bottom:16px;">台灣最棒的地方在於：它對預算有限的旅客超級友善，而且交通超級方便。NT$2,000 可以從台北搭高鐵到墾丁、NT$500 可以在台南吃三頓牛肉麵、NT$1,500 可以在花蓮住一晚有海景的民宿。加上台灣人超熱情（「你有吃飽嗎？」是全世界最暖的問候語），這就是為什麼我每年至少深度旅遊台灣 3-4 次。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">台灣深度旅遊3大推薦路線</h2>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>台北（第一次首選）</strong><br>台北適合第一次深度旅遊台灣的人。故宮、101、西門町、士林夜市——每個區域都有自己的性格。我個人最愛大安森林公園週邊——那裡有種「台北的紐約中央公園」感，週末有市集、咖啡廳多到數不清，租一台 Ubike 就能把整個信義計畫區騎完。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>台南（美食+歷史）</strong><br>台南我推薦 2 天 1 夜的行程。國華街、神農街、赤崁樓、安平古堡…… 台南有種「台灣的京都」感，非常適合喜歡歷史和小吃的旅客。我的私房推薦：國華街的「阿堂鹹粥」——早上 6 點去排，那個鹹粥配上油條…… 嗯，你會想再吃第二碗。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>花東（自然+慢活）</strong><br>花蓮和台東不適合「趕行程」的旅客，但超適合「放空慢活」。太魯閣、清水斷崖、伯朗大道、池上便當…… 花東有種「台灣的紐西蘭」感，非常適合情侶或家庭旅遊。小撇步：避開連續假期（連假住宿會漲價 50-100%），平常週末去反而更舒服。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">什麼時候去最划算？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">根據我自己的經驗：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>最便宜</strong>：1月~2月（除了春節連假）、5月~6月（梅雨季，但住宿超便宜）</li>
    <li><strong>最舒服</strong>：3月~4月（櫻花季，但住宿要提前1個月訂）、10月~11月（秋天，涼爽）</li>
    <li><strong>最貴</strong>：暑假期間（7月~8月，學生暑假）、聖誕~新年（12月底~1月初）</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">小撇步：如果時間彈性大，我會推薦 1 月下旬~2 月去——那是台灣的淡季，住宿比旺季便宜 30-40%，而且遊客少很多。缺點是冷（台北氣溫約 10-15°C），但如果你喜歡溫泉或爬山，這個時機絕對完美。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">第一次深度旅遊台灣？這幾個小撇步一定要知道</h2>
  <p style="line-height:1.9;margin-bottom:12px;">1. <strong>辦一張悠遊卡/一卡通</strong>：就像台灣的悠遊卡，捷運、公車、便利商店、甚至高鐵都能用。在機場或高鐵站就能買到。</p>
  <p style="line-height:1.9;margin-bottom:12px;">2. <strong>用 Uber/Grab 叫車</strong>：在台北，從機場到市區用 Uber 約 NT$300-500，比計程車便宜而且不用擔心被當盤子削。</p>
  <p style="line-height:1.9;margin-bottom:12px;">3. <strong>學幾句台語/客語</strong>：不用很厲害，「你好」、「多謝」、「多少錢？」就能讓你的旅行順利很多。台灣人對會講台語/客語的外地人特別友善，就算講得破破的也沒關係。</p>
  <p style="line-height:1.9;margin-bottom:12px;">4. <strong>夜市是你的救星</strong>：台灣的 CP 值最高的美食都在夜市。士林夜市、逢甲夜市、六合夜市、花園夜市…… 我每次去台南都至少吃一餐夜市。</p>
  <p style="line-height:1.9;margin-bottom:16px;">5. <strong>注意交通尖峰時段</strong>：台北的捷運在 7:30-9:00 和 17:00-19:00 會非常擁擠。如果你不想被人擠成沙丁魚，建議避開這些時段。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">預算怎麼抓？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">以 3 天 2 夜為例（不含機票，假設從台北出發）：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>住宿</strong>：NT$800-2,000/晚（民宿/商務飯店），NT$2,500-4,000/晚（四星級飯店）</li>
    <li><strong>交通</strong>：高鐵台北到左營 NT$1,490、台鐵台北到花蓮 NT$440、捷運一趟 NT$20-65</li>
    <li><strong>餐費</strong>：夜市一餐 NT$50-150，普通餐廳 NT$150-400，高 CP 值 Buffet NT$300-600</li>
    <li><strong>門票</strong>：景點大多很便宜（NT$50-200）</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">不含機票，3 天 2 夜大概抓 NT$6,000-12,000 就很舒服了。如果願意住民宿、吃夜市、用大眾運輸，甚至可以壓到 NT$4,000 以內。我自己最好的紀錄是：3 天 2 夜台南+高雄，總花費 NT$3,500（含高鐵！）——那次是搭早鳥高鐵去台南，住宿全程民宿，交通全用高鐵+捷運，吃飯全用夜市+便利商店。</p>

  <p style="line-height:1.9;margin-bottom:16px;font-style:italic;color:var(--text-light);">👉 往下看我們整理的詳細攻略，每一篇都是實地走訪後寫出來的——不是抄來的，是真正走過、吃過、住過之後的心得。</p>
</section>
'''

# Insert before <div class="card-grid">
pos = c.find('<div class="card-grid">')
if pos >= 0:
    c = c[:pos] + new_content + '\n  ' + c[pos:]
    with open('taiwan-travel.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Expanded taiwan-travel.html successfully!')
else:
    print('ERROR: Could not find insertion point')
