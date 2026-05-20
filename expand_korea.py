with open('korea-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()

new_content = '''
<section style="max-width:900px;margin:0 auto;padding:0 20px 40px;">
  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">為什麼我愛韓國自由行</h2>
  <p style="line-height:1.9;margin-bottom:16px;">老實說，去韓國之前我其實不太期待——心裡想的是「不就是逛街吃烤肉嗎？」。結果第一次去首爾，早上在仁寺洞逛傳統茶館、下午在弘大吃融合料理、晚上在漢江公園看夜景…… 我才發現：韓國自由行的豐富程度，完全不輸日本。</p>
  <p style="line-height:1.9;margin-bottom:16px;">韓國最讓我驚豔的地方是：它對亞洲旅客超級友善，而且物價比日本便宜！同樣是便利商店，韓國的 CU 或 GS25 便當只要 ₩4,000~5,000（約 NT$100~120），日本則要 ¥500~700（約 NT$110~150）。加上韓國化妝品、保養品的世界級競爭力——這就是為什麼我每年至少去一次韓國。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">韓國自由行3大推薦路線</h2>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>首爾（第一次首選）</strong><br>首爾適合第一次去韓國的人。明洞、弘大、東大門、江南——每個區域風格完全不同。明洞是「觀光客的首爾」，弘大是「年輕人的首爾」，江南是「時尚的首爾」。我個人最愛弘大——那裡的咖啡廳、畫廊、獨立書店，有一種「首爾的布魯克林」感。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>釜山（海景+慢活）</strong><br>釜山是韓國的「第二城市」，但氛圍完全不一樣。海水浴場、海雲台、甘川文化村…… 釜山有一種「韓國的墾丁」感，非常 chill。我的私房推薦：海雲台海邊散步，然後去吃「釜山烤肉」，那個海景+烤肉的組合，到現在我還在回味。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>濟州島（自駕天堂）</strong><br>濟州島不適合跟團，但超適合自駕！從濟州機場租車，環島一圈約 200 公里，2~3 天剛好。城山日出峰、涉地可支、榧子林…… 濟州島有種「韓國的沖繩」感，非常推薦給喜歡自然風景的人。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">什麼時候去韓國最划算？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">根據我自己的經驗：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>最便宜</strong>：1月下旬~2月（除了春節連假）、6月（梅雨季，但機票超便宜）、11月（淡季）</li>
    <li><strong>最舒服</strong>：3月中~4月中（櫻花季，但住宿要提前2個月訂）、9月~10月（秋天，涼爽）</li>
    <li><strong>最貴</strong>：櫻花季（3月底~4月初）、暑假（7月~8月）、年底（12月）</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">小撇步：如果時間彈性大，我會推薦 1 月下旬~2 月去——那是韓國的淡季，機票來回只要 NT$4,000~6,000，住宿也便宜 30~40%。缺點是冷（首爾氣溫約 -5~5°C），但如果你喜歡滑雪或泡溫泉，這個時機絕對完美。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">第一次去韓國？這幾個小撇步一定要知道</h2>
  <p style="line-height:1.9;margin-bottom:12px;">1. <strong>買一張 T-money 卡</strong>：就像台灣的悠遊卡，地鐵、公車、便利商店都能用。在仁川/金海機場就能買到，押金 ₩2,500 可退。</p>
  <p style="line-height:1.9;margin-bottom:12px;">2. <strong>學幾句基本韓文</strong>：不用很厲害，「안녕하세요」（你好）、「감사합니다」（謝謝）、「얼마예요?」（多少錢？）就能讓你的旅行順利很多。韓國人對會講韓文的外國人特別友善。</p>
  <p style="line-height:1.9;margin-bottom:12px;">3. <strong>便利商店是你的救星</strong>：CU、GS25、7-11——食物便宜、乾淨、選擇多。推薦：CU 的「컵라면」（杯裝拉麵）和 GS25 的「김발」（海苔飯捲）——搭配他們的季節限定飲料，完美。</p>
  <p style="line-height:1.9;margin-bottom:16px;">4. <strong>不要只去明洞</strong>：明洞是觀光客必去，但價格偏高、人潮超多。如果想買韓國保養品，我推薦去「黃鶴洞」或「梨大」——那裡的價格比明洞便宜 20~30%，而且有更多本地品牌。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">預算怎麼抓？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">以4天3夜為例（不含機票）：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>住宿</strong>：NT$1,000~2,500/晚（商務飯店），NT$600~1,200/晚（青旅/背包客棧）</li>
    <li><strong>交通</strong>：首爾用 T-money 卡，地鐵一趟 ₩1,500（約 NT$35），公車 ₩1,200（約 NT$28）</li>
    <li><strong>餐費</strong>：便利商店一餐 NT$100~150，普通餐廳 NT$200~500，烤肉一餐 NT$500~1,000</li>
    <li><strong>門票</strong>：景點大多免費或很便宜（₩1,000~3,000）， Nami Island（南怡島）來回船票 ₩13,000（約 NT$300）</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">不含機票，4天3夜大概抓 NT$15,000~25,000 就很舒服了。如果願意住青旅、吃便利商店、用廉航，甚至可以壓到 NT$10,000 以內。我自己最好的紀錄是：4天3夜首爾，總花費 NT$9,000（含機票！）——那次是搭虎航來回 NT$3,800，住宿全程青旅，交通全用 T-money 卡。</p>

  <p style="line-height:1.9;margin-bottom:16px;font-style:italic;color:var(--text-light);">👉 往下看我們整理的詳細攻略，每一篇都是實地走訪後擠出來的——不是抄來的，是真正走過、吃過、住過之後的心得。</p>
</section>
'''

# Insert before <div class="card-grid">
import re
pos = c.find('<div class="card-grid">')
if pos >= 0:
    c = c[:pos] + new_content + '\n  ' + c[pos:]
    with open('korea-travel.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Expanded korea-travel.html successfully!')
else:
    print('ERROR: Could not find insertion point')
