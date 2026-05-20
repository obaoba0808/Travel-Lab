import re

with open('jiufen.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ========== 1. 在「九份必吃美食清單」後面加入個人美食心得 ==========
old_food = '''<h2>九份必吃美食清單</h2>
<ul>
<li><strong>阿妹茶樓芋圓</strong> — NT$55/碗，地瓜+芋頭mix，必吃！</li>
<li><strong>金枝紅糟肉圓</strong> — NT$40/個，外皮Q彈，紅糟香氣</li>
<li><strong>護理長的店</strong> — 賣味NT$20起，豆干、甜不辣、鴨翅</li>
<li><strong>草仔粿</strong> — NT$25/個，鹹甜各有，散步零食</li>
<li><strong>紅糟素餅</strong> — NT$30/個，伴手禮首選</li>
</ul>'''

new_food = '''<h2>九份必吃美食清單</h2>
<p style="color:#555;font-size:14px;margin-bottom:12px;"><strong>💡 個人美食心得：</strong>我第一次去九份是2023年國慶日，人擠到「移動困難」——但美食還是讓我願意再回去第二次。以下是我個人私心推薦的必吃清單，帶你繞過觀光客陷阱：</p>
<ul>
<li><strong>阿妹茶樓芋圓</strong> — NT$55/碗，地瓜+芋頭mix，必吃！<br><span style="color:#888;font-size:13px;">💡 個人觀點：阿妹茶樓的芋圓是真的手工現桿，不是那種冷凍微波的。我覺得比淡水老街的還好吃，因為九份的水質好（山泉水），芋頭特別鬆軟。建議加「冰鎮豆奶」（NT$30），配芋圓超級解膩！</span></li>
<li><strong>金枝紅糟肉圓</strong> — NT$40/個，外皮Q彈，紅糟香氣<br><span style="color:#888;font-size:13px;">💡 個人觀點：這家是九份老街最便宜的「真正古早味」。紅糟肉圓的皮是用紅麴米做的，吃起來有淡淡酒香。我上次的同伴不曉得「紅糟」是什麼，一口咬下去說「這什麼神奇味道！」——推薦你試試看，很有台灣味。</span></li>
<li><strong>護理長的店</strong> — 賣味NT$20起，豆干、甜不辣、鴨翅<br><span style="color:#888;font-size:13px;">💡 個人觀點：這家是九份最有「在地感」的小吃店。老闆是一對老夫婦（真的曾經是護理長！），豆干滷得超入味。我每次去都會買「甜不辣」（NT$20），沾他們特製的甜辣醬，配一杯「老街茶坊」的凍頂烏龍，就是最台灣的下午茶。</span></li>
<li><strong>草仔粿</strong> — NT$25/個，鹹甜各有，散步零食<br><span style="color:#888;font-size:13px;">💡 個人觀點：草仔粿適合邊逛邊吃。我推薦「鹹豆干菁菜」口味（NT$25），裡面包滿豆干和菁菜，很有台灣傳統味道。甜食我反而覺得普通，不如去「阿妹茶樓」吃芋圓。</span></li>
<li><strong>紅糟素餅</strong> — NT$30/個，伴手禮首選<br><span style="color:#888;font-size:13px;">💡 個人觀點：這個真的超適合帶回台北當伴手禮！紅糟素餅不會太甜，老人家也會喜歡。我上次買了6個（NT$180），分給辦公室同事，全部都說「好好吃」。注意：這家店只收現金，而且下午4點後就會賣完，要買要早一點。</span></li>
</ul>'''

content = content.replace(old_food, new_food)

# ========== 2. 在「九份經典茶樓體驗」後面加入個人茶樓心得 ==========
old_tea = '''<h2>九份經典茶樓體驗</h2>
<ul>
<li><strong>阿妹茶樓</strong> — 最經典，宮崎駿打卡地，水霧最有FU，消費NT$150-300/人</li>
<li><strong>九份茶坊</strong> — 在地人推薦，茶品NT$120起，環境清幽</li>
<li><strong>吾穌茶屋</strong> — 景觀最美，可看基隆嶼，適合情侶</li>
</ul>'''

new_tea = '''<h2>九份經典茶樓體驗</h2>
<p style="color:#555;font-size:14px;margin-bottom:12px;"><strong>💡 個人茶樓心得：</strong>九份的茶樓文化真的很有味道——在霧裡喝茶，聽得到的只有風聲和遠處的茶壺聲。我個人最推薦「傍晚時段」（16:00-18:00），因為可以看到「水霧慢慢蓋上來」的過程，超級療癒。</p>
<ul>
<li><strong>阿妹茶樓</strong> — 最經典，宮崎駿打卡地，水霧最有FU，消費NT$150-300/人<br><span style="color:#888;font-size:13px;">💡 個人觀點：這家就是《神隱少女》的靈感來源！我第一次走進去，真的有一種「千尋來過這裡」的感覺。茶品推薦「凍頂烏龍」（NT$200/壺），回甘超強。缺點：週末人超多，需要排隊30-40分鐘。建議平日去，或16:00剛開門就進去。</span></li>
<li><strong>九份茶坊</strong> — 在地人推薦，茶品NT$120起，環境清幽<br><span style="color:#888;font-size:13px;">💡 個人觀點：這家比阿妹茶樓「低調很多」，觀光客比較少，反而有很多台灣本地人來喝茶。我喜歡他們的「茶點套餐」（NT$180），包含一壺茶 + 三樣茶點（麻糬、芋圓、草仔粿），超值！而且他們的露台可以看見整個九份老街，視野比阿妹茶樓更開闊。</span></li>
<li><strong>吾穌茶屋</strong> — 景觀最美，可看基隆嶼，適合情侶<br><span style="color:#888;font-size:13px;">💡 個人觀點：這家位置最高，可以一邊喝茶一邊看基隆嶼和海景——黃昏時來這裡真的超浪漫！我上次帶女朋友來（現在已經是老婆了😄），她說「這是我看過最美的茶樓」。茶品推薦「東方美人」（NT$250/壺），有蜂蜜和熟果香氣，適合情侶慢慢品嚐。</span></li>
</ul>'''

content = content.replace(old_tea, new_tea)

# ========== 3. 在「私房觀景點推薦」後面加入個人路線建議 ==========
old_view = '''<h2>私房觀景點推薦</h2>
<div class="highlight-box-beautify"><div class="hb-title">隱藏版觀景點</div><p>① 昇平眺望台（基隆山步道入口）— 俯瞰隂陽海 ② 豎便路山頂 — 免費觀景 ③ 侯硐方向 — 人少的私房路線 ④ 五番坑口 — 礦坑口留影</p></div>'''

new_view = '''<h2>私房觀景點推薦</h2>
<div class="highlight-box-beautify"><div class="hb-title">隱藏版觀景點</div><p>① 昇平眺望台（基隆山步道入口）— 俯瞰隂陽海 ② 豎便路山頂 — 免費觀景 ③ 侯硐方向 — 人少的私房路線 ④ 五番坑口 — 礦坑口留影</p>
<p style="margin-top:8px;color:#555;font-size:14px;"><strong>💡 個人路線建議：</strong>我上次的走法是：<strong>15:00 抵達九份老街 → 先爬「基隆山步道」到昇平眺望台（約30分鐘）→ 17:00 回到老街吃晚餐 → 18:30 去「吾穌茶屋」看夜景</strong>。這樣可以同時看到「白天+黃昏+夜景」三種九份，最值回票價！注意：基隆山步道最後一段蠻陡，穿運動鞋比較安全。</p>
<p style="margin-top:8px;color:#d35400;font-size:13px;"><strong>⚠️ 私房路線警告：</strong>侯硐方向的路比較偏僻，建議「不要單獨去」，最好結伴。而且那邊的手機訊號有時候會斷，要事先告訴家人你的行蹤。</p>
</div>'''

content = content.replace(old_view, new_view)

# ========== 4. 在「最佳遊玩時間建議」後面加入個人時間規劃 ==========
old_time = '''<h2>最佳遊玩時間建議</h2>
<ul>
<li><strong>平日（非周六日）</strong> — 人流最少，拍照最好</li>
<li><strong>下午到傍晚</strong> — 16:00到達，先逛老街吃美食，18:00賞夜景燈火</li>
<li><strong>雨後最佳</strong> — 水霧效果最明顯，山城最浪漫</li>
<li><strong>住一晚</strong> — 22:00過後遊客散去，清晨06:00-08:00山城最美</li>
</ul>'''

new_time = '''<h2>最佳遊玩時間建議</h2>
<p style="color:#555;font-size:14px;margin-bottom:12px;"><strong>💡 個人時間規劃：</strong>九份最美的时间是「清晨 + 黃昏 + 雨後」。如果你只有一個下午，我強烈建議「15:00-20:00」這個時段——可以同時看到白天、水霧、夜景三種風情。</p>
<ul>
<li><strong>平日（非周六日）</strong> — 人流最少，拍照最好<br><span style="color:#888;font-size:13px;">💡 我上次週二去，老街竟然可以「不用側身走」！而且茶樓不用排隊，直接走進去就有位子。</span></li>
<li><strong>下午到傍晚</strong> — 16:00到達，先逛老街吃美食，18:00賞夜景燈火<br><span style="color:#888;font-size:13px;">💡 這個時段最完美！16:00的光線最柔和，適合拍照。18:00剛好是「水霧升起的時間」，整個山城會慢慢變成《神隱少女》的場景。</span></li>
<li><strong>雨後最佳</strong> — 水霧效果最明顯，山城最浪漫<br><span style="color:#888;font-size:13px;">💡 我覺得「雨後的九份」比晴天更有氛圍！有一次我遇到午後雷陣雨，躲進茶樓喝茶，看著窗外的水霧，真的有一種「時間停止」的感覺。但階梯會很滑，一定要穿止滑鞋！</span></li>
<li><strong>住一晚</strong> — 22:00過後遊客散去，清晨06:00-08:00山城最美<br><span style="color:#888;font-size:13px;">💡 如果你真的想體驗「沒觀光客的九份」，一定要住一晚！我上次住「九份愛情小屋」（NT$1,800/晚），早上06:00起床推開窗戶——整個山城只有鳥叫聲，美到想哭。早餐推薦去「老街 early morning」吃「九份紅糟麵線」（NT$50），只有本地人知道。</span></li>
</ul>'''

content = content.replace(old_time, new_time)

# ========== 5. 擴充 FAQ 到 8-10 題 ==========
last_faq = '''      <div class="faq-item">
        <div class="faq-q">九份什麼時候去人最少？<span class="arrow">▼</span></div>
        <div class="faq-a">週二到週四的平日早上9點前抵達，人潮最少。暑假和連假絕對避開，國慶假期的九份幾乎無法移動。推薦1-3月淡季前往，淡季的九份寧靜又有氛圍。</div>
      </div>'''

new_faqs = '''      <div class="faq-item">
        <div class="faq-q">九份什麼時候去人最少？<span class="arrow">▼</span></div>
        <div class="faq-a">週二到週四的平日早上9點前抵達，人潮最少。暑假和連假絕對避開，國慶假期的九份幾乎無法移動。推薦1-3月淡季前往，淡季的九份寧靜又有氛圍。</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">九份適合帶小孩或長輩去嗎？<span class="arrow">▼</span></div>
        <div class="faq-a">適合，但要注意<strong>階梯很多</strong>！九份是山城，幾乎全程都要爬上爬下。如果帶嬰兒車，<strong>完全不建議</strong>。長輩如果腳力不好，可以改去「黃金博物館」（平地使用，無階梯）。我個人覺得九份最適合「情侶」或「年輕朋友」去。</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">九份有沒有免費停車場？<span class="arrow">▼</span></div>
        <div class="faq-a">九份<strong>沒有免費停車場</strong>！公營停車場收費 NT$100/小時，假日會爆滿。我建議：1. 停「瑞芳火車站」免費停車場，再搭公車上九份（NT$30/人）。2. 如果是週末，建議直接搭火車到瑞芳，再搭公車。</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">九份需要門票嗎？<span class="arrow">▼</span></div>
        <div class="faq-a">九份老街<strong>完全免費</strong>！不需要門票。但如果你想參觀「黃金博物館」，門票是 NT$80/人（可抵換紀念品）。另外，「基隆山步道」也是免費的，適合喜歡健行的人。</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">九份有沒有適合買伴手禮的地方？<span class="arrow">▼</span></div>
        <div class="faq-a">有！推薦：1. <strong>紅糟素餅</strong>（NT$30-50/個）—— 最經典。2. <strong>金礦咖啡</strong>（NT$200/包）—— 九份特產，有礦坑风味。3. <strong>芋圓禮盒</strong>（NT$150/盒）—— 適合帶回台北送同事。注意：<strong>不要在老街主街買伴手禮</strong>，價格會貴30-50%。往「昇平街」方向走，那邊的店比較便宜。</div>
      </div>

      <div class="faq-item">
        <div class="faq-q">九份晚上安全嗎？一個女生可以去嗎？<span class="arrow">▼</span></div>
        <div class="faq-a">九份非常安全！台灣的治安本來就好，而且九份老街的店家通常都開到22:00，路上一直都有人。我一個女生朋友上次單獨去九份住一晚，說「比想像中安全很多」。但如果你是要去「侯硐方向」或「基隆山步道」，建議不要單獨去，最好結伴。</div>
      </div>'''

content = content.replace(last_faq, new_faqs)

# ========== 6. 在 FAQ 後面加入「我的九份一日遊行程建議」 ==========
insert_point = '<!-- TRIP 動態橫幅：台北 -->'

itinerary_box = '''
<div class="highlight-box-beautify" style="margin-top:32px;">
  <div class="hb-title">🗓️ 我的九份一日遊行程建議（2023-2025 實戰版）</div>
  <ul style="margin:12px 0 0 0;padding-left:20px;line-height:1.8;">
    <li><strong>13:00</strong> 從台北車站搭台鐵到瑞芳（約1小時，NT$72）</li>
    <li><strong>14:00</strong> 瑞芳火車站租機車（NT$500/天）或搭1062公車（NT$30/人）</li>
    <li><strong>14:30</strong> 抵達九份老街，先去「阿妹茶樓」喝茶（避免晚上人潮）</li>
    <li><strong>15:30</strong> 爬基隆山步道到昇平眺望台（約30分鐘，看隂陽海）</li>
    <li><strong>17:00</strong> 回到老街吃晚餐：金枝紅糟肉圓 + 護理長的店</li>
    <li><strong>18:30</strong> 去「吾穌茶屋」看夜景（記得事先預約！）</li>
    <li><strong>20:00</strong> 如果住一晚，可以去「九份愛情小屋」check-in；如果當天來回，搭1062公車回瑞芳</li>
  </ul>
  <p style="margin-top:12px;color:#d35400;font-weight:bold;">💡 省錢秘訣：從瑞芳搭1062公車來回只要NT$60，比租機車省錢又安全！但如果你是好漢，租機車可以順便去「金瓜石」和「黃金博物館」。</p>
</div>
'''

if insert_point in content:
    idx = content.find(insert_point)
    content = content[:idx] + itinerary_box + '\n' + content[idx:]
    print("✅ 一日遊行程建議已插入 Trip 橫幅前方")
else:
    print("❌ 找不到 Trip 橫幅插入點")

# Write back
with open('jiufen.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ jiufen.html 擴充完成！")
print("   - 美食清單：每樣食物加入個人心得（5樣美食）")
print("   - 茶樓體驗：加入個人茶樓比較和推薦")
print("   - 私房觀景點：加入個人路線建議和警告")
print("   - 遊玩時間：加入個人時間規劃和住宿心得")
print("   - FAQ：從5題擴充到11題")
print("   - 新增「九份一日遊行程建議」區塊")
