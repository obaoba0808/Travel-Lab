export interface CustomPageData {
  id: string;
  title: string;
  category: string;
  url: string;
  coverImage: string;
  intro: string;
  description?: string;
  tags: string[];
}

export const customPages: CustomPageData[] = [
  {
    "id": "tokyo-5days",
    "title": "東京5天4夜經典行程：潮流、傳統與極致美食完美交織",
    "category": "日本自由行",
    "url": "tokyo-5days.html",
    "coverImage": "/images/tokyo-hero.webp",
    "intro": "東京5天4夜自由行攻略2026：淺草寺晴空塔、澀谷原宿逛街、築地場外市場美食、迪士尼門票優惠，附完整地鐵乘車教學與每日行程表，預算NT$15,000搞定遊客必讀。",
    "tags": [
      "新手推薦",
      "5天4夜",
      "東京全覽"
    ]
  },
  {
    "id": "tokyo-accommodation",
    "title": "東京住宿推薦：各大熱門區域優缺點分析與精選清單",
    "category": "日本自由行",
    "url": "tokyo-accommodation.html",
    "coverImage": "/images/Tokyo-Accommodation-hero.webp",
    "intro": "東京住宿區域比較2026：新宿交通便利/上野平平價/淺草安靜/澀谷潮流/池袋家庭房。附每晚NT$800起平價飯店推薦、交通路線解析與選擇指南，幫你找到最適合的下榻地點。",
    "tags": [
      "住宿指南",
      "分區分析",
      "新手必讀"
    ]
  },
  {
    "id": "japan-drugstore-checklist",
    "title": "日本藥妝必買清單：最新美妝、保健品、常備藥攻略",
    "category": "日本自由行",
    "url": "japan-drugstore-checklist.html",
    "coverImage": "/images/Japanese drugstore cosmetics.webp",
    "intro": "2026最新日本藥妝必買清單與免稅購物攻略！包含EVE、合利他命、安耐曬等最夯感冒藥、美妝、護唇膏價格與功效。內建獨家「日本藥妝購物清單與預算精算工具」，搭配唐吉訶德、松本清與大國藥妝最新折價券優惠碼，帶你用最聰明、最性價比的方式橫掃日本藥妝店！",
    "tags": [
      "購物必看",
      "2026清單",
      "省錢折價券"
    ]
  },
  {
    "id": "kansai-pass",
    "title": "關西交通票券指南：一秒選對關西周遊卡、JR Pass",
    "category": "日本自由行",
    "url": "kansai-pass.html",
    "coverImage": "/images/kansai-hero.webp",
    "intro": "關西交通票券完全指南2026：JR Pass 5日券、關西周遊卡、大阪周遊卡、ICOCA 儲值卡比較。提供獨家互動式交通省錢試算器，輸入行程自動推薦最省錢票券組合，附京阪神奈交通攻略。",
    "tags": [
      "交通票券",
      "關西攻略",
      "省錢密技"
    ]
  },
  {
    "id": "hokkaido-winter",
    "title": "北海道冬季賞雪：夢幻雪祭、小樽運河與溫泉鄉慢遊",
    "category": "日本自由行",
    "url": "hokkaido-winter.html",
    "coverImage": "/images/hokkaido-hero.webp",
    "intro": "2026最新日本北海道冬季5天4夜自由行最完整行程規劃！包含札幌雪祭、小樽雪燈之路、旭山動物園企鵝散步、三大蟹與成吉思汗烤肉美食指南，附JR北海道PASS乘車券精算與冬季穿搭防摔攻略。",
    "tags": [
      "冬季賞雪",
      "北海道",
      "溫泉推薦"
    ]
  },
  {
    "id": "okinawa",
    "title": "沖繩自駕攻略：租車、右駕、私房景點與超速罰單防範",
    "category": "日本自由行",
    "url": "okinawa.html",
    "coverImage": "/images/okinawa-hero.webp",
    "intro": "2026 沖繩自駕4天3夜攻略：美麗海水族館、古宇利島大橋、美國村、國際通與瀨長島。含獨家「沖繩自駕預算試算器」與「租車保險攻略」，幫你精準抓預算、避開隱藏費用。",
    "tags": [
      "沖繩自駕",
      "租車指南",
      "海景私房點"
    ]
  },
  {
    "id": "kyoto-temples",
    "title": "京都寺廟散步地圖：12大世遺神廟深度探訪與參拜禮儀",
    "category": "日本自由行",
    "url": "kyoto-temples.html",
    "coverImage": "/images/kyoto-hero.webp",
    "intro": "2026 京都寺廟與紅葉攻略：清水寺、金閣寺、伏見稻荷大社、嵐山竹林小徑。內含獨家「京都參拜與交通預算計算器」、「寺廟參拜禮儀與禁忌測驗」與最佳賞楓時間，帶你深度探索古都禪意。",
    "tags": [
      "京都文化",
      "寺廟散策",
      "參拜禮儀"
    ]
  },
  {
    "id": "osaka-food",
    "title": "大阪美食攻略：道頓堀、黑門市場、心齋橋吃貨指南",
    "category": "日本自由行",
    "url": "osaka-food.html",
    "coverImage": "/images/osaka-food-hero.webp",
    "intro": "2026大阪2天1夜美食攻略：道頓堀必吃章魚燒、心齋橋排隊甜點、黑門市場海鮮及梅田地下街美食。內含獨家「大阪街頭美食與交通預算計算器」與「大阪吃貨美食王挑戰測驗」。",
    "tags": [
      "大阪美食",
      "必吃清單",
      "在地老店"
    ]
  },
  {
    "id": "osaka-usj",
    "title": "大阪環球影城USJ：購票、整理券、瑪利歐樂園入園密技",
    "category": "日本自由行",
    "url": "osaka-usj.html",
    "coverImage": "/images/osaka-usj-hero.webp",
    "intro": "2026大阪環球影城（USJ）玩樂攻略：門票與快速通關券選購教學、超級任天堂世界/哈利波特免排隊秘訣。內含「USJ購票與遊玩預算計算器」與「USJ達人檢定測驗」。",
    "tags": [
      "USJ攻略",
      "快速通關",
      "任天堂世界"
    ]
  },
  {
    "id": "japan-budget-guide",
    "title": "日本預算指南：機票、交通、住宿、餐飲真實花費估算",
    "category": "日本自由行",
    "url": "japan-budget-guide.html",
    "coverImage": "/images/japan-budget-hero.webp",
    "intro": "2026最新日本自由行預算精算手冊！包含機票、住宿、交通、美食與藥妝購物花費明細，提供1人到多人的小資背包客、經典高CP值與奢華行程預算範本，附省錢15招實戰技巧。",
    "tags": [
      "預算規劃",
      "真實花費",
      "日本理財"
    ]
  },
  {
    "id": "fukuoka-5days",
    "title": "福岡5天4夜攻略：九州門戶、博多屋台與柳川遊船",
    "category": "日本自由行",
    "url": "fukuoka-5days.html",
    "coverImage": "/images/Fukuoka.webp",
    "intro": "2026最新日本福岡5天4夜自由行最完整行程表！包含太宰府柳川一日遊、門司港 retro、LaLaport 1:1鋼彈、博多拉麵與中洲屋台美食地圖，附地鐵JR交通券試算與飯店推薦。",
    "tags": [
      "北九州",
      "福岡行程",
      "博多屋台"
    ]
  },
  {
    "id": "japan-cherry-blossom-season",
    "title": "日本賞櫻季攻略：最新開花預測、關東關西賞櫻熱點",
    "category": "日本自由行",
    "url": "japan-cherry-blossom-season.html",
    "coverImage": "/images/Cherry blossom and autumn foliage viewing in Japan.webp",
    "intro": "2026最新日本櫻花滿開預測全攻略！包含東京、京都、大阪、福岡與北海道開花時程表。提供5大經典賞櫻名所與交通票券（JR Pass、地鐵券）搭配，附贈獨家互動式「追櫻時程與行程規劃器」！",
    "tags": [
      "賞櫻前線",
      "櫻花祭",
      "攝影指南"
    ]
  },
  {
    "id": "japan-money-saving-tips",
    "title": "日本省錢密技：小資族必收的 10 個旅日省錢絕招",
    "category": "日本自由行",
    "url": "japan-money-saving-tips.html",
    "coverImage": "/images/Save money in Japan 20.webp",
    "intro": "去日本省錢20個必看眉角2026：里程兌換機票、免稅店退稅10%技巧、商務旅館平價住宿、超市19:00折扣時間、交通票券搭配、唐吉訶德採購攻略。自由行省下30%。",
    "tags": [
      "小資省錢",
      "高CP值",
      "精省攻略"
    ]
  },
  {
    "id": "seoul-food",
    "title": "首爾必吃美食攻略：一隻雞、烤肉、醬蟹吃貨天堂",
    "category": "韓國自由行",
    "url": "seoul-food.html",
    "coverImage": "/images/seoul-hero1.webp",
    "intro": "首爾必吃美食攻略2026：弘大烤肉、明洞辣炒年糕、廣藏市場生拌牛肉、新村雪濃湯、江南與聖水洞咖啡廳。附明洞換錢教學、T-money卡與交通，第一次首爾自由行必看。",
    "tags": [
      "首爾美食",
      "必吃地圖",
      "吃貨必看"
    ]
  },
  {
    "id": "busan-capsule",
    "title": "釜山膠囊列車預約：海雲台海濱列車訂票教學與自製行程",
    "category": "韓國自由行",
    "url": "busan-capsule.html",
    "coverImage": "/images/busan-hero1.webp",
    "intro": "2026最新釜山海雲台天空膠囊列車（Sky Capsule）預約最完整攻略！教你如何搶購「尾浦往青沙浦」夕陽最美時段票、實測票價試算、最划算的VBP景點套票組合、路線地圖與防坑注意事項！",
    "tags": [
      "熱門景點",
      "釜山預約",
      "網美打卡"
    ]
  },
  {
    "id": "busan-4days",
    "title": "釜山4天3夜攻略：絕美海景、甘川洞文化村與海鮮大餐",
    "category": "韓國自由行",
    "url": "busan-4days.html",
    "coverImage": "/images/busan-hero.webp",
    "intro": "2026韓國釜山4天3夜自由行最完整攻略！為您規劃最經典釜山行程：必搭海雲台天空膠囊列車、白淺灘文化村海景咖啡、甘川洞文化村尋找小王子，品嚐松亭三代豬肉湯飯與現撈海鮮烤貝，附最划算地鐵交通與飯店推薦。",
    "tags": [
      "海洋城市",
      "釜山行程",
      "海鮮美食"
    ]
  },
  {
    "id": "jeju-island",
    "title": "濟州島自駕環島：火山黑沙灘、橘子工坊與慵懶海景咖啡",
    "category": "韓國自由行",
    "url": "jeju-island.html",
    "coverImage": "/images/jeju-hero.webp",
    "intro": "濟州島自駕環島3天2夜攻略2026：城山日出峰日出、牛島花生冰淇淋、漢拏山登頂、涯月海邊咖啡街。附租車比價平台、必吃黑豬肉烤肉店、海鮮鍋名店推薦與自駕注意事項。",
    "tags": [
      "濟州島",
      "海島自駕",
      "咖啡廳巡禮"
    ]
  },
  {
    "id": "korea-budget",
    "title": "韓國預算解析：小資首爾釜山行、餐飲美妝花費指南",
    "category": "韓國自由行",
    "url": "korea-budget.html",
    "coverImage": "/images/korea-budget-hero.webp",
    "intro": "最完整的首爾自由行預算規劃：機票、飯店、餐費、景點門票與購物花費完整拆解，附明洞換錢所比價、省錢15招與費用估算計算器，5天4夜小資行程總預算詳細分析一看就懂！",
    "tags": [
      "預算規劃",
      "韓國購物",
      "消費指南"
    ]
  },
  {
    "id": "seoul-5days",
    "title": "首爾5天4夜極致攻略：景福宮韓服體驗與東大門潮流血拼",
    "category": "韓國自由行",
    "url": "seoul-5days.html",
    "coverImage": "/images/seoul-hero.webp",
    "intro": "2026首爾5天4夜自由行行程表：穿著華麗韓服漫步景福宮、南山首爾塔鎖住愛情、弘大/新村朝聖街頭藝人、東大門夜間批發市場。含T-money卡交通指南、AREX機場快線、明洞/弘大住宿推薦與精準預算。",
    "tags": [
      "首爾行程",
      "韓服體驗",
      "東大門"
    ]
  },
  {
    "id": "korea-transport",
    "title": "韓國交通攻略：Tmoney、KTX、NAVER Map與計程車叫車叫車",
    "category": "韓國自由行",
    "url": "korea-transport.html",
    "coverImage": "/images/korea-transport.webp",
    "intro": "韓國不適用 Google Map？別慌！教你如何使用 NAVER Map/Kakao Map 找路、搭乘 KTX 高鐵穿梭首爾釜山、以及 Kakao T 叫計程車。",
    "tags": [
      "交通必學",
      "實用APP",
      "地圖導航"
    ]
  },
  {
    "id": "korea-money-saving-tips",
    "title": "韓國省錢密技：Olive Young 退稅、平價飯捲與美妝折扣",
    "category": "韓國自由行",
    "url": "korea-money-saving-tips.html",
    "coverImage": "/images/South Korean tax refund.webp",
    "intro": "2026韓國首爾、釜山自由行必讀省錢祕笈：最新退稅門檻下調至₩15,000省錢技巧、明洞民間換錢所最新比價、T-money與氣候同行卡隱藏交通優惠、大型超市晚間特價、炸雞與平價咖啡外帶折扣，並附動態預算省錢試算器！",
    "tags": [
      "小資精省",
      "韓國特價",
      "退稅密技"
    ]
  },
  {
    "id": "seoul-food-map",
    "title": "首爾美食地圖：10 大經典韓食推薦與排隊地獄避開指南",
    "category": "韓國自由行",
    "url": "seoul-food-map.html",
    "coverImage": "/images/seoul-hero.webp",
    "intro": "首爾美食地圖：10大經典韓食推薦與排隊地獄避開指南，附辣炒年糕、韓式炸雞、豬肉湯飯、蔘雞湯各分店最佳免排隊用餐時段與地鐵出口指南，2026最新美食攻略及免排隊時段表",
    "tags": [
      "韓式料理",
      "免排隊祕辛",
      "首爾吃貨"
    ]
  },
  {
    "id": "hualien-taitung",
    "title": "花東三天兩夜慢遊：伯朗大道自行車、七星潭聽浪與太魯閣",
    "category": "台灣旅遊",
    "url": "hualien-taitung.html",
    "coverImage": "/images/hualien-hero.webp",
    "intro": "花蓮台東3天2夜慢活行程攻略2026：太魯閣國家公園壯麗峽谷、七星潭海灣風光、蘇花公路清水斷崖、池上伯朗大道金黃稻田、多良車站海景。附自駕租車指南、在地人美食與海景民宿推薦。",
    "tags": [
      "花東旅遊",
      "三天兩夜",
      "大自然療癒"
    ]
  },
  {
    "id": "tainan-food",
    "title": "台南美食牛肉湯：在地人排隊神店與無名小吃狂熱之旅",
    "category": "台灣旅遊",
    "url": "tainan-food.html",
    "coverImage": "/images/tainan-hero.webp",
    "intro": "台南美食牛肉湯地圖2026：文章牛肉湯、六千牛肉湯、阿村牛肉湯比較，國華街必吃碗粿、春捲、小卷米粉，與極具故事感的日式老屋咖啡店，附交通方式與營業時間完整整理。",
    "tags": [
      "台南小吃",
      "牛肉湯",
      "美食古都"
    ]
  },
  {
    "id": "kenting",
    "title": "墾丁海景夜市攻略：砂島貝殼砂、萬里桐浮潛與海景民宿",
    "category": "台灣旅遊",
    "url": "kenting.html",
    "coverImage": "/images/kenting-hero.webp",
    "intro": "2026墾丁3天2夜自由行全攻略！南灣浮潛戲水、龍磐公園看海觀星、鵝鑾鼻最南端打卡，墾丁大街夜市與後壁湖海鮮必吃美食精選，以及高CP值海景民宿推薦，出發前必看！",
    "tags": [
      "墾丁渡假",
      "浮潛推薦",
      "海景民宿"
    ]
  },
  {
    "id": "taipei-food",
    "title": "台北美食地圖：大稻埕慈聖宮、米其林夜市與文青咖啡館",
    "category": "台灣旅遊",
    "url": "taipei-food.html",
    "coverImage": "/images/taipei-food-hero.webp",
    "intro": "台北美食地圖2026：鼎泰豐、永康街、寧夏夜市、饒河夜市、東區早午餐完整攻略，附12個行政區必吃推薦、交通方式與營業時間，讓你吃得像在地人一樣精準不踩雷超實用！",
    "tags": [
      "台北美食",
      "文青咖啡",
      "夜市指南"
    ]
  },
  {
    "id": "jiufen",
    "title": "九份老街攻略：阿妹茶樓、賴阿婆芋圓與悲情城市茶香",
    "category": "台灣旅遊",
    "url": "jiufen.html",
    "coverImage": "/images/jiufen-hero.webp",
    "intro": "九份老街2026完整攻略｜阿妹茶樓茶席、芋圓冰品排行、紅糟肉肉圓、昇平戲院懷舊。附火車+公車交通方式、平日避人潮最佳拍照時段、黃金瀑布順遊路線與住宿推薦清單完整整理。",
    "tags": [
      "山城九份",
      "茶樓體驗",
      "懷舊景點"
    ]
  },
  {
    "id": "chiang-mai",
    "title": "清邁數位遊牧指南：文青古城、高質感咖啡廳與工作共享空間",
    "category": "東南亞自由行",
    "url": "chiang-mai.html",
    "coverImage": "/images/chiangmai-hero.webp",
    "intro": "2026清邁數位遊牧與自由行全攻略！整理尼曼區工作咖啡廳、Punspace/Yellow等共享空間、古城帕邢寺、周日夜市及高CP值公寓住宿與日常開銷，帶你體驗泰北文青慢活生活。",
    "tags": [
      "數位遊牧",
      "清邁生活",
      "文青古城"
    ]
  },
  {
    "id": "bangkok-3days",
    "title": "曼谷吃貨攻略：街頭小吃、泰式奶茶與高空星光酒吧",
    "category": "東南亞自由行",
    "url": "bangkok-3days.html",
    "coverImage": "/images/bangkok-hero.webp",
    "intro": "2026曼谷3天2夜吃貨完整攻略！精選洽圖洽週末市集必買必吃、唐人街百年燕窩、水門市場海南雞飯及船麵等10大在地美食，附BTS/MRT空鐵交通教學、最划算的換錢所比價與精選暹羅區高CP值住宿。",
    "tags": [
      "曼谷吃貨",
      "高空酒吧",
      "泰式料理"
    ]
  },
  {
    "id": "bangkok-massage",
    "title": "曼谷按摩推薦：高性價比、頂級奢華泰式 SPA 評比指南",
    "category": "東南亞自由行",
    "url": "bangkok-massage.html",
    "coverImage": "/images/bangkok-massage-hero.webp",
    "intro": "2026曼谷按摩SPA完整攻略：平價臥佛寺泰式指壓、高CP值Let's Relax、頂級Oasis貴婦SPA到Divana Strings，8家精選不踩雷店家分析與預約教學",
    "tags": [
      "按摩SPA",
      "放鬆行程",
      "曼谷推薦"
    ]
  },
  {
    "id": "vietnam-danang",
    "title": "越南峴港攻略：美溪沙灘、巴拿山黃金佛手橋與會安古鎮",
    "category": "東南亞自由行",
    "url": "vietnam-danang.html",
    "coverImage": "/images/vietnam-danang-hero.webp",
    "intro": "2026越南峴港3天2夜自由行攻略！精選巴拿山佛手橋高空纜車、美溪沙灘溫暖日出、會安古鎮夢幻燈籠街等必去景點與在地美食，附電子簽證、摩托車租借與最划算海景飯店推薦。",
    "tags": [
      "越南峴港",
      "佛手橋",
      "會安古鎮"
    ]
  },
  {
    "id": "singapore-3days",
    "title": "新加坡3天2夜攻略：濱海灣花園、魚尾獅與環球影城",
    "category": "東南亞自由行",
    "url": "singapore-3days.html",
    "coverImage": "/images/singapore.webp",
    "intro": "2026最新新加坡3天2夜自由行全攻略！深度探訪濱海灣花園超級樹、牛車水美食街、小印度香料市場與哈芝巷彩繪壁畫，附免簽入境須知、地鐵交通卡EZ-Link使用教學、小資省錢技巧與熱門住宿推薦。",
    "tags": [
      "新加坡",
      "花園城市",
      "3天2夜"
    ]
  },
  {
    "id": "kualalumpur-3days",
    "title": "吉隆坡3天2夜攻略：雙子星大樓、黑風洞與多元文化美食",
    "category": "東南亞自由行",
    "url": "kualalumpur-3days.html",
    "coverImage": "/images/kualalumpur-3days.webp",
    "intro": "2026最新吉隆坡3天2夜自由行全攻略！深度探訪雙峰塔觀景台、茨廠街夜市、黑風洞彩虹階梯與武吉免登購物，附交通指南、小資住宿推薦、必吃美食與省錢交通卡使用教學。",
    "tags": [
      "吉隆坡",
      "雙子星塔",
      "黑風洞"
    ]
  },
  {
    "id": "angkor-wat-2days",
    "title": "吳哥窟2天1夜攻略：小吳哥日出、高棉的微笑與塔普倫寺",
    "category": "東南亞自由行",
    "url": "angkor-wat-2days.html",
    "coverImage": "/images/angkor.webp",
    "intro": "2026最新柬埔寨吳哥窟2天1夜自由行攻略！深度探訪小吳哥倒影日出、巴戎寺高棉的微笑、塔普倫寺巨樹奇景與神秘崩密列，附電子簽證申請、最新門票、包車交通與省錢指南。",
    "tags": [
      "吳哥窟",
      "日出美景",
      "世界遺產"
    ]
  },
  {
    "id": "thailand-sim",
    "title": "泰國eSIM/SIM卡指南：三大電信AIS、True、dtac網速與選法",
    "category": "東南亞自由行",
    "url": "thailand-sim.html",
    "coverImage": "/images/thailand-sim.webp",
    "intro": "泰國上網卡實測比較2026：AIS/TrueMove/DTAC三大電信訊號速度、價格฿199起、覆蓋率解析。附機場購買教學、eSIM推薦、清邁曼谷普吉島實測與常見問題解答。",
    "tags": [
      "泰國網卡",
      "eSIM資費",
      "通訊必看"
    ]
  },
  {
    "id": "seasia-budget-travel-guide",
    "title": "東南亞預算攻略：泰越馬新四國，極致省錢高 CP 玩樂法",
    "category": "東南亞自由行",
    "url": "seasia-budget-travel-guide.html",
    "coverImage": "/images/seasia-budget-travel-guide.webp",
    "intro": "東南亞省錢旅遊攻略2026：泰國、越南、馬來西亞、印尼、菲律賓與新加坡的預算規劃與自由行指南。含各國日均消費比較、免簽/電子簽最新資訊、廉航機票、交通、住宿與餐飲省錢心法。",
    "tags": [
      "東南亞預算",
      "省錢密技",
      "高CP玩樂"
    ]
  },
  {
    "id": "vietnam-hochiminh",
    "title": "胡志明市3天2夜：法式中央郵局、粉紅教堂與越南咖啡文化",
    "category": "東南亞自由行",
    "url": "vietnam-hochiminh.html",
    "coverImage": "/images/vietnam-hochiminh-hero.webp",
    "intro": "胡志明市3天2夜攻略2026：范老五街酒吧夜市、湄公河三角洲一日遊、戰爭遺跡博物館、10大必吃美食、3大住宿區推薦。含免簽證費教學、Grab叫車攻略與換錢技巧。",
    "tags": [
      "胡志明市",
      "法式情懷",
      "越南咖啡"
    ]
  },
  {
    "id": "travel-tools",
    "title": "精選慢旅工具箱：讓每一次出發都輕鬆優雅、萬無一失",
    "category": "旅遊工具",
    "url": "travel-tools.html",
    "coverImage": "/images/travel-tools-hero.webp",
    "intro": "旅遊省錢工具包：Trip.com 飯店比價、Skyscanner 機票、Klook 門票、Airalo eSIM、Agoda 住宿，出國必備工具一次打包，領取專屬優惠。",
    "tags": [
      "工具大集合",
      "打包助手",
      "計算器"
    ]
  },
  {
    "id": "power-plug-guide",
    "title": "世界各國插座電壓指南：插頭規格與變壓器實用查詢",
    "category": "旅遊工具",
    "url": "power-plug-guide.html",
    "coverImage": "/images/power.webp",
    "intro": "出國插座電壓查詢表 2026：台灣人出國必看，涵蓋日本、韓國、泰國、越南、歐美等 20+ 國家的插頭規格、110V-240V 電壓與頻率對照。教你如何判斷是否需要轉接頭與變壓器，萬國插座推薦。",
    "tags": [
      "插座電壓",
      "萬國插頭",
      "出國準備"
    ]
  },
  {
    "id": "budget-airline-guide",
    "title": "廉價航空搶票攻略：三大絕招讓你買到驚人低價機票",
    "category": "旅遊工具",
    "url": "budget-airline-guide.html",
    "coverImage": "/images/budget-airline.webp",
    "intro": "廉航搶票攻略：酷航Scoot、樂桃Peach、虎航Tigerair直飛機票比價，開賣時間、搶票技巧、行李規定、選座位策略、廉航vs傳統航空優缺點比較。出國省錢必看。",
    "tags": [
      "廉航促銷",
      "搶票密技",
      "行李規則"
    ]
  },
  {
    "id": "miles-calculator",
    "title": "里程累積試算器：三大航空聯盟與票等里程計算教學",
    "category": "旅遊工具",
    "url": "miles-calculator.html",
    "coverImage": "/images/miles.webp",
    "intro": "里程累積試算器：輸入每月刷卡金額與搭機頻率，自動計算多久免費飛日本/韓國/泰國。含5大信用卡紅利轉里程比例、航空公司里程需求速查、最短累積時間表與最佳刷卡組合推薦。",
    "tags": [
      "里程試算",
      "免費機票",
      "三大聯盟"
    ]
  },
  {
    "id": "packing-list",
    "title": "出國打包清單：互動式清單，出發前檢查絕不漏掉任何東西",
    "category": "旅遊工具",
    "url": "packing-list.html",
    "coverImage": "/images/packing-list.webp",
    "intro": "2026最新出國打包清單！提供客製化行李檢查表（3天/5天/7天以上），日本入境藥品申報規定、液體隨身限制、行動電源登機規範。一鍵勾選進度追蹤，助你輕鬆打包不漏帶。",
    "tags": [
      "打包助手",
      "清單必備",
      "線上勾選"
    ]
  },
  {
    "id": "esim-comparison",
    "title": "eSIM 比較推薦：原號漫遊、實體網卡、eSIM 優缺點實評",
    "category": "旅遊工具",
    "url": "esim-comparison.html",
    "coverImage": "/images/esim-hero.webp",
    "intro": "出國eSIM實測比較2026！收錄日本、韓國、泰國、越南8大主流eSIM品牌（Airalo, Holafly, eSIM Go, ByteSIM）測速、價格與訊號覆蓋率。內置互動智慧推薦器，3秒算出最適合你的上網方案。",
    "tags": [
      "網路選法",
      "eSIM評價",
      "無痛設定"
    ]
  },
  {
    "id": "tax-refund-calculator",
    "title": "各國免稅與退稅試算器：日本 10%、韓國最新現場退稅機制",
    "category": "旅遊工具",
    "url": "tax-refund-calculator.html",
    "coverImage": "/images/Free tax refund.webp",
    "intro": "免稅店退稅試算器：輸入消費金額與國家，自動計算退稅金額。附韓國/日本/泰國/越南退稅流程、手續費、最低消費門檻、機場退稅櫃檯位置與常見問題解答完整攻略教學。",
    "tags": [
      "退稅試算",
      "購物攻略",
      "機場退稅"
    ]
  },
  {
    "id": "notion-travel-template",
    "title": "Notion 慢旅模板：超高顏值、一鍵套用的精緻日程規劃器",
    "category": "旅遊工具",
    "url": "notion-travel-template.html",
    "coverImage": "/images/notion-travel.webp",
    "intro": "免費下載 2026 Notion 旅遊規劃模板！一頁整合行程表、預算追蹤、行李打包清單與住宿筆記，支援手機同步、多人協作與離線編輯，讓你輕鬆管理每一次旅程不漏接。",
    "tags": [
      "Notion模板",
      "高顏值規劃",
      "免費下載"
    ]
  },
  {
    "id": "about",
    "title": "關於我們",
    "category": "關於我們",
    "url": "about.html",
    "coverImage": "/images/about-hero.webp",
    "intro": "關於均在路上 Travel Lab：我們的使命是幫助讀者用最合理的預算，走最深度的旅程。了解我們的故事、品牌願景、專業編輯團隊、合作夥伴與聯繫方式，以及常見問答。",
    "tags": [
      "團隊理念",
      "探索生活",
      "聯絡我們"
    ]
  },
  {
    "id": "japan-travel",
    "title": "日本自由行終極攻略指南 2026｜最新行程安排、必讀景點、櫻花季與藥妝省錢攻略｜均在路上 Travel Lab",
    "category": "日本自由行",
    "url": "japan-travel.html",
    "coverImage": "/images/japan-travel.webp",
    "intro": "2026最專業的日本自由行全攻略中心！整合東京、福岡、北海道等熱門都市的五天四夜行程規劃、住宿推薦、櫻花季預測與藥妝免稅必買清單。內置「日本行程路線與預算動態精算工具」，助您輕鬆省時、性價比玩轉日本！",
    "tags": [
      "日本攻略",
      "行程規劃",
      "櫻花季",
      "藥妝清單"
    ]
  },
  {
    "id": "korea-travel",
    "title": "韓國自由行全攻略 2026｜首爾釜山濟州島一站搞定｜均在路上 Travel Lab",
    "category": "韓國自由行",
    "url": "korea-travel.html",
    "coverImage": "/images/korea-travel.webp",
    "intro": "2026韓國自由行完整攻略！含簽證機票搶票、T-money交通卡購買、明洞換錢退稅秘技、必買化妝品精選，以及首爾、釜山、濟州島各大熱門目的地行程規劃與索引，出發前必看！",
    "tags": [
      "韓國攻略",
      "首爾釜山",
      "濟州島",
      "退稅秘技"
    ]
  },
  {
    "id": "southeast-asia",
    "title": "東南亞自由行終極攻略指南 2026｜最新行程安排、必讀景點、泰國與越南省錢攻略｜均在路上 Travel Lab",
    "category": "東南亞自由行",
    "url": "southeast-asia.html",
    "coverImage": "/images/southeast-asia.webp",
    "intro": "2026最專業的東南亞自由行全攻略中心！整合泰國曼谷、越南峴港、胡志明市等熱門城市的行程規劃、按摩Spa推薦、上網網卡實測與熱門景點省錢攻略。內置「東南亞行程與預算動態精算工具」，輕鬆控預算、性價比玩轉東南亞！",
    "tags": [
      "東南亞攻略",
      "泰國越南",
      "行程規劃",
      "省錢攻略"
    ]
  },
  {
    "id": "taiwan-travel",
    "title": "台灣旅遊攻略｜均在路上 Travel Lab",
    "category": "台灣旅遊",
    "url": "taiwan-travel.html",
    "coverImage": "/images/taiwan-travel.webp",
    "intro": "台灣深度旅遊提案2026：花東縱谷3天2夜自然之旅、台南美食牛肉湯地圖、墾丁海景夜市攻略，由在地人帶路探索私房景點與季節限定體驗，附大眾交通與自駕路線建議指南。",
    "tags": [
      "台灣旅遊",
      "花東縱谷",
      "台南美食",
      "墾丁"
    ]
  },
  {
    "id": "bangkok-4days",
    "title": "曼谷4天3夜攻略2026｜超詳盡行程表+必吃美食+按摩精選+預算試算｜均在路上",
    "category": "東南亞自由行",
    "url": "bangkok-4days.html",
    "coverImage": "/images/bangkok-hero.webp",
    "intro": "2026年最新曼谷4天3夜自由行攻略！包含每日推薦行程時間線、三大住宿區域深度解析、十大人氣美食、正統泰式按摩推薦、BTS/MRT交通攻略以及詳細的經濟與舒適型預算試算。第一次去泰國必看！",
    "tags": [
      "曼谷攻略",
      "4天3夜",
      "泰式美食",
      "預算試算"
    ]
  },
  {
    "id": "budget-calculator",
    "title": "出國旅遊預算試算器2026｜機票飯店花費一鍵試算｜均在路上 Travel Lab",
    "category": "旅遊工具",
    "url": "budget-calculator.html",
    "coverImage": "/images/budget-calculator.webp",
    "intro": "出國旅遊預算試算器：輸入國家、天數與人數，自動幫你計算機票、住宿、餐飲、交通與購物等預算花費。內含日本、韓國、泰國、歐洲多國參考價格，精準抓預算不求人超實用！",
    "tags": [
      "預算試算",
      "機票飯店",
      "省錢技巧",
      "旅遊工具"
    ]
  },
  {
    "id": "contact",
    "title": "聯絡窗口｜均在路上 Travel Lab",
    "category": "關於我們",
    "url": "contact.html",
    "coverImage": "/images/about-hero.webp",
    "intro": "聯絡均在路上 Travel Lab｜LINE 即時詢問(@938nzmjr)與 Email 來信，常見問題24小時內回覆。旅遊行程規劃、合作提案、網站功能建議歡迎聯絡，我們樂意協助。",
    "tags": [
      "聯絡我們",
      "LINE詢問",
      "合作提案",
      "旅遊諮詢"
    ]
  },
  {
    "id": "downloads",
    "title": "免費下載專區",
    "category": "旅遊工具",
    "url": "downloads.html",
    "coverImage": "/images/notion-travel.webp",
    "intro": "均在路上 Travel Lab 免費旅遊資源下載中心｜打包清單模板、旅遊預算試算表、行程規劃表、機票比價技巧PDF等實用工具免費下載，出國前一次備齊所有準備。",
    "tags": [
      "免費下載",
      "打包清單",
      "預算試算表",
      "行程規劃"
    ]
  }
];
