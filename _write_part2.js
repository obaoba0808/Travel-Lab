const fs = require('fs');
const path = require('path');

const pythonCode = `

# =============================================================================
# Part 2: Korea PDF Generators
# =============================================================================

def gen_seoul_food():
    """Generate Seoul Food Map PDF - 韓國首爾美食地圖"""
    story = []
    
    # Cover Page
    story += make_cover('首爾美食地圖', '2026 最新版')
    
    # Section 1: Myeongdong Food Overview
    story.append(Paragraph('明洞美食總覽', h1))
    story.append(Paragraph('明洞是首爾最著名的美食街區，聚集了傳統韓式料理、街頭小吃與現代咖啡廳。從明洞站出口步行5分鐘內，就能找到超過50家特色餐廳。本攻略精選15家必吃餐廳，涵蓋烤肉、部隊鍋、韓式炸雞與甜點飲料，價格區間從每人50元到800元台幣不等，適合各種預算的旅客。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['餐廳名稱', '類型', '人均價格(台幣)', '推薦度'],
        ['明洞餃子', '韓式湯餃', '250-350', '★★★★★'],
        ['土俗村參雞湯', '參雞湯', '300-400', '★★★★★'],
        ['N首爾塔韓式烤肉', '烤肉', '600-800', '★★★★☆'],
        ['校村炸雞', '炸雞', '200-300', '★★★★☆'],
        ['雪冰咖啡廳', '甜點飲料', '150-250', '★★★★☆'],
        ['明洞街頭小吃攤', '街頭小吃', '50-150', '★★★★★'],
    ]
    story.append(make_table(['餐廳名稱', '類型', '人均價格(台幣)', '推薦度'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('美食小撇步', [
        '建議避開用餐尖峰時段（12:00-13:30, 18:00-19:30）',
        '部分餐廳需提前電話預約，尤其是週末',
        '街頭小吃攤現金支付較方便，建議準備足夠韓元',
        '明洞餃子與土俗村參雞湯經常排隊，可選擇非尖峰時段前往',
    ]))
    
    # Section 2: Must-Try Street Food
    story.append(Paragraph('必吃街頭小吃', h2))
    story.append(Paragraph('首爾的街頭小吃文化豐富多元，明洞、東大門與弘大商圈都有著名的街頭美食集中區。推薦嘗試辣炒年糕（떡볶이）、魚板湯（어묵）、糖餅（호떡）與韓式煎餅（전）。這些小吃不僅價格親民，更能體驗在地人的飲食文化。平均每樣小吃價格約2,000-4,000韓元（約50-100台幣）。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['小吃名稱', '韓文', '價格(韓元)', '熱量估計'],
        ['辣炒年糕', '떡볶이', '3,000-4,000', '中等'],
        ['魚板湯', '어묵', '2,000-3,000', '低'],
        ['糖餅', '호떡', '2,500-3,500', '高'],
        ['韓式煎餅', '전', '4,000-6,000', '中等'],
        ['烤魷魚', '오징어구이', '5,000-7,000', '低'],
    ]
    story.append(make_table(['小吃名稱', '韓文', '價格(韓元)', '熱量估計'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Restaurant Details
    story.append(Paragraph('精選餐廳詳細介紹', h2))
    story.append(Paragraph('明洞餃子（명동교자）成立於1960年代，是明洞最具代表性的老字號餐廳。招牌菜為手工湯餃與刀削麵，湯頭鮮美，餃子內餡飽滿多汁。營業時間為10:30-21:30，週日公休。土俗村參雞湯（토속촌 삼계탕）位於景福宮附近，以藥膳參雞湯聞名，整隻童子雞腹中填入糯米、人參、紅棗與蒜頭，燉煮4小時以上，湯頭濃郁滋補。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('預算規劃建議', [
        '經濟型：每日餐飲預算 300-500 台幣（以街頭小吃與平價餐廳為主）',
        '中檔型：每日餐飲預算 600-1000 台幣（包含1-2次烤肉或部隊鍋）',
        '奢華型：每日餐飲預算 1200-2000 台幣（包含高級韓牛烤肉與米其林餐廳）',
        '建議準備現金比例：餐飲費用的30%以現金支付較為方便',
    ]))
    
    # Section 4: Food Map and Transportation
    story.append(Paragraph('美食地圖與交通指南', h2))
    story.append(Paragraph('本節提供明洞、弘大、江南三大美食區域的地圖與交通資訊。明洞站（地鐵4號線）周邊步行10分鐘內可達所有推薦餐廳。弘大入口站（地鐵2號線）周邊以德式香腸、創意料理與主題咖啡廳聞名。江南站（地鐵2號線）則有高檔烤肉店與精緻咖啡廳。建議購買T-money卡，方便搭乘地鐵與公車。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['區域', '地鐵站', '必吃特色', '步行時間'],
        ['明洞', '明洞站(4號線)', '湯餃、參雞湯、街頭小吃', '5-10分鐘'],
        ['弘大', '弘大入口站(2號線)', '德式香腸、創意料理、咖啡廳', '5-15分鐘'],
        ['江南', '江南站(2號線)', '高檔烤肉、精緻甜點', '10-20分鐘'],
        ['東大門', '東大門歷史文化公園站(2/4/5號線)', '夜市小吃、24小時餐廳', '5-10分鐘'],
    ]
    story.append(make_table(['區域', '地鐵站', '必吃特色', '步行時間'], tbl_data3))
    
    # CTA
    story += make_cta()
    
    return story


def gen_busan_capsule():
    """Generate Busan Capsule Guide PDF - 釜山膠囊列車預約攻略"""
    story = []
    
    # Cover Page
    story += make_cover('釜山膠囊列車預約攻略', '2026 完整預約教學')
    
    # Section 1: Overview
    story.append(Paragraph('釜山膠囊列車完整指南', h1))
    story.append(Paragraph('釜山膠囊列車（Busan Air Cruise）是韓國釜山廣安里海灘的標誌性觀光設施，於2020年重新開幕。這是一條全長約2公里的海上纜車路線，連接海雲台尾浦碼頭與冬柏島，全程約15-20分鐘。膠囊車廂為透明玻璃地板設計，可360度欣賞釜山海岸線、廣安大橋與海雲台夜景。本攻略提供完整預約流程、票價比較、最佳搭乘時段與攝影技巧。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['票種', '成人票價(韓元)', '兒童票價(韓元)', '台幣約略價格'],
        ['單程票（一般車厢）', '17,000', '12,000', '380 / 270'],
        ['來回票（一般車厢）', '24,000', '18,000', '540 / 400'],
        ['單程票（水晶車廂）', '22,000', '16,000', '490 / 360'],
        ['來回票（水晶車廂）', '30,000', '22,000', '670 / 490'],
        ['快速通關券', '35,000', '25,000', '780 / 560'],
    ]
    story.append(make_table(['票種', '成人票價(韓元)', '兒童票價(韓元)', '台幣約略價格'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('預約小撇步', [
        '強烈建議提前線上預約，現場購票經常售罄',
        '水晶車廂（透明地板）最受歡迎，建議提前3-7天預約',
        '日落時段（17:00-19:00）景色最美，但也是最熱門時段',
        '週間上午時段人潮較少，可享更舒適的搭乘體驗',
        '購買來回票比兩張單程票便宜約10%',
    ]))
    
    # Section 2: Reservation Process
    story.append(Paragraph('線上預約完整流程', h2))
    story.append(Paragraph('釜山膠囊列車官方網站提供多語言介面（含中文），預約流程簡單明瞭。首先進入官網（busanaircruise.com），選擇「線上預約」並註冊會員。接著選擇搭乘日期、時段、票種與數量。付款支援信用卡（VISA/MasterCard/JCB）與PayPal。預約成功後會收到電子票券Email，現場出示QR Code即可搭乘。建議列印實體票券或確保手機網路暢通。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['步驟', '操作說明', '注意事項'],
        ['1. 進入官網', '前往 busanaircruise.com', '建議使用電腦版網頁'],
        ['2. 選擇日期', '挑選搭乘日期與時段', '熱門時段需提前預約'],
        ['3. 選擇票種', '一般車廂或水晶車廂', '水晶車廂視野較佳'],
        ['4. 填寫資料', '輸入護照英文名與人數', '姓名需與護照一致'],
        ['5. 付款', '信用卡或 PayPal', '付款後不可退款'],
        ['6. 收到票券', 'Email 收到 QR Code', '建議截圖保存'],
    ]
    story.append(make_table(['步驟', '操作說明', '注意事項'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Best Viewing Times
    story.append(Paragraph('最佳搭乘時段推薦', h2))
    story.append(Paragraph('釜山膠囊列車全年無休（僅農曆春節暫停），營運時間為10:00-22:00（最後入場21:30）。不同時段有不同風景特色：上午時段（10:00-12:00）光線充足，適合拍攝清晰海景；下午時段（14:00-16:00）可拍攝藍天白雲與海岸線對比；日落時段（17:00-19:00）可欣賞夕陽西下與漸層天空；夜間時段（19:00-22:00）則能欣賞廣安大橋燈光秀與釜山夜景。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('攝影技巧', [
        '使用廣角鏡頭（24-35mm）拍攝車廂內部與海景',
        '透明地板拍攝時注意反光，可穿深色衣服減少倒影',
        '日落時段使用HDR模式平衡亮部與暗部',
        '夜間拍攝建議使用三腳架或穩定器',
        '避免穿著白色衣服，容易造成玻璃反光',
    ]))
    
    # Section 4: Transportation and Nearby Attractions
    story.append(Paragraph('交通方式與周邊景點', h2))
    story.append(Paragraph('釜山膠囊列車尾浦站距離地鐵2號線海雲台站約15分鐘步行距離。也可搭乘公車至「尾浦碼頭」站下車。冬柏島站則可從地鐵2號線冬柏站步行10分鐘抵達。周邊景點包含海雲台海水浴場（步行5分鐘）、廣安里海水浴場（步行15分鐘）、BIFF廣場（車程20分鐘）。建議安排半天行程，上午搭乘膠囊列車，下午遊覽海雲台周邊景點。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['交通方式', '路線說明', '所需時間', '費用'],
        ['地鐵', '2號線海雲台站→步行', '15分鐘', '約1,400韓元'],
        ['公車', '海雲台站搭乘公車至尾浦碼頭', '10分鐘', '約1,300韓元'],
        ['計程車', '從海雲台站出發', '5分鐘', '約5,000-7,000韓元'],
        ['步行', '從海雲台海水浴場出發', '15-20分鐘', '免費'],
    ]
    story.append(make_table(['交通方式', '路線說明', '所需時間', '費用'], tbl_data3))
    
    # CTA
    story += make_cta()
    
    return story


def gen_jeju_driving():
    """Generate Jeju Driving Route PDF - 濟州島自駕路線"""
    story = []
    
    # Cover Page
    story += make_cover('濟州島自駕路線', '2026 精選5條必走路線')
    
    # Section 1: Overview
    story.append(Paragraph('濟州島自駕完整攻略', h1))
    story.append(Paragraph('濟州島是韓國最大的島嶼，面積約1,849平方公里，環島公路全長約181公里。自駕是遊覽濟州島最自由便利的方式，可以隨意停靠景點、調整行程節奏。本攻略精選5條自駕路線，涵蓋東部、西部、南部、北部與環島路線，每條路線規劃2-3天行程。同時提供租車流程、交通規則、停車資訊與路況提醒，讓您的濟州自駕之旅安全順利。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['路線名稱', '天數', '總里程(km)', '適合族群'],
        ['東部海岸路線', '2天1夜', '120', '第一次來濟州'],
        ['西部田園路線', '2天1夜', '110', '喜歡自然風景'],
        ['南部文化路線', '1天', '80', '親子同遊'],
        ['北部都市路線', '1天', '60', '購物美食愛好者'],
        ['環島深度路線', '3天2夜', '200', '深度旅遊玩家'],
    ]
    story.append(make_table(['路線名稱', '天數', '總里程(km)', '適合族群'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('租車注意事項', [
        '台灣遊客需準備國際駕照（IDP）與台灣駕照正本',
        '建議提前線上預約租車，現場租車價格較高',
        '濟州島加油站多為自助式，建議學習韓文加油操作流程',
        '停車場收費約每小時1,000-2,000韓元，部分景點有免費停車場',
        '濟州島限速：市區50km/h，郊區80km/h，高速公路100km/h',
    ]))
    
    # Section 2: Route Details - Eastern Route
    story.append(Paragraph('路線一：東部海岸路線（2天1夜）', h2))
    story.append(Paragraph('東部路線是濟州島最經典的自駕路線，包含城山日出峰、涉地可支、牛島與表善海水浴場等知名景點。第一天從濟州機場出發，沿著1100道路往東部行駛，約1小時抵達城山日出峰。下午遊覽涉地可支與牛島，晚上住宿城山或表善地區。第二天前往萬丈窟熔岩洞與水族館，下午返回濟州市區。全程約120公里，預計駕駛時間4-5小時（不含景點停留）。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['景點', '停留時間', '停車資訊', '門票費用'],
        ['城山日出峰', '2-3小時', '有收費停車場(2,000韓元)', '5,000韓元'],
        ['涉地可治', '1-2小時', '免費停車場', '免費'],
        ['牛島', '3-4小時', '渡輪停車場(5,000韓元)', '渡輪來回8,000韓元'],
        ['萬丈窟', '1-2小時', '有收費停車場(2,000韓元)', '4,000韓元'],
        ['表善海水浴場', '1-2小時', '免費停車場', '免費'],
    ]
    story.append(make_table(['景點', '停留時間', '停車資訊', '門票費用'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Car Rental Process
    story.append(Paragraph('租車流程與費用估算', h2))
    story.append(Paragraph('濟州島租車公司眾多，推薦使用RentalCars、Klook或直接在濟州機場櫃檯租車。經濟型小客車（如Hyundai Avante）每日租金約50,000-70,000韓元（約1,100-1,600台幣），包含基本保險。若升級至SUV或進口車，每日租金約80,000-120,000韓元。建議購買全險（CDW+TPL），每日約增加10,000-15,000韓元。油費預算：環島一圈約需加油1-2次，每次約60,000-80,000韓元。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('自駕安全提醒', [
        '濟州島多彎道與坡道，請減速慢行注意號誌',
        '部分景點路段無人行道，遊客穿梭需特別小心',
        '雨天路面濕滑，尤其火山岩地形容易打滑',
        '導航建議使用韓文版Naver Map或Kakao Map',
        '緊急聯絡電話：112（警察）、119（消防救護）',
    ]))
    
    # Section 4: Recommended 3-Day Itinerary
    story.append(Paragraph('推薦3天2夜自駕行程', h2))
    story.append(Paragraph('若時間充裕，推薦安排3天2夜的環島自駕行程。第一天：濟州市區→翰林公園→Aqua Planet濟州→城山日出峰（住宿城山）。第二天：牛島→萬丈窟→四季之星→正房瀑布→大浦柱狀節理（住宿西歸浦）。第三天：Hello Kitty島→Eco Land→東門市場→返程。此行程涵蓋濟州島精華景點，每天駕駛時間控制在3-4小時內，留有充足時間遊覽與休息。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['天數', '上午行程', '下午行程', '住宿地點'],
        ['Day 1', '濟州市區→翰林公園', 'Aqua Planet→城山日出峰', '城山/表善'],
        ['Day 2', '牛島→萬丈窟', '四季之星→正房瀑布', '西歸浦'],
        ['Day 3', 'Hello Kitty島→Eco Land', '東門市場→返程', '無'],
    ]
    story.append(make_table(['天數', '上午行程', '下午行程', '住宿地點'], tbl_data3))
    
    # CTA
    story += make_cta()
    
    return story


def gen_korea_budget():
    """Generate Korea Budget Sheet PDF - 韓國旅遊預算表"""
    story = []
    
    # Cover Page
    story += make_cover('韓國旅遊預算表', '2026 完整費用規劃')
    
    # Section 1: Overview
    story.append(Paragraph('韓國旅遊預算完整規劃', h1))
    story.append(Paragraph('規劃韓國旅遊預算需要考慮多項因素：旅遊天數、城市選擇、住宿等級、餐飲標準與購物預算。本預算表以7天6夜行程為基準，分為經濟型、中檔型與奢華型三種預算等級，詳細列出各項費用明細。同時提供匯率換算、省錢技巧與預算調整建議，幫助您打造最適合的韓國旅遊財務計畫。所有金額以台幣計算，並附上韓元參考價格。', body))
    story.append(Spacer(1, 8))
    
    tbl_data = [
        ['預算等級', '總費用範圍(台幣)', '每日平均(台幣)', '適合對象'],
        ['經濟型', '25,000-35,000', '3,500-5,000', '背包客、學生族群'],
        ['中檔型', '40,000-60,000', '5,700-8,600', '一般上班族、家庭'],
        ['奢華型', '70,000-120,000', '10,000-17,000', '追求品質的旅客'],
    ]
    story.append(make_table(['預算等級', '總費用範圍(台幣)', '每日平均(台幣)', '適合對象'], tbl_data))
    story.append(Spacer(1, 10))
    
    # Tip Box
    story += make_tip('省錢小撇步', [
        '提前2-3個月預訂機票，可省下3,000-5,000台幣',
        '選擇民宿或青年旅館，住宿費可減少50%',
        '利用便利商店與街頭小吃，餐費可控制在每日300台幣內',
        '購買T-money卡並搭乘大眾運輸，交通費比計程車便宜70%',
        '免稅店商品可退稅（Tax Refund），記得索取退稅單',
    ]))
    
    # Section 2: Detailed Budget Breakdown
    story.append(Paragraph('各項費用詳細分析', h2))
    story.append(Paragraph('機票費用佔旅遊預算的30-40%，經濟型預算可選擇廉航（如台灣虎航、濟州航空），來回機票約8,000-12,000台幣；中檔型可選擇傳統航空（如華航、大韓航空），來回機票約15,000-25,000台幣。住宿費用：青年旅館床位每晚500-800台幣，商務旅館每晚2,000-3,500台幣，五星級飯店每晚5,000-10,000台幣。餐飲費用：經濟型每日300-500台幣，中檔型每日600-1,000台幣，奢華型每日1,200-2,000台幣。', body))
    story.append(Spacer(1, 8))
    
    tbl_data2 = [
        ['費用項目', '經濟型(台幣)', '中檔型(台幣)', '奢華型(台幣)'],
        ['機票（來回）', '8,000-12,000', '15,000-25,000', '25,000-35,000'],
        ['住宿（6晚）', '3,000-5,000', '12,000-20,000', '30,000-60,000'],
        ['餐飲（7天）', '2,100-3,500', '4,200-7,000', '8,400-14,000'],
        ['交通（市內+跨市）', '1,500-2,500', '3,000-5,000', '5,000-10,000'],
        ['門票與活動', '1,000-2,000', '3,000-5,000', '5,000-10,000'],
        ['購物與雜支', '3,000-5,000', '8,000-15,000', '20,000-40,000'],
        ['預備金', '2,000-3,000', '5,000-8,000', '10,000-15,000'],
        ['總計', '20,600-32,000', '45,200-70,000', '103,400-184,000'],
    ]
    story.append(make_table(['費用項目', '經濟型(台幣)', '中檔型(台幣)', '奢華型(台幣)'], tbl_data2))
    story.append(Spacer(1, 10))
    
    # Section 3: Money Exchange and Payment
    story.append(Paragraph('換匯與付款方式建議', h2))
    story.append(Paragraph('韓元（KRW）與台幣（TWD）匯率約為1:0.022-0.025（即1台幣約40-45韓元）。建議在台灣先換部分韓元現金（約總預算的30%），其餘使用提款卡在韓國ATM領取或信用卡消費。韓國ATM提款手續費約100-150台幣/次，匯率較現金換匯優惠。信用卡在韓國普及率高，大部分商店、餐廳與交通都接受VISA/MasterCard。建議攜帶至少兩張不同發卡組織的信用卡以備不時之需。', body))
    story.append(Spacer(1, 8))
    
    story += make_tip('付款方式比較', [
        '現金：適合小吃攤、傳統市場、部分交通（如公車）',
        '信用卡：適合百貨公司、餐廳、網購，部分有海外回饋',
        'T-money卡：適合地鐵、公車、便利商店，可退卡費與餘額',
        '支付寶/微信支付：部分免稅店與觀光區商店接受',
        '旅行支票：已較少使用，不建議攜帶',
    ]))
    
    # Section 4: Budget Adjustment by City
    story.append(Paragraph('不同城市預算調整建議', h2))
    story.append(Paragraph('首爾是韓國消費最高的城市，住宿與餐飲價格比其它城市貴20-30%。釜山與濟州島的物價相對較低，但濟州島交通費（租車或計程車）較高。若行程包含多個城市，建議預算分配為：首爾50%、釜山30%、濟州島20%。若只在首爾一地旅遊，可將預算集中在住宿地段（明洞、弘大較貴，東大門、江南CP值較高）與餐飲選擇（混合高檔餐廳與平價小吃）。', body))
    story.append(Spacer(1, 8))
    
    tbl_data3 = [
        ['城市', '物價指數', '住宿價差', '餐飲價差', '推薦住宿區域'],
        ['首爾', '100% (基準)', '基準', '基準', '明洞、弘大、江南'],
        ['釜山', '85-90%', '便宜15-20%', '便宜10-15%', '海雲台、西面'],
        ['濟州島', '80-85%', '便宜20-25%', '便宜15-20%', '濟州市、西歸浦'],
        ['仁川', '90-95%', '便宜5-10%', '便宜5-10%', '仁川機場周邊'],
    ]
    story.append(make_table(['城市', '物價指數', '住宿價差', '餐飲價差', '推薦住宿區域'], tbl_data3))
    story.append(Spacer(1, 8))
    
    story += make_tip('預算追蹤工具', [
        '推薦使用TravelSpend、TrabeePocket等APP記帳',
        '每天晚上花5分鐘記錄當日花費',
        '設定每日預算上限，避免超支',
        '保留收據或拍照存證，方便回國報稅（如有需要）',
        '回國後分析花費比例，作為下次旅遊參考',
    ]))
    
    # CTA
    story += make_cta()
    
    return story


# =============================================================================
# Main execution: Build all Korea PDFs
# =============================================================================

if __name__ == '__main__':
    import os
    
    # Define output directory
    output_dir = 'pdfs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate all Korea PDFs
    pdf_configs = [
        ('seoul_food_map.pdf', '韓國首爾美食地圖', gen_seoul_food),
        ('busan_capsule_guide.pdf', '釜山膠囊列車預約攻略', gen_busan_capsule),
        ('jeju_driving_route.pdf', '濟州島自駕路線', gen_jeju_driving),
        ('korea_budget_sheet.pdf', '韓國旅遊預算表', gen_korea_budget),
    ]
    
    for filename, title, gen_func in pdf_configs:
        output_path = os.path.join(output_dir, filename)
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            leftMargin=M, rightMargin=M,
            topMargin=M+10, bottomMargin=M+10
        )
        story = gen_func()
        doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
        print(f'✓ Generated: {output_path}')
    
    print('\\nAll Korea PDFs generated successfully!')
`;

// Write the Python code to the file
const targetFile = path.join(__dirname, '_beautify_pdf.py');
fs.appendFileSync(targetFile, pythonCode, 'utf8');

console.log('Successfully appended Korea PDF functions to _beautify_pdf.py');
console.log('Added functions:');
console.log('  - gen_seoul_food()');
console.log('  - gen_busan_capsule()');
console.log('  - gen_jeju_driving()');
console.log('  - gen_korea_budget()');
console.log('');
console.log('The script also includes main execution code to generate all 4 PDFs.');
