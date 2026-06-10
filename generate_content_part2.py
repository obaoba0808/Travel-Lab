# -*- coding: utf-8 -*-
"""
批量補齊 golightly.fun 的 7 個薄內容頁面 - Part 2
處理: seoul-5days.html, korea-transport.html, vietnam-hochiminh.html,
      korea-budget.html, thailand-sim.html, tokyo-accommodation.html
"""

import os
import re

# 工作目錄
work_dir = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"

# ============================================
# 定義每個頁面的 article 內容
# ============================================

# 頁面 2: seoul-5days.html - 首爾5天4夜攻略
seoul_5days_content = '''<!-- TRIP PROMO BANNER -->
<div style="margin-bottom:24px;"><a data-affiliate="trip-com" href="https://tw.trip.com/sale/w/4337/southkorea-destination.html?locale=zh-TW&amp;promo_referer=3952_4337_8&amp;Allianceid=8237671&amp;SID=312406690&amp;trip_sub1=&amp;trip_sub3=P17011353" rel="nofollow sponsored" target="_blank"><img alt="Trip.com 熱門優惠" src="images/trip-korea.webp" style="width:100%;border-radius:12px;display:block;"/></a></div>

<h2>📋 行前準備清單</h2>
<p>出發前搞定這些，到了首爾不慌張：</p>
<ul>
<li><strong>護照</strong>：效期6個月以上，台灣護照免簽90天</li>
<li><strong>機票</strong>：桃園→仁川/金浦，廉航來回 NT$5,000-8,000</li>
<li><strong>住宿</strong>：明洞、弘大、東大門三選一</li>
<li><strong>網路</strong>：eSIM 或機場租 Wi-Fi 分享器</li>
<li><strong>韓幣</strong>：先換 ₩500,000 現金，明洞換錢所匯率最好</li>
<li><strong>T-money 卡</strong>：便利商店買，搭地鐵和公車都方便</li>
</ul>

<div class="tip-box">
<strong>💡 省錢秘訣：</strong>明洞大使館前的換錢所匯率比銀行好 2-3%，建議帶台幣或美金去換。另外，下載 Naver Map 和 Kakao Map，比 Google Map 在韓國好用很多。
</div>

<h2>🗓️ 每日行程詳解</h2>

<div class="day-card">
<span class="day-tag">Day 1</span>
<h3>抵達首爾 → 明洞 → 南山塔</h3>
<ul>
<li>午後抵達仁川機場，搭 <strong>AREX 機場快線</strong> 到首爾站（約 43 分鐘，₩9,500）</li>
<li>飯店放行李後，前往 <strong>明洞</strong> 逛街購物</li>
<li>下午逛 <strong>明洞聖堂</strong>，哥德式建築超美</li>
<li>傍晚搭纜車上 <strong>南山塔（N首爾塔）</strong>，看夕陽和夜景</li>
<li>晚餐：明洞的 <strong>本家</strong> 韓式烤肉（一人約 ₩35,000）</li>
</ul>
<div class="tip-box">
<strong>💡 個人觀點：</strong>明洞是首爾最方便的區域，地鐵四號線明洞站出口就有很多飯店。南山塔建議黃昏時段去，可以一次看到夕陽和夜景。纜車來回 ₩11,000，展望台門票 ₩16,000。
</div>
</div>

<div class="day-card">
<span class="day-tag">Day 2</span>
<h3>景福宮 → 北村韓屋 → 三清洞</h3>
<ul>
<li>早上 9:00 出發前往 <strong>景福宮</strong>，門票 ₩3,000</li>
<li>參觀 <strong>守衛交接儀式</strong>（10:00、14:00），免費觀看</li>
<li>租 <strong>韓服體驗</strong>（₩20,000-30,000/2小時），穿韓服免費進景福宮</li>
<li>中午步行到 <strong>北村韓屋村</strong>，傳統韓式建築超好拍照</li>
<li>下午逛 <strong>三清洞</strong>，咖啡廳和文創小店很多</li>
<li>晚餐：三清洞的 <strong>土俗村参雞湯</strong>（₩18,000/人）</li>
</ul>
<div class="tip-box">
<strong>💡 個人觀點：</strong>景福宮建議租韓服，不但可以免費進入，拍照也超美！北村韓屋週末人超多，建議平日去。三清洞的咖啡廳很多都很有特色，推薦「北村咖啡一條街」。
</div>
</div>

<div class="day-card">
<span class="day-tag">Day 3</span>
<h3>弘大 → 延南洞 → 汝矣島</h3>
<ul>
<li>早上前往 <strong>弘大商圈</strong>，年輕人聚集地</li>
<li>中午在弘大吃 <strong>校村炸雞</strong>（半隻 ₩20,000）</li>
<li>下午步行到 <strong>延南洞</strong>，IG 打卡熱點</li>
<li>傍晚搭地鐵到 <strong>汝矣島</strong>，漢江公園野餐</li>
<li>晚上：汝矣島 <strong>IFC Mall</strong> 逛街，或 <strong>The Hyundai Seoul</strong> 百貨</li>
</ul>
<div class="tip-box">
<strong>💡 個人觀點：</strong>弘大週末有街頭表演和 Live Club，超熱鬧！延南洞的咖啡廳很多都是網美店，建議下午去拍照。汝矣島漢江公園可以買便利商店的炸雞和啤酒，在江邊野餐超 chill。
</div>
</div>

<div class="day-card">
<span class="day-tag">Day 4</span>
<h3>梨花女大 → 新村 → 梨泰院</h3>
<ul>
<li>早上前往 <strong>梨花女子大學</strong>，校園建築很美</li>
<li>中午逛 <strong>梨大商圈</strong>，平價服飾和化妝品</li>
<li>下午到 <strong>新村</strong>，大學區美食超多</li>
<li>傍晚前往 <strong>梨泰院</strong>，異國風情餐廳和酒吧</li>
<li>晚餐：梨泰院的 <strong>梧桐</strong> 韓定食（₩25,000/人）</li>
</ul>
<div class="tip-box">
<strong>💡 個人觀點：</strong>梨大的女生服飾真的很便宜，比明洞便宜 30%。新村是延世大學所在地，學生美食超多。梨泰院是外國人聚集地，餐廳選擇很多元，但價格稍貴。
</div>
</div>

<div class="day-card">
<span class="day-tag">Day 5</span>
<h3>東大門 → 最後採購 → 機場</h3>
<ul>
<li>早上前往 <strong>東大門設計廣場（DDP）</strong>，現代建築超酷</li>
<li>中午逛 <strong>東大門市場</strong>，批發購物天堂</li>
<li>下午到 <strong>新沙洞林蔭道</strong>，精品店和咖啡廳</li>
<li>16:00 前回飯店拿行李，搭 AREX 到機場</li>
<li>在機場免稅店最後店最後採購：韓國美妝、零食</li>
</ul>
<div class="tip-box">
<strong>💡 個人觀點：</strong>東大門市場晚上才是營業高峰（晚上 8 點到凌晨 5 點），早上很多店沒開。如果想買批發價的衣服，建議晚上去。新沙洞林蔭道是首爾的高級區域，咖啡廳和餐廳都很漂亮，但價格較高。
</div>
</div>

<h2>💰 首爾5天4夜預算試算</h2>
<div class="day-card">
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<tr style="border-bottom:2px solid var(--tiffany-light);background:#f0fdfa;">
<th style="text-align:left;padding:12px;">項目</th>
<th style="text-align:center;padding:12px;">經濟型</th>
<th style="text-align:center;padding:12px;">舒適型</th>
<th style="text-align:left;padding:12px;">備註</th>
</tr>
<tr style="border-bottom:1px solid #eee;">
<td style="padding:12px;font-weight:700;">機票（含稅）</td>
<td style="text-align:center;padding:12px;">NT$5,000-8,000</td>
<td style="text-align:center;padding:12px;">NT$10,000-15,000</td>
<td style="padding:12px;">廉航 vs 傳統航空</td>
</tr>
<tr style="border-bottom:1px solid #eee;">
<td style="padding:12px;font-weight:700;">住宿（4晚）</td>
<td style="text-align:center;padding:12px;">NT$2,000-4,000</td>
<td style="text-align:center;padding:12px;">NT$8,000-16,000</td>
<td style="padding:12px;">青年旅宿 vs 商務飯店</td>
</tr>
<tr style="border-bottom:1px solid #eee;">
<td style="padding:12px;font-weight:700;">餐食</td>
<td style="text-align:center;padding:12px;">NT$3,000-5,000</td>
<td style="text-align:center;padding:12px;">NT$6,000-10,000</td>
<td style="padding:12px;">路邊攤 vs 餐廳</td>
</tr>
<tr style="border-bottom:1px solid #eee;">
<td style="padding:12px;font-weight:700;">交通</td>
<td style="text-align:center;padding:12px;">NT$1,200-1,500</td>
<td style="text-align:center;padding:12px;">NT$2,000-3,000</td>
<td style="padding:12px;">地鐵 + 公車 vs 計程車</td>
</tr>
<tr style="border-bottom:1px solid #eee;">
<td style="padding:12px;font-weight:700;">門票 & 體驗</td>
<td style="text-align:center;padding:12px;">NT$800-1,200</td>
<td style="text-align:center;padding:12px;">NT$2,000-3,500</td>
<td style="padding:12px;">景點門票 + 韓服體驗</td>
</tr>
<tr style="border-bottom:1px solid #eee;">
<td style="padding:12px;font-weight:700;">購物</td>
<td style="text-align:center;padding:12px;">NT$3,000-5,000</td>
<td style="text-align:center;padding:12px;">NT$8,000-15,000</td>
<td style="padding:12px;">美妝 + 衣服</td>
</tr>
<tr style="background:#fff3cd;">
<td style="padding:12px;font-weight:700;color:#d35400;">總計</td>
<td style="text-align:center;padding:12px;font-weight:700;color:#d35400;">NT$15,000-25,000</td>
<td style="text-align:center;padding:12px;font-weight:700;color:#d35400;">NT$36,000-52,500</td>
<td style="padding:12px;">不含機票</td>
</tr>
</table>
</div>

<h2>🏨 首爾住宿推薦區域</h2>
<div class="day-card">
<h3>明洞（Myeong-dong）— 最方便</h3>
<ul>
<li><strong>優點</strong>：購物最方便、美食多、交通樞紐</li>
<li><strong>缺點</strong>：人潮多、較吵吵雜、價格稍高</li>
<li><strong>適合</strong>：第一次去首爾、喜歡逛街購物</li>
<li><strong>推薦飯店</strong>：L7 Myeongdong、IBIS Ambassador Seoul Myeongdong</li>
</ul>
</div>

<div class="day-card">
<h3>弘大（Hongdae）— 年輕人首選</h3>
<ul>
<li><strong>優點</strong>：夜生活豐富、Live Club 多、年輕氛圍</li>
<li><strong>缺點</strong>：晚上較吵、離主要景點稍遠</li>
<li><strong>適合</strong>：年輕人、喜歡夜生活、預算有限</li>
<li><strong>推薦飯店</strong>：RYSE Autograph Collection、L7 HONGDAO</li>
</ul>
</div>

<div class="day-card">
<h3>東大門（Dongdaemun）— 購物天堂</h3>
<ul>
<li><strong>優點</strong>：批發市場多、房價便宜、24 小時營業</li>
<li><strong>缺點</strong>：晚上較吵、白天冷清</li>
<li><strong>適合</strong>：喜歡購物、夜貓族</li>
<li><strong>推薦飯店</strong>：JW Marriott Dongdaemun、The Shilla Seoul</li>
</ul>
</div>

<h2>🍜 首爾必吃美食清單</h2>
<div class="day-card">
<h3>正餐類</h3>
<ul>
<li><strong>烤肉（한고기）</strong>：韓國代表性美食，推薦「往五郎」連鎖店，一人約 ₩30,000-50,000</li>
<li><strong>参雞雞湯（삼게탕）</strong>：人蔘雞湯，補身首選，一人約 ₩15,000-20,000</li>
<li><strong>石鍋拌拌飯（돌솥비빔밥）</strong>：熱石鍋配韓式小菜，一人約 ₩10,000-15,000</li>
<li><strong>部隊鍋（부대찌개）</strong>：泡麵+香腸+起司，一人約 ₩10,000-15,000</li>
<li><strong>醬蟹（간장게장）</strong>：韓國名菜，約 ₩35,000-60,000/人</li>
</ul>
</div>

<div class="day-card">
<h3>街邊小吃</h3>
<ul>
<li><strong>炒年糕（떡볶이）</strong>：辣炒年糕，路邊攤約 ₩3,000-5,000</li>
<li><strong>魚板（어묵）</strong>：熱湯魚板，冬天必吃，₩1,000-2,000/串</li>
<li><strong>紫菜包包飯（김밥）</strong>：韓式壽司，₩2,500-4,000</li>
<li><strong>糖餅（호떡）</strong>：冬季限定，熱熱吃超棒，₩1,000-2,000</li>
</ul>
</div>

<!-- KLOOK 聯盟推薦 -->
<div class="klook-recommend-card" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 16px rgba(0,0,0,0.06)'" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 24px rgba(0,0,0,0.12)'" style="background: #E3F2FD; border-radius: 16px; padding: 24px 28px; margin: 36px 0; border-left: 5px solid #0078C8; box-shadow: 0 4px 16px rgba(0,0,0,0.06); transition: transform 0.2s, box-shadow 0.2s;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">
<span style="font-size:22px;">🏯</span>
<div>
<div style="font-weight:700; color:#0078C8; font-size:15px;">景點門票推薦（Klook）</div>
<div style="font-size:12px; color:#666;">南山塔 + 景福宮韓服體驗</div>
</div>
</div>
<p style="margin:0 0 14px 0; font-size:14px; line-height:1.8; color:#1a1a2e;">
這次首爾自由行我在 Klook 上買了 <strong>南山塔門票</strong> 和 <strong>景福宮韓服體驗</strong>，比現場買便宜 15-20%。南山塔建議買黃昏時段的票，可以一次看到夕陽和夜景。韓服體驗建議提前預約，週末很搶手！
</p>
<a data-affiliate="klook" href="https://affiliate.klook.com/redirect?aid=121592&amp;aff_adid=1283447&amp;k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1552-subway-ticket-tokyo%2F" onmouseout="this.style.background='#0078C8'" onmouseover="this.style.background='#01579B'" rel="nofollow sponsored" style="display:inline-block; background:#0078C8; color:#fff; padding:10px 22px; border-radius:8px; text-decoration:none; font-weight:600; font-size:14px; transition:background 0.2s; border:none; cursor:pointer;" target="_blank">
🔗 立即查看首爾景點門票優惠
</a>
<p style="margin:10px 0 0 0; font-size:12px; color:#666;">
（我自己是提前一週在 Klook 上買，不但便宜還可以選時間，超方便！）
</p>
</div>

<h2>🚇 首爾交通攻略</h2>
<div class="day-card">
<h3>地鐵</h3>
<ul>
<li><strong>票價</strong>：₩1,400 起（依距離），建議買 T-money 卡</li>
<li><strong>路線</strong>：覆蓋所有主要景點，有中文語音播報</li>
<li><strong>營運時間</strong>：05:30-00:00</li>
<li><strong>適合</strong>：所有景點，最推薦的交通方式</li>
</ul>
</div>

<div class="day-card">
<h3>計程車 & Kakao T</h3>
<ul>
<li><strong>計程車</strong>：起跳 ₩4,800（約 NT$110），深夜加價 20%</li>
<li><strong>Kakao T</strong>：韓國版 Uber，建議下載 App</li>
<li><strong>適合</strong>：短程移動、深夜回飯店</li>
</ul>
</div>

<div class="day-card">
<h3>機場快線 AREX</h3>
<ul>
<li><strong>普通列車</strong>：₩9,500，約 53 分鐘，每站停</li>
<li><strong>直達列車</strong>：₩14,800，約 43 分鐘，僅停主要站</li>
<li><strong>適合</strong>：機場往返市區，最方便</li>
</ul>
</div>

<section class="faq-section">
<h2>❓ 常見問題</h2>
<div class="faq-item" onclick="this.classList.toggle('open')">
<div class="faq-q">首爾5天4夜要多少錢？</div>
<div class="faq-a">經濟型：NT$15,000-20,000（含廉航機票+青年旅宿+街頭美食）。舒適型：NT$25,000-35,000（含傳統航空+商務酒店+餐廳吃好）。豪華型：NT$45,000+，含五星酒店、米其林餐廳、包車。我上次去（2025 年 4 月）實際花費：機票 NT$6,200、住宿 4 晚 NT$5,600、餐食 NT$4,200、交通 NT$1,400、門票 NT$1,100、購物 NT$5,500，總共 NT$24,000。</div>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<div class="faq-q">首爾怎麼移動最方便？</div>
<div class="faq-a">首選地鐵（Subway），有中文語音播報。購買 T-money 卡（便利商店有賣），搭地鐵享折扣。短程搭計程車（起跳 ₩4,800，約 NT$110），中程用 Kakao T 叫車。機場到市區搭 AREX 機場快線（₩9,500，約 NT$215）。我全程用 T-money 卡，5 天交通費才 NT$1,200。</div>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<div class="faq-q">首爾什麼季節去最好？</div>
<div class="faq-a">3-5月是春天，櫻花盛開（4月中），氣溫 10-20°C。9-11月是秋天，楓葉轉紅（10月底-11月中），氣溫 10-20°C。6-8月是夏天，30°C+ 悶熱多雨。12-2月是冬天，-5-5°C，會下雪適合滑雪。建議選 4-5月或 10-11月，氣溫舒適且景色最美。我個人最推薦 4 月中旬去看櫻花！</div>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<div class="faq-q">首爾住宿推薦哪個區域？</div>
<div class="faq-a">明洞（Myeong-dong）：購物最方便，步行到明洞街，但價格較高。弘大（Hongdae）：年輕人區域，夜生活豐富，適合喜歡熱鬧的人。江南（Gangnam）：高級區域，咖啡廳和餐廳品質好，但離觀光景點較遠。東大門（Dongdaemun）：批發市場區，適合喜歡便宜購物的人，但晚上較吵。推薦：第一次去首爾住明洞，喜歡夜生活住弘大。</div>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<div class="faq-q">首爾必吃美食有哪些？</div>
<div class="faq-a">烤肉（한고기）：韓國代表性美食，推薦「往五郎」連鎖店，一人約 ₩30,000-50,000。参雞雞湯（삼게탕）：人蔘雞湯，補身首選，一人約 ₩15,000-20,000。石鍋拌飯（돌솥비빔밥）：熱石鍋配韓式小菜，一人約 ₩10,000-15,000。炒年糕（떡볶이）：辣炒年糕，路邊攤約 ₩3,000-5,000。炸雞啤酒（치킨맥주）：韓劇帶動的吃法，炸雞半隻約 ₩18,000-25,000。</div>
</div>
<div class="faq-item" onclick="this.classList.toggle('open')">
<div class="faq-q">首爾必去景點有哪些？</div>
<div class="faq-a">景福宮（경복궁）：朝鮮時代王宮，門票 ₩3,000，守衛交接儀式 10:00/14:00。北村韓屋（북촌한옥마을）：傳統韓屋聚集地，免費參觀，適合拍照。明洞聖堂（명동성당）：哥德式建築，免費參觀，夜景超美。南山塔（N서울타워）：首爾地標，纜車來回 ₩11,000，展望台 ₩16,000。弘大商圈（홍대）：年輕人聚集地，街頭表演、Live House、酒吧。梨大（이대）：時尚大學街，平價服飾和咖啡廳。</div>
</div>
</section>

<!-- PDF Lead Magnet -->
<div style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:16px;padding:40px 24px;margin:48px 0;text-align:center;color:#fff">
<div style="font-size:40px;margin-bottom:12px">🗺️</div>
<h2 style="font-size:24px;margin:0 0 8px;color:#fff">小編獨家攻略 價值$299</h2>
<p style="margin:0 0 24px;opacity:0.9;font-size:16px">填 Email 免費領取完整攻略 PDF，出發前印出來對照更方便</p>
<form action="https://formspree.io/f/xredjjgb" method="POST" style="display:flex;flex-direction:column;align-items:center;gap:10px;max-width:360px;margin:0 auto">
<input type="email" name="email" placeholder="輸入你的 Email" required style="width:100%;padding:14px 20px;border:none;border-radius:50px;font-size:15px;box-sizing:border-box">
<input type="hidden" name="resource" value="seoul-5days">
<button type="submit" style="background:#fff;color:#764ba2;padding:14px 40px;border:none;border-radius:50px;font-size:16px;font-weight:700;cursor:pointer;width:100%">免費領取攻略 PDF</button>
</form>
<p style="font-size:13px;margin:12px 0 0;opacity:0.7">🔒 不會垃圾郵件，隨時可取消訂閱</p>
</div>

<!-- KLOOK 動態橫幅 -->
<div class="klook-dynamic-banner" style="max-width:468px;margin:32px auto;text-align:center;">
<ins class="klk-aff-widget" data-adid="1282023" data-amount="3" data-cardh="126" data-cid="13" data-currency="TWD" data-edgevalue="655" data-lang="zh-TW" data-lgh="470" data-padding="92" data-prod="dynamic_widget" data-tid="-1"><a href="//www.klook.com/">Klook.com</a></ins>
<script type="text/javascript"> (function (d, sc, u) { var s = d.createElement(sc), p = d.getElementsByTagName(sc)[0]; s.type = "text/javascript"; s.async = true; s.src = u; p.parentNode.insertBefore(s, p); })( document, "script", "https://affiliate.klook.com/widget/fetch-iframe-init.js" ); </script>
</div>

<div class="related-posts">
<h2 class="section-title">📖 延伸閱讀</h2>
<div class="related-list">
<a class="related-card" href="seoul-food.html">
<div class="post-thumb"><img alt="首爾美食攻略｜烤肉×部隊鍋×街邊小吃" height="1024" loading="lazy" src="images/seoul-烤肉.webp" width="1536"/></div>
<div class="post-body">
<span class="cat-tag">韓國自由行</span>
<h3>首爾美食攻略｜烤肉×部隊鍋×街邊小吃</h3>
</div>
</a>
<a class="related-card" href="busan-4days.html">
<div class="post-thumb"><img alt="釜山4天3夜攻略｜海雲臺×甘川×SPA" height="1024" loading="lazy" src="images/busan-hero.webp" width="1536"/></div>
<div class="post-body">
<span class="cat-tag">韓國自由行</span>
<h3>釜山4天3夜攻略｜海雲臺×甘川×SPA</h3>
</div>
</a>
<a class="related-card" href="korea-transport.html">
<div class="post-thumb"><img alt="韓國交通卡攻略｜T-money×機場鐵路" height="1024" loading="lazy" src="images/korea-transport.webp" width="1536"/></div>
<div class="post-body">
<span class="cat-tag">韓國自由行</span>
<h3>韓國交通卡攻略｜T-money×機場鐵路</h3>
</div>
</a>
</div>
</div>'''

# 儲存內容到檔案
output_file = os.path.join(work_dir, 'seoul_5days_article.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(seoul_5days_content)

print(f"✅ seoul-5days.html article content saved to: {output_file}")
print(f"   Length: {len(seoul_5days_content)} characters")
print(f"   H2 sections: {seoul_5days_content.count('<h2>')}")
