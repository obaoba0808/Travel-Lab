import fs from 'fs';
import path from 'path';

const rootDir = process.cwd();
const files = fs.readdirSync(rootDir).filter(file => file.endsWith('.html'));

const badges = {
  'seoul-5days.html': '🇰🇷 SEOUL',
  'seoul-food.html': '🇰🇷 SEOUL GOURMET',
  'busan-4days.html': '🇰🇷 BUSAN',
  'busan-capsule.html': '🇰🇷 BUSAN CAPSULE',
  'jeju-island.html': '🇰🇷 JEJU ISLAND',
  'korea-budget.html': '🇰🇷 KOREA BUDGET',
  'korea-money-saving-tips.html': '🇰🇷 KOREA TIPS',
  'korea-transport.html': '🇰🇷 KOREA TRANSPORT',
  'korea-travel.html': '🇰🇷 KOREA GUIDE',
  'tokyo-5days.html': '🇯🇵 TOKYO',
  'tokyo-accommodation.html': '🇯🇵 TOKYO STAY',
  'fukuoka-5days.html': '🇯🇵 FUKUOKA',
  'okinawa.html': '🇯🇵 OKINAWA',
  'kyoto-temples.html': '🇯🇵 KYOTO',
  'osaka-food.html': '🇯🇵 OSAKA GOURMET',
  'osaka-usj.html': '🇯🇵 OSAKA USJ',
  'kansai-pass.html': '🇯🇵 KANSAI PASS',
  'japan-money-saving-tips.html': '🇯🇵 JAPAN TIPS',
  'japan-travel.html': '🇯🇵 JAPAN GUIDE',
  'japan-cherry-blossom-season.html': '🇯🇵 SAKURA SEASON',
  'japan-drugstore-checklist.html': '🇯🇵 DRUGSTORE',
  'bangkok-3days.html': '🇹🇭 BANGKOK',
  'bangkok-4days.html': '🇹🇭 BANGKOK EXPERT',
  'chiang-mai.html': '🇹🇭 CHIANG MAI',
  'thailand-sim.html': '🇹🇭 THAILAND SIM',
  'singapore-3days.html': '🇸🇬 SINGAPORE',
  'kualalumpur-3days.html': '🇲🇾 KUALA LUMPUR',
  'vietnam-danang.html': '🇻🇳 DANANG',
  'vietnam-hochiminh.html': '🇻🇳 HO CHI MINH',
  'angkor-wat-2days.html': '🇰🇭 ANGKOR WAT',
  'taiwan-travel.html': '🇹🇼 TAIWAN GUIDE',
  'taipei-food.html': '🇹🇼 TAIPEI GOURMET',
  'tainan-food.html': '🇹🇼 TAIWAN TAINAN',
  'hualien-taitung.html': '🇹🇼 TAIWAN EAST',
  'jiufen.html': '🇹🇼 TAIWAN JIUFEN',
  'hokkaido-winter.html': '🇯🇵 HOKKAIDO',
};

