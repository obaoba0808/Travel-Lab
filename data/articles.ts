import { TravelArticle } from '../types';

export const travelArticles: TravelArticle[] = [
  {
    id: 'kyoto',
    title: '京都迴響：禪意金閣與竹林深處的呢喃',
    subtitle: '步入一座古老木造寺廟與時光抗衡、青苔庭園訴說千年故事的靜謐世界。',
    country: '日本',
    heroImage: 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=1200&auto=format&fit=crop',
    category: 'Culture',
    vibe: '禪意、傳統、寧靜',
    bestSeason: '春季（櫻花）與秋季（紅葉）',
    rating: 4.9,
    readTime: '閱讀時間 8 分鐘',
    author: {
      name: 'Elena Rostova',
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=200&auto=format&fit=crop',
      role: '旅遊專欄作家與文化歷史學者'
    },
    intro: '京都依然是日本傳統文化跳動的心臟。不同於東京霓虹閃爍的摩天大樓，京都將目光凝聚於美妙的枯山水、木造町家、以及祇園石板路上絲綢和服的沙沙細語。',
    publishDate: '2026年6月18日',
    highlights: [
      '漫步在嵐山竹林幽徑，聆聽陽光穿透高聳竹葉的呢喃',
      '親眼見證金閣寺（鹿苑寺）倒映在鏡湖池上的絕美金色倒影',
      '穿梭於伏見稻荷大社那延綿不絕的萬座朱紅色千本鳥居',
      '在祇園品嚐正宗精緻、細膩如畫的季節限定懷石料理'
    ],
    quote: "竹林間的微風聽起來不像是噪音，倒像是一首古老的唱詩班，溫柔地教會我們如何隨風擺動，而非折斷。",
    quoteAuthor: "Elena Rostova",
    content: [
      "體驗京都，是一場讓心跳慢下來的修行。當你穿過南禪寺古樸的木造山門，現代都市的喧囂瞬間退去，取而代之的是石盞中泉水滴落的清脆，以及青銅古鐘沉穩悠揚的迴響。在這裡，枯山水庭園中的每一顆砂石都代表著無垠意識之海中的孤島，每日清晨由僧侶們精細耙制，禪意盡在不言中。",
      "金閣寺這座建築奇蹟，是室町時代奢華美學的終極體現。它通體貼滿金箔，在鏡湖池上投射出近乎完美的對稱倒影。此處最初是將軍足利義滿的退休別墅。站立其前，你會驚覺京都並非僅僅在「保存」歷史，而是將歷史視為其日常韻律中依然鮮活的共同參與者。",
      "當夜幕降臨，祇園古老街區的燈籠逐一亮起。若足夠幸運，你或許能瞥見藝妓或舞妓匆匆趕往晚宴的身影，她們白皙的妝容與華麗的和服在町家深色杉木板的映襯下，勾勒出極其優雅的剪影。這是一個凝固在水晶般精緻中的世界，需要你全然放空心神，方能領略其真正的雅致。"
    ],
    itinerary: [
      {
        day: 1,
        title: '金色小徑與竹林低語',
        description: '清晨前往嵐山以避開人潮，感受竹林遮天蔽日帶來的清涼。隨後前往金閣寺，欣賞晨光下熠熠生輝的金色殿宇，午後在古老寺院中體驗一場洗滌心靈的宇治抹茶茶道。',
        spots: ['嵐山竹林', '金閣寺（鹿苑寺）', '天龍寺曹源池庭園'],
        tips: '建議於早上 7:00 前抵達嵐山竹林，此時光線最為空靈，且能獨享無人的靜謐竹林步道。',
        costEstimate: '約 3,500 日圓',
        image: 'https://images.unsplash.com/photo-1503899036084-c55cdd92da26?q=80&w=600&auto=format&fit=crop'
      },
      {
        day: 2,
        title: '千本鳥居的無盡迴廊',
        description: '南下前往伏見稻荷大社，沿著神聖的山道穿梭在逾萬座鮮紅鳥居之中。午後返回祇園，登上清水寺清水舞台，俯瞰整座京都市景，等待最唯美的夕陽夕照。',
        spots: ['伏見稻荷大社', '清水寺', '二年坂與三年坂'],
        tips: '登頂伏見稻荷大社全程約需 2-3 小時，但其實走到半山腰的「四辻十字路口」即可欣賞到極佳的京都市景，且人潮會減少大半。',
        costEstimate: '約 1,500 日圓',
        image: 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=600&auto=format&fit=crop'
      },
      {
        day: 3,
        title: '禪意庭園與哲學之道',
        description: '沿著哲學之道的櫻花水渠悠閒漫步，沿途有許多精緻的咖啡館。參訪銀閣寺（慈照寺）的向月台與銀沙灘，最後在龍安寺著名的枯山水石庭前靜坐冥想。',
        spots: ['哲學之道', '銀閣寺', '龍安寺石庭'],
        tips: '在龍安寺時，試著坐在木造緣側上，看看能否找到一個能同時看清全部 15 顆石頭的角度（據說傳統上無論從哪個角度看，總有一顆會被遮擋，這正是禪宗殘缺美學的體現）。',
        costEstimate: '約 2,000 日圓',
        image: 'https://images.unsplash.com/photo-1490806843957-31f4c9a91c6d?q=80&w=600&auto=format&fit=crop'
      }
    ],
    budgetEstimates: {
      hotelBudget: 150,
      diningBudget: 80,
      activityBudget: 40,
      flightBudget: 800
    },
    mapSpots: [
      {
        name: '嵐山竹林幽徑',
        lat: '35.0156° N',
        lng: '135.6715° E',
        x: 20,
        y: 35,
        description: '高聳的翠綠竹林在風中沙沙低語，空靈而神聖。',
        image: 'https://images.unsplash.com/photo-1503899036084-c55cdd92da26?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '金閣寺（鹿苑寺）',
        lat: '35.0394° N',
        lng: '135.7292° E',
        x: 45,
        y: 15,
        description: '貼滿金箔的舍利殿倒映在池水中，美得動人心魄。',
        image: 'https://images.unsplash.com/photo-1542044896530-05d85be9b11a?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '清水寺',
        lat: '35.0001° N',
        lng: '135.7840° E',
        x: 80,
        y: 55,
        description: '完全由木材榫接而成、未用一顆釘子的雄偉清水舞台。',
        image: 'https://images.unsplash.com/photo-1490806843957-31f4c9a91c6d?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '伏見稻荷大社',
        lat: '34.9671° N',
        lng: '135.7727° E',
        x: 75,
        y: 85,
        description: '延綿不絕攀升至稻荷山的鮮紅色朱砂鳥居長廊。',
        image: 'https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?q=80&w=400&auto=format&fit=crop'
      }
    ],
    packingList: [
      {
        category: '旅行必備',
        items: ['現金（日圓 - 許多京都古老寺廟僅接受現金購票）', '隨身 Wi-Fi 分享器或 eSIM 上網卡', 'IC卡 (Suica / ICOCA)', '舒適且易穿脫的步行鞋']
      },
      {
        category: '攝影與電子',
        items: ['相機與廣角鏡頭', '行動電源', '雙腳 Type-A 插頭轉接頭']
      },
      {
        category: '參拜禮儀',
        items: ['乾淨的襪子（參觀寺廟木造室內需脫鞋）', '環保摺疊購物袋', '小手帕（洗手舍潔淨雙手用）']
      }
    ],
    weatherForecast: [
      {
        season: '春季（3月 - 5月）',
        temp: '12°C - 20°C',
        description: '櫻花滿開的粉紅世界，微風和煦，氣候宜人。',
        suitability: '最熱門季節 - 適合賞櫻與古寺漫步，需提前預訂。',
        iconName: 'flower'
      },
      {
        season: '夏季（6月 - 8月）',
        temp: '22°C - 32°C',
        description: '氣候濕熱，青翠茂盛，伴隨著盛大的祇園祭祭典。',
        suitability: '色彩繽紛但濕熱 - 注意防暑與午後雷陣雨。',
        iconName: 'sun'
      },
      {
        season: '秋季（9月 - 11月）',
        temp: '10°C - 19°C',
        description: '漫山遍野的火紅楓葉與古樸木造寺廟交相輝映。',
        suitability: '極力推薦 - 氣候最舒適，紅葉景致無可匹敵。',
        iconName: 'leaf'
      },
      {
        season: '冬季（12月 - 2月）',
        temp: '1°C - 8°C',
        description: '遊客稀少、安靜祥和，偶爾迎來銀裝素裹的雪京都。',
        suitability: '避開人潮首選 - 適合享受靜謐，雪景看運氣。',
        iconName: 'snowflake'
      }
    ]
  },
  {
    id: 'switzerland',
    title: '阿爾卑斯遐想：漫步勞特布龍嫩的瀑布山谷',
    subtitle: '佇立於七十二道奔騰瀑布之下，凝望陡峭的花崗岩山峰直插瑞士湛藍的晴空。',
    country: '瑞士',
    heroImage: 'https://images.unsplash.com/photo-1502784444187-359ac186c5bb?q=80&w=1200&auto=format&fit=crop',
    category: 'Nature',
    vibe: '宏偉、絕美、高山祕境',
    bestSeason: '夏季（健行）與冬季（滑雪）',
    rating: 5.0,
    readTime: '閱讀時間 10 分鐘',
    author: {
      name: 'Marcus Vance',
      avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=200&auto=format&fit=crop',
      role: '高山攝影師與極限探險家'
    },
    intro: '坐落在被垂直懸崖合抱的深邃 U 型山谷中，勞特布龍嫩是童話世界的具體化身。七十二道瀑布從四周的峭壁傾瀉而下，沒入松林，在牧場上空織起一層永不散去的縹緲水霧。',
    publishDate: '2026年5月14日',
    highlights: [
      '仰望施陶巴赫瀑布（Staubbach Falls）從村莊後方近 300 公尺高的懸崖飛瀉而下',
      '搭乘歷史悠久的齒軌火車，登上被譽為「歐洲之巔」的少女峰（Jungfraujoch）',
      '漫步於米倫（Mürren）與吉梅爾瓦爾德（Gimmelwald）等禁止燃油車駛入的純淨花卉小鎮',
      '深入特呂默爾河瀑布（Trümmelbach Falls）探索隱匿在山體內部的轟鳴冰川地下暗河'
    ],
    quote: "在勞特布龍嫩山谷，群山並非只是環繞著你；它們將你緊緊擁入懷中，近得讓你彷彿能聽見冰川的心跳。",
    quoteAuthor: "Marcus Vance",
    content: [
      "在勞特布龍嫩醒來，是一場感官尺度的震撼。打開木屋的木窗，迎面而來的是施陶巴赫瀑布，如同一道懸掛在 300 公尺垂直峭壁上的銀色薄紗。空氣中瀰漫著新鮮松木、甜美高山牧草以及在晨光中緩緩融化的冰川氣息。山谷下方，牛鈴輕輕作響，交織成一首悠揚的阿爾卑斯交響樂。",
      "在懸崖頂端，坐落著遺世獨立的米倫小鎮（Mürren），這裡只能乘坐纜車與高山鐵路抵達。鎮上禁止汽車通行，懸掛在 1,600 公尺高的懸崖邊緣，在此可將艾格峰、僧侶峰與少女峰組成的瑞士三巨頭壯麗全景盡收眼底。在此健行宛如漫步在世界之脊，兩旁開滿了野生龍膽花與高山雪絨花。",
      "當你登上少女峰齒軌鐵路，瑞士無與倫比的工程奇蹟便展露無遺。火車直接鑿通艾格峰的堅硬岩壁，將你送達海拔 3,454 公尺的少女峰火車站——這也是歐洲海拔最高的火車站。步入斯芬克斯觀景台，廣袤無垠、白雪皚皚的阿萊奇冰川（阿爾卑斯山最長的冰川）在蔚藍晴空下一直綿延至地平線的盡頭。"
    ],
    itinerary: [
      {
        day: 1,
        title: '追尋山谷中的飛瀑足跡',
        description: '沿著平緩的山谷步道漫步，近距離感受施陶巴赫瀑布的壯麗。隨後深入山腹，參觀特呂默爾河瀑布——十道由巨大冰川融水匯聚而成的瀑布在岩洞中猛烈轟鳴、飛流直下。',
        spots: ['施陶巴赫瀑布', '特呂默爾河瀑布', '勞特布龍嫩村落步道'],
        tips: '參觀特呂默爾河瀑布時請穿戴防水防風外套，岩洞隧道內的風力極大且水霧瀰漫，體感溫度較低。',
        costEstimate: '約 25 瑞士法郎',
        image: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=600&auto=format&fit=crop'
      },
      {
        day: 2,
        title: '懸崖上的無車秘境純淨之旅',
        description: '乘坐纜車前往 Grütschalp，再轉乘高山火車前往米倫。探索這座絕美的無車山城，隨後沿著牧徑健行下山至吉梅爾瓦爾德，沿途可在當地的阿爾卑斯木屋購買手工起司。',
        spots: ['米倫山城', '吉梅爾瓦爾德牧歌山谷', 'Allmendhubel 花卉步道'],
        tips: '一定要在吉梅爾瓦爾德的鄉村酒館品嚐經典的瑞士牧羊人通心粉（Älplermakkaroni，配以濃郁起司與溫熱蘋果醬，風味絕佳）。',
        costEstimate: '約 40 瑞士法郎',
        image: 'https://images.unsplash.com/photo-1531310197839-ccf54634509e?q=80&w=600&auto=format&fit=crop'
      },
      {
        day: 3,
        title: '登臨萬年冰原之巔',
        description: '踏上前往少女峰（歐洲之巔）的史詩鐵路之旅。漫步穿越直接從冰川內部鑿出的水晶冰宮，並佇立在萬年冰雪覆蓋的白雪觀景平台上，沐浴暖陽。',
        spots: ['Kleine Scheidegg 隘口', '少女峰斯芬克斯觀景台', '冰宮'],
        tips: '建議提早購買車票並在出發前查閱少女峰頂即時 WebCam。若山頂雲霧繚繞，可考慮將行程調整至晴朗的午後。',
        costEstimate: '約 180 瑞士法郎',
        image: 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?q=80&w=600&auto=format&fit=crop'
      }
    ],
    budgetEstimates: {
      hotelBudget: 240,
      diningBudget: 110,
      activityBudget: 120,
      flightBudget: 950
    },
    mapSpots: [
      {
        name: '勞特布龍嫩村落',
        lat: '46.5935° N',
        lng: '7.9090° E',
        x: 30,
        y: 65,
        description: '被 72 道垂直懸崖瀑布溫柔環抱的溫馨山谷大本營。',
        image: 'https://images.unsplash.com/photo-1527668752968-14dc70a27c95?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '施陶巴赫瀑布',
        lat: '46.5898° N',
        lng: '7.9103° E',
        x: 45,
        y: 50,
        description: '飛流直下 300 公尺，宛如一襲隨風起舞的縹緲白色婚紗。',
        image: 'https://images.unsplash.com/photo-1502784444187-359ac186c5bb?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '米倫無車山城',
        lat: '46.5594° N',
        lng: '7.8924° E',
        x: 15,
        y: 35,
        description: '高懸在西側懸崖之上、宛如遺世獨立的童話小鎮。',
        image: 'https://images.unsplash.com/photo-1531310197839-ccf54634509e?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '少女峰火車站',
        lat: '46.5475° N',
        lng: '7.9818° E',
        x: 85,
        y: 20,
        description: '全歐洲海拔最高的火車站，俯瞰波瀾壯闊的萬年冰河與冰雪平原。',
        image: 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?q=80&w=400&auto=format&fit=crop'
      }
    ],
    packingList: [
      {
        category: '旅行必備',
        items: ['瑞士旅行通行證 (Swiss Travel Pass，極度推薦)', '專業防水防滑登山鞋', '輕便健行雙肩包', '環保隨身水壺']
      },
      {
        category: '禦寒與服裝',
        items: ['防風防雨衝鋒衣', '保暖抓絨衣或輕便羽絨層', '防紫外線太陽眼鏡（雪地防盲必備）']
      },
      {
        category: '健行裝備',
        items: ['防曬霜（高海拔紫外線極強）', '伸縮登山杖', '下載好離線地圖與健行路線 App']
      }
    ],
    weatherForecast: [
      {
        season: '春季（4月 - 5月）',
        temp: '5°C - 15°C',
        description: '冰雪消融，滿谷蔥鬱，瀑布流量達到全年的轟鳴巔峰。',
        suitability: '賞瀑好時機 - 高海拔步道尚未完全開放，但瀑布最為壯觀。',
        iconName: 'cloud-rain'
      },
      {
        season: '夏季（6月 - 8月）',
        temp: '14°C - 24°C',
        description: '陽光溫和，能見度極佳，是無盡高山健行的黃金季節。',
        suitability: '健行旺季 - 氣候完美，所有纜車與健行路網全部開放。',
        iconName: 'sun'
      },
      {
        season: '秋季（9月 - 10月）',
        temp: '6°C - 16°C',
        description: '落葉松染成金黃，晨霧縹緲，山道寧靜幽美。',
        suitability: '攝影黃金期 - 遊客減少，空氣極其澄澈，秋色迷人。',
        iconName: 'wind'
      },
      {
        season: '冬季（11月 - 3月）',
        temp: '-5°C - 4°C',
        description: '銀裝素裹的純白世界，粉雪厚實，滑雪愛好者的天堂。',
        suitability: '冰雪運動季 - 適合滑雪、雪地健行與欣賞寂靜雪景。',
        iconName: 'snowflake'
      }
    ]
  },
  {
    id: 'iceland',
    title: '環島公路之迴響：極地冰川與極光的冰與火之歌',
    subtitle: '追逐磅礴的巨幅瀑布、漫步深邃的黑沙灘、並佇立於晶瑩剔透的藍色藍寶石冰洞中。',
    country: '冰島',
    heroImage: 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=1200&auto=format&fit=crop',
    category: 'Adventure',
    vibe: '神秘、火山地貌、壯麗史詩',
    bestSeason: '秋季與冬季（追尋北極光與冰洞）或夏季（體驗午夜陽光）',
    rating: 4.95,
    readTime: '閱讀時間 12 分鐘',
    author: {
      name: 'Kristian Sigurd',
      avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=200&auto=format&fit=crop',
      role: '極光探險嚮導與地質學研究員'
    },
    intro: '冰島是一個大地仍在活躍誕生的奇蹟之境。由玄武岩熔岩爆發鑄就，再經巨型大陸冰帽雕琢，這片土地充滿了野性、沉默與電影畫面般的史詩感。',
    publishDate: '2026年4月2日',
    highlights: [
      '穿梭於塞里雅蘭瀑布（Seljalandsfoss）高達 60 公尺的水簾幕後方',
      '目睹巨大冰塊如鑽石般散落在黑沙灘（Diamond Beach）上的奇幻景致',
      '腳穿冰爪，踏上索爾黑馬冰川（Sólheimajökull）如煤黑火山灰覆蓋的冰舌',
      '浸泡在藍湖（Blue Lagoon）溫暖、富含矽礦物且散發藍色微光的溫泉中'
    ],
    quote: "在冰島，你並非只是在「觀賞」風景，而是在用雙腳親自感受地殼深處地熱蒸汽的吐息與哀鳴。",
    quoteAuthor: "Kristian Sigurd",
    content: [
      "行駛在冰島南部的環島公路上，彷彿在另一顆星球的表面飛馳。左手邊是延綿不絕、覆蓋著厚厚苔蘚的黑色古老熔岩原；右手邊則是北大西洋猛烈拍擊著玄武岩石柱的驚濤駭浪。天地浩瀚無垠，人類痕跡寥寥無幾——偶爾只有一座孤零零的紅頂教堂，或是在草場上升起的裊裊地熱蒸汽。",
      "塞里雅蘭瀑布是我們與冰島澎湃水能的第一次親密接觸。與其他瀑布不同，它的後方有一個天然凹陷的濕潤岩洞。沿著濕滑的岩石攀爬，你便能直接佇立在奔騰的水幕後方。隔著溫潤的水簾凝望遠方，看著落日將天際染成橘紅，那一刻，你已徹底融化在冰島的荒野心臟中。",
      "繼續向東，便是冰島最璀璨的冠冕：傑古沙龍冰河湖（Jökulsárlón）。藍得近乎不真實的巨大冰塊自冰川邊緣剝落，在湖中靜靜漂流。部分冰塊隨潮汐被沖上黑色的沙灘，在夕陽下猶如巨大的未經雕琢的藍寶石靜靜躺在黑色絲絨布上——這便是著名的鑽石沙灘。"
    ],
    itinerary: [
      {
        day: 1,
        title: '黃金圈奇觀與藍湖療癒',
        description: '從雷克雅維克出發，穿越辛格韋德利國家公園的板塊大裂谷。觀賞史托克間歇泉（Strokkur）噴發出 30 公尺高的沖天水柱，傍晚在溫暖的藍湖溫泉中徹底放鬆。',
        spots: ['辛格韋德利國家公園', '蓋錫爾間歇泉', '黃金瀑布 (Gullfoss)', '藍湖溫泉'],
        tips: '藍湖溫泉必須提前數週預訂。進入溫泉前請務必在頭髮上抹滿提供的護髮素且不要沖洗，矽礦物雖對皮膚極好，但會讓頭髮變得極其乾枯毛躁！',
        costEstimate: '約 15,000 冰島克朗',
        image: 'https://images.unsplash.com/photo-1504893524553-ac55fce698be?q=80&w=600&auto=format&fit=crop'
      },
      {
        day: 2,
        title: '南部飛瀑與神秘黑沙灘',
        description: '沿南部海岸前行。走入塞里雅蘭瀑布後方，瞻仰斯科加瀑布（Skógafoss）的雄偉水牆，最後佇立於維克鎮附近、擁有高聳風琴岩的黑沙灘上。',
        spots: ['塞里雅蘭瀑布', '斯科加瀑布', '雷尼斯黑沙灘', '維克小鎮'],
        tips: '在黑沙灘時請務必與海浪保持安全距離。這裡常有致命的「瘋狗浪 (Sneaker Waves)」，可在毫無預警的情況下將遊客捲入冰冷深海。',
        costEstimate: '約 4,000 冰島克朗',
        image: 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=600&auto=format&fit=crop'
      },
      {
        day: 3,
        title: '冰河湖遊船與鑽石沙灘',
        description: '向東深入瓦特納冰川國家公園腹地。搭乘遊船穿梭於傑古沙龍冰河湖中，近距離欣賞漂流的幽藍冰山，隨後前往對面的鑽石沙灘捕捉擱淺冰塊在黑沙上的璀璨光芒。',
        spots: ['傑古沙龍冰河湖', '鑽石沙灘', '斯卡夫塔山自然保護區'],
        tips: '強烈推薦搭乘水陸兩棲船或橡皮艇巡遊冰河湖，這能讓你極度貼近晶瑩的冰山，甚至有機會看到在冰塊上曬太陽的可愛海豹。',
        costEstimate: '約 9,500 冰島克朗',
        image: 'https://images.unsplash.com/photo-1518156677180-95a2893f3e9f?q=80&w=600&auto=format&fit=crop'
      }
    ],
    budgetEstimates: {
      hotelBudget: 190,
      diningBudget: 95,
      activityBudget: 85,
      flightBudget: 750
    },
    mapSpots: [
      {
        name: '雷克雅維克（首都）',
        lat: '64.1466° N',
        lng: '21.9426° W',
        x: 10,
        y: 45,
        description: '充滿設計感與活力的世界最北首都。',
        image: 'https://images.unsplash.com/photo-1504829857797-ddff28127792?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '塞里雅蘭瀑布',
        lat: '63.6156° N',
        lng: '19.9885° W',
        x: 35,
        y: 65,
        description: '壯美的水簾洞瀑布，可沿步道繞行至水幕後方。',
        image: 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '雷尼斯黑沙灘',
        lat: '63.4018° N',
        lng: '19.0191° W',
        x: 55,
        y: 75,
        description: '神秘深邃的黑沙灘，襯托著鬼斧神工的玄武岩石柱。',
        image: 'https://images.unsplash.com/photo-1518495973542-4542c06a5843?q=80&w=400&auto=format&fit=crop'
      },
      {
        name: '傑古沙龍冰河湖',
        lat: '64.0489° N',
        lng: '16.1794° W',
        x: 88,
        y: 50,
        description: '晶瑩剔透的湛藍浮冰靜靜漂浮，如夢似幻。',
        image: 'https://images.unsplash.com/photo-1518156677180-95a2893f3e9f?q=80&w=400&auto=format&fit=crop'
      }
    ],
    packingList: [
      {
        category: '全天候防護',
        items: ['防風防雨專業三合一衝鋒衣', '防雨保暖長褲', '保暖美麗諾羊毛內搭衣褲', '保暖針織帽、防水手套與圍脖']
      },
      {
        category: '專業鞋履',
        items: ['高階防水登山鞋', '厚羊毛襪（建議多帶幾雙備用）', '冰爪（若冬季前往探險必備）']
      },
      {
        category: '探險配件',
        items: ['電子設備防水保護袋（防瀑布水霧）', '泳衣（用於溫泉與藍湖）', '眼罩（夏季極晝午夜陽光必備）']
      }
    ],
    weatherForecast: [
      {
        season: '春季（5月）',
        temp: '2°C - 9°C',
        description: '冰雪迅速消融，北極海鸚（Puffins）重返懸崖，公路全線通暢。',
        suitability: '絕佳平季 - 避開人潮、物價合宜，白晝長且氣候溫和。',
        iconName: 'cloud'
      },
      {
        season: '夏季（6月 - 8月）',
        temp: '9°C - 16°C',
        description: '漫山遍野綠意盎然，魯冰花盛開，體驗 24 小時不落的午夜太陽。',
        suitability: '自駕首選 - 路況極佳，內陸 F 公路開放，無盡白晝利於長途自駕。',
        iconName: 'sun'
      },
      {
        season: '秋季（9月 - 10月）',
        temp: '3°C - 10°C',
        description: '苔原轉為金黃火紅，夜空重歸黑暗，北極光初現。',
        suitability: '雙重體驗 - 既有白晝自駕，又有黑夜追光，極具性價比。',
        iconName: 'wind'
      },
      {
        season: '冬季（11月 - 4月）',
        temp: '-6°C - 2°C',
        description: '銀裝素裹，藍冰洞大開，極光頻率極高，白晝短暫。',
        suitability: '冰雪奇境 - 適合冰洞探索、極光狩獵，極具魔幻極地色彩。',
        iconName: 'snowflake'
      }
    ]
  }
];
export type { TravelArticle };
