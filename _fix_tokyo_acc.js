const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'tokyo-accommodation.html');
let html = fs.readFileSync(file, 'utf8');

// === FIX 1: Add missing content after 新宿 H2, before the broken related section ===
// Find: <h2 id="新宿">🏢 新宿住宿攻略</h2>\n<div class="day-card">\n<h2 class="section-title">📖 延伸閱讀
// Replace with: full content + proper structure

const newContent = `
<h2 id="新宿">🏢 新宿住宿攻略</h2>
<div class="day-card">
<h3>為什麼選新宿？</h3>
<p>新宿是東京最大的交通樞紐，JR 山手線、中央線、總武線、都營地下鐵、京王線、小田急線全部交會於此。從成田機場搭 N'EX 直達、羽田機場搭利木津巴士也到這裡。對第一次去東京的人來說，住新宿是最不會出錯的選擇。</p>

<h3>🚃 交通優勢</h3>
<ul style="list-style:none;padding-left:0;">
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>JR 新宿站</strong> — 全世界最繁忙車站，山手線/中央線/總武線/埼京線</li>
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>都營大江戶線</strong> — 直達六本木、築地、台場</li>
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>京王線/小田急線</strong> — 往高尾山、箱根、河口湖方向</li>
<li style="padding:8px 0;">✅ <strong>成田 N'EX / 羽田利木津</strong> — 機場直達不用轉車</li>
</ul>

<h3>🏨 區域推薦</h3>
<table style="width:100%;border-collapse:collapse;font-size:14px;margin:16px 0;">
<tr style="background:#f0fdfa;border-bottom:2px solid var(--tiffany-light);">
<th style="text-align:left;padding:10px;">區域</th><th style="text-align:center;padding:10px;">房價/晚</th><th style="text-align:left;padding:10px;">特色</th></tr>
<tr><td style="padding:10px;"><strong>西口（歌舞伎町）</strong></td><td style="text-align:center;padding:10px;">¥10,000-18,000</td><td style="padding:10px;">夜生活、餐廳多、吵雜但方便</td></tr>
<tr><td style="padding:10px;"><strong>南口（新都心）</strong></td><td style="text-align:center;padding:10px;">¥12,000-22,000</td><td style="padding:10px;">商務飯店集中、安靜整潔</td></tr>
<tr><td style="padding:10px;"><strong>東口（百貨商圈）</strong></td><td style="text-align:center;padding:10px;">¥15,000-25,000</td><td style="padding:10px;">伊勢丹/ Lumine、購物方便</td></tr>
</table>

<div class="tip-box" style="margin-top:16px;">
<strong>💡 省錢技巧：</strong>西口的超級酒店（Super Hotel）和東橫INN性價比很高，¥6,000-9,000 就有乾淨的單人房。缺點是房間很小（約 10-12 坪）。
</div>
</div>

<h2 id="上野">🏯 上野住宿攻略</h2>
<div class="day-card">
<h3>為什麼選上野？</h3>
<p>上野是東京預算住宿的首選。離淺草寺一站距離、上野公園（博物館群/動物園）步行可達、阿美橫丁逛街便宜又好玩。JR 上野站也是北上的起點（往宇都宮、日光方向），交通同樣便利。</p>

<h3>🚃 交通優勢</h3>
<ul style="list-style:none;padding-left:0;">
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>JR 上野站</strong> — 山手線/京濱東北線/高崎線/宇都宮線</li>
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>銀座線/日比谷線</strong> — 直達銀座、澀谷、六本木</li>
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>京成上野站</strong> — 成田 Skyliner 終點（36 分鐘到機場）</li>
<li style="padding:8px 0;">✅ <strong>上野站步行圈</strong> — 公園、博物館、阿美橫丁全走路</li>
</ul>

<h3>🏨 區域推薦</h3>
<table style="width:100%;border-collapse:collapse;font-size:14px;margin:16px 0;">
<tr style="background:#fff7ed;border-bottom:2px solid #ff6b35;">
<th style="text-align:left;padding:10px;">區域</th><th style="text-align:center;padding:10px;">房價/晚</th><th style="text-align:left;padding:10px;">特色</th></tr>
<tr><td style="padding:10px;"><strong>站前出口廣場</strong></td><td style="text-align:center;padding:10px;">¥5,000-9,000</td><td style="padding:10px;">商務旅館密集、出站就到</td></tr>
<tr><td style="padding:10px;"><strong>御徒町/阿美橫</strong></td><td style="text-align:center;padding:10px;">¥4,000-8,000</td><td style="padding:10px;">最便宜區域、藥妝零食天堂</td></tr>
<tr><td style="padding:10px;"><strong>不忍池畔</strong></td><td style="text-align:center;padding:10px;">¥8,000-14,000</td><td style="padding:10px;">公園景觀、安靜、較高級</td></tr>
</table>

<div class="tip-box" style="margin-top:16px;">
<strong>💡 省錢技巧：</strong>御徒町一帶的 Business Hotel 超多競爭，¥4,500-7,000 就有附早餐的雙人房。推薦用 Trip.com 或 Agoda 比價。
</div>
</div>

<h2 id="淺草">⛩️ 淺草住宿攻略</h2>
<div class="day-card">
<h3>為什麼選淺草？</h3>
<p>想感受「老東京」氛圍就住淺草。雷門、仲見世通商店街、晴空塔步行距離、隅田川河岸步道——這裡的氣質跟新宿完全不同，適合喜歡傳統文化的旅行者。</p>

<h3>🚃 交通</h3>
<ul style="list-style:none;padding-left:0;">
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>銀座線/淺草線</strong> — 到上野 5 分鐘、銀座 15 分鐘</li>
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>東武晴空塔線</strong> — 直達晴空塔、春日部</li>
<li style="padding:8px 0;">⚠️ <strong>JR 沒有直達</strong> — 需要在上野或東京轉車</li>
</ul>

<h3>🏨 推薦類型</h3>
<table style="width:100%;border-collapse:collapse;font-size:14px;margin:16px 0;">
<tr style="background:#fef3c7;border-bottom:2px solid #eab308;">
<th style="text-align:left;padding:10px;">類型</th><th style="text-align:center;padding:10px;">房價/晚</th><th style="text-align:left;padding:10px;">適合</th></tr>
<tr><td style="padding:10px;"><strong>民宿/旅館（Ryokan）</strong></td><td style="text-align:center;padding:10px;">¥6,000-12,000</td><td style="padding:10px;">體驗日式榻榻米、共浴</td></tr>
<tr><td style="padding:10px;"><strong>商務旅館</strong></td><td style="text-align:center;padding:10px;">¥4,000-8,000</td><td style="padding:10px;">純睡覽、省預算</td></tr>
<tr><td style="padding:10px;"><strong>高級飯店</strong></td><td style="text-align:center;padding:10px;">¥15,000-30,000</td><td style="padding:10px;">雷門景觀房、特殊紀念</td></tr>
</table>
</div>

<h2 id="澀谷">🎪 澀谷住宿攻略</h2>
<div class="day-card">
<h3>為什麼選澀谷？</h3>
<p>年輕人的天堂。109 百貨、Shibuya Sky、忠犬八公像、原宿竹下通都在步行範圍。澀谷是時尚潮流中心，晚上比白天更熱鬧。</p>

<h3>🚃 交通</h3>
<ul style="list-style:none;padding-left:0;">
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>山手線</strong> — 到原宿 3 分鐘、新宿 7 分鐘、表參道 4 分鐘</li>
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>半藏門線/副都心線</strong> — 直達表參道、明治神宮前</li>
<li style="padding:8px 0;">✅ <strong>東急東橫線</strong> — 往自由之丘、二子玉川</li>
</ul>

<h3>🏨 注意事項</h3>
<div class="tip-box" style="margin-top:16px;">
<strong>⚠️ 澀谷房價偏高：</strong>因為地點太熱門，同級別飯店比新宿貴 20-30%。如果主要目的是逛澀谷/原宿，其實住<strong>新宿或池袋</strong>搭電車過來也只要 10-15 分鐘，可以省不少錢。
</div>
</div>

<h2 id="池袋">🎌 池袋住宿攻略</h2>
<div class="day-card">
<h3>為什麼選池袋？</h3>
<p>動漫聖地 + 購物天堂。陽光城（Sunshine City）、乙女路、動漫店集中在這裡。房價比新宿便宜一大截，交通同樣方便（山手線）。</p>

<h3>🚃 交通</h3>
<ul style="list-style:none;padding-left:0;">
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>山手線</strong> — 到新宿 12 分鐘、澀谷 18 分鐘、上野 15 分鐘</li>
<li style="padding:8px 0;border-bottom:1px solid #f0f0f0;">✅ <strong>副都心線</strong> — 直達涉谷、明治神宮前</li>
<li style="padding:8px 0;">✅ <strong>多条私鐵</strong> — 東武/西武/東急，往埼玉方向</li>
</ul>

<h3>💰 性價比之王</h3>
<div class="tip-box" style="margin-top:16px;">
<strong>💡 池袋是隱藏寶石：</strong>同樣是山手線大站，池袋房價比新宿便宜 30-40%。陽光城 60 樓展望台免費、周邊百貨/動漫店/拉麵街應有盡有。不想花大錢住新宿的人，池袋是最好的替代方案。
</div>
</div>

<h2 id="常見問題">❓ 東京住宿常見問題</h2>
<div class="faq-section">
<div class="faq-item">
<div class="faq-q">第一次去東京住哪裡最好？</div>
<div class="faq-a"><p>首推<strong>新宿</strong>。交通最方便（機場直達）、餐廳最多、換錢/購物/看醫生什麼都有。房價雖然比其他區貴一些，但省下的時間和交通費絕對值得。預算有限則選<strong>上野</strong>。</p></div>
</div>
<div class="faq-item">
<div class="faq-q">東京飯店房間為什麼那麼小？</div>
<div class="faq-a"><p>日本土地昂貴，東京尤甚。一般商務旅館的單人房約 10-12 坁（3-4 坪），行李打開後幾乎沒有多餘空間。建議選擇有行李寄存櫃的飯店，或者改訂「半雙人房」（semi-double）會稍微宽敞一點。</p></div>
</div>
<div class="faq-item">
<div class="faq-q">怎麼訂東京飯店最便宜？</div>
<div class="faq-a"><p>比價策略：<strong>Trip.com → Agoda → Booking.com → 飯店官網</strong>。Trip.com 中文介面+台灣付款最方便；Agoga 常有閃購；Booking.com 可以到店付款；部分連鎖飯店官網有會員獨家折扣（如東橫 INN 會員送免費早餐）。</p></div>
</div>
<div class="faq-item">
<div class="faq-q">需要住幾晚比較划算？</div>
<div class="faq-a"><p>東京合理行程至少 <strong>4-5 晚</strong>。少於 3 晚的話每天換飯店的打包時間和交通成本太高。週末（五六日）房價比平日貴 30-50%，如果能彈性調整日期，週一到週四入住可以省很多。</p></div>
</div>
<div class="faq-item">
<div class="faq-q">Check-in / Check-out 時間要注意什麼？</div>
<div class="faq-a"><p>日本飯店標準：<strong>Check-in 15:00 / Check-out 11:00</strong>。早到通常可以寄放行李（免費）。晚 check-out 要額外付費（約 ¥3,000-5,000/小時）。有些商務旅館提供 24 小時 Check-in（自助 kiosk），適合深夜航班抵達。</p></div>
</div>
</div>

<!-- CTA -->
<div class="cta-box-beautify">
<h3>🗾 需要更多東京旅遊建議？</h3>
<p>LINE 詢問行程規劃，24 小時內回覆</p>
<a class="btn-white" href="https://line.me/ti/g/NbNGnW4Eh6" rel="noopener noreferrer" target="_blank">💬 加入 LINE 詢問</a>
</div>
`;