const heroImages = {
  'tokyo-5days.html': '/images/tokyo-hero.webp',
  'tokyo-accommodation.html': '/images/Tokyo-Accommodation-hero.webp',
  'japan-drugstore-checklist.html': '/images/Japanese drugstore cosmetics.webp',
  'kansai-pass.html': '/images/kansai-hero.webp',
  'hokkaido-winter.html': '/images/hokkaido-hero.webp',
  'okinawa.html': '/images/okinawa-hero.webp',
  'kyoto-temples.html': '/images/kyoto-hero.webp',
  'osaka-food.html': '/images/osaka-food-hero.webp',
  'osaka-usj.html': '/images/osaka-usj-hero.webp',
  'japan-budget-guide.html': '/images/japan-budget-hero.webp',
  'fukuoka-5days.html': '/images/Fukuoka.webp',
  'japan-cherry-blossom-season.html': '/images/Cherry blossom and autumn foliage viewing in Japan.webp',
  'japan-money-saving-tips.html': '/images/Save money in Japan 20.webp',
  'seoul-food.html': '/images/seoul-hero.webp',
  'busan-capsule.html': '/images/busan-hero.webp',
  'busan-4days.html': '/images/busan-hero.webp',
  'jeju-island.html': '/images/jeju-hero.webp',
  'korea-budget.html': '/images/korea-budget-hero.webp',
  'seoul-5days.html': '/images/seoul-hero.webp',
  'korea-transport.html': '/images/korea-transport.webp',
  'korea-money-saving-tips.html': '/images/korea-money.webp',
  'seoul-food-map.html': '/images/seoul-hero.webp',
  'hualien-taitung.html': '/images/hualien-hero.webp',
  'tainan-food.html': '/images/tainan-hero.webp',
  'kenting.html': '/images/kenting-hero.webp',
  'taipei-food.html': '/images/taipei-food-hero.webp',
  'jiufen.html': '/images/jiufen-hero.webp',
  'chiang-mai.html': '/images/chiangmai-hero.webp',
  'bangkok-3days.html': '/images/bangkok-hero.webp',
  'bangkok-massage.html': '/images/bangkok-massage-hero.webp',
  'vietnam-danang.html': '/images/vietnam-danang-hero.webp',
  'singapore-3days.html': '/images/singapore.webp',
  'kualalumpur-3days.html': '/images/kualalumpur-3days.webp',
  'angkor-wat-2days.html': '/images/angkor.webp',
  'thailand-sim.html': '/images/thailand-sim.webp',
  'seasia-budget-travel-guide.html': '/images/budget-airline.webp',
  'vietnam-hochiminh.html': '/images/vietnam-hochiminh-hero.webp',
  'travel-tools.html': '/images/travel-tools-hero.webp',
  'power-plug-guide.html': '/images/power.webp',
  'budget-airline-guide.html': '/images/budget-airline.webp',
  'miles-calculator.html': '/images/miles.webp',
  'packing-list.html': '/images/packing-list.webp',
  'esim-comparison.html': '/images/esim-hero.webp',
  'tax-refund-calculator.html': '/images/Free tax refund.webp',
  'notion-travel-template.html': '/images/notion-travel.webp',
  'about.html': '/images/about-hero.webp',
  'japan-travel.html': 'images/japan-travel.webp',
  'korea-travel.html': 'images/korea-travel.webp',
  'taiwan-travel.html': 'images/taiwan-travel.webp',
  'southeast-asia.html': 'images/southeast-asia.webp'
};

