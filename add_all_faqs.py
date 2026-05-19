import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

# All pages that need FAQs added (currently have 0-1 displayed FAQ items, need 5 total)
# Format: onclick for section-based pages, arrow format for article-container pages

new_faqs = {
    # Pages with 1 FAQ, onclick format (section-based)
    'busan-capsule.html': [
        ('膠囊列車體驗多久？', '一程約30分鐘，包含拍照時間全程約1小時。來回票比單程划算，建議購買來回套票含海雲台纜車。'),
        ('膠囊列車適合帶小孩嗎？', '可以！但3歲以下不建議（膠囊空間狹小會害怕）。4-7歲需家長陪同，8歲以上可以自己坐。有身高限制110cm以上。'),
        ('海雲台還有什麼好玩？', '①海雲台海灘散步②冬柏島看夜景③BLUE LINE PARK天空步道④青沙浦文化村⑤海雲台市場吃生魚片。建議安排半天到一天。'),
        ('釜山有什麼必買特產？', '①魚糕伴手禮（Samjin Amook）②蝦餅海苔③韓國護膚品（OLIVE YOUNG）④海苔製品⑤罐裝魚餅湯。機場免稅店也可以補貨。'),
        ('冬天去釜山會太冷嗎？', '1-2月均溫0-5°C，比首爾暖一些。海風較大需注意防風。冬天適合吃熱呼呼的猪肉湯飯和海鮮鍋，溫泉也很推薦（海雲台附近有Spa Land）。'),
    ],
    'hokkaido-winter.html': [
        ('北海道冬天幾天夠玩？', '最少5天4夜：札幌2天+小樽1天+富良野或旭川1天。若加旭山動物園和溫泉，建議7天6夜。冬天交通較慢，時間要預留充裕。'),
        ('北海道冬天租車安全嗎？', '有雪地駕駛經驗可以租車，車行會提供雪胎。但新手不建議，路面积雪結冰危險。推荐搭JR或巴士，北海道JR周遊券（Hokkaido Rail Pass）7天約¥16,000很划算。'),
        ('札幌雪祭什麼時候？', '每年2月上旬（通常2月5-12日），在大通公園舉行。有巨型雪雕和冰雕，晚上有燈光秀。建議提前3-6個月訂房，這段時間住宿價格翻倍。'),
        ('北海道冬天要帶什麼裝備？', '必帶：防風羽絨外套、保暖內衣（Heattech）、防滑雪靴、毛帽圍巾手套、暖暖包。選帶：雪鏡、防滑鞋套、暖暖貼。機場和便利店也能買到保暖用品。'),
        ('北海道有什麼必吃美食？', '①味噌拉麵（札幌）②海鮮丼（函館朝市）③湯咖喱（札幌）④成吉思汗烤肉（旭川）⑤白色戀人冰淇淋（小樽）⑥札幌啤酒。冬天吃熱騰騰的拉麵最幸福！'),
    ],
    'seoul-food.html': [
        ('首爾哪裡可以吃到正宗韓式烤肉？', '弘大「Maple Tree House」平價好吃、江南「Potful」豬五花肉專賣、明洞「姜虎東烤肉」連鎖品質穩定。預算每人₩15,000-30,000，建議提前用APP排隊。'),
        ('首爾咖啡廳推薦？', '弘大和聖水洞是咖啡廳聚集區。推薦：①聖水洞Cafe Onion ②弘大Born Coffee ③漢南洞Cheetah Electric。韓國咖啡廳氛圍感極強，拍照打卡必去。'),
        ('首爾街頭小吃必吃？', '①辣炒年糕（₩3,000）②魚糕串（₩1,000）③韓式煎餅（₩5,000）④紫菜包飯（₩2,000）⑤旋轉烤雞（₩8,000）。廣藏市場和明洞街頭小吃最多最集中。'),
        ('韓國有用餐禮儀嗎？', '長輩先動筷、不要用筷子插飯、喝酒要轉頭用手遮擋、吃烤肉時幫旁邊的人夾菜。基本禮儀不難，韓國人對外國人很包容，不用太緊張。'),
        ('首爾有素食選擇嗎？', '比以前多很多！弘大有純素食韓餐店，仁寺洞有素食寺院料理。用HappyCow APP可以搜到素食餐廳。便利商店有豆腐沙拉和蔬菜饭团可以備用。'),
    ],
    'tainan-food.html': [
        ('台南哪裡可以吃到虱目魚粥？', '安平區「周氏蝦捲」旁邊就有好幾家，市區「阿霞飯店」的虱目魚粥最有名但價格較高。平價選擇推薦永福路上的路邊攤，一碗NT$50-80超新鮮。'),
        ('台南甜湯推薦哪家？', '①「台南舊市場冰店」豆花和芋圓 ②「阿明冰店」芒果冰 ③「洪媽媽湯圓」花生湯 ④「新market湯圓」芝麻湯圓。夏天必吃冰，冬天喝熱湯圓，各有各的好。'),
        ('台南牛肉湯哪一家最好？', '「阿村牛肉湯」和「布莊牛肉湯」是兩大經典。阿村湯頭清甜、布莊肉質軟嫩。另外「南門牛肉湯」和「世合牛肉湯」也很受歡迎。每家風格不同，建議都試試。'),
        ('台南美食怎麼安排一天？', '早上5點吃牛肉湯→早餐後逛安平古堡→午餐吃蝦捲虱目魚→下午喝冰飲逛神農街→晚餐吃台南小吃（棺材板、碗粿、魚粥）→消夜割包或牛肉湯。一天吃5-6餐剛剛好。'),
        ('台南美食區域推薦？', '①安平區（蝦捲、蚵仔煎、海產粥）②西門路一帶（牛肉湯、鱔魚意麵）③國華街（小吃集中地）④神農街（文青咖啡+老屋）⑤花園夜市（週四六日）。不同區域不同風味。'),
    ],
    'kansai-pass.html': [
        ('關西機場到大阪市區怎麼去最便宜？', '最便宜：南海電鐵特急Rapi:t約¥1,490（40分鐘）。更便宜：南海電鐵普通車¥920（45分鐘）。JR關西機場快速¥1,170（最快但較貴）。若買關西周遊卡可含南海電鐵。'),
        ('大阪交通一日券值得買嗎？', '大阪周遊卡（Osaka Metro全線＋大阪巴士＋16個景點免費）1日¥2,800，去3個以上景點就回本。若只在市區移動搭地鐵，比買單程票划算。'),
        ('京都和奈良怎麼安排一起玩？', '建議：早上京都市區（清水寺、伏見稻荷）→下午搭近鐵到奈良（40分鐘）→看小鹿→傍晚回大阪。關西周遊卡可搭近鐵，非常方便。一天可以搞定京都精華+奈良。'),
        ('關西機場有免費Wi-Fi嗎？', '有！關西機場全區提供免費Wi-Fi「KIX-FREE-WIFI」。另外可以租行動Wi-Fi（一出關就取）或提前買eSIM。日本便利商店也有免費Wi-Fi可用。'),
        ('關西旅遊買什麼票券最省？', '行程只在大阪：買大阪周遊卡。大阪+京都+奈良：買關西周遊卡或JR關西地區鐵路周遊券。大阪+神戶：買JR神戶線一日券¥1,680。先排行程再決定買哪張票券。'),
    ],
    'hualien-taitung.html': [
        ('花蓮台東幾天最合適？', '最少3天2夜：Day1花蓮（太魯閣+七星潭）→Day2花東公路南下（清水斷崖+瑞穗牧場+伯朗大道）→Day3台東（綠島或都蘭）→回程。想玩更深度建議4-5天。'),
        ('花東自駕要注意什麼？', '①蘇花公路注意落石，下雨天別走 ②台11線部分路段窄，禮讓大型車 ③花東不少路段無手機信號，提前下載離線地圖 ④日落後避免走山路 ⑤加油站的間隔較遠，見到加油站就加滿。'),
        ('花蓮有什麼必吃美食？', '①公正街包子（早上排隊名店）②廟口紅茶③花蓮薯（扁鵲醬油旁邊）④原住民石板烤肉⑤海鮮（七星潭附近）⑥液香扁食。公正街和自強夜市是美食集中區。'),
        ('台東有什麼好玩的？', '①綠島（浮潛+溫泉+梅花鹿）②蘭嶼（潛水+環島）③都蘭海岸④池上便當（便當博物館）⑤多良車站（最美海景車站）⑥红叶温泉。台東適合慢活，不要排太滿行程。'),
        ('花蓮台東住宿推薦？', '花蓮：市區（交通便利、餐廳多）、七星潭（海景民宿）、太魯閣附近（山景靜謐）。台東：市區（平價）、都蘭（文青背包客）、綠島民宿（需提前預約）。花蓮住宿選擇比台東多，旺季務必提前1個月訂房。'),
    ],
    # Pages with 3-4 FAQs
    'japan-travel.html': [
        ('日本旅遊第一次去選哪裡？', '首選東京或大阪：交通便利、英文標示多、美食豐富。5天以內選東京（景點密集），7天以上可以東京+京都+大阪。有小孩推薦大阪（USJ+環球影城）。'),
        ('日本自由行一定要買JR Pass嗎？', '不一定！只在東京玩完全不需要。東京→大阪→京都→東京這種行程才值得買。2023年後JR Pass大幅漲價（7天¥50,000），短程反而比單程票貴。先算帳再決定。'),
    ],
    'southeast-asia.html': [
        ('東南亞旅遊要注意什麼安全問題？', '①選擇評價好的住宿 ②夜間避免偏僻地區 ③搭Grab取代街邊攬客 ④貴重物品放保險箱 ⑤喝瓶裝水不喝生水 ⑥注意交通安全（機車事故率高）。泰國和越南整體安全，基本常識即可。'),
        ('東南亞自由行機票怎麼買最便宜？', '提前2-3個月訂票、選週二週三出發、用Skyscanner比價、廉航（越捷、亞航、酷鳥）比傳統航空便宜50%以上。設價格提醒，機票降到心理價就下手。'),
    ],
    'taiwan-travel.html': [
        ('台灣國內機票怎麼買最便宜？', '提前2-4週訂票、選平日出發、用樂天或Trip.com比價。星宇航空和台灣虎航常有促銷。去花蓮/台東也可以搭火車代替飛機，時間差不多但風景更好。'),
        ('台灣旅遊推薦季節？', '全年皆宜！春天（3-4月）賞花、夏天（6-8月）去墾丁看海、秋天（10-11月）氣候最舒服、冬天（12-2月）泡溫泉。梅雨季（5-6月）和颱風季（7-9月）需注意天氣。'),
    ],
    'korea-budget.html': [
        ('韓國機票最便宜什麼時候買？', '提前2-3個月、選週二週三出發、廉航（德威、易斯達、釜山航空）比大航便宜30-50%。避開農曆新年、中秋連假和暑假旺季。用Skyscanner設價格提醒抓低價。'),
        ('韓國住宿怎麼選最划算？', '首爾：弘大和東大門的Guest House最平價（NT$500-1,500/晚），明洞位置好但較貴。釜山：海雲塔附近民宿CP值高。用Agoda或HotelsCombined比價，韓國住宿比日本便宜不少。'),
    ],
    'travel-tools.html': [
        ('出國旅行一定要帶什麼？', '必帶：護照、機票住宿確認單（截圖備用）、海外旅遊保險、信用卡+少許現金、行動電源、轉換插頭。選帶：常備藥、防盜腰包、壓縮袋。最重要是保險，醫療費在國外可能天價。'),
        ('旅行保險怎麼選？', '重點看三項：①海外醫療保額（建議NT$100萬以上）②緊急醫療轉送 ③行程取消/延誤理賠。富邦、國泰、安達的旅遊險都不錯，用比價網站比較。一週旅程保費約NT$500-1,200。'),
        ('海外上網最省錢的方式？', '短期旅行推薦eSIM（日本5天NT$200起，韓國NT$250起），出發前裝好落地就有網。長期或多國：租行動Wi-Fi（每天NT$100-150）。eSIM好處是不用還設備、不佔一個設備。'),
        ('機場免稅店比市區便宜嗎？', '不一定！化妝品和香水通常便宜10-20%，但電子產品未必。韓國仁川免稅店化妝品最划算，日本成田免稅店巧克力便宜。建議先記好市區價格，到免稅店再比。'),
        ('旅行行李怎麼打包最省空間？', '①捲式收納比摺疊省30%空間 ②真空壓縮袋裝外套 ③鞋內塞襪子 ④貴重物品隨身帶 ⑤用旅行分裝瓶裝洗沐用品。手提行李7kg內盡量搞定，省托運費又省等行李時間。'),
    ],
}

