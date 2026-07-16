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
    "intro": "初訪東京的最佳全攻略！帶你穿梭於澀谷繁華十字路口、淺草寺江戶情懷與新宿的深夜居酒屋，打造無懈可擊的五日行程。",
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
    "intro": "新宿、澀谷、銀座、上野、淺草到底該住哪？一圖看懂各大商圈交通便利度、平均預算、購物指數，附高性價比旅宿推薦。",
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
    "intro": "最新日本松本清、大國藥妝必買神物！包含爆紅保養品、長輩指名保健品與家庭常備藥，提供現場結帳退稅折價券。",
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
    "intro": "京阪神奈自由行交通全解析！關西ICOCA、JR PASS關西地區鐵路周遊券、京都巴士一日券究竟哪個最省？超簡單判斷公式。",
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
    "intro": "走入銀裝素裹的純白童話世界。札榥雪祭、小樽運河裝扮夜景、登別地獄谷溫泉，附極寒氣候防寒穿搭與自駕/大眾交通指南。",
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
    "intro": "沖繩自駕必讀手冊！從台灣駕照譯本辦理、OTS租車流程、MapCode使用到日本道路安全規則，附中北部絕美海景自駕路線。",
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
    "intro": "深度感受京都千年底蘊。清水寺、金閣寺、伏見稻荷大社、銀閣寺經典散策，教你洗手舍洗手、拜殿二拜二拍手一拜的精確禮儀。",
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
    "intro": "「大阪之胃」完全吃貨地圖！章魚燒、大阪燒、炸串、黑門市場海鮮與排隊拉麵，精選 15 家當地人也愛去的傳奇老店。",
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
    "intro": "別當無頭蒼蠅！最新 USJ 超級任天堂世界、哈利波特魔法世界無痛入園全攻略，教你如何搶快速通關與保證入園整理券。",
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
    "intro": "去日本到底要準備多少錢？本篇拆解特價機票、平價青年旅館、百元便當到米其林餐廳的真實消費區間，附動態預算試算器。",
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
    "intro": "九州鐵道之旅起點！博多豚骨拉麵發源地屋台巡禮、太宰府天滿宮求學問、柳川乘著搖櫓船品嚐蒸蒸鰻魚飯，一網打盡。",
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
    "intro": "追逐粉紅春瀾。包含氣象株式會社最新櫻前線預測、東京目黑川、京都哲學之道、大阪城公園野餐指南，教你如何拍出空靈大片。",
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
    "intro": "超市晚上 8 點後的半價便當、超商限定平價神物、飯店免費溫泉與接駁、跨區域夜間大巴，教你如何花少少錢玩到最極致。",
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
    "coverImage": "/images/seoul-hero.webp",
    "intro": "首爾美食饕客指南！孔陵一隻雞、明洞神仙雪濃湯、弘大荒謬的生肉、廣藏市場生拌牛肉與綠豆煎餅，不踩雷在地推薦。",
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
    "coverImage": "/images/busan-hero.webp",
    "intro": "最新爆紅海雲台天空膠囊火車（Sky Capsule）超詳細預約訂票步驟教學！避開排隊人潮的秘密時段，拍出最美海景。",
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
    "intro": "海洋都市慢遊提案！甘川洞文化村尋找小王子、廣安里大橋絕美夜景、機張市場現撈大雪蟹、影島青沙浦網美咖啡，慵懶出發。",
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
    "intro": "韓國的世外桃源。濟州島自駕路況解析、漢拏山健行、城山日出峰、涯月邑絕美夕陽咖啡街，體驗最慵懶的島嶼度假情調。",
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
    "intro": "去韓國需要準備多少預算？從 WOWPASS/NAMANE 卡儲值、路邊攤辣炒年糕、人參雞、美妝店 Olive Young 血拼花費大公開。",
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
    "intro": "經典首爾行程！穿着華麗韓服漫步景福宮、南山首爾塔鎖住愛情、弘大/新村朝聖街頭藝人、東大門夜間不眠批發市場。",
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
    "coverImage": "/images/korea-money.webp",
    "intro": "小資族不可不知的韓國旅遊省錢攻略！超商 2+1/1+1 優惠買法、Olive Young 現場退稅、地鐵免費轉乘公車等隱藏細節。",
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
    "intro": "辣炒年糕、韓式炸雞、豬肉湯飯、韓式烤五花肉、蔘雞湯，最地道的首爾巷弄美食與各分店最佳免排隊用餐時段。",
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
    "intro": "逃離城市，大口吸飽花東純淨空氣。池上伯朗大道、七星潭鵝卵石海灘、石梯坪獨特海蝕地貌，來一場療癒心靈的蔚藍慢旅行。",
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
    "intro": "清晨 4 點的牛肉湯狂熱！六千、文章、阿村牛肉湯大比拼，加上小卷米粉、蝦仁飯、鱔魚意麵，為你解鎖台南古都的甜美滋味。",
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
    "intro": "台灣最南端的陽光、沙灘與碧海。砂島純淨貝殼砂沙灘、萬里桐潮間帶與夕陽浮潛，精選 5 間躺在床上就能看日落的海景民宿。",
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
    "intro": "台北多層次的美食面貌！在大稻埕大榕樹下品嚐排骨湯、探索饒河與寧夏夜市的米其林必比登推薦小吃、隱匿於赤峰街的深夜咖啡。",
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
    "intro": "紅燈籠高掛的山城。神似千與千尋場景的阿妹茶樓、品嚐軟 Q 的賴阿婆芋圓、遠眺基隆嶼海景、在茶館中靜聽雨水滴落聲。",
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
    "intro": "數位遊牧民族的天堂！清邁尼曼區最棒的網路工作咖啡廳、Punspace 共享空間推薦、古城帕邢寺、周日夜市慵懶慢活日常。",
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
    "intro": "辛辣、酸甜、繽紛的曼谷街頭滋味。米其林街頭泰式炒河粉、火山排骨、路邊隨手一杯的手標泰奶，晚上登上無邊際星空酒吧俯瞰夜色。",
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
    "intro": "一洗旅途疲憊！精選曼谷 8 家絕不踩雷的按摩店，包含百元平價泰式指壓（Let's Relax）到令人驚豔的頂級奢華貴婦 SPA（Oasis）。",
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
    "intro": "東方夏威夷的獨特魅力。漫步於世界最美沙灘之一的美溪沙灘、打卡巴拿山雲霧繚繞的黃金佛手橋、傍晚在會安古鎮釋放許願水燈。",
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
    "intro": "精緻而震撼的花園城市。濱海灣花園超級樹燈光秀、打卡噴水魚尾獅、品嚐亞坤斑蘭吐司與松發肉骨茶、聖淘沙小島漫步。",
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
    "intro": "驚豔的融合之美！登上著名的雙子星塔空中天橋、攀爬擁有巨大印度神像的彩虹階梯黑風洞、在阿羅街大啖沙嗲與椰漿飯。",
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
    "intro": "沉睡在森林中的宏偉廢墟。破曉時分靜待小吳哥蓮花池上的日出倒影、造訪擁有「高棉微笑」的巴戎寺、探索被巨樹纏繞的塔普倫寺。",
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
    "intro": "去曼谷清邁該用哪家電信？泰國三大電信 AIS（網速第一）、True/dtac（合併後訊號極佳）資費方案與免換卡 eSIM 設定完全指南。",
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
    "coverImage": "/images/budget-airline.webp",
    "intro": "教你如何分配東南亞旅行預算！從超便宜的越南街頭美食、泰國嘟嘟車議價密技、到如何利用大眾運輸玩轉昂貴的新加坡。",
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
    "intro": "東方小巴黎的慢步調旅行。西貢聖母大教堂、百年郵局寄一張明信片、參訪極具少女心的耶穌聖心堂（粉紅教堂），喝一杯香醇蛋咖啡。",
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
    "intro": "我們為您打造的專屬旅行工具合集。整合插座查詢、打包清單、里程試算與免稅計算，讓旅行準備工作變得和度假一樣迷人。",
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
    "intro": "出國電器燒掉就糟了！本篇收錄日本、韓國、歐洲、東南亞等熱門地區插座形式（A/C/SE/BF等）、電壓（110V/220V）及萬國轉接頭選購要點。",
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
    "intro": "樂桃、酷航、虎航買票心法！本篇公開航空公司促銷時間點、手提行李重量規則、以及清空瀏覽器 Cookie 買到最低價格的實測密技。",
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
    "intro": "機票里程累積到底怎麼算？星空聯盟、天合聯盟、寰宇一家里程計算公式，手把手教你如何將出國機票的價值最大化，免費換下張機票。",
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
    "intro": "專為自由行旅客設計的智能打包清單！提供行李進度條，涵蓋護照、充電線、常備藥品，可隨時勾選、自訂新增項目。",
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
    "intro": "免插拔、不丟卡！最新 eSIM 電信方案實測，告訴你它在日韓和東南亞的真實現速，附三大主要國家的最優 eSIM 商家推薦表。",
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
    "intro": "出國購物血拼，退稅流程好複雜？本篇一鍵幫您試算在各國可退回多少稅額，附帶成田機場、仁川機場現場退稅手續與櫃檯引導。",
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
    "intro": "我們為讀者獨家開發的 Notion 旅行計畫模板！包含美觀的看板行程、每日支出表、打包清單、景點卡片，免費提供一鍵複製。",
    "tags": [
      "Notion模板",
      "高顏值規劃",
      "免費下載"
    ]
  },
  {
    "id": "about",
    "title": "關於我們：均在路上 Travel Lab — 傾聽靈魂深處的探險足音",
    "category": "關於我們",
    "url": "about.html",
    "coverImage": "/images/about-hero.webp",
    "intro": "我們是一群不願意走馬看花的漫遊者。不堆砌網紅打卡點，只為尋找晨霧、清泉、古鐘與那些藏在青苔底下的地方靈魂。",
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
    "intro": "台灣深度旅遊提案2026：花東縱谷三天兩夜、台南美食牛肉湯、墾丁海景夜市，在地人帶路私房景點。",
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
    "coverImage": "/images/miles-calculator.webp",
    "intro": "出國旅遊預算試算器：輸入國家、天數與人數，自動幫你計算機票、住宿、餐飲、交通與購物等預算花費。內含日本、韓國、泰國、歐洲與美國最新小資省錢技巧。",
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
    "title": "免費下載專區｜Travel Lab 均在路上",
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