const originalBullets = {
  'seoul-5days.html': [
    { emoji: '⛩️', text: '景福宮' },
    { emoji: '🗼', text: 'N首爾塔' },
    { emoji: '🛍️', text: '明洞商圈' },
    { emoji: '🍗', text: '弘大不眠夜' },
    { emoji: '☕', text: '聖水文青洞' }
  ],
  'tokyo-accommodation.html': [
    { emoji: '🏢', text: '交通樞紐 新宿' },
    { emoji: '🏯', text: '平價首選 上野' },
    { emoji: '⛩️', text: '傳統情懷 淺草' },
    { emoji: '🎪', text: '潮流購物 澀谷' },
    { emoji: '🎌', text: '動漫聖地 池袋' }
  ],
  'seoul-food.html': [
    { emoji: '🍖', text: '烤五花肉' },
    { emoji: '🍲', text: '部隊鍋' },
    { emoji: '🍗', text: '韓式炸雞' },
    { emoji: '🦀', text: '醬蟹偷飯賊' },
    { emoji: '🗺️', text: '美食地圖' }
  ],
  'okinawa.html': [
    { emoji: '🚗', text: '沖繩自駕' },
    { emoji: '🦈', text: '美麗海水族館' },
    { emoji: '🎡', text: '美國村落日' },
    { emoji: '🥩', text: '頂級石垣牛' },
    { emoji: '🏝️', text: '瀨長島飛機' }
  ],
  'kyoto-temples.html': [
    { emoji: '⛩️', text: '清水寺散步' },
    { emoji: '🍁', text: '金閣寺賞楓' },
    { emoji: '🦊', text: '伏見稻荷大社' },
    { emoji: '🍵', text: '宇治抹茶' },
    { emoji: '🗺️', text: '散步地圖' }
  ],
  'jeju-island.html': [
    { emoji: '🚗', text: '濟州島自駕' },
    { emoji: '⛰️', text: '城山日出峰' },
    { emoji: '☕', text: '涯月邑咖啡' },
    { emoji: '🐖', text: '海景黑豬肉' },
    { emoji: '🗺️', text: '預算地圖' }
  ],
  'japan-money-saving-tips.html': [
    { emoji: '🎫', text: '新幹線優惠' },
    { emoji: '🛍', text: '藥妝店折扣' },
    { emoji: '🍱', text: '超市半價' },
    { emoji: '📱', text: '漫遊上網' },
    { emoji: '💱', text: '匯率精算' }
  ],
  'korea-budget.html': [
    { emoji: '✈️', text: '便宜機票' },
    { emoji: '🏨', text: '小資住宿' },
    { emoji: '🍢', text: '在地餐費' },
    { emoji: '💳', text: 'WOWPASS卡' },
    { emoji: '💱', text: '換錢退稅' }
  ],
  'osaka-usj.html': [
    { emoji: '🏰', text: '任天堂世界' },
    { emoji: '⚡', text: '哈利波特' },
    { emoji: '🎫', text: '快速通關' },
    { emoji: '🏃', text: '免排隊路線' },
    { emoji: '🛍️', text: '限定周邊' }
  ],
  'korea-money-saving-tips.html': [
    { emoji: '💱', text: '換錢所比較' },
    { emoji: '🛍️', text: '現場退稅' },
    { emoji: '🚌', text: '免費轉乘' },
    { emoji: '🏪', text: '超市優惠' },
    { emoji: '💰', text: '預算試算' }
  ],
  'kansai-pass.html': [
    { emoji: '🚇', text: '關西周遊卡' },
    { emoji: '🚄', text: 'JR Pass 關西' },
    { emoji: '💳', text: 'ICOCA 神卡' },
    { emoji: '🏯', text: '京都大阪' },
    { emoji: '📊', text: '省錢試算' }
  ],
  'osaka-food.html': [
    { emoji: '🐙', text: '道頓堀章魚燒' },
    { emoji: '🍢', text: '黑門市場' },
    { emoji: '🛍️', text: '心齋橋必吃' },
    { emoji: '🍻', text: '梅田地下街' },
    { emoji: '🗺️', text: '美食地圖' }
  ],
  'korea-transport.html': [
    { emoji: '💳', text: 'T-money交通卡' },
    { emoji: '🚇', text: '氣候同行卡' },
    { emoji: '💳', text: 'WOWPASS儲值' },
    { emoji: '🚄', text: 'KTX高鐵' },
    { emoji: '🚕', text: 'Kakao T叫車' }
  ],
  'hualien-taitung.html': [
    { emoji: '🚲', text: '伯朗大道' },
    { emoji: '🌊', text: '七星潭聽浪' },
    { emoji: '⛰️', text: '太魯閣峽谷' },
    { emoji: '☕', text: '慢活咖啡' },
    { emoji: '🗺️', text: '放空行程' }
  ],
  'taipei-food.html': [
    { emoji: '🍲', text: '大稻埕慈聖宮' },
    { emoji: '🍢', text: '寧夏夜市' },
    { emoji: '☕', text: '赤峰街文青咖啡' },
    { emoji: '🍜', text: '經典牛肉麵' },
    { emoji: '🗺️', text: '吃貨地圖' }
  ],
  'bangkok-3days.html': [
    { emoji: '🍜', text: '唐人街必吃' },
    { emoji: '🛍️', text: '洽圖洽市集' },
    { emoji: '🍹', text: '星光空中酒吧' },
    { emoji: '🏨', text: '暹羅精選住區' },
    { emoji: '🪷', text: '平價泰式按摩' }
  ],
  'bangkok-4days.html': [
    { emoji: '📅', text: '2026年最新' },
    { emoji: '🛕', text: '大皇宮與老城' },
    { emoji: '🛶', text: '丹嫩莎朵水上市場' },
    { emoji: '💆', text: '正宗古法SPA' },
    { emoji: '🚇', text: 'BTS交通攻略' }
  ],
  'singapore-3days.html': [
    { emoji: '🇸🇬', text: '免簽入境 30 天' },
    { emoji: '🚇', text: '地鐵捷運 EZ-Link' },
    { emoji: '🍲', text: '天天海南雞飯' },
    { emoji: '🎡', text: '星耀樟宜瀑布' },
    { emoji: '🏝️', text: '聖淘沙渡假' }
  ],
  'kualalumpur-3days.html': [
    { emoji: '🏢', text: '雙子星大樓' },
    { emoji: '🌈', text: '黑風洞彩虹階梯' },
    { emoji: '🍡', text: '阿羅街沙嗲' },
    { emoji: '🕌', text: '粉紅清真寺' },
    { emoji: '🗺️', text: '三天兩夜行程' }
  ],
  'chiang-mai.html': [
    { emoji: '💻', text: '尼曼區共享空間' },
    { emoji: '☕', text: '網美咖啡廳巡禮' },
    { emoji: '⛩️', text: '古城帕邢寺' },
    { emoji: '🛍️', text: '週日無邊夜市' },
    { emoji: '🐘', text: '大象保護區' }
  ],
  'angkor-wat-2days.html': [
    { emoji: '🌅', text: '小吳哥日出' },
    { emoji: '🗿', text: '巴戎寺高棉微笑' },
    { emoji: '🌿', text: '塔普倫寺巨樹' },
    { emoji: '🛶', text: '洞里薩湖落日' },
    { emoji: '🗺️', text: '大圈小圈地圖' }
  ],
  'taiwan-travel.html': [
    { emoji: '🏢', text: '台北都會漫遊' },
    { emoji: '🍵', text: '九份雨霧山城' },
    { emoji: '🍲', text: '台南美食之旅' },
    { emoji: '🌊', text: '花東放空海景' },
    { emoji: '🏄', text: '墾丁陽光沙灘' }
  ],
  'japan-travel.html': [
    { emoji: '🗼', text: '東京潮流冒險' },
    { emoji: '⛩️', text: '京都古意散策' },
    { emoji: '🐙', text: '大阪美食天堂' },
    { emoji: '❄️', text: '北海道冬雪' },
    { emoji: '🌴', text: '沖繩度假自駕' }
  ],
  'southeast-asia.html': [
    { emoji: '🇹🇭', text: '泰國曼谷清邁' },
    { emoji: '🇻🇳', text: '越南峴港胡志明' },
    { emoji: '🇸🇬', text: '新加坡花園城市' },
    { emoji: '🇲🇾', text: '馬來西亞吉隆坡' },
    { emoji: '🇰🇭', text: '柬埔寨吳哥古蹟' }
  ],
  'tainan-food.html': [
    { emoji: '🥩', text: '現宰溫體牛肉湯' },
    { emoji: '🦐', text: '國華街道地小吃' },
    { emoji: '☕', text: '老屋文青咖啡' },
    { emoji: '🏯', text: '府城古蹟漫步' },
    { emoji: '🗺️', text: '散步美食地圖' }
  ],
  'about.html': [
    { emoji: '📝', text: '關於 Travel Lab' },
    { emoji: '✈️', text: '慢活旅遊提案' },
    { emoji: '📧', text: '聯絡合作洽詢' }
  ],
  'hokkaido-winter.html': [
    { emoji: '❄️', text: '札幌小樽雪祭' },
    { emoji: '🐧', text: '旭山企鵝散步' },
    { emoji: '🦀', text: '三大蟹吃到飽' },
    { emoji: '♨️', text: '登別極致溫泉' },
    { emoji: '🗺️', text: '鐵路PASS精算' }
  ]
};