// Replace the broken part: from 新宿 H2 to the start of footer
// The broken pattern is: <h2 id="新宿">...</h2>\n<div class="day-card">\n<h2 class="section-title">📖 延伸閱讀
const brokenPattern = /<h2 id="新宿">[\s\S]*?<h2 class="section-title">📖 延伸閱讀/;
const replacement = newContent.trim() + '\n\n<!-- RELATED POSTS -->\n<div class="day-card">\n<h2 class="section-title">📖 延伸閱讀';

html = html.replace(brokenPattern, replacement);

// === FIX 2: Close article-container properly before footer ===
// The footer is currently inside article-container div (missing </div></div>)
// Pattern: ...</a>\n</div>\n<footer class="site-footer">
// Should be: ...</a>\n</div>\n</div>\n<footer class="site-footer">
html = html.replace(
  /<\/a>\n<\/div>\n<footer class="site-footer">/,
  '</a>\n</div>\n</div>\n<footer class="site-footer">'
);

fs.writeFileSync(file, html, 'utf8');

// Verify
const verify = fs.readFileSync(file, 'utf8');
const vBodyStart = verify.indexOf('<body>');
const vFooterIdx = verify.indexOf('site-footer');
const vBody = verify.substring(vBodyStart, vFooterIdx);
console.log('File size:', verify.length, 'bytes');
console.log('H2 count:', (vBody.match(/<h2/g) || []).length);
console.log('FAQ items:', (vBody.match(/faq-item/g) || []).length);
console.log('Has 新宿 content:', vBody.includes('為什麼選新宿'));
console.log('Has 上野 content:', vBody.includes('為什麼選上野'));
console.log('Has 淺草 content:', vBody.includes('為什麼選淺草'));
console.log('Has 澀谷 content:', vBody.includes('為什麼選澀谷'));
console.log('Has 池袋 content:', vBody.includes('為什麼選池袋'));
console.log('Has FAQ:', vBody.includes('常見問題'));

// Check div balance
const opens = (vBody.match(/<div/g) || []).length;
const closes = (vBody.match(/<\/div>/g) || []).length;
console.log('Div balance: open=' + opens + ' close=' + closes + ' diff=' + (opens-closes));

// Check footer position - should NOT be inside article-container
const artClose = verify.lastIndexOf('</div>', vFooterIdx);
const beforeFooter = verify.substring(Math.max(0, vFooterIdx-100), vFooterIdx);
console.log('\nBefore footer:', JSON.stringify(beforeFooter));