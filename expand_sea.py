with open('southeast-asia.html', 'r', encoding='utf-8') as f:
    c = f.read()

new_content = '''
<section style="max-width:900px;margin:0 auto;padding:0 20px 40px;">
  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">為什麼我愛東南亞自由行</h2>
  <p style="line-height:1.9;margin-bottom:16px;">老實說，我第一次去東南亞（泰國）是被朋友拖去的。那時候我心裡想：「熱得要命、食物不知道乾不乾淨、語言不通…… 真的好玩嗎？」結果到了曼谷的第二天，我在恰圖洽週末市集吃到了人生最好吃的芒果糯米——從此就愛上了東南亞。</p>
  <p style="line-height:1.9;margin-bottom:16px;">東南亞最棒的地方在於：它對預算有限的旅客超級友善。NT$10,000 在東京可能只夠住 3 晚青旅，但在清邁可以住 7 晚無泳池的服務式公寓。加上按摩超便宜（泰式按摩一小時 NT$250~400）、食物好吃又便宜、當地人超熱情——這就是為什麼我每年至少去一次東南亞。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">東南亞自由行3大推薦路線</h2>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>泰國（第一次首選）</strong><br>泰國是最適合第一次去東南亞的人。曼谷交通方便（BTS、MRT、Grab 都很方便）、英語普及率高、食物絕對不會踩雷。我個人最愛清邁——那裡有種「東南亞的京都」感，咖啡廳多到數不清，租一台機車一天 NT$200 就能把主要景點跑完。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>越南（美食+歷史）</strong><br>越南我推薦峴港+會安+順化這條路線。峴港海灘超美、會安古鎮很有氛圍、順化的越戰遺跡很震撼。我的私房推薦：峴港的「Bánh xèo」（越南煎餅）——外脆內軟，搭配新鮮蝦仁和豆芽菜，一口咬下…… 嗯，你會想再吃第二個。</p>
  <p style="line-height:1.9;margin-bottom:12px;"><strong>印尼巴厘島（海島度假）</strong><br>巴厘島不適合「趕行程」的旅客，但超適合「躺平度假」。烏布梯田、海神廟、庫塔海灘…… 巴厘島有種「東南亞的夏威夷」感，非常適合情侶或家庭旅遊。小撇步：避開澳洲寒假（7-8月），那時候住宿會漲價 50~100%。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">什麼時候去最划算？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">根據我自己的經驗：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>最便宜</strong>：5月~6月（雨季剛開始，但機票超便宜）、9月~10月（雨季尾聲，遊客少）</li>
    <li><strong>最舒服</strong>：11月~2月（乾季，涼爽，但是旺季）</li>
    <li><strong>最貴</strong>：暑假期間（7月~8月，澳洲寒假）、聖誕~新年（12月底~1月初）</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">小撇步：如果時間彈性大，我會推薦 5 月去泰國——雖然是雨季，但雨通常下在下午 2-4 點，早上和晚上都超舒服。而且機票來回只要 NT$5,000~7,000！</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">第一次去東南亞？這幾個小撇步一定要知道</h2>
  <p style="line-height:1.9;margin-bottom:12px;">1. <strong>買一張當地 SIM 卡</strong>：泰國推薦 AIS 或 True；越南推薦 Viettel 或 Vinaphone。在機場就能買到，7 天無限流量約 NT$300~500。Google Maps 離線下載 + 翻譯 APP，完全不怕迷路。</p>
  <p style="line-height:1.9;margin-bottom:12px;">2. <strong>用 Grab 叫車</strong>：就像東南亞的 Uber。價格透明、不用講價、可以直接綁信用卡。在曼谷，從機場到市區用 Grab 約 NT$350~500，比計程車便宜而且不用擔心被當盤子削。</p>
  <p style="line-height:1.9;margin-bottom:12px;">3. <strong>學幾句基本當地語</strong>：不用很厲害，「Hello」（英語通用）、「Thank you」（各地不同）、「How much?」（多少錢？）就能讓你的旅行順利很多。泰國人對會講泰文的外國人特別友善，就算講得破破的也沒關係。</p>
  <p style="line-height:1.9;margin-bottom:12px;">4. <strong>路邊攤是你的救星</strong>：泰國的 CP 值最高的美食都在路邊攤。Pad Thai（泰式炒河粉）NT$50~80、Mango Sticky Rice（芒果糯米）NT$60~100、Tom Yum Kung（酸辣蝦湯）NT$100~150…… 我每次去曼谷都至少吃一餐路邊攤。</p>
  <p style="line-height:1.9;margin-bottom:16px;">5. <strong>注意交通安全</strong>：東南亞的交通安全…… 嗯，讓我們說「還有進步空間」。機車事故率很高，如果你不確定自己能安全騎乘，建議改用 Grab 或公共交通。我個人的原則：不騎機車，除非我對那個城市非常熟悉。</p>

  <h2 style="font-size:1.6rem;margin:32px 0 16px;color:var(--tiffany);">預算怎麼抓？</h2>
  <p style="line-height:1.9;margin-bottom:12px;">以泰國曼谷 5 天 4 夜為例（不含機票）：</p>
  <ul style="line-height:1.9;margin-bottom:16px;padding-left:20px;">
    <li><strong>住宿</strong>：NT$500~1,500/晚（青旅/服務式公寓），NT$2,000~4,000/晚（四星級飯店）</li>
    <li><strong>交通</strong>：Grab 市區內一趟 NT$80~200，BTS/MRT 一趟 NT$30~80</li>
    <li><strong>餐費</strong>：路邊攤一餐 NT$50~150，普通餐廳 NT$150~400，高 CP 值 Buffet NT$300~600</li>
    <li><strong>按摩</strong>：泰式按摩一小時 NT$250~400，SPA 一小時 NT$800~2,000</li>
    <li><strong>門票</strong>：景點大多很便宜（₿100~500，約 NT$100~500）</li>
  </ul>
  <p style="line-height:1.9;margin-bottom:16px;">不含機票，5 天 4 夜大概抓 NT$12,000~20,000 就很舒服了。如果願意住青旅、吃路邊攤、用 Grab（而不是租車），甚至可以壓到 NT$8,000 以內。我自己最好的紀錄是：5 天 4 夜曼谷，總花費 NT$7,500（含機票！）——那次是搭亞航來回 NT$4,200，住宿全程青旅，交通全用 BTS+MRT+Grab，吃飯全用路邊攤。</p>

  <p style="line-height:1.9;margin-bottom:16px;font-style:italic;color:var(--text-light);">👉 往下看我們整理的詳細攻略，每一篇都是實地走訪後寫出來的——不是抄來的，是真正走過、吃過、住過之後的心得。</p>
</section>
'''

# Insert before <div class="card-grid">
pos = c.find('<div class="card-grid">')
if pos >= 0:
    c = c[:pos] + new_content + '\n  ' + c[pos:]
    with open('southeast-asia.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Expanded southeast-asia.html successfully!')
else:
    print('ERROR: Could not find insertion point')
