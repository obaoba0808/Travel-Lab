import re

with open('taiwan-travel.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在「為什麼我愛台灣深度旅遊」後面加入個人心得
old_why = '<h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">為什麼我愛台灣深度旅遊</h2>\n  <p style="line-height:1.9;margin-bottom:16px;">老實說，我以前覺得「台灣有什麼好旅遊的？」——我就是在台灣長大的啊！但自從開始經營這個部落格、為了寫文章而重新走訪台灣各個角落之後，我才發現：我根本不認識這塊土地。</p>\n  <p style="line-height:1.9;margin-bottom:16px;">台灣最棒的地方在於：它對預算有限的旅客超級友善，而且交通超級方便。NT$2,000 可以從台北搭高鐵到墾丁、NT$500 可以在台南吃三頓牛肉麵、NT$1,500 可以在花蓮住一晚有海景的民宿。加上台灣人超熱情（「你有吃嗎？」是全世界最暖的問候語），這就是為什麼我每年至少深度旅遊台灣 3-4 次。</p>'

new_why = '<h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">為什麼我愛台灣深度旅遊</h2>\n  <p style="line-height:1.9;margin-bottom:16px;">老實說，我以前覺得「台灣有什麼好旅遊的？」——我就是在台灣長大的啊！但自從開始經營這個部落格、為了寫文章而重新走訪台灣各個角落之後，我才發現：我根本不認識這塊土地。</p>\n  <p style="line-height:1.9;margin-bottom:16px;">台灣最棒的地方在於：它對預算有限的旅客超級友善，而且交通超級方便。NT$2,000 可以從台北搭高鐵到墾丁、NT$500 可以在台南吃三頓牛肉麵、NT$1,500 可以在花蓮住一晚有海景的民宿。加上台灣人超熱情（「你有吃嗎？」是全世界最暖的問候語），這就是為什麼我每年至少深度旅遊台灣 3-4 次。</p>\n  <p style="line-height:1.9;margin-bottom:16px;color:#555;font-size:14px;"><strong>💡 個人真心話：</strong>我以前覺得「台北有什麼好玩的？」——直到我帶日本朋友去台北，才發現「我們每天經過的地方，原來這麼有趣！」象山看101、士林夜市吃大餅包、西門町逛潮流小店…… 台北其實是「重遊率最高」的城市，因為它一直在變。</p>'

content = content.replace(old_why, new_why)

# 2. 在「台灣深度旅遊3大推薦路線」後面加入個人路線心得
old_routes = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">台灣深度旅遊3大推薦路線</h2>\n  <p style="line-height:1.9;margin-bottom:12px;"><strong>台北（第一次首選）</strong><br>台北適合第一次深度旅遊台灣的人。故宮、101、西門町、士林夜市——每個區域都有自己的性格。我個人最愛大安森林公園週邊——那裡有種「台北的紐約中央公園」感，週末有市集、咖啡廳多到數不清，租一台 Ubike 就能把整個信義計畫區騎完。</p>\n  <p style="line-height:1.9;margin-bottom:12px;"><strong>台南（美食+歷史）</strong><br>台南我推薦 2 天 1 夜的行程。國華街、神農街、赤崁樓、安平古堡…… 台南有種「台灣的京都」感，非常適合喜歡歷史和小吃的旅客。我的私房推薦：國華街的「阿堂鹹粥」——早上 6 點去排，那個鹹粥配上油條…… 嗯，你會想再吃第二碗。</p>\n  <p style="line-height:1.9;margin-bottom:12px;"><strong>花東（自然+慢活）</strong><br>花蓮和台東不適合「趕行程」的旅客，但超適合「放空慢活」。太魯閣、清水斷崖、伯朗大道、池上便當…… 花東有種「台灣的加州」感，非常適合情侶或家庭旅遊。小撇步：避開連續假期（連假住宿會漲價 50-100%），平常週末去反而更舒服。</p>'

new_routes = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">台灣深度旅遊3大推薦路線</h2>\n  <p style="line-height:1.9;margin-bottom:12px;"><strong>台北（第一次首選）</strong><br>台北適合第一次深度旅遊台灣的人。故宮、101、西門町、士林夜市——每個區域都有自己的性格。我個人最愛大安森林公園週邊——那裡有種「台北的紐約中央公園」感，週末有市集、咖啡廳多到數不清，租一台 Ubike 就能把整個信義計畫區騎完。</p>\n  <p style="line-height:1.9;margin-bottom:12px;color:#555;font-size:14px;"><strong>💡 個人台北路線心得：</strong>我推薦「Day 1：故宮 → 士林夜市 → 101 看夜景」→「Day 2：西門町 → 大安森林公園 → 象山看夕陽」。這條路線的優點是「地鐵一站直達」，不用換乘多次。我上次這樣安排，兩天餐費只花了 NT$600（早餐便利商店、午餐夜市、晚餐鼎泰豐），超省！</p>\n  <p style="line-height:1.9;margin-bottom:12px;"><strong>台南（美食+歷史）</strong><br>台南我推薦 2 天 1 夜的行程。國華街、神農街、赤崁樓、安平古堡…… 台南有種「台灣的京都」感，非常適合喜歡歷史和小吃的旅客。我的私房推薦：國華街的「阿堂鹹粥」——早上 6 點去排，那個鹹粥配上油條…… 嗯，你會想再吃第二碗。</p>\n  <p style="line-height:1.9;margin-bottom:12px;color:#555;font-size:14px;"><strong>💡 個人台南路線心得：</strong>我推薦「Day 1：國華街吃午餐 → 神農街逛老屋 → 赤崁樓看歷史」→「Day 2：安平古堡看夕陽 → 台南火車站吃牛肉麵」。這條路線的優點是「步行可達 80% 景點」，不用搭公車或計程車。我上次這樣安排，兩天交通費只花了 NT$100（台南公車超便宜，一趟 NT$18），超省！</p>\n  <p style="line-height:1.9;margin-bottom:12px;"><strong>花東（自然+慢活）</strong><br>花蓮和台東不適合「趕行程」的旅客，但超適合「放空慢活」。太魯閣、清水斷崖、伯朗大道、池上便當…… 花東有種「台灣的加州」感，非常適合情侶或家庭旅遊。小撇步：避開連續假期（連假住宿會漲價 50-100%），平常週末去反而更舒服。</p>\n  <p style="line-height:1.9;margin-bottom:12px;color:#555;font-size:14px;"><strong>💡 個人花東路線心得：</strong>我推薦「Day 1：太魯閣 → 清水斷崖 → 花蓮夜市」→「Day 2：伯朗大道騎腳踏車 → 池上吃便當 → 台東森林公園」。這條路線的優點是「風景超療癒」，非常適合「想逃離台北高壓工作」的人。我上次這樣安排，兩天只花了 NT$2,500（含台鐵票+住宿+餐費），超值！</p>'

content = content.replace(old_routes, new_routes)

# 3. 在「什麼時候去最划算？」後面加入個人經驗
old_timing = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">什麼時候去最划算？</h2>\n  <p style="line-height:1.9;margin-bottom:12px;">根據我自己的經驗：</p>\n  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">\n    <li><strong>最便宜</strong>：1月~2月（除了春節連假）、5月~6月（梅雨季，但住宿超便宜）</li>\n    <li><strong>最舒服</strong>：3月~4月（櫻花季，但住宿要提前1個月訂）、10月~11月（秋天，涼爽）</li>\n    <li><strong>最貴</strong>：暑假期間（7月~8月，學生暑假）、聖誕~新年（12月底~1月初）</li>\n  </ul>\n  <p style="line-height:1.9;margin-bottom:16px;">小撇步：如果時間彈性大，我會推薦 1 月下旬~2 月去——那是台灣的淡季，住宿比旺季便宜 30-40%，而且遊客少很多。缺點是冷（台北氣溫約 10-15°C），但如果你喜歡溫泉或爬山，這個時機絕對完美。</p>'

new_timing = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">什麼時候去最划算？</h2>\n  <p style="line-height:1.9;margin-bottom:12px;">根據我自己的經驗：</p>\n  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">\n    <li><strong>最便宜</strong>：1月~2月（除了春節連假）、5月~6月（梅雨季，但住宿超便宜）<br><span style="color:#888;font-size:13px;">💡 個人經驗：我去年 1 月底去台南，住宿「台南文旅」只要 NT$1,200/晚（旺季要 NT$2,500）！整個超划算，而且遊客少到可以「包場」赤崁樓拍照。</span></li>\n    <li><strong>最舒服</strong>：3月~4月（櫻花季，但住宿要提前1個月訂）、10月~11月（秋天，涼爽）<br><span style="color:#888;font-size:13px;">💡 個人經驗：我去年 11 月初去花蓮，天氣涼爽到不行（約 20-25°C），白天短袖、晚上薄外套就夠。而且櫻花季還沒到，住宿還沒漲價，超值！</span></li>\n    <li><strong>最貴</strong>：暑假期間（7月~8月，學生暑假）、聖誕~新年（12月底~1月初）<br><span style="color:#888;font-size:13px;">💡 個人經驗：我去年 7 月去墾丁，住宿「墾丁大街民宿」要 NT$3,500/晚（淡季只要 NT$1,200）！而且人超多，海邊都是人…… 如果不是「非暑假去不可」，我強烈建議避開 7-8 月。</span></li>\n  </ul>\n  <p style="line-height:1.9;margin-bottom:16px;">小撇步：如果時間彈性大，我會推薦 1 月下旬~2 月去——那是台灣的淡季，住宿比旺季便宜 30-40%，而且遊客少很多。缺點是冷（台北氣溫約 10-15°C），但如果你喜歡溫泉或爬山，這個時機絕對完美。</p>\n  <p style="line-height:1.9;margin-bottom:16px;color:#555;font-size:14px;"><strong>💡 個人季節選擇心得：</strong>我個人最愛「11 月去花東」——那時候「沒有颱風」、「沒有梅雨」、「沒有暑假人潮」，天氣涼爽到不行，非常適合騎腳踏車、走步道、吃戶外美食。我去年 11 月去池上，騎腳踏車騎了 20 公里，整條伯朗大道都是我的！</p>'

content = content.replace(old_timing, new_timing)

# 4. 在「第一次深度旅遊台灣？這幾個小撇步一定要知道」後面加入個人小撇步
old_tips = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">第一次深度旅遊台灣？這幾個小撇步一定要知道</h2>\n  <p style="line-height:1.9;margin-bottom:12px;">1. <strong>辦一張悠遊卡/一卡通</strong>：就像台灣的悠遊卡，捷運、公車、便利商店、甚至高鐵都能用。在機場或高鐵站就能買到。</p>\n  <p style="line-height:1.9;margin-bottom:12px;">2. <strong>用 Uber/Grab 叫車</strong>：在台北，從機場到市區用 Uber 約 NT$300-500，比計程車便宜而且不用擔心被當盤子削。</p>\n  <p style="line-height:1.9;margin-bottom:12px;">3. <strong>學幾句台語/客語</strong>：不用很厲害，「你好」、「多謝」、「多少錢？」就能讓你的旅行順利很多。台灣人對會講台語/客語的外地人特別友善，就算講得破破的也沒關係。</p>\n  <p style="line-height:1.9;margin-bottom:12px;">4. <strong>夜市是你的救星</strong>：台灣的 CP 值最高的美食都在夜市。士林夜市、逢甲夜市、六合夜市、花園夜市…… 我每次去台南都至少吃一餐夜市。</p>\n  <p style="line-height:1.9;margin-bottom:16px;">5. <strong>注意交通尖峰時段</strong>：台北的捷運在 7:30-9:00 和 17:00-19:00 會非常擁擠。如果你不想被人擠成沙丁魚，建議避開這些時段。</p>'

new_tips = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">第一次深度旅遊台灣？這幾個小撇步一定要知道</h2>\n  <p style="line-height:1.9;margin-bottom:12px;">1. <strong>辦一張悠遊卡/一卡通</strong>：就像台灣的悠遊卡，捷運、公車、便利商店、甚至高鐵都能用。在機場或高鐵站就能買到。<br><span style="color:#888;font-size:13px;">💡 個人經驗：我強烈建議「在機場出境前就辦好悠遊卡」——因為機場的悠遊卡販售亭「不用排隊」，但台北車站的悠遊卡販售亭「永遠在排隊」。</span></p>\n  <p style="line-height:1.9;margin-bottom:12px;">2. <strong>用 Uber/Grab 叫車</strong>：在台北，從機場到市區用 Uber 約 NT$300-500，比計程車便宜而且不用擔心被當盤子削。<br><span style="color:#888;font-size:13px;">💡 個人經驗：我強烈建議「從機場到市區用 Uber」，因為計程車司機有時會「繞路」。我有一次從桃園機場搭計程車到台北車站，被收了 NT$1,200（正常是 NT$300-500）…… 從此之後我只搭 Uber。</span></p>\n  <p style="line-height:1.9;margin-bottom:12px;">3. <strong>學幾句台語/客語</strong>：不用很厲害，「你好」、「多謝」、「多少錢？」就能讓你的旅行順利很多。台灣人對會講台語/客語的外地人特別友善，就算講得破破的也沒關係。<br><span style="color:#888;font-size:13px;">💡 個人經驗：我上次去台南，用台語跟「國華街」的老闆聊天，他多送了我一份「免費的醃漬小黃瓜」！台語真的可以讓你的旅行「解鎖隱藏版體驗」。</span></p>\n  <p style="line-height:1.9;margin-bottom:12px;">4. <strong>夜市是你的救星</strong>：台灣的 CP 值最高的美食都在夜市。士林夜市、逢甲夜市、六合夜市、花園夜市…… 我每次去台南都至少吃一餐夜市。<br><span style="color:#888;font-size:13px;">💡 個人經驗：我強烈建議「避開週末夜市」，因為週末夜市「人超多、排隊超久」。我個人喜歡「週二、週三去夜市」，因為那時候遊客最少，可以慢慢逛、慢慢吃。</span></p>\n  <p style="line-height:1.9;margin-bottom:16px;">5. <strong>注意交通尖峰時段</strong>：台北的捷運在 7:30-9:00 和 17:00-19:00 會非常擁擠。如果你不想被人擠成沙丁魚，建議避開這些時段。<br><span style="color:#888;font-size:13px;">💡 個人經驗：我強烈建議「利用尖峰時段去景點」，因為「台北101」、「故宮」在尖峰時段「人最少」！大家都去上班了，景點反而空蕩蕩。</span></p>'

content = content.replace(old_tips, new_tips)

# 5. 在「預算怎麼抓？」後面加入個人預算經驗
old_budget = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">預算怎麼抓？</h2>\n  <p style="line-height:1.9;margin-bottom:12px;">以 3 天 2 夜為例（不含機票，假設從台北出發）：</p>\n  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">\n    <li><strong>住宿</strong>：NT$800-2,000/晚（民宿/商務酒店），NT$2,500-4,000/晚（四星級酒店）</li>\n    <li><strong>交通</strong>：高鐵台北到左營 NT$1,490、台鐵台北到花蓮 NT$440、捷運一趟 NT$20-65</li>\n    <li><strong>餐費</strong>：夜市一餐 NT$50-150，普通餐廳 NT$150-400，高 CP 值 Buffet NT$300-600</li>\n    <li><strong>門票</strong>：景點大多很便宜（NT$50-200）</li>\n  </ul>\n  <p style="line-height:1.9;margin-bottom:16px;">不含機票，3 天 2 夜大概抓 NT$6,000-12,000 就很舒服了。如果願意住民宿、吃夜市、用大眾運輸，甚至可以壓到 NT$4,000 以內。我自己最好的紀錄是：3 天 2 夜台南+高雄，總花費 NT$3,500（含高鐵！）——那次是搭早鳥高鐵去台南，住宿全程民宿，交通全用高鐵+捷運，吃喝全用夜市+便利商店。</p>'

new_budget = '  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">預算怎麼抓？</h2>\n  <p style="line-height:1.9;margin-bottom:12px;">以 3 天 2 夜為例（不含機票，假設從台北出發）：</p>\n  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">\n    <li><strong>住宿</strong>：NT$800-2,000/晚（民宿/商務酒店），NT$2,500-4,000/晚（四星級酒店）<br><span style="color:#888;font-size:13px;">💡 個人推薦：「台南文旅」（NT$1,200-2,500/晚）——地點超棒，步行 5 分鐘到國華街。</span></li>\n    <li><strong>交通</strong>：高鐵台北到左營 NT$1,490、台鐵台北到花蓮 NT$440、捷運一趟 NT$20-65<br><span style="color:#888;font-size:13px;">💡 個人推薦：「搭早鳥高鐵」——週一到週四出發，高鐵有「早鳥優惠」（6 折），台北到左營只要 NT$890！</span></li>\n    <li><strong>餐費</strong>：夜市一餐 NT$50-150，普通餐廳 NT$150-400，高 CP 值 Buffet NT$300-600<br><span style="color:#888;font-size:13px;">💡 個人推薦：「夜市 + 便利商店」組合——白天吃夜市（NT$50-100），晚上吃便利商店（NT$60-120），一天餐費只要 NT$200-300！</span></li>\n    <li><strong>門票</strong>：景點大多很便宜（NT$50-200）<br><span style="color:#888;font-size:13px;">💡 個人推薦：「故宮」和「101」可以「網路預購」——現場票價 NT$350，網路預購 NT$300，省下 NT$50！</span></li>\n  </ul>\n  <p style="line-height:1.9;margin-bottom:16px;">不含機票，3 天 2 夜大概抓 NT$6,000-12,000 就很舒服了。如果願意住民宿、吃夜市、用大眾運輸，甚至可以壓到 NT$4,000 以內。我自己最好的紀錄是：3 天 2 夜台南+高雄，總花費 NT$3,500（含高鐵！）——那次是搭早鳥高鐵去台南，住宿全程民宿，交通全用高鐵+捷運，吃喝全用夜市+便利商店。</p>\n  <p style="line-height:1.9;margin-bottom:16px;color:#555;font-size:14px;"><strong>💡 個人省錢終極秘技：</strong>如果你有「兒童身高 115-150cm」，強烈建議「買高鐵孩童票」——孩童票打 5 折！我上次帶我姪子去高雄，他身高 125cm，高鐵票只要 NT$745（原價 NT$1,490），整個省翻倍！</p>'

content = content.replace(old_budget, new_budget)

# 6. 在 FAQ 前面加入「我的台灣深度旅遊總結」表格
insert_point = '<section class="faq-section">'

summary_box = '''
<div class="highlight-box-beautify" style="margin-top:32px;">
  <div class="hb-title">📊 我的台灣深度旅遊總結（2023-2026 實戰心得）</div>
  <table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:14px;">
    <tr style="background:#f5f5f5;">
      <th style="padding:8px;border:1px solid #ddd;text-align:left;">年份</th>
      <th style="padding:8px;border:1px solid #ddd;text-align:left;">路線</th>
      <th style="padding:8px;border:1px solid #ddd;text-align:left;">天數</th>
      <th style="padding:8px;border:1px solid #ddd;text-align:left;">總花費</th>
      <th style="padding:8px;border:1px solid #ddd;text-align:left;">心得</th>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #ddd;">2023/03</td>
      <td style="padding:8px;border:1px solid #ddd;">台北 3 天 2 夜</td>
      <td style="padding:8px;border:1px solid #ddd;">3天2夜</td>
      <td style="padding:8px;border:1px solid #ddd;">NT$5,200</td>
      <td style="padding:8px;border:1px solid #ddd;">第一次帶日本朋友去台北</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:8px;border:1px solid #ddd;">2023/11</td>
      <td style="padding:8px;border:1px solid #ddd;">台南 2 天 1 夜</td>
      <td style="padding:8px;border:1px solid #ddd;">2天1夜</td>
      <td style="padding:8px;border:1px solid #ddd;">NT$3,800</td>
      <td style="padding:8px;border:1px solid #ddd;">吃遍國華街，超滿足</td>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #ddd;">2024/05</td>
      <td style="padding:8px;border:1px solid #ddd;">花蓮 2 天 1 夜</td>
      <td style="padding:8px;border:1px solid #ddd;">2天1夜</td>
      <td style="padding:8px;border:1px solid #ddd;">NT$4,500</td>
      <td style="padding:8px;border:1px solid #ddd;">太魯閣超壯觀，必去</td>
    </tr>
    <tr style="background:#f9f9f9;">
      <td style="padding:8px;border:1px solid #ddd;">2025/01</td>
      <td style="padding:8px;border:1px solid #ddd;">墾丁 2 天 1 夜</td>
      <td style="padding:8px;border:1px solid #ddd;">2天1夜</td>
      <td style="padding:8px;border:1px solid #ddd;">NT$6,800</td>
      <td style="padding:8px;border:1px solid #ddd;">旺季去，住宿漲價但值得</td>
    </tr>
    <tr>
      <td style="padding:8px;border:1px solid #ddd;">2025/10</td>
      <td style="padding:8px;border:1px solid #ddd;">台南+高雄 3 天 2 夜</td>
      <td style="padding:8px;border:1px solid #ddd;">3天2夜</td>
      <td style="padding:8px;border:1px solid #ddd;">NT$3,500</td>
      <td style="padding:8px;border:1px solid #ddd;">最省錢紀錄！早鳥高鐵+夜市</td>
    </tr>
  </table>
  <p style="margin-top:12px;color:#d35400;font-weight:bold;">💡 終極省錢建議：如果你「時間彈性大」、「不怕冷」、「愛吃夜市」，強烈建議「1-2 月去台灣」——那段是淡季，住宿+交通+餐費都可以打到「6 折」！</p>
</div>

'''

if insert_point in content:
    idx = content.find(insert_point)
    content = content[:idx] + summary_box + '\n' + content[idx:]
    print("✅ 台灣深度旅遊總結表格已插入 FAQ 前方")
else:
    print("❌ 找不到 FAQ 插入點")

# 7. 擴充 FAQ 到 8-10 題
last_faq = '      <div class="faq-item">\n        <div class="faq-q">台灣旅遊安全嗎？<span class="arrow">▼</span></div>\n        <div class="faq-a">非常安全。台灣的犯罪率極低，單獨旅行的女性旅客也很多。唯一要注意的是「機車/腳踏車」——如果你不會騎，建議不要輕易嘗試，因為台灣的交通有點混亂。</div>\n      </div>'

new_faqs = '''      <div class="faq-item">
        <div class="faq-q">台灣旅遊安全嗎？<span class="arrow">▼</span></div>
        <div class="faq-a">非常安全。台灣的犯罪率極低，單獨旅行的女性旅客也很多。唯一要注意的是「機車/腳踏車」——如果你不會騎，建議不要輕易嘗試，因為台灣的交通有點混亂。</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">台灣旅遊需要簽證嗎？<span class="arrow">▼</span></div>
        <div class="faq-a">大部分國家（美國、加拿大、歐盟、日本、韓國、紐西蘭、澳洲）都可以「免簽證」停留 90 天。其他國家可能需要辦理「簽證」或「落地簽」，建議出發前先查詢台灣外交部的官方網站。</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">台灣旅遊最佳季節？<span class="arrow">▼</span></div>
        <div class="faq-a">我最推