const descriptions = {
  'seoul-5days.html': '穿梭於璀璨繁華的現代商圈與莊嚴古典的宮殿歷史，帶你玩轉最完美的 5 天 4 夜首爾探索之旅。',
  'seoul-food.html': '從街邊香氣四溢的道地小吃，到精緻誘人的經典韓式料理，為你開啟一場極致的首爾吃貨饗宴。',
  'busan-4days.html': '依山傍海的絕美海雲台、夢幻的彩色天空膠囊列車，為你規劃一場最浪漫、最治癒的釜山自由行。',
  'busan-capsule.html': '超詳細的海雲台膠囊列車預約祕訣、夕陽拍照點與票券攻略，教你避開排隊天坑。',
  'jeju-island.html': '駕車環遊絕美的濟州海岸線，探訪火山地質奇景、海景黑豬肉與文青祕境。',
  'korea-budget.html': '機票住宿、餐費門票與退稅換錢終極精算，用最划算的預算玩出最高品質的韓國之旅。',
  'korea-money-saving-tips.html': '換錢密技、退稅流程與隱藏版交通卡優惠全公開，教你如何一鍵精省荷包。',
  'korea-transport.html': 'T-money、WOWPASS 與氣候同行卡深度比較，為你挑選出最省時、省力、省錢的交通方案。',
  'korea-travel.html': '匯集首爾、釜山、濟州島的一站式深度旅遊地圖，為你量身打造最詳盡的韓國行前全攻略。',
  'tokyo-accommodation.html': '精心篩選新宿、上野、淺草、澀谷與池袋五大黃金住宿區，為你提供高CP值的無痛避坑指南。',
  'fukuoka-5days.html': '高CP值的博多屋台美食、天神購物與近郊太宰府一日遊，帶你輕鬆體驗最熱情的九州門戶。',
  'okinawa.html': '蔚藍海岸、美麗海水族館自駕、美國村落日與頂級石垣牛，開啟最悠閒的沖繩度假之旅。',
  'kyoto-temples.html': '穿梭於清水寺、金閣寺與伏見稻荷大社的古意長廊，為你呈現一場極具禪意與詩意的京都散策。',
  'osaka-food.html': '吃通天閣、逛黑門市場，在道頓堀與心齋橋間探訪老饕最推的必吃關西限定美食。',
  'osaka-usj.html': '超級任天堂世界與哈利波特免排隊終極攻略，教你如何用最聰明的路線玩轉大阪環球影城。',
  'kansai-pass.html': '關西周遊卡、JR Pass 與 ICOCA 的無腦對比指南，教你一分鐘選對票券、省下大筆交通費。',
  'japan-money-saving-tips.html': '藥妝店折扣、新幹線搶票與超市半價便當，老手才知道的 20 個日本精省神祕眉角。',
  'japan-travel.html': '東京、大阪、京都、北海道等熱門地區全覆蓋，為你準備最完整、最精緻的日本自由行指南。',
  'japan-cherry-blossom-season.html': '最新日本櫻花滿開預測、追櫻必訪名所推薦與行前準備，帶你邂逅浪漫的粉色櫻景。',
  'japan-drugstore-checklist.html': '日本連鎖藥妝店優惠券、精選必買藥物、護膚美妝與退稅防坑全攻略。',
  'bangkok-3days.html': '從街頭 ฿40 經典炒河粉到泰北船麵與頂級星光空中酒吧，不浪費天使之城的任何一餐。',
  'bangkok-4days.html': '每日精緻行程表、SPA 按摩選店、BTS 交通與三大落腳區，第一次去泰國自由行也能輕鬆上手。',
  'chiang-mai.html': '漫步古城、漫享網美咖啡廳與數位遊牧聖地，為你開啟一段最放鬆、最有深度的清邁慢活時光。',
  'thailand-sim.html': '實測 AIS、TrueMove、DTAC 三大電信商，為你帶來最順暢、最划算的出國網速體驗。',
  'singapore-3days.html': '璀璨濱海灣夜景、多元異國風情街與天天海南雞飯，帶你用最聰明、最划算的方式玩轉星國。',
  'kualalumpur-3days.html': '雙子星塔絕美夜色、粉紅清真寺探祕與道地沙嗲美食，開啟一場色彩斑斕的吉隆坡 3 天 2 夜奇幻探索。',
  'vietnam-danang.html': '巴拿山佛手雙手巨橋、黃金會安古鎮與美溪沙灘落日，為你規劃一場最放鬆的越南中越度假。',
  'vietnam-hochiminh.html': '漫步粉紅教堂、漫步法式歌劇院與湄公河三角洲探險，帶你用最迷人的視角解鎖西貢。',
  'angkor-wat-2days.html': '探秘千年吳哥窟神祕微笑、絕美落日點與小大圈行程規劃，帶你重溫古老王朝的永恆輝煌。',
  'taiwan-travel.html': '從繁華台北到慢活花東、熱情墾丁與古意台南，為你呈現一站式最接地氣的台灣寶島探索地圖。',
  'taipei-food.html': '經典牛肉麵、夜市人氣排隊小吃與文青老屋咖啡，為你帶來最對味的台北吃貨漫遊指南。',
  'tainan-food.html': '清晨現宰溫體牛肉湯、國華街道地小吃與古老府城古蹟漫步，帶你品味最純粹的台南慢活靈魂。',
  'hualien-taitung.html': '蔚藍太平洋海岸線、太魯閣壯麗峽谷與池上稻田漫遊，為你規劃一場洗滌心靈的花東放空慢活之旅。',
  'jiufen.html': '水霧繚繞的茶樓、千與千尋夢幻階梯與隱藏版觀海祕境，為你帶來最浪漫的九份深度全攻略。',
  'hokkaido-winter.html': '漫步於銀裝素裹的純白雪境，探訪夢幻小樽運河、旭山企鵝散步與三大蟹極致海鮮，為您打造完美升級的 5 天 4 夜冬日北國探索。',
};