fixed = 0

for fname, faqs in new_faqs.items():
    if not os.path.exists(fname):
        print(f"SKIP {fname}: not found")
        continue

    with open(fname, encoding='utf-8') as f:
        c = f.read()

    existing_count = len(re.findall(r'class="faq-item"', c))

    # Generate new FAQ HTML
    # Detect format: arrow format vs onclick format
    has_arrow = '<span class="arrow">' in c
    has_onclick = 'onclick="this.classList.toggle' in c

    new_html = ''
    for q, a in faqs:
        if has_onclick:
            new_html += f'''<div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>
'''
        elif has_arrow:
            new_html += f'''      <div class="faq-item">
        <div class="faq-q">{q}<span class="arrow">▼</span></div>
        <div class="faq-a">{a}</div>
      </div>
'''
        else:
            new_html += f'''<div class="faq-item">
  <div class="faq-q">{q}</div>
  <div class="faq-a">{a}</div>
</div>
'''

    # Find insertion point: after the last existing faq-item's closing </div></div>
    items = list(re.finditer(r'class="faq-item"', c))
    if not items:
        # No FAQ items yet, insert after FAQ h2
        h2_match = re.search(r'<h2[^>]*>.*?FAQ.*?</h2>', c, re.IGNORECASE)
        if not h2_match:
            print(f"SKIP {fname}: no FAQ h2 found")
            continue
        insert_pos = h2_match.end()
        c = c[:insert_pos] + '\n' + new_html + c[insert_pos:]
    else:
        last_item = items[-1]
        after = c[last_item.start():]
        close_match = re.search(r'</div>\s*</div>', after)
        if not close_match:
            print(f"SKIP {fname}: can't find faq-item closing")
            continue
        insert_pos = last_item.start() + close_match.end()
        c = c[:insert_pos] + '\n' + new_html + c[insert_pos:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)

    new_total = existing_count + len(faqs)
    print(f"DONE {fname}: {existing_count} -> {new_total} FAQs (+{len(faqs)})")
    fixed += 1

print(f"\nTotal: {fixed} pages fixed")
