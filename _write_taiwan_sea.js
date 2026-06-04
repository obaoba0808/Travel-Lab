const fs = require('fs');
const path = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab/_beautify_pdf.py';

const taiwan_sea = `

# ============================================================
# PART 3: TAIWAN + SEA PDFS (10)
# ============================================================

def gen_hualien():
    \"\"\"花蓮行程規劃 - 完整攻略\"\"\"
    s = []
    s += make_cover('花蓮行程規劃', '2026 最新版')
    
    s.append(Paragraph('花蓮旅遊總覽', h1))
    s.append(Paragraph('花蓮是台灣東部最美的縣市，擁有太魯閣國家公園、七星潭、清水斷崖等絕景。建議安排2-3天行程，搭配台東或宜蘭做成小環線。2026年台鐵普悠瑪號已恢復全線通車，台北→花蓮最快2小時10分。', body))
    
    # Section 1
    s.append(Paragraph('2天1夜行程推薦', h2))
    itinerary_data = [
        ['天數', '上午', '下午', '住宿'],
        ['Day 1', '太魯閣長春祠', '七星潭→自強夜市', '花蓮市區'],
        ['Day 2', '清水斷崖→清水', '鯉魚潭→返程', '—'],
    ]
    s.append(make_table(['天數', '上午', '下午', '住宿'], itinerary_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('必去景點評分', h2))
    spots_data = [
        ['景點', '票價', '停留時間', '推薦度'],
        ['太魯閣國家公園', '免費', '3-4小時', '★★★★★'],
        ['七星潭', '免費', '1-2小時', '★★★★★'],
        ['清水斷崖', '免費', '30分鐘', '★★★★☆'],
        ['鯉魚潭', 'NT$100', '1-2小時', '★★★☆☆'],
        ['自強夜市', '免費入場', '2-3小時', '★★★★☆'],
        ['東大門夜市', '免費入場', '2-3小時', '★★★★★'],
    ]
    s.append(make_table(['景點', '票價', '停留時間', '推薦度'], spots_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('花蓮旅遊必知', [
        '太魯閣建議早上8:00前抵達，避開遊覽車人潮',
        '七星潭風浪大，禁止下水游泳（有暗流）',
        '自強夜市週二、週五休市；東大門夜市每天營業',
        '花蓮→台東火車票難搶，建議提前14天購票',
        '租機車遊花蓮最方便（NT$500/天），需重型機車駕照',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('預算分配（2天1夜/人）', h2))
    budget_data = [
        ['項目', '費用(NT$)', '備註'],
        ['台鐵來回（台北→花蓮）', 'NT$900', '普悠瑪號'],
        ['住宿（雙人房）', 'NT$1,200/人', '花蓮市區民宿'],
        ['租機車（2天）', 'NT$500/人', '油資自付'],
        ['餐飲（2天）', 'NT$800', '夜市+公正包子'],
        ['太魯閣一日遊（包車）', 'NT$400/人', '4人座車分摊'],
        ['合計', 'NT$3,800', '不含購物'],
    ]
    s.append(make_table(['項目', '費用(NT$)', '備註'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_tainan_food():
    \"\"\"台南美食地圖 - 完整攻略\"\"\"
    s = []
    s += make_cover('台南美食地圖', '2026 最新版')
    
    s.append(Paragraph('台南美食總覽', h1))
    s.append(Paragraph('台南被稱為「台灣美食首都」，擔子麵、蝦捲、碗粿、牛肉湯、芒果冰等名產多到數不清。台南人吃早餐從早上6:00開始，晚了就排隊。本攻略精選15家必吃店家，附營業時間與推薦菜品。', body))
    
    # Section 1
    s.append(Paragraph('必吃TOP 10', h2))
    food_data = [
        ['美食', '推薦店家', '價格', '營業時間'],
        ['擔子麵', '度小月擔子麵', 'NT$45', '11:00-21:00'],
        ['蝦捲', '文章牛肉湯', 'NT$80/份', '17:00-23:00'],
        ['碗粿', '再發號碗粿', 'NT$35', '06:00-11:00'],
        ['牛肉湯', '文章牛肉湯', 'NT$120/碗', '17:00-23:00'],
        ['芒果冰', '莉莉水果店', 'NT$90', '11:00-21:30'],
        ['鱔魚意麵', '阿江鱔魚意麵', 'NT$80', '11:00-20:00'],
        ['蚵仔煎', '阿堂蚵仔煎', 'NT$60', '16:00-23:00'],
        ['肉圓', '武廟肉圓', 'NT$40', '10:00-19:00'],
        ['米糕', '瑞珍小吃店', 'NT$50', '11:00-20:00'],
        ['豆花', '雙全紅豆牛奶冰', 'NT$60', '13:00-22:00'],
    ]
    s.append(make_table(['美食', '推薦店家', '價格', '營業時間'], food_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('美食路線規劃', h2))
    s.append(Paragraph('路線A（古蹟線）：赤崁樓 → 大天后宮 → 武廟 → 度小月擔子麵 → 莉莉水果店\\n'
                     '路線B（運河線）：台南運河 → 四草綠色隧道 → 七股鹽山 → 阿堂蚵仔煎\\n'
                     '路線C（安平線）：安平古堡 → 安平樹屋 → 蜷尾家 → 再發號碗粿', body_compact))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('台南美食小撇步', [
        '牛肉湯只有早上新鮮（11:00前），下午的品質差很多',
        '擔子麵建議加「魚皮」或「蝦仁」配料（NT$20）',
        '芒果冰4-6月吃最甜（愛文芒果產季）',
        '週末景點人潮多，建議平日前往',
        '台南計程車起跳NT$85，可用Uber',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('一日美食預算', h2))
    budget_data = [
        ['餐次', '推薦組合', '價格'],
        ['早餐', '碗粿+豆漿（再發號）', 'NT$60'],
        ['午餐', '擔子麵+小菜（度小月）', 'NT$150'],
        ['下午茶', '芒果冰（莉莉）', 'NT$90'],
        ['晚餐', '牛肉湯+蝦捲（文章）', 'NT$250'],
        ['點心', '蚵仔煎+肉圓', 'NT$100'],
        ['合計', '', 'NT$650'],
    ]
    s.append(make_table(['餐次', '推薦組合', '價格'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_kenting_night():
    \"\"\"墾丁夜市攻略 - 完整攻略\"\"\"
    s = []
    s += make_cover('墾丁夜市攻略', '2026 最新版')
    
    s.append(Paragraph('墾丁夜市總覽', h1))
    s.append(Paragraph('墾丁大街夜市是台灣最南端的觀光夜市，全長1.5公里，約300個攤位。每年4-10月是旺季（暑假最貴），11-3月是淡季（民宿價格打對折）。本攻略涵蓋必吃美食、住宿推薦、交通方式、預算分配。', body))
    
    # Section 1
    s.append(Paragraph('必吃美食TOP 8', h2))
    food_data = [
        ['美食', '價格', '推薦攤位', '特色'],
        ['墾丁街邊烤肉', 'NT$80-120', '大街中段', '現烤豬肉'],
        ['熱帶水果冰', 'NT$60-90', '大街南段', '芒果/香蕉/火龍果'],
        ['棺材板', 'NT$50', '大街北段', '台南傳來的創意料理'],
        ['紅燒鰻魚飯', 'NT$100', '海邊路', '墾丁特色海鮮'],
        ['地瓜球', 'NT$30/袋', '大街各處', '現炸現吃'],
        ['椰子水', 'NT$80', '沙灘入口', '現砍椰子'],
        ['鐵板燒', 'NT$150-250', '大街中段', '現場表演'],
        ['墨西哥捲餅', 'NT$100', '大街南段', '異國風味'],
    ]
    s.append(make_table(['美食', '價格', '推薦攤位', '特色'], food_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('住宿推薦（墾丁大街周邊）', h2))
    hotel_data = [
        ['類型', '價格(淡季/旺季)', '推薦區域', '適合對象'],
        ['民宿（雙人房）', 'NT$1,200 / NT$2,800', '大街步行5分', '情侶/夫妻'],
        ['飯店（四人房）', 'NT$2,400 / NT$5,600', '大街步行3分', '家庭'],
        ['青年旅館（床位）', 'NT$400 / NT$800', '大街內', '背包客'],
        ['露營區', 'NT$300/人', '船帆石', '戶外愛好者'],
    ]
    s.append(make_table(['類型', '價格(淡季/旺季)', '推薦區域', '適合對象'], hotel_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('墾丁旅遊必知', [
        '旺季（7-8月）民宿需提前2個月預訂，現場找貴一倍',
        '墾丁大街夜市每週日公休（部分攤位週一休）',
        '騎機車遊墾丁最方便（NT$500/天），需注意安全帽',
        '南灣海灘可游泳（7-9月），其他季節浪大危險',
        '墾丁→高雄火車→墾丁街車（NT$350，2.5小時）',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('2天1夜預算表（淡季/人）', h2))
    budget_data = [
        ['項目', '費用(NT$)', '備註'],
        ['高鐵/台鐵到高雄', 'NT$1,500', '台北出發'],
        ['墾丁街車（高雄→墾丁）', 'NT$350', '統聯/國光'],
        ['住宿（雙人房）', 'NT$600', '淡季價格'],
        ['機車租借（2天）', 'NT$500', '油資自付'],
        ['餐飲（夜市+早餐）', 'NT$600', '2天份'],
        ['南灣海灘門票', 'NT$200', '夏季開放'],
        ['合計', 'NT$3,750', '不含購物'],
    ]
    s.append(make_table(['項目', '費用(NT$)', '備註'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_taipei_food():
    \"\"\"台北美食地圖 - 完整攻略\"\"\"
    s = []
    s += make_cover('台北美食地圖', '2026 最新版')
    
    s.append(Paragraph('台北美食總覽', h1))
    s.append(Paragraph('台北是台灣美食最多元的城市，從夜市小吃到米其林餐廳應有盡有。本攻略精選台北5大夜市、10間必吃名店、3條美食散步路線，幫你用最有效率的方式吃遍台北。', body))
    
    # Section 1
    s.append(Paragraph('5大夜市比較', h2))
    night_data = [
        ['夜市', '特色', '必吃', '營業時間'],
        ['士林夜市', '最大、觀光客最多', '大餅包小餅、豪大大雞排', '16:00-01:00'],
        ['饒河街夜市', '最長（600公尺）', '藥燉排骨、胡椒餅', '17:00-23:00'],
        ['寧夏夜市', '最道地（本地人愛）', '劉芋仔、圓環邊蚵仔煎', '17:00-01:00'],
        ['遼寧夜市', '最便宜', '麻辣臭豆腐、滷味', '18:00-02:00'],
        ['華西街夜市', '最老牌（蛇店出名）', '鱉肉、蛇酒', '18:00-02:00'],
    ]
    s.append(make_table(['夜市', '特色', '必吃', '營業時間'], night_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('台北必吃TOP 10', h2))
    food_data = [
        ['美食', '推薦店家', '價格', '位置'],
        ['鼎泰豐小籠包', '鼎泰豐（信義）', 'NT$240/8顆', '信義區'],
        ['牛肉麵', '林東芳牛肉麵', 'NT$180', '松山區'],
        ['滷肉飯', '金峰滷肉飯', 'NT$35', '中正區'],
        ['珍珠奶茶', '春水堂', 'NT$70', '大安區'],
        ['雞肉飯', '圓環迴轉雞肉飯', 'NT$50', '大同區'],
        ['芒果冰', '冰讚（永康街）', 'NT$130', '大安區'],
        ['生煎包', '京星小吃的生煎包', 'NT$60/4顆', '中山區'],
        ['胡椒餅', '饒河街胡椒餅', 'NT$60', '松山區'],
        ['大餅包小餅', '士林夜市大餅包小餅', 'NT$60', '士林區'],
        ['紅豆餅', '紅豆森林', 'NT$50', '大安區'],
    ]
    s.append(make_table(['美食', '推薦店家', '價格', '位置'], food_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('台北美食小撇步', [
        '鼎泰豐最便宜是在台灣（比香港/新加坡便宜30%）',
        '夜市建議19:00前去，避開人潮高峰',
        '林東芳牛肉麵週日公休，注意營業時間',
        '台北捷運站內有「悠遊卡」可刷卡（超商/公車/YouBike）',
        '週末景點人潮多，建議平日前往',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('一日美食預算', h2))
    budget_data = [
        ['餐次', '推薦組合', '價格'],
        ['早餐', '永和豆漿+蛋餅', 'NT$60'],
        ['午餐', '鼎泰豐小籠包套餐', 'NT$400'],
        ['下午茶', '芒果冰（冰讚）', 'NT$130'],
        ['晚餐', '士林夜市（10樣小吃）', 'NT$300'],
        ['點心', '珍珠奶茶+紅豆餅', 'NT$120'],
        ['合計', '', 'NT$1,010'],
    ]
    s.append(make_table(['餐次', '推薦組合', '價格'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_jiufen():
    \"\"\"九份老街攻略 - 完整攻略\"\"\"
    s = []
    s += make_cover('九份老街攻略', '2026 最新版')
    
    s.append(Paragraph('九份旅遊總覽', h1))
    s.append(Paragraph('九份是台灣最富魅力的山城小鎮，因電影《悲情城市》與《千與千尋》靈感而聞名。主要景點：九份老街、昇平戲院、基山觀海平台、黃金博物館（鄰近金瓜石）。本攻略提供交通、美食、攝影、住宿完整資訊。', body))
    
    # Section 1
    s.append(Paragraph('交通方式', h2))
    transport_data = [
        ['出發地', '方式', '時間', '價格'],
        ['台北車站', '台鐵→瑞芳站+公車', '1.5小時', 'NT$120'],
        ['台北車站', '客運（基隆/福和）', '1.5小時', 'NT$90'],
        ['瑞芳站', '公車（856/7888）', '20分', 'NT$30'],
        ['九份', '計程車（瑞芳→九份）', '15分', 'NT$250'],
    ]
    s.append(make_table(['出發地', '方式', '時間', '價格'], transport_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('九份老街必吃美食', h2))
    food_data = [
        ['美食', '推薦店家', '價格', '特色'],
        ['芋圓（必吃）', '賴阿婆芋圓', 'NT$50', 'Q彈口感'],
        ['草仔粿', '九份老街入口', 'NT$40', '九份傳統點心'],
        ['紅糟肉圓', '老街中段', 'NT$50', '九份限定'],
        ['魚丸湯', '阿柑魚丸', 'NT$50', '手工魚丸'],
        ['黑糖麻糬', '昇平戲院旁', 'NT$60', '現包現吃'],
        ['花生捲冰淇淋', '老街各處', 'NT$50', '古早味'],
    ]
    s.append(make_table(['美食', '推薦店家', '價格', '特色'], food_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('九份旅遊必知', [
        '九份老街週末人潮極多，建議平日或早上9:00前抵達',
        '黃金博物館（金瓜石）可順遊，門票NT$80（可抵購物）',
        '九份日落最美（17:30-18:30），基山觀海平台是最佳觀景點',
        '老街階梯多，不建議推嬰兒車或帶長輩（無障礙設施少）',
        '九份住宿推薦老街內民宿（NT$1,500-2,500/間），可看夜景',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('一日遊行程', h2))
    s.append(Paragraph('09:00 台北出發（搭台鐵或客運）\\n'
                     '10:30 抵達九份，開始逛老街（賴阿婆芋圓）\\n'
                     '12:30 午餐（紅糟肉圓+魚丸湯）\\n'
                     '14:00 昇平戲院（九份歷史介紹）\\n'
                     '15:30 基山觀海平台（看海景）\\n'
                     '17:00 黃金博物館（金瓜石）\\n'
                     '18:30 回九份看夜景（老街夜景超美）\\n'
                     '20:00 返回台北', body_compact))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_chiang_mai():
    \"\"\"清邁旅遊攻略 - 完整攻略\"\"\"
    s = []
    s += make_cover('清邁旅遊攻略', '2026 最新版')
    
    s.append(Paragraph('清邁旅遊總覽', h1))
    s.append(Paragraph('清邁是泰國北部的文化首都，擁有300多座寺廟、豐富的夜市文化、便宜的按摩與SPA。11-2月是涼季（氣溫20-28°C），最適合旅遊。清邁國際機場直飛台北僅3.5小時，是中台灣人最愛的短程旅遊地。', body))
    
    # Section 1
    s.append(Paragraph('必去寺廟TOP 5', h2))
    temple_data = [
        ['寺廟', '特色', '門票', '停留時間'],
        ['帕辛寺（Wat Phra Singh）', '清邁最重要寺廟', '免費', '1小時'],
        ['契迪龍寺（Wat Chedi Luang）', '毀損佛塔（600年歷史）', '免費', '1小時'],
        ['素貼寺（Wat Suan Dok）', '蘭納王朝皇家寺廟', '免費', '1小時'],
        ['雙龍寺（Doi Suthep）', '清邁地標（山頂）', '30泰銖', '2小時'],
        ['悟孟寺（Wat Umong）', '隧道寺廟（冥想聖地）', '免費', '1小時'],
    ]
    s.append(make_table(['寺廟', '特色', '門票', '停留時間'], temple_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('週日夜市（Sunday Walking Street）', h2))
    s.append(Paragraph('清邁週日夜市是泰國最大的步行街（全長1公里），每週日16:00-22:00在Ratchadamnoen Rd舉行。必買：泰絲圍巾（200-500泰銖）、木雕工藝品、手工肥皂、北部泰式小吃。', body))
    
    night_data = [
        ['品項', '價格(泰銖)', '推薦'],
        ['泰絲圍巾', '200-500', '送禮自用兩相宜'],
        ['木雕大象', '300-1,000', '清邁特產'],
        ['手工肥皂', '50-100/塊', '天然成分'],
        ['北部香腸（Sai Oua）', '10-20/串', '必吃美食'],
        ['芒果汁', '30-50/杯', '現榨新鮮'],
    ]
    s.append(make_table(['品項', '價格(泰銖)', '推薦'], night_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('清邁旅遊必知', [
        '進寺廟需脫鞋、穿著端莊（不可穿短褲/無袖）',
        '雙龍寺需爬306階梯，建議早上8:00前去（避開人潮+不熱）',
        '清邁按摩超便宜（泰式按摩1小時200-300泰銖）',
        '租機車（NT$200/天）需注意安全帽與泰國駕照',
        '清邁→曼谷可搭飛機（1.5小時，AirAsia常特價NT$1,200）',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('3天2夜預算表（經濟型/人）', h2))
    budget_data = [
        ['項目', '費用(NT$)', '備註'],
        ['台北→清邁機票', 'NT$5,000', '來回含稅'],
        ['住宿（雙人房，2晚）', 'NT$1,000', 'NT$500/晚'],
        ['交通（雙條車/Tuk-tuk）', 'NT$600', '約600泰銖'],
        ['按摩（3次，每次2小時）', 'NT$900', '每次300泰銖'],
        ['餐飲（3天）', 'NT$1,500', '平均每餐NT$150'],
        ['門票（雙龍寺+博物館）', 'NT$200', '約200泰銖'],
        ['合計', 'NT$9,200', '不含購物'],
    ]
    s.append(make_table(['項目', '費用(NT$)', '備註'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_bangkok_food():
    \"\"\"曼谷美食地圖 - 完整攻略\"\"\"
    s = []
    s += make_cover('曼谷美食地圖', '2026 最新版')
    
    s.append(Paragraph('曼谷美食總覽', h1))
    s.append(Paragraph('曼谷是東南亞美食首都，價格只有台北的1/3。路邊攤（Street Food）是美食靈魂，米其林必比登（Bib Gourmand）推薦了超過200家曼谷小吃店。本攻略精選15家必吃店家，附泰文地址與營業時間。', body))
    
    # Section 1
    s.append(Paragraph('必吃美食TOP 10', h2))
    food_data = [
        ['美食', '價格(泰銖)', '推薦店家', '特色'],
        ['打拋豬（Pad Kaprow）', '50-80', '路邊攤', '國民美食'],
        ['冬蔭功（Tom Yum Goong）', '150-250', '路邊攤', '酸辣蝦湯'],
        ['泰式炒河粉（Pad Thai）', '60-100', '百年老店', '泰國國民麵'],
        ['芒果糯米飯（Mango Sticky Rice）', '50-80', '路邊攤', '甜點之王'],
        ['船麵（Boat Noodle）', '15-20/碗', '船麵街', '一口一碗'],
        ['綠咖哩（Green Curry）', '80-120', '路邊攤', '泰式咖哩'],
        ['泰式奶茶（Thai Tea）', '20-40', '路邊攤', '超甜好喝'],
        ['炸魚餅（Tod Mun Pla）', '40-60', 'Chatuchak', '市集美食'],
        ['鳳梨炒飯（Pineapple Fried Rice）', '100-150', '觀光餐廳', '遊客最愛'],
        ['泰式冰咖啡（Oliang）', '30-50', '路邊攤', '超濃咖啡'],
    ]
    s.append(make_table(['美食', '價格(泰銖)', '推薦店家', '特色'], food_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('米其林必比登推薦（曼谷）', h2))
    michelin_data = [
        ['店家', '美食', '價格', '位置'],
        ['Jay Fai', '蟹肉歐姆蛋', '1,000-1,500泰銖', 'Old Town'],
        ['Raam Sa', '泰南咖哩', '100-200泰銖', '唐人街'],
        ['Charmgang', '泰式咖哩麵', '80-150泰銖', 'Chinatown'],
        ['Sometam Daday', '青木瓜沙拉', '60-100泰銖', 'Victory Monument'],
    ]
    s.append(make_table(['店家', '美食', '價格', '位置'], michelin_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('曼谷美食小撇步', [
        '路邊攤衛生比想像中好，跟著當地人排隊就對了',
        '怕辣說「Mai Pet」（ไม่เผ็ด = 不辣）',
        '曼谷夜市（Chatuchak/Rot Fai）週末才有',
        '米其林必比登需提前1個月預約（Jay Fai最難訂）',
        '水（Nam）一定要喝瓶裝（40泰銖），避免拉肚子',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('一日美食預算（超省錢版）', h2))
    budget_data = [
        ['餐次', '推薦組合', '價格(泰銖)'],
        ['早餐', '泰式奶茶+吐司', '50'],
        ['午餐', '打拋豬+飯', '80'],
        ['下午茶', '芒果糯米飯', '80'],
        ['晚餐', '冬蔭功+炒河粉', '250'],
        ['點心', '船麵（3碗）', '60'],
        ['合計', '', '520泰銖（約NT$520）'],
    ]
    s.append(make_table(['餐次', '推薦組合', '價格(泰銖)'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_bangkok_massage():
    \"\"\"曼谷按摩地圖 - 完整攻略\"\"\"
    s = []
    s += make_cover('曼谷按摩地圖', '2026 最新版')
    
    s.append(Paragraph('曼谷按摩總覽', h1))
    s.append(Paragraph('曼谷按摩是全球最物超所值的，從250泰銖的路邊按摩到5,000泰銖的頂級SPA。泰式按摩（Thai Massage）與油壓按摩（Oil Massage）是最受歡迎的兩種。本攻略推薦10家優質按摩店，附價格、評價、預約方式。', body))
    
    # Section 1
    s.append(Paragraph('按摩種類與價格', h2))
    massage_data = [
        ['類型', '價格(2h)', '特色', '推薦度'],
        ['泰式按摩（Thai Massage）', '400-800泰銖', '拉筋伸展', '★★★★★'],
        ['油壓按摩（Oil Massage）', '600-1,200泰銖', '放鬆舒壓', '★★★★☆'],
        ['足部按摩（Foot Massage）', '250-500泰銖', '最便宜', '★★★★☆'],
        ['頂級SPA（Luxury SPA）', '2,500-5,000泰銖', '奢華體驗', '★★★☆☆'],
        ['路邊按摩（Street Massage）', '200-300泰銖', '超便宜', '★★☆☆☆'],
    ]
    s.append(make_table(['類型', '價格(2h)', '特色', '推薦度'], massage_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('推薦按摩店TOP 5', h2))
    shop_data = [
        ['店名', '類型', '價格(2h)', '特色'],
        ['Health Land', '泰式/油壓', '500-800泰銖', '高CP值，連鎖品牌'],
        ['Let\\'s Relax', '泰式/油壓', '600-1,000泰銖', '品質穩定，環境舒适'],
        ['Diva Massage', '油壓按摩', '800-1,200泰銖', '年輕人最愛'],
        ['SPA 1930', '頂級SPA', '2,500-4,000泰銖', '百年建築，奢華體驗'],
        ['路邊攤（任意）', '泰式按摩', '250-400泰銖', '超值體驗'],
    ]
    s.append(make_table(['店名', '類型', '價格(2h)', '特色'], shop_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('曼谷按摩必知', [
        '泰式按摩不是愈痛愈好！說「Bao Bao」（เบาๆ = 輕一點）調整力道',
        'Health Land 需提前1天預約（電話：02-391-1111）',
        '路邊按摩衛生條件較差，建議選有空調的店',
        '按摩後多喝水（代謝乳酸），避免酒後按摩',
        '小費：按摩師傅每人給20-50泰銖（非強制，但會很開心）',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('按摩+美食一日行程', h2))
    s.append(Paragraph('10:00 抵達曼谷（素汪納普機場）\\n'
                     '12:00 午餐（Pad Thai 老店）\\n'
                     '14:00 飯店 check-in + 休息\\n'
                     '16:00 泰式按摩（Health Land，2小時）\\n'
                     '19:00 晚餐（冬蔭功+炒河粉）\\n'
                     '21:00 夜市散步（Chatuchak/Rot Fai）\\n'
                     '23:00 回飯店休息', body_compact))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


def gen_danang():
    \"\"\"峴港旅遊地圖 - 完整攻略\"\"\"
    s = []
    s += make_cover('峴港旅遊地圖', '2026 最新版')
    
    s.append(Paragraph('峴港旅遊總覽', h1))
    s.append(Paragraph('峴港是越南中部的海濱城市，擁有美溪海灘（全球六大最美海灘之一）、巴拿山（Golden Bridge）、會安古城（世界文化遺產）。台灣人前往峴港可辦理落地簽（或電子簽證ETA），飛行時間僅2.5小時。', body))
    
    # Section 1
    s.append(Paragraph('必去景點TOP 5', h2))
    spots_data = [
        ['景點', '門票', '停留時間', '推薦度'],
        ['美溪海灘（My Khe Beach）', '免費', '半天', '★★★★★'],
        ['巴拿山（Ba Na Hills）', '700,000 VND', '1天', '★★★★★'],
        ['會安古城（Hoi An）', '120,000 VND', '半天', '★★★★☆'],
        ['山茶半島（Son Tra Peninsula）', '免費', '3小時', '★★★☆☆'],
        ['五行山（Marble Mountains）', '40,000 VND', '2小時', '★★★☆☆'],
    ]
    s.append(make_table(['景點', '門票', '停留時間', '推薦度'], spots_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 2
    s.append(Paragraph('巴拿山 Golden Bridge（黃金橋）', h2))
    s.append(Paragraph('巴拿山是峴港最熱門的景點，海拔1,487公尺，有「越南的小法國」之稱。最著名的「黃金橋」（Cau Vang）由兩隻巨手托著，Instagram打卡聖地。建議早上7:00前抵達，避開人潮。', body))
    
    ba_na_data = [
        ['項目', '說明'],
        ['門票', '700,000 VND（約NT$900）'],
        ['纜車', '世界最長纜車（5,801公尺）'],
        ['最佳時間', '早上7:00-9:00（霧少）'],
        ['建議停留', '6-8小時'],
        ['穿著', '帶外套（山頂15°C）'],
    ]
    s.append(make_table(['項目', '說明'], ba_na_data[1:]))
    s.append(Spacer(1, 8))
    
    # Section 3
    s += make_tip('峴港旅遊必知', [
        '越南盾（VND）很長（1,000,000 VND = NT$1,300），建議用App換算',
        '美溪海灘游泳最佳時間：早上6:00-9:00（浪小）',
        '會安古城晚上超美（燈籠節），建議住一晚',
        '峴港→會安可搭Grab（约200,000 VND，45分鐘）',
        '台灣護照可辦ETA（電子簽證），提前3天申請',
    ]))
    s.append(Spacer(1, 8))
    
    # Section 4
    s.append(Paragraph('4天3夜預算表（雙人/人）', h2))
    budget_data = [
        ['項目', '費用(NT$)', '備註'],
        ['台灣→峴港機票', 'NT$4,500', '來回含稅（越捷/VietJet）'],
        ['住宿（3晚，雙人房）', 'NT$1,500', 'NT$500/晚'],
        ['巴拿山門票（2人）', 'NT$1,800', '700,000 VND/人'],
        ['會安古城門票（2人）', 'NT$300', '120,000 VND/人'],
        ['Grab交通（4天）', 'NT$1,200', '約1,000,000 VND'],
        ['餐飲（4天）', 'NT$2,400', '平均每餐NT$200'],
        ['合計', 'NT$11,700', '不含購物'],
    ]
    s.append(make_table(['項目', '費用(NT$)', '備註'], budget_data[1:]))
    s.append(Spacer(1, 10))
    
    s += make_cta()
    return s


# ============================================================
# MAIN: BUILD ALL 21 PDFS
# ============================================================

if __name__ == '__main__':
    output_dir = 'downloads'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    pdf_configs = [
        # Japan (7)
        ('tokyo-metro-map.pdf', '東京地鐵路線圖', gen_tokyo_metro),
        ('kansai-pass-calculator.pdf', '關西機場轉乘計算機', gen_kansai_pass),
        ('hokkaido-packing-list.pdf', '北海道冬季穿搭清單', gen_hokkaido_packing),
        ('okinawa-driving-map.pdf', '沖繩自駕地圖', gen_okinawa_driving),
        ('kyoto-momiji-schedule.pdf', '京都紅葉日程表', gen_kyoto_momiji),
        ('osaka-food-map.pdf', '大阪美食地圖', gen_osaka_food),
        ('usj-quick-pass.pdf', 'USJ快速通關攻略', gen_usj_quick_pass),
        # Korea (4)
        ('seoul-food-map.pdf', '韓國首爾美食地圖', gen_seoul_food),
        ('busan-capsule-guide.pdf', '釜山膠囊列車預約攻略', gen_busan_capsule),
        ('jeju-driving-route.pdf', '濟州島自駕路線', gen_jeju_driving),
        ('korea-budget-sheet.pdf', '韓國旅遊預算表', gen_korea_budget),
        # Taiwan (5)
        ('hualien-itinerary.pdf', '花蓮行程規劃', gen_hualien),
        ('tainan-food-map.pdf', '台南美食地圖', gen_tainan_food),
        ('kenting-night-market.pdf', '墾丁夜市攻略', gen_kenting_night),
        ('taipei-food-map.pdf', '台北美食地圖', gen_taipei_food),
        ('jiufen-guide.pdf', '九份老街攻略', gen_jiufen),
        # SEA (5)
        ('chiang-mai-guide.pdf', '清邁旅遊攻略', gen_chiang_mai),
        ('bangkok-food-map.pdf', '曼谷美食地圖', gen_bangkok_food),
        ('bangkok-massage-map.pdf', '曼谷按摩地圖', gen_bangkok_massage),
        ('danang-map.pdf', '峴港旅遊地圖', gen_danang),
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
    
    print('\\nAll 21 PDFs generated successfully!')
`;

fs.appendFileSync(path, taiwan_sea, 'utf-8');
console.log('Taiwan+SEA 10 PDFs appended. Final file size:', fs.statSync(path).size, 'bytes');