console.log("Beginning precise Hero Section conversion (v3) with complete authentic dictionaries...");

files.forEach(file => {
  const filePath = path.join(rootDir, file);
  let content = fs.readFileSync(filePath, 'utf-8');

  // Let's identify the Hero Section
  // Match either:
  // 1) Already converted editorial block
  // 2) Original full-width hero block
  const sectionRegex = /<!-- EDITORIAL HERO REGION WITH BEAST-UNMASKED CARD -->[\s\S]*?<section class="max-w-7xl[\s\S]*?<\/section>|<section[^>]*?(?:class="relative bg-|class="[^"]*?hero-region|id="hero-banner-section"|class="relative bg-tiffany-obsidian")[^>]*?>([\s\S]*?)<\/section>/i;
  const sectionMatch = content.match(sectionRegex);

  if (!sectionMatch) {
    return;
  }

  const fullSectionHTML = sectionMatch[0];

  // Extract Title (H1)
  const h1Match = fullSectionHTML.match(/<h1[^>]*?>([\s\S]*?)<\/h1>/i);
  if (!h1Match) {
    return;
  }
  const h1Text = h1Match[1].replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();

  // Extract Tag (Badge)
  let tagText = badges[file] || '✈️ TRAVEL LAB';

  // Extract Image Src & fallback from dictionary or extract from page
  let imgSrc = heroImages[file];
  if (!imgSrc) {
    imgSrc = 'images/hero-golightly.webp';
    const imgRegex = /<img[^>]*?src=["']([^"']+)["']/i;
    const imgMatch = fullSectionHTML.match(imgRegex);
    if (imgMatch) {
      imgSrc = imgMatch[1];
    } else {
      const styleMatch = fullSectionHTML.match(/background-image:\s*url\(['"]?([^'")]+)['"]?\)/i);
      if (styleMatch) {
        imgSrc = styleMatch[1];
      }
    }
  }

  // Extract Description (p)
  let descText = descriptions[file] || '潮流、傳統與極致美食完美交織，為你開啟最專業、最精緻的自由行探索之旅。';

  // Get Bullets from our perfect originalBullets dictionary
  const bullets = originalBullets[file] || [
    { emoji: '🗺️', text: '行前規劃' },
    { emoji: '🍲', text: '在地美食' },
    { emoji: '🛍️', text: '必訪景點' },
    { emoji: '🏨', text: '推薦住宿' }
  ];

  // Build the new Capsule Subtitle
  const capsuleItems = bullets.map(b => {
    return `          <span class="flex items-center gap-1.5 text-tiffany"><span class="font-sans">${b.emoji}</span> ${b.text}</span>`;
  }).join('\n          <span class="text-white">•</span>\n');

  const regionTag = `
        <!-- GRADIENT REGION TAG -->
        <div class="inline-flex items-center justify-center">
          <span class="inline-block bg-gradient-to-r from-tiffany to-red-500 text-white text-[10px] font-display font-semibold uppercase tracking-[0.25em] px-4 py-1.5 rounded-full shadow-md shadow-tiffany/20">
            ${tagText}
          </span>
        </div>`;

  const capsuleHTML = `
        <!-- CONTRAST CAPSULE SUBTITLE -->
        <div class="inline-flex flex-wrap items-center justify-center gap-x-4 gap-y-2 px-6 py-3 bg-slate-950/95 text-xs font-semibold rounded-full shadow-md max-w-3xl mx-auto border border-slate-800">
${capsuleItems}
        </div>`;

  // Construct the brand-new Editorial Hero section
  const newHeroHTML = `  <!-- EDITORIAL HERO REGION WITH BEAST-UNMASKED CARD -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8 sm:mb-12">
    <div class="bg-white rounded-b-[2.5rem] md:rounded-b-[4.5rem] overflow-hidden">
      
      <!-- HERO IMAGE - FULLY UNMASKED -->
      <div class="w-full overflow-hidden bg-slate-950">
        <img alt="${h1Text}" class="w-full h-auto block mx-auto hover:scale-[1.01] transition-transform duration-700" loading="eager" src="${imgSrc}"/>
      </div>
      
      <!-- HERO CONTENT BLOCK -->
      <div class="py-8 px-6 md:py-10 md:px-12 text-center bg-white space-y-5">
        ${regionTag}
        
        <!-- MAIN TITLE -->
        <h1 class="font-serif text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-wide text-slate-900 max-w-4xl mx-auto leading-tight md:leading-[1.15]">
          ${h1Text}
        </h1>
        ${capsuleHTML}
        
        <!-- SITE DESCRIPTION / INTRODUCTION -->
        <p class="text-sm md:text-base text-slate-500 max-w-2xl mx-auto leading-relaxed">
          ${descText}
        </p>
        
        <!-- DATE & AUTHOR -->
        <div class="text-xs text-slate-400 flex items-center justify-center gap-3 pt-2 font-display uppercase tracking-widest">
          <span>📝 Travel Lab 編輯部</span>
          <span class="text-slate-300">•</span>
          <span>更新於 2026 年 6 月</span>
        </div>
      </div>
    </div>
  </section>`;

  // Replace old section with new editorial hero
  content = content.replace(fullSectionHTML, newHeroHTML);
  fs.writeFileSync(filePath, content, 'utf-8');
  console.log(`[${file}]: Successfully updated Hero layout to match tokyo-5days.html precisely!`);
});

console.log("Hero Section layout alignments completed successfully!");
