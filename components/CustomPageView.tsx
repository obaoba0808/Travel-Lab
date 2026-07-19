import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  ArrowLeft, Heart, Check, Plus, Trash2, Shield, Calendar, Clock, Sparkles, 
  MapPin, Coins, Navigation, HelpCircle, Flame, Copy, Coffee, Store, Hotel, 
  Compass, Info, Send, Camera, Plane, Layers, ExternalLink, Zap, X, Globe, ArrowRight
} from 'lucide-react';
import { CustomPageData, customPages } from '../data/customPages';
import { getArticleContent } from '../data/articleContents';

// --- 首爾美食地圖 10 大名物與避坑熱點數據 ---
export interface SeoulFoodItem {
  id: string;
  name: string;
  koName: string;
  category: 'bbq' | 'soup' | 'street' | 'seafood' | 'chicken';
  categoryName: string;
  price: number;
  rating: number;
  district: 'hongdae' | 'myeongdong' | 'gwangjang' | 'seongsu' | 'sincheon';
  districtName: string;
  busyScore: Record<number, number>;
  bestTime: string;
  recommendPlace: string;
  intro: string;
  tips: string;
  x: number;
  y: number;
}

export const seoulFoods: SeoulFoodItem[] = [
  {
    id: 'samgyeopsal',
    name: '厚切炭烤豬五花',
    koName: '삼겹살',
    category: 'bbq',
    categoryName: '炭烤肉類',
    price: 18000,
    rating: 4.9,
    district: 'hongdae',
    districtName: '弘大',
    busyScore: { 11: 40, 12: 70, 13: 40, 14: 30, 15: 25, 16: 30, 17: 60, 18: 95, 19: 100, 20: 85, 21: 60, 22: 45 },
    bestTime: '11:00 前或 21:30 之後',
    recommendPlace: '小豬儲蓄罐 (石頭烤肉)、荒謬的生肉',
    intro: '在滾燙鐵盤或鑄鐵上將厚切五花肉烤得香氣四溢、油脂逼出，包裹在芝麻葉與大蒜泡菜中，每一口都是高脂肪、高碳水的極致狂歡。',
    tips: '弘大烤肉一條街是主戰場，推薦平日 17:00 前入場可免排隊。',
    x: 180,
    y: 190
  },
  {
    id: 'ganjang-gejang',
    name: '生醃醬油蟹',
    koName: '간장게장',
    category: 'seafood',
    categoryName: '精緻海鮮',
    price: 35000,
    rating: 4.8,
    district: 'myeongdong',
    districtName: '明洞',
    busyScore: { 11: 50, 12: 90, 13: 80, 14: 55, 15: 40, 16: 45, 17: 65, 18: 90, 19: 95, 20: 80, 21: 50, 22: 30 },
    bestTime: '13:30 之後或 17:00 剛開門',
    recommendPlace: '明洞 普樂醬蟹、阿峴洞醬油蟹',
    intro: '「偷飯賊」之王！將生蟹以秘製醬油低溫醃漬，蟹黃飽滿香滑，完全不腥。舀起熱飯拌入蟹殼，是直衝腦門的美味。',
    tips: '醬蟹通常現點現開，用餐尖峰大排長龍，建議利用線上預約 CATCH TABLE APP。',
    x: 350,
    y: 210
  },
  {
    id: 'fried-chicken',
    name: '橋村韓式炸雞',
    koName: '치킨',
    category: 'chicken',
    categoryName: '炸物雞肉',
    price: 22000,
    rating: 4.7,
    district: 'hongdae',
    districtName: '弘大',
    busyScore: { 11: 20, 12: 40, 13: 30, 14: 30, 15: 35, 16: 45, 17: 60, 18: 85, 19: 95, 20: 100, 21: 90, 22: 80 },
    bestTime: '17:30 之前或 21:00 之後宵夜場',
    recommendPlace: '橋村炸雞 (BHC炸雞、Nene炸雞)',
    intro: '外皮經過兩次高溫油炸，極致酥脆卻不油膩。裹上特調蜂蜜、大蒜醬油或香辣醬汁，配上酸甜醃蘿蔔與冰啤酒。',
    tips: '大部份門市下午才營業，宵夜時段排隊最久。可以外帶回民宿吃！',
    x: 210,
    y: 170
  },
  {
    id: 'samgyetang',
    name: '百濟人參雞湯',
    koName: '삼계탕',
    category: 'soup',
    categoryName: '養生湯品',
    price: 18000,
    rating: 4.6,
    district: 'myeongdong',
    districtName: '明洞 / 景福宮',
    busyScore: { 11: 60, 12: 98, 13: 85, 14: 60, 15: 40, 16: 40, 17: 55, 18: 75, 19: 80, 20: 60, 21: 40, 22: 20 },
    bestTime: '10:30 剛開門或 15:00-16:30 下午茶時段',
    recommendPlace: '土俗村參雞湯 (景福宮旁)、明洞百濟參雞湯',
    intro: '幼雞肚中塞入高麗參、糯米、紅棗和板栗，慢火熬至骨肉分離。高湯黏稠溫潤，兼具人參清香與雞肉甜美。',
    tips: '景福宮的土俗村參雞湯是排隊地獄，中午 12 點排隊最長，建議穿完韓服早上 11:00 前去吃。',
    x: 280,
    y: 130
  },
  {
    id: 'gamjatang',
    name: '馬鈴薯燉排骨湯',
    koName: '감자탕',
    category: 'soup',
    categoryName: '養生湯品',
    price: 15000,
    rating: 4.8,
    district: 'gwangjang',
    districtName: '東大門 / 廣藏',
    busyScore: { 11: 50, 12: 85, 13: 60, 14: 45, 15: 40, 16: 45, 17: 65, 18: 80, 19: 90, 20: 95, 21: 85, 22: 70 },
    bestTime: '下午 14:00 - 17:00 或晚上 21:30 之後',
    recommendPlace: '東大門 24小時馬鈴薯排骨湯',
    intro: '大塊軟爛的豬脊骨、綿密馬鈴薯與乾白菜，在紅亮辛辣的高湯中滾煮，再灑上香氣鋪鼻的野芝麻粉，是解酒神湯。',
    tips: '多數店家是 24 小時營業，非常適合深夜玩完東大門血拼後來一鍋。',
    x: 430,
    y: 160
  },
  {
    id: 'yukhoe',
    name: '廣藏市場生拌牛肉',
    koName: '육회',
    category: 'street',
    categoryName: '傳統小吃',
    price: 19000,
    rating: 4.9,
    district: 'gwangjang',
    districtName: '廣藏市場',
    busyScore: { 11: 70, 12: 95, 13: 90, 14: 65, 15: 50, 16: 55, 17: 70, 18: 85, 19: 90, 20: 75, 21: 50, 22: 30 },
    bestTime: '早上 10:30 或下午 15:00 - 16:30',
    recommendPlace: '富村生拌牛肉 (米其林推薦)、昌信生拌牛肉',
    intro: '新鮮無腥味的牛里肌切絲拌入香油與白芝麻，鋪在甜脆的水梨絲上，頂端打上一顆鮮雞蛋黃。入口彈牙清甜。',
    tips: '富村生拌牛肉是米其林必比登推薦，人潮洶湧，同條巷子的昌信味道也極好且排隊快。',
    x: 460,
    y: 190
  },
  {
    id: 'budae-jigae',
    name: '邪惡起司部隊鍋',
    koName: '부대찌개',
    category: 'soup',
    categoryName: '養生湯品',
    price: 10000,
    rating: 4.5,
    district: 'sincheon',
    districtName: '新村',
    busyScore: { 11: 40, 12: 80, 13: 70, 14: 50, 15: 35, 16: 40, 17: 60, 18: 75, 19: 85, 20: 70, 21: 40, 22: 25 },
    bestTime: '中午 11:30 前或晚上 20:00 之後',
    recommendPlace: '金剛部隊鍋、熙正食堂',
    intro: '火腿、午餐肉、起司、年糕、辛拉麵融匯於鮮辣高湯中，碳水化合物與起司乳香交融，是小資族保證飽腹的美味。',
    tips: '金剛部隊鍋的拉麵和白飯是無限量免費自取，CP值天花板！',
    x: 160,
    y: 240
  },
  {
    id: 'tteokbokki',
    name: '街邊辣炒年糕+魚板',
    koName: '떡볶이',
    category: 'street',
    categoryName: '傳統小吃',
    price: 8000,
    rating: 4.6,
    district: 'myeongdong',
    districtName: '明洞',
    busyScore: { 11: 30, 12: 50, 13: 40, 14: 45, 15: 55, 16: 70, 17: 85, 18: 95, 19: 100, 20: 90, 21: 75, 22: 60 },
    bestTime: '下午 16:00 剛開市或晚上 22:00 之後',
    recommendPlace: '明洞街邊攤、新堂洞年糕街',
    intro: '街頭布帳馬車的招牌！Q彈有嚼勁的年糕與魚板裹滿甜辣濃稠的紅辣椒醬。配上一杯滾燙的昆布高湯，暖心無比。',
    tips: '明洞小吃攤約在下午 16:00 陸續開攤，可以多攤合吃，體驗在地站立文化。',
    x: 320,
    y: 240
  },
  {
    id: 'jajangmyeon',
    name: '韓式炸醬麵',
    koName: '짜장면',
    category: 'street',
    categoryName: '傳統小吃',
    price: 8500,
    rating: 4.6,
    district: 'seongsu',
    districtName: '聖水洞',
    busyScore: { 11: 40, 12: 85, 13: 65, 14: 50, 15: 35, 16: 40, 17: 55, 18: 70, 19: 80, 20: 70, 21: 45, 22: 30 },
    bestTime: '13:30 - 15:00 下午時段',
    recommendPlace: '香港飯店0410 (白鐘元旗下)、大上海',
    intro: '焦香黑亮的春醬炒入大量洋蔥丁和豬肉碎，淋在嚼勁十足的手拉麵上。入口滋味鹹甜濃稠、香氣逼人，吃時一定要發出吸吮聲！',
    tips: '搭配糖醋肉 (Tangsuyuk) 是最正宗的韓式中華料理雙壁，通常外送速度極快！',
    x: 520,
    y: 220
  },
  {
    id: 'chicken-one',
    name: '陳玉華一隻雞',
    koName: '닭한마리',
    category: 'soup',
    categoryName: '養生湯品',
    price: 15000,
    rating: 4.8,
    district: 'gwangjang',
    districtName: '東大門 / 廣藏',
    busyScore: { 11: 50, 12: 90, 13: 75, 14: 55, 15: 40, 16: 45, 17: 65, 18: 95, 19: 100, 20: 90, 21: 65, 22: 40 },
    bestTime: '中午 11:00 之前或下午 15:00 - 16:30',
    recommendPlace: '陳玉華一隻雞、孔陵一隻雞',
    intro: '整隻鮮雞放入加入大量大蒜蓉的清湯中烹煮。雞肉滑嫩清香，搭配大蒜辣椒醬醋，最後加入手切麵條吸滿鮮濃高湯，鮮甜至極。',
    tips: '東大門一隻雞胡同名店林立，陳玉華排隊最長，陳源祖或孔陵一隻雞也極受在地老饕喜愛。',
    x: 400,
    y: 130
  }
];

// --- 花蓮台東三天兩夜 12 大山海名勝與美食數據 ---
export interface HualienTaitungPoi {
  id: string;
  name: string;
  category: 'spot' | 'food' | 'stay';
  categoryName: string;
  district: 'hualien' | 'coast' | 'valley' | 'taitung';
  districtName: string;
  intro: string;
  tips: string;
  recommendTime: string;
  budgetEst: string;
  x: number;
  y: number;
}

export const hualienTaitungPois: HualienTaitungPoi[] = [
  {
    id: 'taroko',
    name: '太魯閣國家公園 (砂卡礑步道)',
    category: 'spot',
    categoryName: '自然景觀',
    district: 'hualien',
    districtName: '花蓮市/太魯閣',
    intro: '大自然鬼斧神工的峽谷奇景！碧綠幽靜的溪水沿著大理石岩壁緩緩流過，砂卡礑步道平緩好走，沿途充滿了原住民文化的雕刻與美麗景色。',
    tips: '受0403地震影響部分步道修復中，砂卡礑與燕子口行前務必上官網查詢最新開放資訊。建議早上 08:00 前抵達避開人潮。',
    recommendTime: '2 - 3 小時',
    budgetEst: '免費',
    x: 40,
    y: 18
  },
  {
    id: 'chixingtan',
    name: '七星潭海岸風景區',
    category: 'spot',
    categoryName: '自然景觀',
    district: 'hualien',
    districtName: '花蓮市/太魯閣',
    intro: '呈優美弧形的礫石海灣，可以一邊聆聽太平洋澎湃的浪濤聲，一邊撿拾光滑可愛的圓潤鵝卵石。是等候日出與黃昏漫步的絕佳聖地。',
    tips: '海灘為陡降型深海，海浪暗流極強，請絕對不要下水游泳或過度靠近浪線！',
    recommendTime: '1 - 1.5 小時',
    budgetEst: '免費',
    x: 52,
    y: 28
  },
  {
    id: 'chingshui',
    name: '清水斷崖',
    category: 'spot',
    categoryName: '自然景觀',
    district: 'hualien',
    districtName: '花蓮市/太魯閣',
    intro: '台灣八大景之一！千公尺高的懸崖峭壁直插入深邃的三色果凍海中，海天一色的極致漸層與鬼斧神工的絕壁，展現出台灣東海岸最震撼的視覺。',
    tips: '設有匯德觀景台，停車場步行5分鐘即可抵達。蘇花公路車流量大、大型車多，自駕或騎機車北上時請靠右慢行並務必注意後方來車。',
    recommendTime: '40 分鐘',
    budgetEst: '免費',
    x: 42,
    y: 10
  },
  {
    id: 'shitiping',
    name: '石梯坪地質景觀',
    category: 'spot',
    categoryName: '自然景觀',
    district: 'coast',
    districtName: '台11線海岸公路',
    intro: '擁有極為壯觀的火山噴發岩與海蝕地貌。這裡隆起的珊瑚礁、海蝕溝、海蝕崖與壯麗的單面山，是親近潮間帶生態的絕佳天然教室。',
    tips: '爬上單面山拍照時風力極強且岩石銳利，請務必穿著防滑好走的包鞋，注意腳下安全。',
    recommendTime: '1.5 - 2 小時',
    budgetEst: '小型車停車費 NT$60',
    x: 58,
    y: 48
  },
  {
    id: 'xinshe-rice-terrace',
    name: '豐濱新社海梯田',
    category: 'spot',
    categoryName: '自然景觀',
    district: 'coast',
    districtName: '台11線海岸公路',
    intro: '全台唯一的臨海黃金水稻梯田。當秋收時節，金黃色的稻浪隨著太平洋的海風起伏，彷彿一條鋪在深藍大海旁的金色毛毯，美得令人摒息。',
    tips: '現場設有許多可愛的原住民竹編與稻草人裝置藝術可以拍照，請尊重農夫心血，切勿踩踏或隨意跨入水稻田中央。',
    recommendTime: '1 小時',
    budgetEst: '免費',
    x: 56,
    y: 43
  },
  {
    id: 'brown-avenue',
    name: '池上伯朗大道 (金城武樹)',
    category: 'spot',
    categoryName: '人文打卡',
    district: 'valley',
    districtName: '台9線花東縱谷',
    intro: '一條沒有任何電線桿的翠綠天堂路，兩側滿是無邊無際的金色稻浪（5月與10月最美）。遠處中央山脈高聳入雲，騎單車漫遊無比愜意。',
    tips: '大道全面管制外來汽機車，必須在入口處租借自行車或電動協力車（約NT$100-350），建議早晨 07:00 來能享受無人空景。',
    recommendTime: '2 小時',
    budgetEst: '單車租借 NT$150起',
    x: 32,
    y: 60
  },
  {
    id: 'duoliang',
    name: '多良車站 (全台最美車站)',
    category: 'spot',
    categoryName: '人文打卡',
    district: 'taitung',
    districtName: '台東市區/多良',
    intro: '架設在紅色鐵軌與湛藍太平洋之間的傳奇車站。當火車從山洞呼嘯而出，在鮮紅欄杆與無垠藍海的映襯下，構成一幅令人動容的明信片絕景。',
    tips: '車站目前已不提供客運停靠，改為觀光園區。建議先上網查詢南迴線火車時刻表，才能精準拍到火車過站的瞬間。',
    recommendTime: '1 小時',
    budgetEst: '清潔費 NT$10',
    x: 28,
    y: 88
  },
  {
    id: 'scallion-pancake',
    name: '花蓮正宗炸蛋蔥油餅 (復興街)',
    category: 'food',
    categoryName: '地道美食',
    district: 'hualien',
    districtName: '花蓮市/太魯閣',
    intro: '花蓮最具代表性的超人氣街頭小吃！高溫油炸至金黃酥脆的蓬鬆餅皮，包覆著半熟蛋，咬下的瞬間蛋黃爆漿交織鹹甜醬汁，邪惡度破表。',
    tips: '老牌黃車與藍車並排在復興街上，下午 13:00 開賣即開始大排長龍，可先打電話預訂再過去拿，蛋可以選擇全熟或半熟。',
    recommendTime: '30 分鐘',
    budgetEst: 'NT$35 - NT$45',
    x: 48,
    y: 30
  },
  {
    id: 'dongdamen-night-market',
    name: '東大門夜市 (風味街)',
    category: 'food',
    categoryName: '地道美食',
    district: 'hualien',
    districtName: '花蓮市/太魯閣',
    intro: '由福町夜市、原住民風味街、各省一條街與自強夜市合體而成的超巨大美食戰區！推薦竹筒飯、石板烤肉、第一家烤肉與林記燒番麥。',
    tips: '夜市占地極廣且有寬敞的人行步道，週五、週六晚上常有街頭藝人與原住民歌手駐唱，氛圍極佳，非常適合安排在第一晚。',
    recommendTime: '2 小時',
    budgetEst: 'NT$150 - NT$300',
    x: 46,
    y: 34
  },
  {
    id: 'rice-noodles-tree',
    name: '台東榕樹下米苔目',
    category: 'food',
    categoryName: '地道美食',
    district: 'taitung',
    districtName: '台東市區/多良',
    intro: '超過五十年的經典台東古早味早餐！滑Q細緻的手工米苔目，撒上滿滿的韭菜、肉燥與大把香氣撲鼻的柴魚片，湯頭濃郁鮮甜，必加特製辣醬。',
    tips: '店面全新裝潢過。建議搭配滷得極為入味的特製滷味盤，以及點一杯冰涼清爽的太和香草茶解膩。',
    recommendTime: '1 小時',
    budgetEst: 'NT$50 - NT$100',
    x: 35,
    y: 75
  },
  {
    id: 'santorini-stay',
    name: '花蓮聖托里尼海景民宿',
    category: 'stay',
    categoryName: '海景住宿',
    district: 'hualien',
    districtName: '花蓮市/太魯閣',
    intro: '坐落於花蓮東海岸公路旁的夢幻希臘風白色與亮藍建築，陽台直面無垠的太平洋。清晨睜開眼就能看見橘紅日出從海平面緩緩升起。',
    tips: '靠近海洋公園，景觀絕佳，非常適合情侶或需要看海放鬆的旅客。建議提早1個月在各大平台預訂海景雙人房。',
    recommendTime: '一晚',
    budgetEst: 'NT$2,200起 / 晚',
    x: 50,
    y: 38
  },
  {
    id: 'dulan-cafe',
    name: '都蘭糖廠 & 小房子咖啡',
    category: 'stay',
    categoryName: '人文打卡',
    district: 'taitung',
    districtName: '台東市區/多良',
    intro: '充滿濃厚台東慢活文青氣息的都蘭遺址聚落！老糖廠改建成的手作藝術聚落與特色咖啡廳，夜間常有在地樂團或原住民歌手在小酒館演出。',
    tips: '都蘭充滿了許多移居台東的外國人與衝浪好手，非常推薦下午在這裡喝杯手沖咖啡，聽聽太平洋的風聲，感受最純粹的台東慢靈魂。',
    recommendTime: '2 小時',
    budgetEst: '咖啡消費約 NT$150',
    x: 36,
    y: 70
  }
];

interface CustomPageViewProps {
  page: CustomPageData;
  onBackToHome: () => void;
}

export const CustomPageView: React.FC<CustomPageViewProps> = ({ page, onBackToHome }) => {
  const contentData = getArticleContent(page.id, page.title, page.category);

  // --- 1. 共通狀態 ---
  const [activeTab, setActiveTab] = useState<'content' | 'interactive' | 'notes'>('content');
  const [isSaved, setIsSaved] = useState(false);
  const [copiedLink, setCopiedLink] = useState(false);

  // --- 2. 關於我們狀態 ---
  const [feedbackName, setFeedbackName] = useState('');
  const [feedbackEmail, setFeedbackEmail] = useState('');
  const [feedbackMsg, setFeedbackMsg] = useState('');
  const [feedbackSent, setFeedbackSent] = useState(false);

  // --- 3. 插座指南狀態 ---
  const [selectedPlugCountry, setSelectedPlugCountry] = useState('JP');
  const plugData: Record<string, { name: string; voltage: string; freq: string; plugs: string[]; tips: string; shapeSvg: string }> = {
    JP: {
      name: '日本',
      voltage: '100V',
      freq: '50Hz / 60Hz',
      plugs: ['A型 (扁平雙針)'],
      tips: '台灣電器（110V、A型插頭）可在日本直接使用，無須轉接頭。但高功率電器（如大風量吹風機）建議確認電壓容許度。',
      shapeSvg: 'M 25 35 L 25 65 M 45 35 L 45 65'
    },
    KR: {
      name: '韓國',
      voltage: '220V',
      freq: '60Hz',
      plugs: ['C型 / F型 (圓頭雙孔)'],
      tips: '韓國使用的是德規 220V 圓孔插座（直徑 4.7mm）。台灣 110V 雙平頭插頭必須加上轉接頭，且電器需支援國際電壓（100-240V）。',
      shapeSvg: 'M 20 50 A 5 5 0 1 1 20 49 M 50 50 A 5 5 0 1 1 50 49'
    },
    TH: {
      name: '泰國',
      voltage: '220V',
      freq: '50Hz',
      plugs: ['A型 / B型 / C型 / O型'],
      tips: '泰國插座相容性極高，多數酒店使用萬規插座，台灣 A 型雙平頭插頭可直接插入，但仍須確保電器支持 220V 電壓。',
      shapeSvg: 'M 20 40 L 20 60 M 50 40 L 50 60 M 35 60 A 3 3 0 1 1 35 59'
    },
    SG: {
      name: '新加坡 / 馬來西亞',
      voltage: '230V',
      freq: '50Hz',
      plugs: ['G型 (英規三腳方型)'],
      tips: '採用英規三角方插。必須使用轉接頭，且確認電器支援 220V-240V 國際電壓。',
      shapeSvg: 'M 35 25 L 35 45 M 15 65 L 25 65 M 45 65 L 55 65'
    },
    VN: {
      name: '越南',
      voltage: '220V',
      freq: '50Hz',
      plugs: ['A型 / C型 / G型'],
      tips: '南部通常能相容雙平頭與雙圓頭插座，部分商務酒店支援萬規。高功率電器如電熱水壺請注意安全電壓。',
      shapeSvg: 'M 20 50 L 20 60 A 3 3 0 0 1 23 63 M 50 50 L 50 60 A 3 3 0 0 1 53 63'
    },
    TW: {
      name: '台灣',
      voltage: '110V',
      freq: '60Hz',
      plugs: ['A型 / B型'],
      tips: '標準兩扁腳或兩扁一圓接地插頭。日本電器可直接在台灣插孔使用（偶爾有10V電壓差但通常安全）。',
      shapeSvg: 'M 25 35 L 25 65 M 45 35 L 45 65 M 35 65 A 4 4 0 1 1 35 64'
    },
    EU: {
      name: '歐洲通用 / 冰島',
      voltage: '230V',
      freq: '50Hz',
      plugs: ['C型 / F型'],
      tips: '歐洲與冰島多使用 C 型歐規雙圓頭插頭，插座通常向內凹陷。建議備妥萬國轉接頭。',
      shapeSvg: 'M 20 50 A 5 5 0 1 1 20 49 M 50 50 A 5 5 0 1 1 50 49'
    },
    CH: {
      name: '瑞士',
      voltage: '230V',
      freq: '50Hz',
      plugs: ['J型 (細三圓頭)'],
      tips: '瑞士擁有獨特的 J 型內凹三圓頭插座。一般的 C 型歐規雙圓插通常可插入使用，但有時會因插座外圈邊框太厚而卡住。',
      shapeSvg: 'M 18 45 A 3 3 0 1 1 18 44 M 52 45 A 3 3 0 1 1 52 44 M 35 60 A 3 3 0 1 1 35 59'
    }
  };

  // --- 4. 里程計算器狀態 ---
  const [milesRoute, setMilesRoute] = useState('tpe-nrt');
  const [milesCabin, setMilesCabin] = useState('y'); // y=eco, pe=prem-eco, j=biz, f=first
  const [milesAlliance, setMilesAlliance] = useState('star');
  const routeDistances: Record<string, { label: string; miles: number }> = {
    'tpe-nrt': { label: '台北 (TPE) ↔ 東京 (NRT/HND)', miles: 1356 },
    'tpe-icn': { label: '台北 (TPE) ↔ 首爾 (ICN)', miles: 912 },
    'tpe-bkk': { label: '台北 (TPE) ↔ 曼谷 (BKK)', miles: 1565 },
    'tpe-sin': { label: '台北 (TPE) ↔ 新加坡 (SIN)', miles: 2011 },
    'tpe-zrh': { label: '台北 (TPE) ↔ 蘇黎世 (ZRH)', miles: 5980 },
    'tpe-kef': { label: '台北 (TPE) ↔ 雷克雅維克 (KEF)', miles: 6420 }
  };
  const cabinMultipliers: Record<string, { label: string; rate: number }> = {
    'y_promo': { label: '經濟艙 (特惠票 50%)', rate: 0.5 },
    'y': { label: '經濟艙 (標準/年票 100%)', rate: 1.0 },
    'pe': { label: '豪華經濟艙 (115%)', rate: 1.15 },
    'j': { label: '商務艙 (125% - 150%)', rate: 1.35 },
    'f': { label: '頭等艙 (150% - 200%)', rate: 1.5 }
  };

  const calculateEarnedMiles = () => {
    const base = routeDistances[milesRoute]?.miles || 1000;
    const mult = cabinMultipliers[milesCabin]?.rate || 1.0;
    const oneway = Math.round(base * mult);
    return {
      oneway,
      roundtrip: oneway * 2,
      percentOfFreeTicket: Math.round(((oneway * 2) / 35000) * 100)
    };
  };

  // --- 5. 退稅計算器狀態 ---
  const [refundCountry, setRefundCountry] = useState('JP');
  const [refundAmount, setRefundAmount] = useState<number>(30000);
  const refundConfigs: Record<string, { name: string; currency: string; taxRate: number; feePercent: number; minSpend: number; minSpendLabel: string; tips: string }> = {
    JP: {
      name: '日本',
      currency: 'JPY',
      taxRate: 0.10,
      feePercent: 0.0155, // 一般百貨公司扣1.55%
      minSpend: 5000,
      minSpendLabel: '未稅滿 5,000 日圓 (同一天同一家店)',
      tips: '通常在免稅櫃台直接退現或不收消費稅，若是在大型百貨公司，會收取 1.55% 手續費，實際拿到約 8.45% 退稅額。分為「一般物品」與「消耗品」，消耗品需特殊包裝且在出境前不得拆封。'
    },
    KR: {
      name: '韓國',
      currency: 'KRW',
      taxRate: 0.10,
      feePercent: 0.03, // 級距退稅，大約實退 5% - 7%
      minSpend: 15000,
      minSpendLabel: '含稅滿 15,000 韓元',
      tips: '推行「現場退稅 (Instant Tax Refund)」，在貼有 Tax Free 標誌的店鋪出示護照，結帳時直接扣除稅金。部分小店需至機場自助退稅機，掃描退稅單。'
    },
    TH: {
      name: '泰國',
      currency: 'THB',
      taxRate: 0.07,
      feePercent: 0.018, // 階梯式退稅表，實退大約 4.5% - 6%
      minSpend: 2000,
      minSpendLabel: '單店單日滿 2,000 泰銖，全旅程總額滿 5,000 泰銖',
      tips: '購物時請商家填寫 P.P.10 表格。出境當天在曼谷機場海關辦公室(出境大廳前)蓋章核實，過安檢後到退稅窗口領取現金，每筆退稅有 100 泰銖手續費。'
    },
    EU: {
      name: '歐洲 / 冰島',
      currency: 'EUR',
      taxRate: 0.24, // 冰島標準稅率 24%，食品類 11%
      feePercent: 0.09, // 實退大約 11% - 15%
      minSpend: 6000, // 冰島克朗 6,000 ISK
      minSpendLabel: '單店單日滿 6,000 冰島克朗 (約 40 EUR)',
      tips: '退稅單需在離開歐盟/冰島的最後一個機場海關蓋印。冰島非歐盟國家，需在雷克雅維克機場單獨辦理。請保留商品未拆封供抽查。'
    }
  };

  const calculateTaxRefund = () => {
    const config = refundConfigs[refundCountry];
    if (!config) return { rawTax: 0, actualRefund: 0, fee: 0 };
    const rawTax = Math.round(refundAmount * config.taxRate);
    const fee = Math.round(refundAmount * config.feePercent);
    const actualRefund = Math.max(0, rawTax - fee);
    const inTwd = Math.round(actualRefund * (refundCountry === 'JP' ? 0.21 : refundCountry === 'KR' ? 0.024 : refundCountry === 'TH' ? 0.89 : 35));
    return {
      rawTax,
      fee,
      actualRefund,
      inTwd
    };
  };

  // --- 6. eSIM 比較狀態 ---
  const [esimCountry, setEsimCountry] = useState('JP');
  const [esimDays, setEsimDays] = useState(5);
  const esimPlans = [
    { id: 1, name: 'DJB 暢日卡 PLUS', speed: '極速、極低延遲', carrier: 'Softbank/Docomo 雙網', unlimited: true, pricePerDay: 130, rating: 4.9, tags: ['極力推薦', '網速霸主'] },
    { id: 2, name: 'Klook 每日高速定量', speed: '中規中矩、穩健', carrier: 'Softbank', unlimited: false, limit: '每日 2GB 後降速', pricePerDay: 65, rating: 4.6, tags: ['高CP值', '大廠保障'] },
    { id: 3, name: 'Airalo 歐亞多國通用', speed: '各國即時漫遊', carrier: '多電信漫遊', unlimited: false, limit: '總量 10GB 方案', pricePerDay: 90, rating: 4.5, tags: ['跨國首選', '英文界面'] },
    { id: 4, name: 'KKday 原生卡直營', speed: '順暢原生路由', carrier: 'Docomo', unlimited: true, pricePerDay: 110, rating: 4.8, tags: ['原生線路'] }
  ];

  // --- 7. 打包清單狀態 ---
  const [packingItems, setPackingItems] = useState([
    { id: 1, text: '護照與護照影本、台胞證/駕照譯本', checked: true, category: '證件檔案' },
    { id: 2, text: '萬國轉接頭、高規快充頭、多合一充電線', checked: false, category: '電子通訊' },
    { id: 3, text: '極輕便雨傘/超輕防雨衝鋒衣', checked: false, category: '衣物鞋履' },
    { id: 4, text: '個人常備藥（感冒藥、止痛藥、暈車藥）', checked: false, category: '日常備藥' },
    { id: 5, text: '保濕乳液、護唇膏、小瓶防曬乳', checked: false, category: '盥洗美妝' },
    { id: 6, text: '當地交通卡/周遊券實體或電子票證', checked: true, category: '證件檔案' }
  ]);
  const [newPackingText, setNewPackingText] = useState('');
  const [newPackingCat, setNewPackingCat] = useState('電子通訊');

  const addPackingItem = () => {
    if (!newPackingText.trim()) return;
    setPackingItems([...packingItems, {
      id: Date.now(),
      text: newPackingText,
      checked: false,
      category: newPackingCat
    }]);
    setNewPackingText('');
  };

  const togglePackingItem = (id: number) => {
    setPackingItems(packingItems.map(item => item.id === id ? { ...item, checked: !item.checked } : item));
  };

  const deletePackingItem = (id: number) => {
    setPackingItems(packingItems.filter(item => item.id !== id));
  };

  const packedCount = packingItems.filter(i => i.checked).length;
  const totalPackingCount = packingItems.length;
  const packingPercent = totalPackingCount > 0 ? Math.round((packedCount / totalPackingCount) * 100) : 0;

  // --- 8. 東京住宿推薦狀態 ---
  const [selectedTokyoArea, setSelectedTokyoArea] = useState('shinjuku');
  const tokyoAreas: Record<string, { name: string; pros: string; cons: string; budget: string; shops: string; train: string; recommendHotels: string[] }> = {
    shinjuku: {
      name: '新宿 (Shinjuku)',
      pros: '交通無敵、直達箱根與河口湖、購物百貨密集、深夜居酒屋與美食無數。',
      cons: '車站迷宮極易迷路、歌舞伎町一帶環境較為嘈雜。',
      budget: '★★★★☆ (中高)',
      shops: '★★★★★ (極佳)',
      train: '★★★★★ (頂級樞紐)',
      recommendHotels: ['新宿格拉斯麗酒店 (哥吉拉飯店)', '由緣 新宿 溫泉旅館 (極力推薦日式美學)', '新宿燦路都廣場大飯店']
    },
    ueno: {
      name: '上野 (Ueno)',
      pros: '京成電鐵 Skyliner 直達新昌、阿美橫丁藥妝美食超便宜、公園博物館雲集。',
      cons: '夜晚居酒屋街較多喝醉的人、精品購物較少。',
      budget: '★★★☆☆ (平價高CP)',
      shops: '★★★★☆ (藥妝雜貨強)',
      train: '★★★★★ (直達機場與新幹線)',
      recommendHotels: ['上野御徒町SUPER HOTEL (有免費溫泉)', '上野雷索爾酒店', 'MIMARU東京 上野東 (家庭公寓房)']
    },
    ginza: {
      name: '銀座 (Ginza)',
      pros: '街道精緻優雅、名牌百貨旗艦店集中、頂級米其林餐廳無數、氛圍安靜高貴。',
      cons: '住宿預算偏高、地鐵轉乘去郊區通常需要到東京站換車。',
      budget: '★★★★★ (奢華頂規)',
      shops: '★★★★★ (奢華精品)',
      train: '★★★☆☆ (以地鐵為主)',
      recommendHotels: ['銀座五丁目美居酒店', '東京千禧三井花園飯店', 'AC Hotel by Marriott Tokyo Ginza']
    },
    asakusa: {
      name: '淺草 (Asakusa)',
      pros: '江戶風情濃厚、晴空塔就在眼前、許多高CP值的特色青年旅館與老店。',
      cons: '前往澀谷、新宿等西側景點較遠，晚上 8 點後店鋪多關閉、街區安靜。',
      budget: '★★☆☆☆ (經濟平價)',
      shops: '★★★☆☆ (伴手禮老街)',
      train: '★★★☆☆ (有淺草線/銀座線)',
      recommendHotels: ['淺草豪景酒店 (晴空塔景觀頂規)', 'The Gate Hotel 雷門 by Hulic', '淺草駒形WING國際精選酒店']
    }
  };

  // --- 9. 日本藥妝推薦狀態 ---
  const [drugstoreCart, setDrugstoreCart] = useState<Record<string, number>>({});
  const drugstoreProducts = [
    { id: 'p1', name: 'Wakamoto 若元錠', desc: '助消化、整腸、營養三效合一，長輩指名神物', price: '2,100 JPY', localPrice: '約 NT$450' },
    { id: 'p2', name: 'EVE QUICK 止痛藥', desc: '針對頭痛快速舒緩，溫和不傷胃 (藍色包裝)', price: '1,280 JPY', localPrice: '約 NT$270' },
    { id: 'p3', name: 'ROIHI-TSUBOKO 溫感大貼布', desc: '圓形穴位貼布，舒緩肩頸酸痛，超強滲透', price: '798 JPY', localPrice: '約 NT$170' },
    { id: 'p4', name: 'MINON 氨基酸保濕面膜', desc: '敏感肌救星，超強保濕力，溫和抗乾敏', price: '1,200 JPY', localPrice: '約 NT$250' }
  ];

  const toggleDrugstoreCart = (id: string) => {
    setDrugstoreCart(prev => ({
      ...prev,
      [id]: prev[id] ? 0 : 1
    }));
  };

  // --- 10. 預算規劃工具狀態 ---
  const [budgetDays, setBudgetDays] = useState(5);
  const [budgetHotel, setBudgetHotel] = useState(2500); // TWD/night
  const [budgetFlight, setBudgetFlight] = useState(12000); // TWD
  const [budgetFood, setBudgetFood] = useState(1200); // TWD/day
  const [budgetShopping, setBudgetShopping] = useState(10000); // TWD

  const calcTotalBudget = () => {
    return budgetFlight + (budgetHotel * budgetDays) + (budgetFood * budgetDays) + budgetShopping;
  };

  // 處理書籤保存
  useEffect(() => {
    const bookmarks = JSON.parse(localStorage.getItem('custom_page_bookmarks') || '[]');
    setIsSaved(bookmarks.includes(page.id));
  }, [page.id]);

  // 處理隨行備忘錄
  const [memoText, setMemoText] = useState<string>('');
  const [memoSavedStatus, setMemoSavedStatus] = useState<boolean>(false);

  useEffect(() => {
    const saved = localStorage.getItem('slow_travel_memo_' + page.id);
    if (saved) {
      setMemoText(saved);
    } else {
      setMemoText('');
    }
  }, [page.id]);

  const handleSaveMemo = () => {
    localStorage.setItem('slow_travel_memo_' + page.id, memoText);
    setMemoSavedStatus(true);
    setTimeout(() => setMemoSavedStatus(false), 2000);
  };

  // 動態 SEO Head 標籤與結構化數據 (JSON-LD) 注入
  useEffect(() => {
    const originalTitle = document.title;
    document.title = `${page.title}｜均在路上 Travel Lab`;

    const setMetaTag = (attrName: string, attrVal: string, contentVal: string) => {
      let element = document.querySelector(`meta[${attrName}="${attrVal}"]`);
      if (!element) {
        element = document.createElement('meta');
        element.setAttribute(attrName, attrVal);
        document.head.appendChild(element);
      }
      element.setAttribute('content', contentVal);
    };

    const setLinkTag = (rel: string, hrefVal: string) => {
      let element = document.querySelector(`link[rel="${rel}"]`);
      if (!element) {
        element = document.createElement('link');
        element.setAttribute('rel', rel);
        document.head.appendChild(element);
      }
      element.setAttribute('href', hrefVal);
    };

    // 備份與設定 Description
    const originalDescElement = document.querySelector('meta[name="description"]');
    const originalDesc = originalDescElement ? originalDescElement.getAttribute('content') : '';
    setMetaTag('name', 'description', page.intro || '');
    setMetaTag('name', 'robots', 'index, follow');

    // 設定關鍵字
    const keywordsMap: Record<string, string> = {
      'tokyo-5days': '東京自由行, 東京5天4夜, 東京行程推薦, 澀谷, 淺草寺, 新宿, 東京美食, 築地市場, 台場, 自由行攻略',
      'tokyo-accommodation': '東京住宿, 東京飯店推薦, 上野住宿, 銀座住宿, 澀谷住宿, 新宿住宿, 日本自由行',
      'japan-drugstore-checklist': '日本藥妝, 日本必買, 藥妝清單, 松本清, 大國藥妝, 日本伴手禮',
      'japan-budget-guide': '日本旅遊花費, 日本自由行預算, 日本省錢, 關西旅遊預算',
      'kenting': '墾丁自由行, 墾丁3天2夜, 墾丁旅遊景點, 恆春美食, 國境之南, 墾丁玩水'
    };
    const pageKeywords = keywordsMap[page.id] || `${page.title}, 自由行, 旅遊攻略, 均在路上`;
    setMetaTag('name', 'keywords', pageKeywords);

    // 設定 Canonical
    const originalCanonicalElement = document.querySelector('link[rel="canonical"]');
    const originalCanonical = originalCanonicalElement ? originalCanonicalElement.getAttribute('href') : '';
    const pageUrl = `https://golightly.fun/${page.url || page.id + '.html'}`;
    setLinkTag('canonical', pageUrl);

    // 設定 Open Graph 標籤
    setMetaTag('property', 'og:title', `${page.title}｜均在路上 Travel Lab`);
    setMetaTag('property', 'og:description', page.intro || '');
    setMetaTag('property', 'og:image', page.coverImage || '');
    setMetaTag('property', 'og:url', pageUrl);
    setMetaTag('property', 'og:type', 'article');

    // 設定 Twitter 標籤
    setMetaTag('name', 'twitter:card', 'summary_large_image');
    setMetaTag('name', 'twitter:title', `${page.title}｜均在路上 Travel Lab`);
    setMetaTag('name', 'twitter:description', page.intro || '');
    setMetaTag('name', 'twitter:image', page.coverImage || '');

    // 移除舊的動態 JSON-LD
    const existingJsonLd = document.getElementById('dynamic-jsonld');
    if (existingJsonLd) {
      existingJsonLd.remove();
    }

    // 插入新動態 JSON-LD
    const script = document.createElement('script');
    script.id = 'dynamic-jsonld';
    script.type = 'application/ld+json';

    let jsonLdContent: any = {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": page.title,
      "image": page.coverImage || "https://golightly.fun/images/logo.webp",
      "genre": "旅遊攻略",
      "keywords": pageKeywords,
      "publisher": {
        "@type": "Organization",
        "name": "均在路上 Travel Lab",
        "url": "https://golightly.fun",
        "logo": {
          "@type": "ImageObject",
          "url": "https://golightly.fun/images/logo.webp"
        }
      },
      "url": pageUrl,
      "datePublished": "2026-06-25",
      "author": {
        "@type": "Person",
        "name": "Ollie Yu"
      },
      "description": page.intro || ""
    };

    if (page.id === 'tokyo-5days') {
      jsonLdContent = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": "東京5天4夜經典行程：潮流、傳統與極致美食完美交織",
        "description": page.intro || "",
        "image": page.coverImage,
        "genre": "日本旅遊",
        "keywords": pageKeywords,
        "datePublished": "2026-06-25",
        "url": pageUrl,
        "author": {
          "@type": "Person",
          "name": "Ollie Yu"
        },
        "publisher": {
          "@type": "Organization",
          "name": "均在路上 Travel Lab",
          "url": "https://golightly.fun",
          "logo": {
            "@type": "ImageObject",
            "url": "https://golightly.fun/images/logo.webp"
          }
        },
        "mainEntityOfPage": {
          "@type": "WebPage",
          "@id": pageUrl
        }
      };
    }

    script.text = JSON.stringify(jsonLdContent);
    document.head.appendChild(script);

    // 卸載時還原
    return () => {
      document.title = originalTitle;
      if (originalDesc) {
        setMetaTag('name', 'description', originalDesc);
      }
      if (originalCanonical) {
        setLinkTag('canonical', originalCanonical);
      }
      const dynLd = document.getElementById('dynamic-jsonld');
      if (dynLd) {
        dynLd.remove();
      }
    };
  }, [page]);

  const handleToggleSave = () => {
    const bookmarks = JSON.parse(localStorage.getItem('custom_page_bookmarks') || '[]');
    let updated;
    if (bookmarks.includes(page.id)) {
      updated = bookmarks.filter((id: string) => id !== page.id);
      setIsSaved(false);
    } else {
      updated = [...bookmarks, page.id];
      setIsSaved(true);
    }
    localStorage.setItem('custom_page_bookmarks', JSON.stringify(updated));
  };

  // --- 11. 墾丁 3天2夜專利狀態 ---
  const [kentingDay, setKentingDay] = useState<number>(1);
  const [kentingTransport, setKentingTransport] = useState<string>('scooter');
  const [kentingStay, setKentingStay] = useState<string>('homestay');
  const [kentingFood, setKentingFood] = useState<string>('standard');
  const [kentingActivities, setKentingActivities] = useState<string[]>(['snorkeling']);

  const toggleKentingActivity = (actId: string) => {
    if (kentingActivities.includes(actId)) {
      setKentingActivities(kentingActivities.filter(a => a !== actId));
    } else {
      setKentingActivities([...kentingActivities, actId]);
    }
  };

  const calculateKentingBudget = () => {
    let transportCost = 0;
    if (kentingTransport === 'scooter') transportCost = 450 * 2; // 機車 2 天
    else if (kentingTransport === 'electric') transportCost = 550 * 2; // 免照電動 2 天
    else if (kentingTransport === 'car') transportCost = 1800 * 2; // 租車 2 天
    else if (kentingTransport === 'charter') transportCost = 3500; // 包車 1 日

    let stayCost = 0;
    if (kentingStay === 'hostel') stayCost = 500 * 2; // 背包客 2 晚
    else if (kentingStay === 'homestay') stayCost = 1800 * 2; // 標準民宿 2 晚
    else if (kentingStay === 'seaview') stayCost = 3500 * 2; // 海景民宿 2 晚

    let foodCost = 0;
    if (kentingFood === 'budget') foodCost = 400 * 3;
    else if (kentingFood === 'standard') foodCost = 700 * 3;
    else if (kentingFood === 'luxury') foodCost = 1500 * 3;

    let actCost = 0;
    kentingActivities.forEach(act => {
      if (act === 'snorkeling') actCost += 350;
      else if (act === 'jetski') actCost += 500;
      else if (act === 'bananaboat') actCost += 300;
      else if (act === 'sup') actCost += 1000;
      else if (act === 'parasail') actCost += 1200;
    });

    const ticketCost = 60 + 30 + 60; // 鵝鑾鼻 + 貓鼻頭 + 關山
    const total = transportCost + stayCost + foodCost + actCost + ticketCost;

    return {
      total,
      transportCost,
      stayCost,
      foodCost,
      actCost,
      ticketCost
    };
  };

  // --- 12. 首爾美食地圖專屬狀態與處理器 ---
  const [seoulDistrict, setSeoulDistrict] = useState<string>('all');
  const [seoulCategory, setSeoulCategory] = useState<string>('all');
  const [seoulHour, setSeoulHour] = useState<number>(18);
  const [seoulSearch, setSeoulSearch] = useState<string>('');
  
  // 美食測驗狀態
  const [seoulQuizStep, setSeoulQuizStep] = useState<number>(0); // 0=開始, 1=辣度, 2=類別, 3=預算, 4=結果
  const [seoulQuizSpicy, setSeoulQuizSpicy] = useState<string>(''); // none, low, high
  const [seoulQuizType, setSeoulQuizType] = useState<string>(''); // bbq, soup, street, adventurous
  const [seoulQuizBudget, setSeoulQuizBudget] = useState<string>(''); // low, medium, high
  const [seoulQuizMatch, setSeoulQuizMatch] = useState<any>(null);

  const calculateSeoulQuizResult = () => {
    let matched = seoulFoods[0]; // 預設五花肉
    
    if (seoulQuizType === 'bbq') {
      matched = seoulFoods.find(f => f.id === 'samgyeopsal') || seoulFoods[0];
    } else if (seoulQuizType === 'soup') {
      if (seoulQuizSpicy === 'high') {
        matched = seoulFoods.find(f => f.id === 'gamjatang') || seoulFoods[4]; // 馬鈴薯排骨湯
      } else if (seoulQuizSpicy === 'low') {
        matched = seoulFoods.find(f => f.id === 'budae-jigae') || seoulFoods[6]; // 部隊鍋
      } else {
        matched = seoulFoods.find(f => f.id === 'samgyetang') || seoulFoods.find(f => f.id === 'chicken-one') || seoulFoods[3]; // 參雞湯或一隻雞
      }
    } else if (seoulQuizType === 'street') {
      if (seoulQuizSpicy === 'high' || seoulQuizSpicy === 'low') {
        matched = seoulFoods.find(f => f.id === 'tteokbokki') || seoulFoods[7]; // 辣炒年糕
      } else {
        matched = seoulFoods.find(f => f.id === 'jajangmyeon') || seoulFoods[8]; // 炸醬麵
      }
    } else if (seoulQuizType === 'adventurous') {
      if (seoulQuizBudget === 'high') {
        matched = seoulFoods.find(f => f.id === 'ganjang-gejang') || seoulFoods[1]; // 醬油蟹
      } else {
        matched = seoulFoods.find(f => f.id === 'yukhoe') || seoulFoods[5]; // 生拌牛肉
      }
    }
    
    setSeoulQuizMatch(matched);
    setSeoulQuizStep(4);
  };

  const resetSeoulQuiz = () => {
    setSeoulQuizStep(0);
    setSeoulQuizSpicy('');
    setSeoulQuizType('');
    setSeoulQuizBudget('');
    setSeoulQuizMatch(null);
  };

  // --- 13. 花東三天兩夜專屬狀態與處理器 ---
  const [htDistrict, setHtDistrict] = useState<string>('all');
  const [htCategory, setHtCategory] = useState<string>('all');
  const [htStyle, setHtStyle] = useState<string>('relax'); // relax, trek, food, culture
  const [htTransport, setHtTransport] = useState<string>('scooter'); // scooter, car, charter
  const [htBudget, setHtBudget] = useState<number>(6000);
  const [htPoiSearch, setHtPoiSearch] = useState<string>('');
  const [htSelectedPoi, setHtSelectedPoi] = useState<string | null>(null);
  const [htCustomNotes, setHtCustomNotes] = useState<string>('');
  const [htShowSuccess, setHtShowSuccess] = useState<boolean>(false);
  const [htSyncSuccess, setHtSyncSuccess] = useState<boolean>(false);

  // 13.1 行程智慧生成算法
  const getHtItinerary = (style: string, transport: string) => {
    const isScooter = transport === 'scooter';
    const isCar = transport === 'car';
    
    let day1 = {
      title: '花蓮山海初見：峽谷與星空夜市',
      spots: [
        { time: '09:00 - 10:00', name: '抵達花蓮 & 交通整備', desc: isScooter ? '抵達花蓮火車站，在站前租用 125cc 慢活機車，裝載行李準備出發。' : isCar ? '開車抵達花蓮，沿台9線進城，感受東台灣的微風。' : '包車司機在花蓮火車站前親切迎賓，搭乘豪華商務車開始專屬旅程。' },
        { time: '10:30 - 13:30', name: style === 'trek' ? '太魯閣國家公園 (錐麓古道 / 砂卡礑)' : '太魯閣牌樓 & 砂卡礑步道慢步', desc: style === 'trek' ? '挑戰鬼斧神工的太魯閣錐麓古道，俯瞰直落千米的大理石絕壁。' : '漫步砂卡礑步道，碧綠清澈的溪水伴隨微風，是絕佳的吸氧體驗。' },
        { time: '14:00 - 15:30', name: style === 'food' ? '復興街炸蛋蔥油餅與戴記扁食' : '清水斷崖與崇德步道觀景', desc: style === 'food' ? '朝聖下午剛開賣的爆漿炸蛋蔥油餅，再搭配一碗皮薄餡豐的在地老字號扁食。' : '站在蘇花公路上眺望絕美清水斷崖，看著翠綠峭壁筆直切入三色漸層海中。' },
        { time: '16:00 - 18:00', name: '七星潭海灘看海放空', desc: '坐在鵝卵石海灘上聆聽太平洋的「歌唱」— 鵝卵石隨海浪滾動的療癒聲響。' },
        { time: '18:30 - 21:00', name: '東大門夜市大飽口福', desc: '逛逛原住民風味街，享用竹筒飯、鹹豬肉、第一家烤肉，配上一杯清涼的小米酒。' }
      ]
    };

    let day2 = {
      title: '台11線藍色公路：太平洋海風吹拂的長跑',
      spots: [
        { time: '08:30 - 09:30', name: '太平洋海景日出晨喚', desc: '在海景民宿的陽台上迎接入選全台最美的太平洋日出。' },
        { time: '10:30 - 12:00', name: style === 'culture' ? '芭崎瞭望台與磯崎海水浴場' : '親不知子天空步道 / 新社梯田', desc: style === 'culture' ? '在瞭望台喝杯手沖咖啡，俯瞰完美的弧形磯崎海灣與文青裝置藝術。' : '站在全台唯一的臨海新社黃金海梯田旁，拍攝稻浪與藍海交織的絕景。' },
        { time: '12:30 - 13:30', name: style === 'food' ? '石梯港嚐九碗海鮮麵' : '石梯坪生猛海鮮大餐', desc: style === 'food' ? '在港口旁享用鮮美無比的小卷海鮮麵與燙章魚，滿滿的在地海味。' : '在石梯港現挑現煮尚青的生猛海鮮，大啖旗魚刺身與鹽烤活魚。' },
        { time: '14:00 - 16:00', name: '石梯坪單面山探索', desc: '攀登壯麗的海蝕單面山，探訪潮間帶清澈水窪中的小魚、寄居蟹與珊瑚。' },
        { time: '16:30 - 18:30', name: '台11線沿海公路馳騁', desc: '伴隨夕陽餘暉，沿著全台最美的海岸公路南下，入住都蘭或台東市區海景旅宿。' },
        { time: '19:00 - 21:30', name: style === 'culture' ? '鐵花村聚落音樂漫步' : '台東正氣路夜市吃貨行', desc: style === 'culture' ? '漫步在掛滿彩繪熱氣球燈籠的鐵花新創聚落，聆聽草地上的在地歌手彈唱。' : '品嚐大名鼎鼎的林家臭豆腐與東台米苔目，外酥內嫩的臭豆腐簡直一絕！' }
      ]
    };

    let day3 = {
      title: '台9線金黃稻香與全台最美車站',
      spots: [
        { time: '09:00 - 11:30', name: style === 'trek' ? '鹿野高台茶園健行' : '池上伯朗大道金黃稻浪', desc: style === 'trek' ? '登上鹿野高台，俯瞰整個卑南溪谷與遠處山嵐，感受滑翔傘翱翔的鹿野美景。' : '租用文青單車，奔馳在沒有一根電線桿的伯朗大道，跟金城武樹合照。' },
        { time: '12:00 - 13:00', name: '池上鐵路便當原味實測', desc: '在池上飯包文化故事館的懷舊火車車廂內，享用香Q透亮、用木盒裝盛的池上米便當。' },
        { time: '14:30 - 16:00', name: style === 'culture' ? '都蘭糖廠文青巡禮' : '南迴多良車站拍火車', desc: style === 'culture' ? '在充滿異國與原民風情的都蘭遺址中喝咖啡、買手作編織品。' : '站在半山腰，等候南迴線火車從山洞鑽出、奔向湛藍太平洋那一刻的動人絕景。' },
        { time: '16:30 - 17:30', name: '返程與交通歸還', desc: '騎回花蓮或直接在台東火車站還車，帶著滿滿的蔚藍海風與稻香記憶，搭乘台鐵返家。' }
      ]
    };

    return [day1, day2, day3];
  };

  // 13.2 經費智慧估算算法
  const calcHtBudget = () => {
    const transportMap: Record<string, number> = {
      scooter: 1500,
      car: 6600,
      charter: 16500
    };
    const transportCost = transportMap[htTransport] || 1500;
    const stayCost = (htStyle === 'relax' || htStyle === 'culture') ? 6000 : 3600;
    const foodCost = htStyle === 'food' ? 2400 : 1800;
    const actCost = htStyle === 'trek' ? 300 : 100;
    const miscCost = 500;
    const total = transportCost + stayCost + foodCost + actCost + miscCost;

    return {
      total,
      transportCost,
      stayCost,
      foodCost,
      actCost,
      miscCost
    };
  };

  // 13.3 複製行程文字
  const handleCopyHtItinerary = (itinerary: any[], totalCost: number) => {
    let text = `✨ 均在路上 Travel Lab - 我的專屬花東三天兩夜慢遊行程 ✨\n`;
    text += `━━━━━━━━━━━━━━━━━━━━━━━━\n`;
    text += `🚗 交通方式：${htTransport === 'scooter' ? '火車 + 租機車' : htTransport === 'car' ? '全家自駕開車' : '專屬包車導覽'}\n`;
    text += `🎨 旅程風格：${htStyle === 'relax' ? '看海慢活' : htStyle === 'trek' ? '戶外徒步' : htStyle === 'food' ? '吃貨掃街' : '文青打卡'}\n`;
    text += `💰 預估每人預算：NT$ ${totalCost} 元 (理想預算：NT$ ${htBudget} 元)\n\n`;
    
    itinerary.forEach((day, index) => {
      text += `📅 Day ${index + 1}: ${day.title}\n`;
      day.spots.forEach((spot: any) => {
        text += `  🕒 ${spot.time} | ${spot.name}\n`;
        text += `     👉 ${spot.desc}\n`;
      });
      text += `\n`;
    });
    
    text += `💡 貼心提醒：花東看海放空慢旅行，把步調放到最慢，大口呼吸太平洋純淨空氣！`;
    
    navigator.clipboard.writeText(text);
    setHtShowSuccess(true);
    setTimeout(() => setHtShowSuccess(false), 2000);
  };

  // 13.4 同步到我的慢遊筆記
  const handleSyncHtToNotes = (itinerary: any[], totalCost: number) => {
    let text = `### 🌊 我的專屬花東山海慢旅備份\n`;
    text += `* **交通方式**: ${htTransport === 'scooter' ? '火車 + 租機車' : htTransport === 'car' ? '全家自駕開車' : '專屬包車導覽'}\n`;
    text += `* **旅程風格**: ${htStyle === 'relax' ? '看海慢活' : htStyle === 'trek' ? '戶外徒步' : htStyle === 'food' ? '吃貨掃街' : '文青打卡'}\n`;
    text += `* **預估每人總花費**: NT$ ${totalCost} 元 (理想預算: NT$ ${htBudget} 元)\n\n`;
    
    itinerary.forEach((day, index) => {
      text += `#### Day ${index + 1}: ${day.title}\n`;
      day.spots.forEach((spot: any) => {
        text += `* **${spot.time}** | ${spot.name}\n  ${spot.desc}\n`;
      });
      text += `\n`;
    });

    setMemoText(prev => prev ? `${prev}\n\n${text}` : text);
    setHtSyncSuccess(true);
    setTimeout(() => setHtSyncSuccess(false), 2000);
  };

  // 拷貝頁面連結
  const handleCopyLink = () => {
    navigator.clipboard.writeText(window.location.href);
    setCopiedLink(true);
    setTimeout(() => setCopiedLink(false), 2000);
  };

  // 發送反饋
  const handleSendFeedback = (e: React.FormEvent) => {
    e.preventDefault();
    if (!feedbackEmail || !feedbackMsg) return;
    setFeedbackSent(true);
    setTimeout(() => {
      setFeedbackName('');
      setFeedbackEmail('');
      setFeedbackMsg('');
    }, 1500);
  };

  return (
    <div className="bg-tiffany-cream min-h-screen text-slate-800 pb-20 relative">
      
      {/* 頂部封面圖區 - 無裁剪整張顯示 */}
      <div className="w-full bg-slate-950 relative overflow-hidden">
        {/* 返回與珍藏 */}
        <div className="absolute top-6 left-6 right-6 z-30 flex justify-between items-center max-w-7xl mx-auto">
          <button 
            onClick={onBackToHome}
            className="p-3 bg-slate-900/40 hover:bg-[#e63946] text-white rounded-full transition-all duration-300 backdrop-blur-md cursor-pointer border border-white/10"
          >
            <ArrowLeft size={18} />
          </button>
          
          <div className="flex gap-3">
            <button 
              onClick={handleToggleSave}
              className={`p-3 rounded-full transition-all duration-300 backdrop-blur-md cursor-pointer border border-white/10 ${
                isSaved ? 'bg-[#e63946] text-white' : 'bg-slate-900/40 text-slate-200 hover:text-white'
              }`}
            >
              <Heart size={18} className={isSaved ? 'fill-white' : ''} />
            </button>
            <button 
              onClick={handleCopyLink}
              className={`p-3 rounded-full transition-all duration-300 backdrop-blur-md cursor-pointer border border-white/10 bg-slate-900/40 text-slate-200 hover:text-white`}
              title="複製文章連結"
            >
              {copiedLink ? <span className="text-xs px-1 font-bold">已複製!</span> : <Copy size={18} />}
            </button>
          </div>
        </div>

        <img 
          src={page.coverImage} 
          alt={page.title} 
          className="w-full h-auto block mx-auto hover:scale-[1.01] transition-transform duration-700"
          style={{ filter: 'brightness(0.8)' }}
        />
      </div>

      {/* 標題與引言區塊 - 編輯室風格 */}
      <div className="py-8 px-6 md:py-10 md:px-12 text-center bg-white space-y-4 border-b border-slate-100 shadow-2xs">
        <div className="inline-flex items-center justify-center">
          <span className="px-3.5 py-1.5 bg-[#e63946]/90 text-white text-[10px] tracking-widest font-extrabold uppercase rounded-full shadow-md">
            {page.category}
          </span>
        </div>
        <h1 className="text-2xl sm:text-3xl md:text-4xl font-serif font-extrabold tracking-wide text-slate-900 max-w-4xl mx-auto leading-tight md:leading-[1.15]">
          {page.title}
        </h1>
        <p className="text-sm md:text-base text-slate-500 max-w-2xl mx-auto leading-relaxed">
          {page.intro}
        </p>
      </div>

      {/* 主要內容網格區 */}
      <main className="container mx-auto px-6 max-w-5xl mt-12 grid grid-cols-1 lg:grid-cols-12 gap-10">
        
        {/* 左側詳細面板與互動區 */}
        <div className="lg:col-span-8 space-y-10">
          
          {/* 切換頁面視角 */}
          <div className="flex border-b border-tiffany-ice/40 pb-px gap-6">
            <button 
              onClick={() => setActiveTab('content')}
              className={`pb-4 text-xs font-bold tracking-widest uppercase transition-colors relative cursor-pointer ${
                activeTab === 'content' ? 'text-slate-950 font-extrabold' : 'text-slate-400 hover:text-slate-600'
              }`}
            >
              專欄內文
              {activeTab === 'content' && <motion.div layoutId="customActiveTab" className="absolute bottom-0 left-0 right-0 h-0.5 bg-[#e63946]" />}
            </button>
            <button 
              onClick={() => setActiveTab('interactive')}
              className={`pb-4 text-xs font-bold tracking-widest uppercase transition-colors relative cursor-pointer flex items-center gap-1.5 ${
                activeTab === 'interactive' ? 'text-slate-950 font-extrabold' : 'text-slate-400 hover:text-slate-600'
              }`}
            >
              <Sparkles size={12} className="text-[#e63946]" />
              讀者互動工具
              {activeTab === 'interactive' && <motion.div layoutId="customActiveTab" className="absolute bottom-0 left-0 right-0 h-0.5 bg-[#e63946]" />}
            </button>
            <button 
              onClick={() => setActiveTab('notes')}
              className={`pb-4 text-xs font-bold tracking-widest uppercase transition-colors relative cursor-pointer ${
                activeTab === 'notes' ? 'text-slate-950 font-extrabold' : 'text-slate-400 hover:text-slate-600'
              }`}
            >
              慢遊筆記
              {activeTab === 'notes' && <motion.div layoutId="customActiveTab" className="absolute bottom-0 left-0 right-0 h-0.5 bg-[#e63946]" />}
            </button>
          </div>

          {/* 視圖內容 */}
          <div className="min-h-[400px]">
            {activeTab === 'content' && (
              <motion.div 
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                className="prose prose-stone max-w-none space-y-6 leading-relaxed text-tiffany-obsidian/90 font-sans"
              >
                <div className="flex flex-wrap gap-2 pt-2 pb-4">
                  {page.tags.map((tag, idx) => (
                    <span key={idx} className="px-2.5 py-1 bg-white border border-tiffany-ice text-[#e63946] text-[10px] font-bold tracking-wider rounded-md shadow-2xs">
                      #{tag}
                    </span>
                  ))}
                </div>

                <p className="text-base font-serif italic text-tiffany-obsidian/95 border-l-4 border-[#e63946] pl-4 py-2 bg-white/70 shadow-2xs rounded-r-lg">
                  「{contentData.quote}」
                </p>

                {contentData.sections.map((section, sIdx) => (
                  <React.Fragment key={sIdx}>
                    <h3 className="text-lg font-serif font-bold text-tiffany-obsidian pt-4 flex items-center gap-2">
                      <span className="w-1.5 h-6 bg-[#e63946] rounded-full inline-block" />
                      {section.heading}
                    </h3>
                    {section.paragraphs.map((pText, pIdx) => (
                      <p key={pIdx} className="text-tiffany-obsidian/90 leading-relaxed text-base md:text-lg">{pText}</p>
                    ))}
                  </React.Fragment>
                ))}

                <div className="bg-tiffany-obsidian text-slate-200 p-6 rounded-2xl border border-slate-800/50 space-y-4 shadow-sm mt-8">
                  <h4 className="text-sm font-bold tracking-widest text-white uppercase flex items-center gap-2">
                    <Compass size={14} className="text-[#e63946] animate-spin-slow" />
                    編輯特別叮嚀
                  </h4>
                  <ul className="text-xs space-y-2 list-disc list-inside text-slate-300 font-mono">
                    <li>出國前請務必確保護照有效期在 6 個月以上（非常重要！）。</li>
                    <li>建議備妥手機雲端備份，並將重要文件（護照首頁、回程機票、保險單）存一份離線 PDF 到手機。</li>
                    <li>放慢腳步，感受地方的靈魂，而非急著打卡。</li>
                  </ul>
                </div>
              </motion.div>
            )}

            {/* 互動工具區 - 根據 page.id 渲染極致精美的實用工具 */}
            {activeTab === 'interactive' && (
              <motion.div 
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-8"
              >
                {/* 1. 各國插座電壓指南 */}
                {page.id === 'power-plug-guide' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Zap size={18} className="text-[#e63946]" />
                        插座電壓規格動態查詢
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">電器防燒保險箱</span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                      <div className="md:col-span-1 space-y-3">
                        <label className="text-xs font-bold text-slate-500 block uppercase tracking-wider">選擇目的地國家/地區</label>
                        <div className="flex flex-col gap-2">
                          {Object.entries(plugData).map(([code, d]) => (
                            <button
                              key={code}
                              onClick={() => setSelectedPlugCountry(code)}
                              className={`w-full text-left px-4 py-2.5 rounded-lg text-xs font-bold transition-all flex justify-between items-center cursor-pointer ${
                                selectedPlugCountry === code 
                                  ? 'bg-[#e63946] text-white' 
                                  : 'bg-slate-50 hover:bg-tiffany-cream/50 text-slate-700 border border-slate-200/50'
                              }`}
                            >
                              <span>{d.name}</span>
                              <span className="text-[10px] opacity-80">{d.voltage}</span>
                            </button>
                          ))}
                        </div>
                      </div>

                      <div className="md:col-span-2 bg-slate-50 p-6 rounded-xl border border-slate-200/40 space-y-4 flex flex-col justify-between">
                        <div className="space-y-4">
                          <div className="flex justify-between items-start">
                            <div>
                              <h5 className="font-serif font-bold text-slate-900 text-base">{plugData[selectedPlugCountry].name} 規格說明</h5>
                              <p className="text-xs text-slate-500 mt-1">電壓：{plugData[selectedPlugCountry].voltage} | 頻率：{plugData[selectedPlugCountry].freq}</p>
                            </div>
                            <div className="px-2.5 py-1 bg-white border border-tiffany-ice/60 rounded-md text-[10px] font-bold text-[#e63946]">
                              插頭形式：{plugData[selectedPlugCountry].plugs.join(', ')}
                            </div>
                          </div>

                          {/* 插頭插座形狀示意圖 (精緻 SVG) */}
                          <div className="h-28 bg-white border border-slate-200/40 rounded-xl flex items-center justify-center relative overflow-hidden">
                            <div className="absolute top-2 left-3 text-[9px] font-mono font-bold text-slate-400">插座孔洞形狀示意</div>
                            <svg width="80" height="80" viewBox="0 0 80 80" className="text-slate-400">
                              <rect x="10" y="10" width="60" height="60" rx="15" fill="#FAF9F6" stroke="#CDDBDB" strokeWidth="2" />
                              <circle cx="40" cy="40" r="24" fill="none" stroke="#EAEAEA" strokeWidth="1" strokeDasharray="3 3" />
                              <path d={plugData[selectedPlugCountry].shapeSvg} stroke="#213333" strokeWidth="6" strokeLinecap="round" />
                            </svg>
                          </div>

                          <div className="p-4 bg-tiffany-cream/40 border-l-2 border-[#e63946] rounded-r-lg">
                            <h6 className="text-xs font-bold text-slate-900 mb-1 flex items-center gap-1">
                              <Info size={12} className="text-[#e63946]" />
                              小編叮嚀
                            </h6>
                            <p className="text-xs text-slate-600 leading-relaxed font-sans">{plugData[selectedPlugCountry].tips}</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 2. 里程計算器 */}
                {page.id === 'miles-calculator' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Plane size={18} className="text-[#e63946]" />
                        航空公司哩程累積計算器
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">機票回饋極大化</span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div className="space-y-4">
                        <div className="space-y-1.5">
                          <label className="text-xs font-bold text-slate-500 block uppercase tracking-wider">飛行航線</label>
                          <select 
                            value={milesRoute}
                            onChange={(e) => setMilesRoute(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-lg p-2.5 text-xs font-bold focus:outline-none focus:border-[#e63946]"
                          >
                            {Object.entries(routeDistances).map(([k, v]) => (
                              <option key={k} value={k}>{v.label} (單程 {v.miles} 哩)</option>
                            ))}
                          </select>
                        </div>

                        <div className="space-y-1.5">
                          <label className="text-xs font-bold text-slate-500 block uppercase tracking-wider">子艙等 / 票等</label>
                          <select 
                            value={milesCabin}
                            onChange={(e) => setMilesCabin(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-lg p-2.5 text-xs font-bold focus:outline-none focus:border-[#e63946]"
                          >
                            {Object.entries(cabinMultipliers).map(([k, v]) => (
                              <option key={k} value={k}>{v.label}</option>
                            ))}
                          </select>
                        </div>

                        <div className="space-y-1.5">
                          <label className="text-xs font-bold text-slate-500 block uppercase tracking-wider">航空聯盟</label>
                          <div className="grid grid-cols-3 gap-2">
                            {[
                              { id: 'star', label: '星空聯盟', desc: '長榮、全日空、泰航' },
                              { id: 'skyteam', label: '天合聯盟', desc: '華航、大韓、越南航' },
                              { id: 'oneworld', label: '寰宇一家', desc: '星宇、國泰、日航' }
                            ].map((all) => (
                              <button
                                key={all.id}
                                onClick={() => setMilesAlliance(all.id)}
                                className={`p-2 rounded-lg text-left transition-all cursor-pointer ${
                                  milesAlliance === all.id 
                                    ? 'bg-slate-900 text-white' 
                                    : 'bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200/50'
                                }`}
                              >
                                <div className="text-[10px] font-bold">{all.label}</div>
                                <div className="text-[8px] opacity-70 mt-0.5 leading-tight">{all.desc}</div>
                              </button>
                            ))}
                          </div>
                        </div>
                      </div>

                      <div className="bg-[#FAFDFD] p-6 rounded-xl border border-tiffany-ice/50 flex flex-col justify-between">
                        <div className="space-y-4">
                          <div className="text-xs font-bold text-slate-500 uppercase tracking-widest">哩程計算結果</div>
                          
                          <div className="grid grid-cols-2 gap-4">
                            <div className="bg-white p-3 rounded-lg border border-slate-100 shadow-3xs">
                              <div className="text-[9px] text-slate-400 font-bold uppercase font-mono">單程可累積</div>
                              <div className="text-xl font-serif font-extrabold text-[#e63946] mt-1 font-mono">
                                {calculateEarnedMiles().oneway} <span className="text-xs font-sans font-bold text-slate-500">Miles</span>
                              </div>
                            </div>
                            <div className="bg-white p-3 rounded-lg border border-slate-100 shadow-3xs">
                              <div className="text-[9px] text-slate-400 font-bold uppercase font-mono">往返可累積</div>
                              <div className="text-xl font-serif font-extrabold text-[#e63946] mt-1 font-mono">
                                {calculateEarnedMiles().roundtrip} <span className="text-xs font-sans font-bold text-slate-500">Miles</span>
                              </div>
                            </div>
                          </div>

                          <div className="space-y-2 pt-2">
                            <div className="flex justify-between text-xs font-bold text-slate-600">
                              <span>距離免費兌換亞洲區間機票 (35,000哩) 還有：</span>
                              <span>{calculateEarnedMiles().percentOfFreeTicket}%</span>
                            </div>
                            <div className="w-full bg-slate-100 h-2 rounded-full overflow-hidden">
                              <div 
                                className="bg-[#e63946] h-full transition-all duration-500" 
                                style={{ width: `${Math.min(100, calculateEarnedMiles().percentOfFreeTicket)}%` }}
                              />
                            </div>
                          </div>
                        </div>

                        <div className="text-[10px] text-slate-500 font-mono leading-relaxed mt-4 border-t border-slate-100 pt-3">
                          *實際哩程可能依航空公司票務規定及票價等級有些微差異。一般機票促銷票累積率常為 50% 以下，購買時建議看清艙等代碼 (如 L, V, T 等)。
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 3. 退稅計算器 */}
                {page.id === 'tax-refund-calculator' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Coins size={18} className="text-[#e63946]" />
                        出國購物免稅退稅試算器
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">血拼省錢好幫手</span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div className="space-y-4">
                        <div className="space-y-1.5">
                          <label className="text-xs font-bold text-slate-500 block uppercase tracking-wider">選擇消費國家</label>
                          <select 
                            value={refundCountry}
                            onChange={(e) => setRefundCountry(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-lg p-2.5 text-xs font-bold focus:outline-none focus:border-[#e63946]"
                          >
                            {Object.entries(refundConfigs).map(([k, v]) => (
                              <option key={k} value={k}>{v.name} (稅率 {v.taxRate * 100}%)</option>
                            ))}
                          </select>
                        </div>

                        <div className="space-y-1.5">
                          <div className="flex justify-between text-xs font-bold text-slate-500">
                            <label className="uppercase tracking-wider">消費金額 ({refundConfigs[refundCountry].currency})</label>
                            <span className="font-mono">{refundAmount.toLocaleString()}</span>
                          </div>
                          <input 
                            type="range" 
                            min={refundConfigs[refundCountry].minSpend} 
                            max={refundCountry === 'JP' ? 300000 : refundCountry === 'KR' ? 2000000 : refundCountry === 'TH' ? 50000 : 3000} 
                            step={refundCountry === 'JP' ? 5000 : refundCountry === 'KR' ? 10000 : refundCountry === 'TH' ? 500 : 50}
                            value={refundAmount}
                            onChange={(e) => setRefundAmount(Number(e.target.value))}
                            className="w-full accent-[#e63946]"
                          />
                          <div className="flex justify-between text-[10px] text-slate-400 font-mono">
                            <span>門檻: {refundConfigs[refundCountry].minSpendLabel}</span>
                            <span>最大試算上限</span>
                          </div>
                        </div>

                        <div className="p-4 bg-tiffany-cream/40 rounded-xl text-xs space-y-1">
                          <span className="font-bold text-slate-900 block">💡 該國退稅政策核心</span>
                          <p className="text-slate-600 font-sans leading-relaxed">{refundConfigs[refundCountry].tips}</p>
                        </div>
                      </div>

                      <div className="bg-slate-50 p-6 rounded-xl border border-slate-200/40 flex flex-col justify-between">
                        <div className="space-y-4">
                          <span className="text-xs font-bold text-slate-500 tracking-widest uppercase block">退稅明細估計</span>
                          
                          <div className="space-y-2.5 font-mono text-xs border-b border-slate-200/50 pb-3">
                            <div className="flex justify-between">
                              <span className="text-slate-500">消費總額：</span>
                              <span className="font-bold">{refundAmount.toLocaleString()} {refundConfigs[refundCountry].currency}</span>
                            </div>
                            <div className="flex justify-between">
                              <span className="text-slate-500">應退稅金 ({refundConfigs[refundCountry].taxRate * 100}%)：</span>
                              <span className="text-slate-900 font-bold">+{calculateTaxRefund().rawTax.toLocaleString()} {refundConfigs[refundCountry].currency}</span>
                            </div>
                            <div className="flex justify-between">
                              <span className="text-slate-500">扣除手續費/級距差：</span>
                              <span className="text-red-500 font-bold">-{calculateTaxRefund().fee.toLocaleString()} {refundConfigs[refundCountry].currency}</span>
                            </div>
                          </div>

                          <div className="flex justify-between items-baseline pt-1">
                            <span className="text-xs font-bold text-slate-800">預估實際到手：</span>
                            <div className="text-right">
                              <div className="text-xl font-serif font-extrabold text-[#e63946] font-mono">
                                {calculateTaxRefund().actualRefund.toLocaleString()} {refundConfigs[refundCountry].currency}
                              </div>
                              <div className="text-[10px] font-sans font-bold text-slate-400 mt-1">
                                相當於約 <span className="text-slate-600 font-extrabold font-mono">NT$ {calculateTaxRefund().inTwd.toLocaleString()}</span>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div className="p-3 bg-[#FAFDFD] border border-tiffany-ice/60 rounded-lg text-[10px] text-slate-500 leading-relaxed mt-4">
                          *此計算結果僅為依據標準稅率之估算，實際退稅金額會受現場退稅代理公司（如 Global Blue、Planet 等）手續費規則及即時匯率影響。
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 4. 互動打包清單 */}
                {page.id === 'packing-list' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Check size={18} className="text-[#e63946]" />
                        出國行李互動打包檢查表
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">進度條百分百才安心</span>
                    </div>

                    <div className="space-y-4">
                      {/* 進度條 */}
                      <div className="bg-tiffany-cream/40 p-4 rounded-xl border border-tiffany-ice/30">
                        <div className="flex justify-between items-center text-xs font-bold text-slate-800 mb-2">
                          <span>打包進度：已收拾 {packedCount} / {totalPackingCount} 件物品</span>
                          <span className="text-[#e63946] text-sm font-mono">{packingPercent}%</span>
                        </div>
                        <div className="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden">
                          <div 
                            className="bg-[#e63946] h-full transition-all duration-300"
                            style={{ width: `${packingPercent}%` }}
                          />
                        </div>
                      </div>

                      {/* 勾選列表 */}
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 max-h-[300px] overflow-y-auto pr-2">
                        {packingItems.map((item) => (
                          <div 
                            key={item.id}
                            className={`flex items-center justify-between p-3 rounded-lg border transition-all cursor-pointer ${
                              item.checked 
                                ? 'bg-slate-50/50 border-slate-200/50 opacity-60' 
                                : 'bg-white border-slate-200 hover:border-[#e63946]/40 shadow-3xs'
                            }`}
                            onClick={() => togglePackingItem(item.id)}
                          >
                            <div className="flex items-center gap-3 min-w-0">
                              <div className={`w-4.5 h-4.5 rounded-md border flex items-center justify-center transition-all ${
                                item.checked ? 'bg-[#e63946] border-[#e63946] text-white' : 'border-slate-300'
                              }`}>
                                {item.checked && <Check size={12} strokeWidth={3} />}
                              </div>
                              <div className="flex flex-col min-w-0">
                                <span className="text-[9px] text-[#e63946] font-mono font-bold tracking-wider uppercase mb-0.5">{item.category}</span>
                                <span className={`text-xs font-medium text-slate-800 truncate ${item.checked ? 'line-through text-slate-400' : ''}`}>
                                  {item.text}
                                </span>
                              </div>
                            </div>
                            <button 
                              onClick={(e) => {
                                e.stopPropagation();
                                deletePackingItem(item.id);
                              }}
                              className="text-slate-300 hover:text-red-500 p-1.5 transition-colors"
                            >
                              <Trash2 size={13} />
                            </button>
                          </div>
                        ))}
                      </div>

                      {/* 新增打包項目 */}
                      <div className="grid grid-cols-1 md:grid-cols-12 gap-2 pt-3 border-t border-slate-100">
                        <div className="md:col-span-6">
                          <input 
                            type="text" 
                            placeholder="輸入自訂想打包的物品..."
                            value={newPackingText}
                            onChange={(e) => setNewPackingText(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-lg px-3 py-2 text-xs font-semibold focus:outline-none focus:border-[#e63946]"
                            onKeyDown={(e) => e.key === 'Enter' && addPackingItem()}
                          />
                        </div>
                        <div className="md:col-span-4">
                          <select 
                            value={newPackingCat}
                            onChange={(e) => setNewPackingCat(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-lg px-3 py-2 text-xs font-semibold focus:outline-none focus:border-[#e63946]"
                          >
                            <option value="證件檔案">📁 證件檔案</option>
                            <option value="電子通訊">🔌 電子通訊</option>
                            <option value="衣物鞋履">🧥 衣物鞋履</option>
                            <option value="日常備藥">💊 日常備藥</option>
                            <option value="盥洗美妝">🧴 盥洗美妝</option>
                          </select>
                        </div>
                        <div className="md:col-span-2">
                          <button 
                            onClick={addPackingItem}
                            className="w-full h-full bg-[#e63946] hover:bg-[#C1121F] text-white rounded-lg text-xs font-bold transition-all flex items-center justify-center gap-1 py-2 cursor-pointer"
                          >
                            <Plus size={14} /> 新增
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 5. eSIM 比較推薦 */}
                {page.id === 'esim-comparison' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Globe size={18} className="text-[#e63946]" />
                        主要目的地 eSIM 實測資費比較
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">免插卡・掃碼極速上網</span>
                    </div>

                    <div className="space-y-4">
                      <div className="flex flex-wrap justify-between items-center gap-4 bg-slate-50 p-4 rounded-xl">
                        <div className="flex items-center gap-3">
                          <span className="text-xs font-bold text-slate-500">目的地國家：</span>
                          <div className="flex gap-1.5">
                            {['JP', 'KR', 'TH'].map((c) => (
                              <button
                                key={c}
                                onClick={() => setEsimCountry(c)}
                                className={`px-3 py-1.5 rounded-md text-xs font-bold transition-all cursor-pointer ${
                                  esimCountry === c 
                                    ? 'bg-[#e63946] text-white' 
                                    : 'bg-white hover:bg-slate-100 text-slate-700 border border-slate-200/50'
                                }`}
                              >
                                {c === 'JP' ? '日本' : c === 'KR' ? '韓國' : '泰國'}
                              </button>
                            ))}
                          </div>
                        </div>

                        <div className="flex items-center gap-3">
                          <span className="text-xs font-bold text-slate-500">使用天數：</span>
                          <div className="flex gap-1.5">
                            {[3, 5, 7, 10].map((d) => (
                              <button
                                key={d}
                                onClick={() => setEsimDays(d)}
                                className={`w-8 h-8 rounded-full text-xs font-mono font-bold flex items-center justify-center transition-all cursor-pointer ${
                                  esimDays === d 
                                    ? 'bg-slate-900 text-white' 
                                    : 'bg-white hover:bg-slate-100 text-slate-700 border border-slate-200/50'
                                }`}
                              >
                                {d}
                              </button>
                            ))}
                          </div>
                        </div>
                      </div>

                      {/* 比較表格 */}
                      <div className="space-y-3">
                        {esimPlans.map((plan) => (
                          <div 
                            key={plan.id}
                            className="bg-white border border-slate-200/60 p-4 rounded-xl hover:border-[#e63946]/50 hover:shadow-2xs transition-all flex flex-col md:flex-row md:items-center justify-between gap-4"
                          >
                            <div className="space-y-1.5">
                              <div className="flex items-center gap-2">
                                <span className="font-serif font-bold text-slate-900 text-sm">{plan.name}</span>
                                {plan.tags.map((t, i) => (
                                  <span key={i} className={`px-2 py-0.5 rounded text-[8px] font-bold ${
                                    t === '極力推薦' ? 'bg-[#e63946]/10 text-[#e63946]' : 'bg-slate-100 text-slate-500'
                                  }`}>
                                    {t}
                                  </span>
                                ))}
                              </div>
                              <div className="flex flex-wrap gap-x-4 gap-y-1 text-xs text-slate-500 font-sans">
                                <span>網絡：{plan.carrier}</span>
                                <span className="w-px h-3.5 bg-slate-200 self-center hidden sm:inline" />
                                <span>限速：{plan.unlimited ? '不降速無限流量' : plan.limit}</span>
                                <span className="w-px h-3.5 bg-slate-200 self-center hidden sm:inline" />
                                <span>速度滿意度：★ {plan.rating}</span>
                              </div>
                            </div>

                            <div className="flex items-center justify-between md:justify-end gap-6 border-t md:border-t-0 pt-2.5 md:pt-0">
                              <div className="text-left md:text-right">
                                <div className="text-xs text-slate-400 font-bold">預估 {esimDays} 天總價</div>
                                <div className="text-base font-serif font-extrabold text-[#e63946] font-mono mt-0.5">
                                  NT$ {plan.pricePerDay * esimDays}
                                </div>
                              </div>
                              <button className="px-4 py-2 bg-[#e63946] hover:bg-[#C1121F] text-white rounded-lg text-xs font-bold transition-all cursor-pointer">
                                立即申辦
                              </button>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}

                {/* 6. Notion 旅遊模板 */}
                {page.id === 'notion-travel-template' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Layers size={18} className="text-[#e63946]" />
                        高顏值精緻 Notion 行程規劃模板
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">一鍵複製・完美排程</span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
                      <div className="space-y-4">
                        <span className="px-3 py-1 bg-[#e63946]/10 text-[#e63946] text-[10px] font-extrabold tracking-wider uppercase rounded-full">
                          讀者專屬・完全免費
                        </span>
                        <h5 className="font-serif font-extrabold text-slate-900 text-base leading-relaxed">
                          「均在路上 Travel Lab — 極致美學日程規劃盤」
                        </h5>
                        <p className="text-xs text-slate-600 leading-relaxed font-sans">
                          我們將多年旅行規劃的心血提煉成這套兼具美學與實用性的 Notion 模板。
                          整合了看板日曆、預算記帳、景點收藏卡、打卡美食清單與打包進度器，助您輕鬆管理下一次慢旅。
                        </p>

                        <div className="space-y-2">
                          <div className="flex items-center gap-2 text-xs text-slate-700 font-bold">
                            <Check size={14} className="text-[#e63946]" />
                            <span>自動化預算看板 (輸入即時算出旅費分配)</span>
                          </div>
                          <div className="flex items-center gap-2 text-xs text-slate-700 font-bold">
                            <Check size={14} className="text-[#e63946]" />
                            <span>精美卡片式景點地圖 (直接嵌入 Google Map)</span>
                          </div>
                          <div className="flex items-center gap-2 text-xs text-slate-700 font-bold">
                            <Check size={14} className="text-[#e63946]" />
                            <span>手機完美適配佈局 (出行在路上一目了然)</span>
                          </div>
                        </div>

                        <button 
                          onClick={handleCopyLink}
                          className="w-full md:w-auto px-6 py-3 bg-[#e63946] hover:bg-[#C1121F] text-white text-xs font-bold tracking-widest uppercase rounded-xl transition-all duration-300 flex items-center justify-center gap-2 cursor-pointer shadow-sm"
                        >
                          {copiedLink ? '模板連結已複製！' : '一鍵複製 Notion 模板連結'}
                          <ExternalLink size={14} />
                        </button>
                      </div>

                      <div className="relative rounded-2xl overflow-hidden border border-slate-200/50 shadow-sm bg-slate-100 p-2">
                        <img 
                          src="/images/notion-travel.webp" 
                          alt="Notion Template Mockup"
                          className="rounded-xl w-full object-cover h-64"
                        />
                        <div className="absolute inset-0 bg-slate-900/30 flex items-center justify-center">
                          <span className="px-4 py-2 bg-white/90 backdrop-blur-md text-slate-900 font-serif font-extrabold text-xs rounded-full shadow-lg">
                            美學規劃盤・預覽
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 7. 旅遊工具合集主頁 */}
                {page.id === 'travel-tools' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg">
                        均在路上 旅遊工具箱
                      </h4>
                      <p className="text-xs text-slate-500 mt-1">
                        點擊下方任意卡片，即刻在本頁頂部切換加載對應的智能讀者交互工具：
                      </p>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {[
                        { id: 'power-plug-guide', name: '插座電壓規格查詢', desc: '快速比對日韓、東南亞各國電壓與插孔形式', tags: ['安全必備'] },
                        { id: 'miles-calculator', name: '里程回饋計算器', desc: '手把手教您累積三大航空聯盟機票里數', tags: ['理財精省'] },
                        { id: 'tax-refund-calculator', name: '各國購物退稅試算', desc: '一鍵得出日、韓、泰等國實退金額與手續費', tags: ['血拼省錢'] },
                        { id: 'packing-list', name: '行李智能打包檢查', desc: '互動式行李勾選單，進度條一目了然', tags: ['收拾行李'] },
                        { id: 'esim-comparison', name: 'eSIM 實測資費評比', desc: '對比網速、無限流量及各天數最佳方案', tags: ['網絡通訊'] },
                        { id: 'notion-travel-template', name: 'Notion 美學日程盤', desc: '完全免費複製的精美看板行程規劃器', tags: ['高顏值規畫'] }
                      ].map((tool) => (
                        <div 
                          key={tool.id}
                          className="bg-slate-50 hover:bg-tiffany-cream/40 border border-slate-200/50 p-4 rounded-xl transition-all duration-300 flex flex-col justify-between"
                        >
                          <div className="space-y-1">
                            <div className="flex justify-between items-start">
                              <span className="font-serif font-extrabold text-slate-900 text-sm">{tool.name}</span>
                              <span className="px-2 py-0.5 bg-white border border-slate-200 rounded text-[8px] font-bold text-slate-500">{tool.tags[0]}</span>
                            </div>
                            <p className="text-xs text-slate-500 font-sans leading-relaxed">{tool.desc}</p>
                          </div>
                          
                          <div className="border-t border-slate-100 mt-3 pt-2 text-right">
                            <span className="text-[10px] font-bold text-[#e63946] group-hover:text-[#C1121F] inline-flex items-center gap-1">
                              使用此工具 <ArrowRight size={10} />
                            </span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* 8. 東京住宿推薦互動卡 */}
                {page.id === 'tokyo-accommodation' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Hotel size={18} className="text-[#e63946]" />
                        東京熱門區域住宿評級查詢
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">分區避坑指南</span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                      <div className="md:col-span-1 space-y-2">
                        {Object.entries(tokyoAreas).map(([k, v]) => (
                          <button
                            key={k}
                            onClick={() => setSelectedTokyoArea(k)}
                            className={`w-full text-left px-4 py-2.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                              selectedTokyoArea === k 
                                ? 'bg-[#e63946] text-white shadow-xs' 
                                : 'bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200/50'
                            }`}
                          >
                            {v.name}
                          </button>
                        ))}
                      </div>

                      <div className="md:col-span-2 bg-slate-50 p-5 rounded-xl border border-slate-200/40 space-y-4">
                        <div className="flex justify-between items-start border-b border-slate-200/30 pb-3">
                          <h5 className="font-serif font-bold text-slate-900 text-base">{tokyoAreas[selectedTokyoArea].name} 分析</h5>
                          <span className="px-2 py-1 bg-white border border-slate-200 rounded text-[9px] font-bold text-[#e63946]">推薦入住</span>
                        </div>

                        <div className="grid grid-cols-2 gap-3 text-xs font-sans">
                          <div>
                            <span className="text-slate-400 font-bold block">消費預算：</span>
                            <span className="font-mono text-slate-800 font-bold">{tokyoAreas[selectedTokyoArea].budget}</span>
                          </div>
                          <div>
                            <span className="text-slate-400 font-bold block">交通樞紐度：</span>
                            <span className="font-mono text-slate-800 font-bold">{tokyoAreas[selectedTokyoArea].train}</span>
                          </div>
                        </div>

                        <div className="space-y-2 text-xs font-sans">
                          <p className="text-slate-700 leading-relaxed"><strong className="text-green-600 font-bold">✔️ 優點：</strong>{tokyoAreas[selectedTokyoArea].pros}</p>
                          <p className="text-slate-700 leading-relaxed"><strong className="text-red-500 font-bold">❌ 缺點：</strong>{tokyoAreas[selectedTokyoArea].cons}</p>
                        </div>

                        <div className="pt-3 border-t border-slate-200/30">
                          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-widest block mb-2">精選推薦飯店（讀者特惠）</span>
                          <ul className="text-xs space-y-1.5 font-mono text-slate-800 list-inside list-disc">
                            {tokyoAreas[selectedTokyoArea].recommendHotels.map((h, i) => (
                              <li key={i}>{h}</li>
                            ))}
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 9. 日本藥妝勾選與優惠券 */}
                {page.id === 'japan-drugstore-checklist' && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Store size={18} className="text-[#e63946]" />
                        最新日本藥妝人氣清單勾選簿
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">買對不買貴</span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div className="space-y-3">
                        <span className="text-xs font-bold text-slate-400 tracking-widest uppercase block">必買藥品美妝列表</span>
                        {drugstoreProducts.map((p) => (
                          <div 
                            key={p.id}
                            onClick={() => toggleDrugstoreCart(p.id)}
                            className={`p-3.5 rounded-xl border transition-all cursor-pointer flex justify-between items-center ${
                              drugstoreCart[p.id] 
                                ? 'bg-tiffany-cream/40 border-[#e63946]' 
                                : 'bg-white border-slate-200 hover:border-slate-300'
                            }`}
                          >
                            <div className="space-y-1">
                              <span className="font-serif font-extrabold text-slate-900 text-xs flex items-center gap-1.5">
                                <div className={`w-3.5 h-3.5 rounded border flex items-center justify-center ${drugstoreCart[p.id] ? 'bg-[#e63946] border-[#e63946] text-white' : 'border-slate-300'}`}>
                                  {drugstoreCart[p.id] && <Check size={10} />}
                                </div>
                                {p.name}
                              </span>
                              <p className="text-[10px] text-slate-500 font-sans leading-relaxed">{p.desc}</p>
                            </div>
                            <div className="text-right shrink-0">
                              <span className="text-[11px] text-slate-800 font-mono font-bold block">{p.price}</span>
                              <span className="text-[9px] text-[#e63946] font-sans font-bold block">{p.localPrice}</span>
                            </div>
                          </div>
                        ))}
                      </div>

                      {/* 優惠券區域 */}
                      <div className="bg-slate-900 text-slate-100 p-6 rounded-2xl border border-slate-800 relative overflow-hidden flex flex-col justify-between">
                        <div className="absolute top-0 right-0 w-24 h-24 bg-[#e63946]/10 rounded-full blur-2xl pointer-events-none" />
                        
                        <div className="space-y-4">
                          <div className="flex justify-between items-center border-b border-slate-800 pb-3">
                            <div>
                              <span className="text-[#e63946] text-[9px] font-mono font-bold tracking-widest uppercase">松本清 / 大國藥妝</span>
                              <h5 className="font-serif font-extrabold text-white text-base mt-0.5">讀者專屬免稅折扣券</h5>
                            </div>
                            <span className="px-2 py-0.5 bg-red-500 text-white text-[8px] font-bold rounded">2026 最新</span>
                          </div>

                          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 flex justify-between items-center text-center">
                            <div>
                              <div className="text-[9px] text-slate-400 font-mono">免稅</div>
                              <div className="text-xl font-serif font-extrabold text-[#e63946] font-mono">10%</div>
                            </div>
                            <div className="text-slate-700 font-mono text-xl">X</div>
                            <div>
                              <div className="text-[9px] text-slate-400 font-mono">店內加碼</div>
                              <div className="text-xl font-serif font-extrabold text-white font-mono">5% ~ 7%</div>
                            </div>
                          </div>

                          <p className="text-[10px] text-slate-400 leading-relaxed font-sans">
                            *使用說明：於結帳前出示此條碼，購買含稅滿 10,000 日圓，即可享有 10% 免稅 + 5% 折扣；滿 30,000 日圓可享 10% 免稅 + 7% 折扣！
                          </p>
                        </div>

                        <button 
                          onClick={handleCopyLink}
                          className="w-full bg-[#e63946] hover:bg-[#C1121F] text-white rounded-lg py-2.5 text-xs font-bold transition-all duration-300 mt-4 flex items-center justify-center gap-1.5 cursor-pointer"
                        >
                          <Camera size={14} /> 點擊下載條碼圖片
                        </button>
                      </div>
                    </div>
                  </div>
                )}

                {/* 10. 預算試算動態工具 (japan-budget-guide 和 korea-budget 共享) */}
                {(page.id === 'japan-budget-guide' || page.id === 'korea-budget') && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                    <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                      <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                        <Coins size={18} className="text-[#e63946]" />
                        個人化旅行預算動態計算器
                      </h4>
                      <span className="text-[10px] font-mono text-slate-400">掌握每一分支出</span>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div className="space-y-4">
                        <div className="space-y-1.5">
                          <div className="flex justify-between text-xs font-bold text-slate-500">
                            <label className="uppercase tracking-wider">旅行天數</label>
                            <span className="font-mono text-slate-900 font-bold">{budgetDays} 天</span>
                          </div>
                          <input 
                            type="range" min={2} max={15} value={budgetDays}
                            onChange={(e) => setBudgetDays(Number(e.target.value))}
                            className="w-full accent-[#e63946]"
                          />
                        </div>

                        <div className="space-y-1.5">
                          <div className="flex justify-between text-xs font-bold text-slate-500">
                            <label className="uppercase tracking-wider">往返機票預算 (TWD)</label>
                            <span className="font-mono text-[#e63946] font-bold">NT$ {budgetFlight.toLocaleString()}</span>
                          </div>
                          <input 
                            type="range" min={4000} max={30000} step={500} value={budgetFlight}
                            onChange={(e) => setBudgetFlight(Number(e.target.value))}
                            className="w-full accent-[#e63946]"
                          />
                        </div>

                        <div className="space-y-1.5">
                          <div className="flex justify-between text-xs font-bold text-slate-500">
                            <label className="uppercase tracking-wider">每日住宿預算 (TWD / 房)</label>
                            <span className="font-mono text-[#e63946] font-bold">NT$ {budgetHotel.toLocaleString()}</span>
                          </div>
                          <input 
                            type="range" min={1000} max={10000} step={200} value={budgetHotel}
                            onChange={(e) => setBudgetHotel(Number(e.target.value))}
                            className="w-full accent-[#e63946]"
                          />
                        </div>

                        <div className="space-y-1.5">
                          <div className="flex justify-between text-xs font-bold text-slate-500">
                            <label className="uppercase tracking-wider">每日餐飲與交通 (TWD / 人)</label>
                            <span className="font-mono text-[#e63946] font-bold">NT$ {budgetFood.toLocaleString()}</span>
                          </div>
                          <input 
                            type="range" min={500} max={5000} step={100} value={budgetFood}
                            onChange={(e) => setBudgetFood(Number(e.target.value))}
                            className="w-full accent-[#e63946]"
                          />
                        </div>

                        <div className="space-y-1.5">
                          <div className="flex justify-between text-xs font-bold text-slate-500">
                            <label className="uppercase tracking-wider">預估購物/伴手禮/娛樂 (TWD)</label>
                            <span className="font-mono text-[#e63946] font-bold">NT$ {budgetShopping.toLocaleString()}</span>
                          </div>
                          <input 
                            type="range" min={0} max={50000} step={1000} value={budgetShopping}
                            onChange={(e) => setBudgetShopping(Number(e.target.value))}
                            className="w-full accent-[#e63946]"
                          />
                        </div>
                      </div>

                      <div className="bg-[#FAFDFD] p-6 rounded-xl border border-tiffany-ice/50 flex flex-col justify-between">
                        <div className="space-y-5">
                          <span className="text-xs font-bold text-slate-500 tracking-widest uppercase block">總預算分攤圖估算</span>
                          
                          <div className="text-center py-4 bg-white rounded-xl border border-slate-200/30">
                            <div className="text-[10px] text-slate-400 font-bold uppercase tracking-widest">預估旅行總支出</div>
                            <div className="text-3xl font-serif font-extrabold text-slate-900 mt-1 font-mono">
                              NT$ {calcTotalBudget().toLocaleString()}
                            </div>
                            <span className="text-[9px] text-[#e63946] font-bold block mt-1">人均預算試算結果</span>
                          </div>

                          {/* 預算分配進度條拼裝 */}
                          <div className="space-y-3 pt-2">
                            <div className="text-xs font-bold text-slate-500">分配比例分解</div>
                            <div className="space-y-2">
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">1. 往返機票：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {budgetFlight.toLocaleString()} ({Math.round(budgetFlight/calcTotalBudget()*100)}%)</span>
                              </div>
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">2. 住宿天數總計：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {(budgetHotel*budgetDays).toLocaleString()} ({Math.round((budgetHotel*budgetDays)/calcTotalBudget()*100)}%)</span>
                              </div>
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">3. 餐飲交通小計：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {(budgetFood*budgetDays).toLocaleString()} ({Math.round((budgetFood*budgetDays)/calcTotalBudget()*100)}%)</span>
                              </div>
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">4. 娛樂與血拼：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {budgetShopping.toLocaleString()} ({Math.round(budgetShopping/calcTotalBudget()*100)}%)</span>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div className="text-[9px] text-slate-400 leading-relaxed font-mono mt-4 border-t border-slate-100 pt-3">
                          *此為一般個人旅行預估。若為賞櫻/紅葉旺季、跨國假期、寒暑假，機票及住宿預算通常需額外加成 20% - 50%。
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* 11. 墾丁 3天2夜專屬互動工具區 */}
                {page.id === 'kenting' && (
                  <div className="space-y-6">
                    {/* 頂部引言與圖片展示區 */}
                    <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs">
                      <div className="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
                        <div className="md:col-span-7 space-y-4">
                          <span className="px-2.5 py-1 bg-[#e63946]/10 text-[#e63946] border border-[#e63946]/20 rounded-full text-[10px] font-bold tracking-widest uppercase inline-block">
                            慢旅特別提案
                          </span>
                          <h4 className="font-serif font-extrabold text-slate-900 text-2xl">
                            墾丁三天兩夜「慢活避暑」完美手冊
                          </h4>
                          <p className="text-xs text-slate-600 leading-relaxed">
                            這份日程是針對想要避開大眾旅行團、享受真正純淨碧海與幽靜夜景的慢遊者所設計。
                            透過下方工具，您可以自訂交通與享樂清單，即刻運算出您的個人化旅行預算！
                          </p>
                          <div className="grid grid-cols-2 gap-3 pt-2">
                            <div className="bg-slate-50 p-3 rounded-xl border border-slate-100 flex items-center gap-2.5">
                              <Clock size={16} className="text-[#e63946]" />
                              <div>
                                <div className="text-[10px] text-slate-400 font-bold uppercase">建議天數</div>
                                <div className="text-xs font-bold text-slate-800">3 天 2 夜 (慢享型)</div>
                              </div>
                            </div>
                            <div className="bg-slate-50 p-3 rounded-xl border border-slate-100 flex items-center gap-2.5">
                              <Compass size={16} className="text-[#e63946]" />
                              <div>
                                <div className="text-[10px] text-slate-400 font-bold uppercase">主打體驗</div>
                                <div className="text-xs font-bold text-slate-800">水上活動、落日與夜市</div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div className="md:col-span-5">
                          <div className="relative rounded-xl overflow-hidden border border-slate-200 shadow-sm aspect-3/4">
                            <img 
                              src="/images/kenting_nanwan.jpg" 
                              alt="墾丁蔚藍海岸" 
                              className="w-full h-full object-cover"
                              referrerPolicy="no-referrer"
                            />
                            <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent p-3 text-white text-center">
                              <span className="text-[10px] tracking-wider uppercase font-bold text-tiffany-cream">實地探訪拍攝 ‧ 慢旅實驗室</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* 3天2夜動態行程看板 */}
                    <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-4">
                      <div className="flex justify-between items-center border-b border-slate-100 pb-3">
                        <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                          <Calendar size={18} className="text-[#e63946]" />
                          三天兩夜「精選行程」數位看板
                        </h4>
                        <span className="text-[10px] font-mono text-slate-400">點擊切換每日攻略</span>
                      </div>

                      {/* 每日切換 Tab */}
                      <div className="flex gap-2">
                        {[1, 2, 3].map(dayNum => (
                          <button
                            key={dayNum}
                            onClick={() => setKentingDay(dayNum)}
                            className={`flex-1 py-2.5 rounded-lg text-xs font-bold transition-all duration-300 cursor-pointer ${
                              kentingDay === dayNum
                                ? 'bg-[#e63946] text-white shadow-xs'
                                : 'bg-slate-50 hover:bg-slate-100 text-slate-600 border border-slate-200/40'
                            }`}
                          >
                            第 {dayNum} 天 · {dayNum === 1 ? '海岸線初探' : dayNum === 2 ? '貝殼秘境與落日' : '生態森林與古城'}
                          </button>
                        ))}
                      </div>

                      {/* 每日詳細 Timeline */}
                      <div className="bg-slate-50 p-4 rounded-xl border border-slate-200/35 space-y-4">
                        {kentingDay === 1 && (
                          <div className="space-y-4">
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">1</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  10:00 抵達恆春/墾丁 <span className="text-[9px] px-1.5 py-0.5 bg-green-50 text-green-600 rounded">起點</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">抵達民宿辦理行李寄存，在蔚藍晴空與南國椰林的迎風搖曳中，感受國境之南的慵懶海風。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">2</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  13:00 南灣沙灘戲水、水上運動 <span className="text-[9px] px-1.5 py-0.5 bg-[#e63946]/10 text-[#e63946] rounded">熱門</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">租一把洋傘躺在細沙上，或是立刻穿上救生衣，體驗浮潛、香蕉船、水上摩托車狂飆，享受巴士海峽的澄澈洗禮。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">3</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  15:30 鵝鑾鼻燈塔 <span className="text-[9px] px-1.5 py-0.5 bg-yellow-50 text-yellow-700 rounded">地標</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">造訪全台光力最強、歷史悠久的圓形白鐵塔。在寬闊無垠的大片綠地上與燈塔留影，眺望巴士海峽與太平洋的洶湧交會。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">4</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  17:00 龍磐草原崩崖景觀 <span className="text-[9px] px-1.5 py-0.5 bg-purple-50 text-purple-700 rounded">奇觀</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">沿著東海岸騎往龍磐，這裡的石灰岩台地因經年雨水溶蝕，形成令人震撼的崩崖與裂溝，海天一色無邊際，入夜後是全台最佳觀星點。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-slate-900 text-white flex items-center justify-center text-[10px] font-bold">5</div>
                              </div>
                              <div className="flex-1">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  19:00 墾丁大街夜市與露天小酌 <span className="text-[9px] px-1.5 py-0.5 bg-red-50 text-red-600 rounded">美食</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">傍晚大街封街成為一整條夜市，必嚐炭烤魷魚、原住民石板烤肉、山豬肉香腸，隨後挑一間美式露天酒吧，聽著輕快旋律享受南國微醺之夜。</p>
                              </div>
                            </div>
                          </div>
                        )}

                        {kentingDay === 2 && (
                          <div className="space-y-4">
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">1</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  09:30 砂島貝殼砂展示館 <span className="text-[9px] px-1.5 py-0.5 bg-blue-50 text-blue-600 rounded">生態</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">砂島是墾丁最為純淨的珊瑚礁岩小海灣，其沙灘由高比例的貝殼、珊瑚與孔蟲碎屑組成。在木棧道上凝望純淨如冰的牛奶色淺灘，極其療癒。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">2</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  11:30 後壁湖平價生魚片狂嗑 <span className="text-[9px] px-1.5 py-0.5 bg-orange-50 text-orange-600 rounded">必吃</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">直奔後壁湖觀光漁港。這裡的海產店物美價廉，爆量肥美厚切鮭魚刺身一大盤（20片）只要 NT$ 100-200！搭配海膽、現炒時蔬與雨來菇，誠意滿滿。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">3</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  14:30 白沙灣《少年 Pi》海灘散步 <span className="text-[9px] px-1.5 py-0.5 bg-teal-50 text-teal-700 rounded">電影</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">細緻柔滑的白砂海灣，是李安導演《少年 PI 的奇幻漂流》中理查帕克老虎上岸的終點。在這裡踏浪嬉戲，踩著柔軟細砂，體驗不受打擾的午後時光。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-slate-900 text-white flex items-center justify-center text-[10px] font-bold">4</div>
                              </div>
                              <div className="flex-1">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  17:00 關山高地觀世界級夕陽 <span className="text-[9px] px-1.5 py-0.5 bg-rose-50 text-rose-600 rounded">奇蹟</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">關山曾被 CNN 評選為「全球十二大最美落日」之一。登上高處俯瞰，看著金黃而巨大的太陽缓缓沉入巴士海峽，將整片天空與汪洋渲染得一片火紅，壯美難忘。</p>
                              </div>
                            </div>
                          </div>
                        )}

                        {kentingDay === 3 && (
                          <div className="space-y-4">
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">1</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  08:30 社頂自然公園生態芬多精 <span className="text-[9px] px-1.5 py-0.5 bg-emerald-50 text-emerald-600 rounded">生態</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">社頂公園擁有鬼斧神工的石灰岩大峽谷、一線天、以及古老的礁岩林。清晨涼爽時漫步步道，享受天然森林浴，幸運的話還能看到野生梅花鹿。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-[#e63946]/20 text-[#e63946] flex items-center justify-center text-[10px] font-bold">2</div>
                                <div className="w-0.5 h-12 bg-slate-200"></div>
                              </div>
                              <div className="flex-1 pb-2">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  11:30 恆春古城散策與品嚐阿伯綠豆蒜 <span className="text-[9px] px-1.5 py-0.5 bg-amber-50 text-amber-700 rounded">古早味</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">探訪保留完善的百年城門牆。中午來到老街點一碗去殼綠豆精心熬煮、佐以黑糖刨冰、粉條與綠豆饌的「阿伯綠豆蒜」，冰涼消暑，滋味甘甜。</p>
                              </div>
                            </div>
                            <div className="flex gap-3">
                              <div className="flex flex-col items-center">
                                <div className="w-5 h-5 rounded-full bg-slate-900 text-white flex items-center justify-center text-[10px] font-bold">3</div>
                              </div>
                              <div className="flex-1">
                                <h5 className="text-xs font-bold text-slate-900 flex items-center gap-1.5">
                                  14:00 啟程返回高雄/溫馨歸途 <span className="text-[9px] px-1.5 py-0.5 bg-slate-100 text-slate-600 rounded">回程</span>
                                </h5>
                                <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">收拾滿滿的日光能量、伴手禮（如洋蔥餅、綠豆蒜）與蔚藍回憶，搭乘墾丁快線直達高鐵左營站，結束慢旅行程。</p>
                              </div>
                            </div>
                          </div>
                        )}
                      </div>
                    </div>

                    {/* 墾丁個人專屬預算精算器 */}
                    <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                      <div className="flex justify-between items-center border-b border-slate-100 pb-4">
                        <h4 className="font-serif font-extrabold text-slate-900 text-lg flex items-center gap-2">
                          <Coins size={18} className="text-[#e63946]" />
                          墾丁自主小資「預算精算器」
                        </h4>
                        <span className="text-[10px] font-mono text-slate-400">自訂天數與享樂</span>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {/* 左側選單 */}
                        <div className="space-y-4">
                          {/* 交通型態 */}
                          <div className="space-y-1.5">
                            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block">島上交通型態</label>
                            <div className="grid grid-cols-2 gap-2">
                              {[
                                { id: 'scooter', label: '重型機車 (NT$450/天)', desc: '機動靈活' },
                                { id: 'electric', label: '電動機車 (NT$550/天)', desc: '免駕照首選' },
                                { id: 'car', label: '自駕汽車 (NT$1800/天)', desc: '風雨無阻' },
                                { id: 'charter', label: '舒適包車 (NT$3500/次)', desc: '免動腦最輕鬆' }
                              ].map(item => (
                                <button
                                  key={item.id}
                                  onClick={() => setKentingTransport(item.id)}
                                  className={`p-2.5 rounded-lg border text-left transition-all cursor-pointer ${
                                    kentingTransport === item.id
                                      ? 'border-[#e63946] bg-[#e63946]/5 text-slate-900'
                                      : 'border-slate-200 hover:border-slate-300 text-slate-600'
                                  }`}
                                >
                                  <div className="text-xs font-bold flex items-center gap-1">
                                    {kentingTransport === item.id && <Check size={12} className="text-[#e63946]" />}
                                    {item.label}
                                  </div>
                                  <div className="text-[9px] text-slate-400 mt-0.5">{item.desc}</div>
                                </button>
                              ))}
                            </div>
                          </div>

                          {/* 住宿等級 */}
                          <div className="space-y-1.5">
                            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block">住宿奢華程度 (雙人分攤計)</label>
                            <div className="grid grid-cols-3 gap-2">
                              {[
                                { id: 'hostel', label: '背包客棧', price: 'NT$500/晚' },
                                { id: 'homestay', label: '標準民宿', price: 'NT$1800/晚' },
                                { id: 'seaview', label: '奢華海景房', price: 'NT$3500/晚' }
                              ].map(item => (
                                <button
                                  key={item.id}
                                  onClick={() => setKentingStay(item.id)}
                                  className={`p-2 rounded-lg border text-left transition-all cursor-pointer ${
                                    kentingStay === item.id
                                      ? 'border-[#e63946] bg-[#e63946]/5 text-slate-900'
                                      : 'border-slate-200 hover:border-slate-300 text-slate-600'
                                  }`}
                                >
                                  <div className="text-xs font-bold flex items-center gap-1">
                                    {kentingStay === item.id && <Check size={10} className="text-[#e63946]" />}
                                    {item.label}
                                  </div>
                                  <div className="text-[9px] text-slate-400 mt-0.5">{item.price}</div>
                                </button>
                              ))}
                            </div>
                          </div>

                          {/* 每日餐飲 */}
                          <div className="space-y-1.5">
                            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block">餐飲享樂級距</label>
                            <div className="grid grid-cols-3 gap-2">
                              {[
                                { id: 'budget', label: '在地小吃/夜市', price: 'NT$400/天' },
                                { id: 'standard', label: '海鮮大餐+熱炒', price: 'NT$700/天' },
                                { id: 'luxury', label: '海景酒吧+大餐', price: 'NT$1500/天' }
                              ].map(item => (
                                <button
                                  key={item.id}
                                  onClick={() => setKentingFood(item.id)}
                                  className={`p-2 rounded-lg border text-left transition-all cursor-pointer ${
                                    kentingFood === item.id
                                      ? 'border-[#e63946] bg-[#e63946]/5 text-slate-900'
                                      : 'border-slate-200 hover:border-slate-300 text-slate-600'
                                  }`}
                                >
                                  <div className="text-xs font-bold flex items-center gap-1">
                                    {kentingFood === item.id && <Check size={10} className="text-[#e63946]" />}
                                    {item.label}
                                  </div>
                                  <div className="text-[9px] text-slate-400 mt-0.5">{item.price}</div>
                                </button>
                              ))}
                            </div>
                          </div>

                          {/* 水上活動加購 */}
                          <div className="space-y-1.5">
                            <label className="text-xs font-bold text-slate-500 uppercase tracking-wider block">水上娛樂活動 (可複選)</label>
                            <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
                              {[
                                { id: 'snorkeling', label: '後壁湖浮潛 (NT$350)', desc: '珊瑚小魚' },
                                { id: 'jetski', label: '水上摩托車 (NT$500)', desc: '極速尖叫' },
                                { id: 'bananaboat', label: '香蕉船 (NT$300)', desc: '團體甩尾' },
                                { id: 'sup', label: 'SUP立槳 (NT$1000)', desc: '優雅漂流' },
                                { id: 'parasail', label: '海上拖曳傘 (NT$1200)', desc: '高空美景' }
                              ].map(item => {
                                const isChecked = kentingActivities.includes(item.id);
                                return (
                                  <button
                                    key={item.id}
                                    onClick={() => toggleKentingActivity(item.id)}
                                    className={`p-2 rounded-lg border text-left transition-all flex flex-col justify-between cursor-pointer ${
                                      isChecked
                                        ? 'border-[#e63946] bg-[#e63946]/5 text-slate-900'
                                        : 'border-slate-200 hover:border-slate-300 text-slate-600'
                                    }`}
                                  >
                                    <div className="text-xs font-bold flex items-center justify-between w-full">
                                      <span>{item.label.split(' ')[0]}</span>
                                      <div className={`w-3.5 h-3.5 rounded border flex items-center justify-center text-white ${isChecked ? 'bg-[#10B981] border-[#10B981]' : 'border-slate-300 bg-white'}`}>
                                        {isChecked && <Check size={10} />}
                                      </div>
                                    </div>
                                    <div className="text-[8px] text-slate-400 mt-1">{item.label.split(' ')[1]}</div>
                                  </button>
                                );
                              })}
                            </div>
                          </div>
                        </div>

                        {/* 右側結果與分析 */}
                        <div className="bg-[#FAFDFD] p-5 rounded-xl border border-tiffany-ice/50 flex flex-col justify-between">
                          <div className="space-y-4">
                            <span className="text-[10px] font-bold text-slate-500 tracking-widest uppercase block">人均預算分析分解</span>
                            
                            <div className="text-center py-4 bg-white rounded-xl border border-slate-200/30 shadow-xs">
                              <div className="text-[9px] text-slate-400 font-bold uppercase tracking-widest">個人化旅行預估總支出</div>
                              <div className="text-3xl font-serif font-extrabold text-[#e63946] mt-1 font-mono">
                                NT$ {calculateKentingBudget().total.toLocaleString()}
                              </div>
                              <span className="text-[8px] text-slate-400 block mt-1">包含：2晚住宿 + 交通機車 + 餐飲 + 自選娛樂</span>
                            </div>

                            {/* 預算比例細項 */}
                            <div className="space-y-2 pt-2 border-t border-slate-100">
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">🛵 島上交通小計：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {calculateKentingBudget().transportCost.toLocaleString()}</span>
                              </div>
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">🏨 民宿住宿 (2晚)：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {calculateKentingBudget().stayCost.toLocaleString()}</span>
                              </div>
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">🍕 餐飲及夜市 (3天)：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {calculateKentingBudget().foodCost.toLocaleString()}</span>
                              </div>
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">⛵ 自選水上活動：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {calculateKentingBudget().actCost.toLocaleString()}</span>
                              </div>
                              <div className="flex justify-between text-xs">
                                <span className="text-slate-600 font-medium">🎟️ 鵝鑾鼻/社頂門票：</span>
                                <span className="font-mono font-bold text-slate-800">NT$ {calculateKentingBudget().ticketCost.toLocaleString()}</span>
                              </div>
                            </div>
                          </div>

                          <div className="text-[9px] text-slate-400 leading-relaxed font-mono mt-4 border-t border-slate-200/40 pt-3 flex items-start gap-1">
                            <Info size={10} className="text-[#e63946] shrink-0 mt-0.5" />
                            <span>
                              * 門票包含鵝鑾鼻燈塔全票NT$60、貓鼻頭NT$30、關山夕陽高地NT$60。生魚片為平價後壁湖自費享用，不含高雄往返墾丁的長途大眾交通票。
                            </span>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* 墾丁玩水與騎車「避坑智慧手冊」 */}
                    <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-4">
                      <div className="border-b border-slate-100 pb-3 flex items-center gap-2">
                        <Shield size={18} className="text-amber-500" />
                        <h4 className="font-serif font-extrabold text-slate-900 text-base">國境之南 ‧ 慢遊避坑指南</h4>
                      </div>
                      
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="bg-amber-50/50 p-4 rounded-xl border border-amber-100 space-y-1.5">
                          <span className="text-xs font-bold text-amber-700 flex items-center gap-1">
                            🌬️ 1. 秋冬強勁落山風安全
                          </span>
                          <p className="text-[11px] text-slate-600 leading-relaxed">
                            每年 10 月至隔年 3 月是墾丁著名的「落山風」季節。瞬間陣風可達 10 級（相當於輕度颱風）！
                            騎乘機車行經龍磐公園、聯勤雷達站一帶的開闊路段時，強烈風吹極易造成晃動，<strong>務必雙手握緊龍頭，放慢車速</strong>，切勿超速。
                          </p>
                        </div>

                        <div className="bg-sky-50/50 p-4 rounded-xl border border-sky-100 space-y-1.5">
                          <span className="text-xs font-bold text-sky-700 flex items-center gap-1">
                            🧴 2. 海洋友善防曬與水分補充
                          </span>
                          <p className="text-[11px] text-slate-600 leading-relaxed">
                            墾丁陽光極其強烈，即便多雲天氣也極易曬傷。浮潛或下海戲水時，<strong>請務必選用海洋友善（Ocean Friendly）防曬乳</strong>，或是直接穿著長袖水母衣以防物理曬傷，保護海洋珊瑚礁生態。
                          </p>
                        </div>

                        <div className="bg-orange-50/50 p-4 rounded-xl border border-orange-100 space-y-1.5">
                          <span className="text-xs font-bold text-orange-700 flex items-center gap-1">
                            📸 3. 台 26 線測速照相
                          </span>
                          <p className="text-[11px] text-slate-600 leading-relaxed">
                            省道台 26 線（車城、恆春、南灣到墾丁大街）路段筆直寬敞，因此設有多處固定式及區間測速照相機。
                            部分路段限速僅有 50-60 km/h。在國境之南慢遊，切記不要急躁，<strong>遵守速限才能保住荷包</strong>。
                          </p>
                        </div>

                        <div className="bg-green-50/50 p-4 rounded-xl border border-green-100 space-y-1.5">
                          <span className="text-xs font-bold text-green-700 flex items-center gap-1">
                            🐢 4. 砂島與海洋保護區法規
                          </span>
                          <p className="text-[11px] text-slate-600 leading-relaxed">
                            砂島貝殼砂海灣屬於生態保護區，沙灘外圍設有鐵絲網與木棧道。
                            <strong>嚴禁翻越鐵網進入沙灘或撿拾貝殼沙</strong>，違者會面臨最高新台幣 30,000 元以上的重罰！讓我們用眼睛記錄牛奶藍美景，把自然留給大自然。
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* --- 12. 首爾美食地圖專屬互動介面 --- */}
                {page.id === 'seoul-food-map' && (
                  <div className="space-y-6 animate-fade-in text-slate-800">
                    {/* Intro Hero banner for interactive tab */}
                    <div className="bg-gradient-to-r from-[#e63946] to-[#C1121F] p-6 md:p-8 rounded-3xl text-white shadow-md relative overflow-hidden">
                      <div className="absolute right-0 bottom-0 opacity-10 pointer-events-none transform translate-y-12 translate-x-12">
                        <Compass size={280} />
                      </div>
                      <div className="relative z-10 max-w-2xl space-y-2">
                        <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-[10px] tracking-widest uppercase font-bold text-white">
                          SEOUL FOODIE MAP 2026
                        </span>
                        <h3 className="font-serif font-extrabold text-2xl md:text-3xl leading-snug">
                          首爾互動美食街區探索 & 避坑地圖
                        </h3>
                        <p className="text-xs text-slate-100 leading-relaxed max-w-lg">
                          點擊下方地圖中的熱門美食街區、或使用美食分類篩選，即可獲得編輯部誠意挑選的 10 大必吃經典！
                          配合我們特別設計的「避開排隊地獄」即時時段模擬器與「美食靈魂測驗」，讓你的首爾吃貨之旅萬無一失。
                        </p>
                      </div>
                    </div>

                    {/* Quick Statistics Grid */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-orange-50 flex items-center justify-center text-orange-500 shrink-0">
                          <Flame size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">熱門菜單</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">10 道經典料理</span>
                        </div>
                      </div>
                      
                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-[#e63946]/10 flex items-center justify-center text-[#e63946] shrink-0">
                          <MapPin size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">核心街區</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">5 大吃貨戰區</span>
                        </div>
                      </div>

                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-emerald-50 flex items-center justify-center text-emerald-500 shrink-0">
                          <Clock size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">避坑指引</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">即時時段模擬</span>
                        </div>
                      </div>

                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-violet-50 flex items-center justify-center text-violet-500 shrink-0">
                          <Sparkles size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">靈魂測驗</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">1秒契合推薦</span>
                        </div>
                      </div>
                    </div>

                    {/* Map & Grid Dashboard */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
                      {/* Left: Beautiful SVG Seoul Map & Filters */}
                      <div className="lg:col-span-7 bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                        <div className="space-y-1">
                          <h4 className="font-serif font-extrabold text-slate-900 text-base">📍 首爾美食街區與交通示意圖</h4>
                          <p className="text-[11px] text-slate-400 font-sans">點擊地圖上的地標按鈕，可快速切換街區進行美食對焦：</p>
                        </div>

                        {/* Interactive SVG Seoul Map */}
                        <div className="relative w-full aspect-[4/3] bg-slate-50 rounded-2xl border border-slate-100 overflow-hidden shadow-inner flex items-center justify-center p-2">
                          <div className="absolute inset-0 bg-[linear-gradient(to_right,#f1f5f9_1px,transparent_1px),linear-gradient(to_bottom,#f1f5f9_1px,transparent_1px)] bg-[size:2rem_2rem] opacity-70"></div>
                          
                          {/* Stylized Han River */}
                          <svg className="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 600 450">
                            <path 
                              d="M -20 280 Q 150 260 300 300 T 620 280" 
                              fill="none" 
                              stroke="#cbd5e1" 
                              strokeWidth="32" 
                              strokeLinecap="round"
                              opacity="0.5"
                            />
                            <path 
                              d="M -20 280 Q 150 260 300 300 T 620 280" 
                              fill="none" 
                              stroke="#bae6fd" 
                              strokeWidth="20" 
                              strokeLinecap="round"
                              opacity="0.8"
                            />
                            <text x="310" y="315" fill="#38bdf8" className="text-[10px] font-bold tracking-widest uppercase font-mono" opacity="0.8">漢江 Han River</text>
                          </svg>

                          {/* Interactive clickable District Bubbles */}
                          <div className="absolute inset-0 w-full h-full">
                            {[
                              { id: 'hongdae', label: '弘大 (Hongdae)', desc: '燒肉 ‧ 炸雞 ‧ 潮流', x: '25%', y: '35%' },
                              { id: 'myeongdong', label: '明洞 (Myeongdong)', desc: '街頭小吃 ‧ 參雞湯', x: '50%', y: '42%' },
                              { id: 'gwangjang', label: '廣藏市場 (Gwangjang)', desc: '生牛肉 ‧ 傳統小吃', x: '68%', y: '32%' },
                              { id: 'seongsu', label: '聖水洞 (Seongsu)', desc: '文青咖啡 ‧ 炸醬麵', x: '82%', y: '48%' },
                              { id: 'sincheon', label: '新村 (Sinchon)', desc: '部隊鍋 ‧ 烤肉', x: '18%', y: '52%' }
                            ].map(district => (
                              <button
                                key={district.id}
                                onClick={() => setSeoulDistrict(district.id)}
                                style={{ left: district.x, top: district.y }}
                                className={`absolute -translate-x-1/2 -translate-y-1/2 p-3 rounded-2xl border-2 shadow-lg hover:scale-105 active:scale-95 transition-all text-left group cursor-pointer ${
                                  seoulDistrict === district.id
                                    ? 'border-[#e63946] bg-white ring-4 ring-[#e63946]/10 z-20'
                                    : 'border-slate-200 bg-white/95 z-10'
                                }`}
                              >
                                <div className="flex items-center gap-1.5">
                                  <div className={`w-2.5 h-2.5 rounded-full animate-pulse ${
                                    seoulDistrict === district.id ? 'bg-[#e63946]' : 'bg-slate-300'
                                  }`}></div>
                                  <span className="text-xs font-bold text-slate-800 font-sans">{district.label}</span>
                                </div>
                                <span className="block text-[9px] text-slate-400 mt-0.5 font-medium font-sans">{district.desc}</span>
                              </button>
                            ))}
                          </div>

                          {/* Compass Indicator */}
                          <div className="absolute right-4 top-4 bg-white/80 backdrop-blur-xs p-2 rounded-xl border border-slate-200/50 text-[10px] text-slate-400 flex items-center gap-1 font-mono pointer-events-none">
                            <span>🧭 N 37.566°</span>
                          </div>
                        </div>

                        {/* District Filter Badges */}
                        <div className="space-y-2">
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">選擇街區：</span>
                          <div className="flex flex-wrap gap-2">
                            {[
                              { id: 'all', label: '🗺️ 全部街區' },
                              { id: 'hongdae', label: '🥩 弘大' },
                              { id: 'myeongdong', label: '🍲 明洞/景福宮' },
                              { id: 'gwangjang', label: '🥞 廣藏市場/東大門' },
                              { id: 'seongsu', label: '☕ 聖水洞' },
                              { id: 'sincheon', label: '🥘 新村' }
                            ].map(btn => (
                              <button
                                key={btn.id}
                                onClick={() => setSeoulDistrict(btn.id)}
                                className={`px-3 py-1.5 rounded-full text-xs font-bold cursor-pointer transition-all ${
                                  seoulDistrict === btn.id
                                    ? 'bg-[#e63946] text-white shadow-md'
                                    : 'bg-slate-100 hover:bg-slate-200 text-slate-600'
                                }`}
                              >
                                {btn.label}
                              </button>
                            ))}
                          </div>
                        </div>

                        {/* Category Filter Badges */}
                        <div className="space-y-2">
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">美食種類：</span>
                          <div className="flex flex-wrap gap-2">
                            {[
                              { id: 'all', label: '🍽️ 全部' },
                              { id: 'bbq', label: '🥩 炭烤肉類' },
                              { id: 'soup', label: '🍲 養生湯品' },
                              { id: 'street', label: '🍡 傳統小吃' },
                              { id: 'seafood', label: '🦀 精緻海鮮' },
                              { id: 'chicken', label: '🍗 炸物雞肉' }
                            ].map(btn => (
                              <button
                                key={btn.id}
                                onClick={() => setSeoulCategory(btn.id)}
                                className={`px-3 py-1.5 rounded-full text-xs font-bold cursor-pointer transition-all ${
                                  seoulCategory === btn.id
                                    ? 'bg-[#e63946] text-white shadow-md'
                                    : 'bg-slate-100 hover:bg-slate-200 text-slate-600'
                                }`}
                              >
                                {btn.label}
                              </button>
                            ))}
                          </div>
                        </div>

                        {/* Keyword Search Input */}
                        <div className="relative">
                          <input
                            type="text"
                            placeholder="輸入美食名稱、韓文或關鍵字搜尋..."
                            value={seoulSearch}
                            onChange={(e) => setSeoulSearch(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 pl-10 text-xs font-semibold focus:outline-none focus:border-[#e63946] text-slate-800 font-sans"
                          />
                          <div className="absolute left-3.5 top-3.5 text-slate-400">
                            <Compass size={14} />
                          </div>
                          {seoulSearch && (
                            <button 
                              onClick={() => setSeoulSearch('')} 
                              className="absolute right-3 top-2.5 text-slate-400 hover:text-slate-600 p-1 rounded-full hover:bg-slate-200"
                            >
                              <X size={12} />
                            </button>
                          )}
                        </div>
                      </div>

                      {/* Right: Selected Foods List Cards */}
                      <div className="lg:col-span-5 flex flex-col gap-4">
                        <div className="flex justify-between items-center px-1">
                          <span className="text-xs font-bold text-slate-500 font-display">
                            精選美食清單 ({
                              seoulFoods.filter(f => 
                                (seoulDistrict === 'all' || f.district === seoulDistrict || (seoulDistrict === 'myeongdong' && f.district.includes('myeongdong')) || (seoulDistrict === 'gwangjang' && (f.district === 'gwangjang' || f.district.includes('gwangjang')))) &&
                                (seoulCategory === 'all' || f.category === seoulCategory) &&
                                (f.name.includes(seoulSearch) || f.koName.includes(seoulSearch) || f.intro.includes(seoulSearch) || f.recommendPlace.includes(seoulSearch))
                              ).length
                            } / {seoulFoods.length})
                          </span>
                          
                          {(seoulDistrict !== 'all' || seoulCategory !== 'all' || seoulSearch) && (
                            <button
                              onClick={() => {
                                setSeoulDistrict('all');
                                setSeoulCategory('all');
                                setSeoulSearch('');
                              }}
                              className="text-[10px] text-[#e63946] font-bold hover:underline font-display"
                            >
                              重設篩選
                            </button>
                          )}
                        </div>

                        <div className="space-y-4 max-h-[550px] overflow-y-auto pr-1">
                          {seoulFoods.filter(f => 
                            (seoulDistrict === 'all' || f.district === seoulDistrict || (seoulDistrict === 'myeongdong' && f.district.includes('myeongdong')) || (seoulDistrict === 'gwangjang' && (f.district === 'gwangjang' || f.district.includes('gwangjang')))) &&
                            (seoulCategory === 'all' || f.category === seoulCategory) &&
                            (f.name.includes(seoulSearch) || f.koName.includes(seoulSearch) || f.intro.includes(seoulSearch) || f.recommendPlace.includes(seoulSearch))
                          ).map(food => (
                            <motion.div
                              layout
                              key={food.id}
                              className="bg-white p-5 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-3.5 hover:border-[#e63946] transition-all"
                            >
                              <div className="flex justify-between items-start">
                                <div>
                                  <div className="flex items-center gap-2">
                                    <span className="text-sm font-extrabold text-slate-900 font-sans">{food.name}</span>
                                    <span className="text-xs text-slate-400 font-mono">({food.koName})</span>
                                  </div>
                                  <div className="flex items-center gap-1.5 mt-1 font-sans">
                                    <span className="bg-slate-100 text-slate-500 text-[9px] font-bold px-1.5 py-0.5 rounded-sm">{food.categoryName}</span>
                                    <span className="bg-[#e63946]/10 text-[#e63946] text-[9px] font-bold px-1.5 py-0.5 rounded-sm">{food.districtName}</span>
                                  </div>
                                </div>
                                <div className="text-right">
                                  <span className="block text-xs font-bold text-slate-900 font-mono">₩{food.price.toLocaleString()}</span>
                                  <span className="block text-[9px] text-slate-400 font-mono">≈ NT$ {(food.price * 0.025).toLocaleString()}</span>
                                </div>
                              </div>

                              <p className="text-[11px] text-slate-500 leading-relaxed font-sans">{food.intro}</p>

                              <div className="bg-slate-50 p-2.5 rounded-xl text-[10px] space-y-1 font-sans border border-slate-100">
                                <div className="flex items-start gap-1">
                                  <strong className="text-slate-800 shrink-0">📍 經典名店：</strong>
                                  <span className="text-slate-600">{food.recommendPlace}</span>
                                </div>
                                <div className="flex items-start gap-1">
                                  <strong className="text-teal-700 shrink-0">⏰ 避排隊時段：</strong>
                                  <span className="text-teal-600 font-semibold">{food.bestTime}</span>
                                </div>
                                <div className="flex items-start gap-1">
                                  <strong className="text-orange-700 shrink-0">💡 專家吃法：</strong>
                                  <span className="text-orange-600">{food.tips}</span>
                                </div>
                              </div>
                            </motion.div>
                          ))}

                          {seoulFoods.filter(f => 
                            (seoulDistrict === 'all' || f.district === seoulDistrict || (seoulDistrict === 'myeongdong' && f.district.includes('myeongdong')) || (seoulDistrict === 'gwangjang' && (f.district === 'gwangjang' || f.district.includes('gwangjang')))) &&
                            (seoulCategory === 'all' || f.category === seoulCategory) &&
                            (f.name.includes(seoulSearch) || f.koName.includes(seoulSearch) || f.intro.includes(seoulSearch) || f.recommendPlace.includes(seoulSearch))
                          ).length === 0 && (
                            <div className="p-12 text-center bg-white rounded-2xl border border-slate-100 text-slate-400 space-y-2">
                              <HelpCircle className="mx-auto text-slate-300" size={32} />
                              <span className="block text-xs font-bold">找不到符合篩選的美食項目</span>
                              <p className="text-[10px] text-slate-400">可以調整上方街區或種類，或者重新搜尋關鍵字哦！</p>
                            </div>
                          )}
                        </div>
                      </div>
                    </div>

                    {/* Section 2: Avoid Line Hell Optimizer */}
                    <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-6">
                      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-100 pb-4">
                        <div className="space-y-1">
                          <h4 className="font-serif font-extrabold text-slate-900 text-base flex items-center gap-2">
                            <span>🔥</span> 首爾排隊地獄避開指南（熱門時段即時模擬）
                          </h4>
                          <p className="text-[11px] text-slate-400 font-sans">拉動下方時間滑桿，看看您想吃的美食此時是否擁擠，並獲得黃金避開密技！</p>
                        </div>
                        
                        {/* Time indicator badge */}
                        <div className="bg-[#e63946]/10 border border-[#e63946]/20 px-4 py-2 rounded-xl text-center shrink-0">
                          <span className="block text-[9px] text-[#e63946] font-extrabold uppercase tracking-widest font-mono">SIMULATION TIME</span>
                          <span className="block text-xl font-mono font-bold text-slate-950">{seoulHour}:00</span>
                        </div>
                      </div>

                      {/* Hourly range slider */}
                      <div className="space-y-4 bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <div className="flex justify-between text-[10px] text-slate-400 font-bold font-mono">
                          <span>早午餐 11:00</span>
                          <span>午餐尖峰 12:00</span>
                          <span>下午茶 14:00</span>
                          <span>晚餐剛開 17:00</span>
                          <span>晚餐尖峰 19:00</span>
                          <span>宵夜戰場 21:00</span>
                        </div>
                        <input
                          type="range"
                          min="11"
                          max="22"
                          value={seoulHour}
                          onChange={(e) => setSeoulHour(parseInt(e.target.value))}
                          className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-[#e63946]"
                        />
                        <div className="flex justify-between text-[10px] text-slate-500 font-bold px-1 font-mono">
                          <span className={`${seoulHour === 11 ? 'text-[#e63946] font-extrabold' : ''}`}>11:00</span>
                          <span className={`${seoulHour === 12 ? 'text-[#e63946] font-extrabold' : ''}`}>12:00</span>
                          <span className={`${seoulHour === 13 ? 'text-[#e63946] font-extrabold' : ''}`}>13:00</span>
                          <span className={`${seoulHour === 14 ? 'text-[#e63946] font-extrabold' : ''}`}>14:00</span>
                          <span className={`${seoulHour === 15 ? 'text-[#e63946] font-extrabold' : ''}`}>15:00</span>
                          <span className={`${seoulHour === 16 ? 'text-[#e63946] font-extrabold' : ''}`}>16:00</span>
                          <span className={`${seoulHour === 17 ? 'text-[#e63946] font-extrabold' : ''}`}>17:00</span>
                          <span className={`${seoulHour === 18 ? 'text-[#e63946] font-extrabold' : ''}`}>18:00</span>
                          <span className={`${seoulHour === 19 ? 'text-[#e63946] font-extrabold' : ''}`}>19:00</span>
                          <span className={`${seoulHour === 20 ? 'text-[#e63946] font-extrabold' : ''}`}>20:00</span>
                          <span className={`${seoulHour === 21 ? 'text-[#e63946] font-extrabold' : ''}`}>21:00</span>
                          <span className={`${seoulHour === 22 ? 'text-[#e63946] font-extrabold' : ''}`}>22:00</span>
                        </div>
                      </div>

                      {/* Displaying Live Congestion status for each food at selected hour */}
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {seoulFoods.slice(0, 8).map(food => {
                          const busyVal = food.busyScore[seoulHour] || 50;
                          let statusLabel = '舒適暢快';
                          let statusColor = 'bg-emerald-500';
                          let cardBg = 'hover:border-emerald-200';
                          let textStyle = 'text-emerald-700';
                          
                          if (busyVal >= 85) {
                            statusLabel = '排隊地獄 (排隊30-60分+)';
                            statusColor = 'bg-rose-500 animate-pulse';
                            cardBg = 'hover:border-rose-200 bg-rose-50/20';
                            textStyle = 'text-rose-700 font-bold';
                          } else if (busyVal >= 60) {
                            statusLabel = '人潮眾多 (排隊10-25分)';
                            statusColor = 'bg-amber-500';
                            cardBg = 'hover:border-amber-200 bg-amber-50/20';
                            textStyle = 'text-amber-700';
                          }
                          
                          return (
                            <div key={food.id} className={`p-4 rounded-xl border border-slate-200/60 transition-all ${cardBg}`}>
                              <div className="flex justify-between items-center mb-2 font-sans">
                                <span className="text-xs font-extrabold text-slate-800">{food.name}</span>
                                <div className="flex items-center gap-1.5">
                                  <span className={`w-2 h-2 rounded-full ${statusColor}`}></span>
                                  <span className={`text-[10px] ${textStyle}`}>{statusLabel}</span>
                                </div>
                              </div>
                              
                              {/* Busy bar */}
                              <div className="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
                                <div className={`h-full ${statusColor}`} style={{ width: `${busyVal}%` }}></div>
                              </div>
                              
                              <div className="flex justify-between items-center mt-2.5 text-[10px] text-slate-400 font-sans">
                                <span>擁擠係數: {busyVal}%</span>
                                <span>最佳避坑時段: <strong className="text-[#e63946]">{food.bestTime}</strong></span>
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>

                    {/* Section 3: Interactive Seoul Food Matching Quiz */}
                    <div className="bg-gradient-to-br from-slate-900 to-slate-950 text-white p-6 md:p-8 rounded-3xl border border-slate-800 shadow-xl space-y-6 relative overflow-hidden">
                      <div className="absolute right-0 top-0 w-64 h-64 bg-[#e63946]/10 rounded-full blur-3xl"></div>
                      
                      <div className="space-y-2 relative z-10">
                        <span className="text-[#e63946] text-[10px] font-mono tracking-widest font-extrabold uppercase">SEOUL SOUL FOOD FINDER</span>
                        <h4 className="font-serif font-extrabold text-xl md:text-2xl text-white">🔮 找尋你的首爾「靈魂美食」契合度測驗</h4>
                        <p className="text-xs text-slate-300 leading-relaxed max-w-xl font-sans">
                          不知道第一餐吃什麼？回答 3 個簡單問題，我們的演算法將為您精準契合出最符合你此時此刻胃袋的首爾靈魂美食！
                        </p>
                      </div>

                      <div className="bg-slate-950/60 p-6 rounded-2xl border border-slate-800 relative z-10 font-sans">
                        {/* Step 0: Welcome / Start */}
                        {seoulQuizStep === 0 && (
                          <div className="text-center py-6 space-y-4">
                            <span className="text-5xl block animate-bounce">🥘</span>
                            <h5 className="font-bold text-sm text-white">啟動首爾美食契合演算法</h5>
                            <p className="text-xs text-slate-400 max-w-sm mx-auto leading-relaxed">
                              我們將根據你對辣度、食材喜好及預算範圍，為您配對出在首爾最對味的那一味！
                            </p>
                            <button
                              onClick={() => setSeoulQuizStep(1)}
                              className="px-6 py-2.5 bg-[#e63946] hover:bg-[#C1121F] text-white rounded-xl text-xs font-bold transition-all shadow-md active:scale-95 cursor-pointer"
                            >
                              開始 1 秒測驗
                            </button>
                          </div>
                        )}

                        {/* Step 1: Spiciness */}
                        {seoulQuizStep === 1 && (
                          <div className="space-y-4 animate-fade-in">
                            <div className="flex justify-between text-xs text-slate-400 font-bold font-mono">
                              <span>問題 1 / 3</span>
                              <span>辛辣接受度</span>
                            </div>
                            <h5 className="font-bold text-sm text-white">你的「辣度」極限在哪裡？🌶️</h5>
                            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                              {[
                                { id: 'none', label: '一點辣都不行 👶', desc: '喜歡甜鹹或甘醇清湯' },
                                { id: 'low', label: '微辣到小辣 🌶️', desc: '能接受韓國大醬或微辛' },
                                { id: 'high', label: '重度辣癮者 🥵', desc: '紅亮辛辣是我的靈魂' }
                              ].map(opt => (
                                <button
                                  key={opt.id}
                                  onClick={() => {
                                    setSeoulQuizSpicy(opt.id);
                                    setSeoulQuizStep(2);
                                  }}
                                  className="p-4 rounded-xl border border-slate-800 bg-slate-900/40 hover:bg-slate-900 text-left hover:border-[#e63946] transition-all cursor-pointer"
                                >
                                  <span className="block text-xs font-bold text-white mb-1">{opt.label}</span>
                                  <span className="block text-[10px] text-slate-400">{opt.desc}</span>
                                </button>
                              ))}
                            </div>
                            <button onClick={() => setSeoulQuizStep(0)} className="text-xs text-slate-500 hover:text-slate-300 font-bold block pt-2">返回上一步</button>
                          </div>
                        )}

                        {/* Step 2: Food Type / Style */}
                        {seoulQuizStep === 2 && (
                          <div className="space-y-4 animate-fade-in">
                            <div className="flex justify-between text-xs text-slate-400 font-bold font-mono">
                              <span>問題 2 / 3</span>
                              <span>食材及風格喜好</span>
                            </div>
                            <h5 className="font-bold text-sm text-white">今天用餐最想朝哪個方向走？🍖</h5>
                            <div className="grid grid-cols-1 sm:grid-cols-4 gap-3">
                              {[
                                { id: 'bbq', label: '大口吃肉 🥩', desc: '油脂與炭烤香氣' },
                                { id: 'soup', label: '暖胃熱湯 🍲', desc: '熬煮精華湯頭' },
                                { id: 'street', label: '街邊傳統 🍡', desc: '市井經典年糕春醬' },
                                { id: 'adventurous', label: '特色海鮮/生食 🦀', desc: '挑戰醬蟹或米其林生拌牛' }
                              ].map(opt => (
                                <button
                                  key={opt.id}
                                  onClick={() => {
                                    setSeoulQuizType(opt.id);
                                    setSeoulQuizStep(3);
                                  }}
                                  className="p-4 rounded-xl border border-slate-800 bg-slate-900/40 hover:bg-slate-900 text-left hover:border-[#e63946] transition-all cursor-pointer"
                                >
                                  <span className="block text-xs font-bold text-white mb-1">{opt.label}</span>
                                  <span className="block text-[9px] text-slate-400">{opt.desc}</span>
                                </button>
                              ))}
                            </div>
                            <button onClick={() => setSeoulQuizStep(1)} className="text-xs text-slate-500 hover:text-slate-300 font-bold block pt-2">返回上一步</button>
                          </div>
                        )}

                        {/* Step 3: Budget Range */}
                        {seoulQuizStep === 3 && (
                          <div className="space-y-4 animate-fade-in">
                            <div className="flex justify-between text-xs text-slate-400 font-bold font-mono">
                              <span>問題 3 / 3</span>
                              <span>預算限度</span>
                            </div>
                            <h5 className="font-bold text-sm text-white">這一餐的「人均預算」範圍？🪙</h5>
                            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                              {[
                                { id: 'low', label: '台幣 250 元以內 (₩10,000)', desc: '平民小資吃飽飽' },
                                { id: 'medium', label: '台幣 400 - 600 元 (₩15,000-22,000)', desc: '標準經典名物' },
                                { id: 'high', label: '台幣 800 元以上 (₩35,000+)', desc: '極致享受，犒賞靈魂' }
                              ].map(opt => (
                                <button
                                  key={opt.id}
                                  onClick={() => {
                                    setSeoulQuizBudget(opt.id);
                                    calculateSeoulQuizResult();
                                  }}
                                  className="p-4 rounded-xl border border-slate-800 bg-slate-900/40 hover:bg-slate-900 text-left hover:border-[#e63946] transition-all cursor-pointer"
                                >
                                  <span className="block text-xs font-bold text-white mb-1">{opt.label}</span>
                                  <span className="block text-[10px] text-slate-400">{opt.desc}</span>
                                </button>
                              ))}
                            </div>
                            <button onClick={() => setSeoulQuizStep(2)} className="text-xs text-slate-500 hover:text-slate-300 font-bold block pt-2">返回上一步</button>
                          </div>
                        )}

                        {/* Step 4: Completed result */}
                        {seoulQuizStep === 4 && seoulQuizMatch && (
                          <div className="text-center py-4 space-y-5 animate-fade-in">
                            <span className="text-base font-bold text-teal-400 block tracking-widest uppercase">✨ 完美的吃貨靈魂契合 ✨</span>
                            
                            <div className="max-w-md mx-auto bg-slate-900 p-5 rounded-2xl border-2 border-[#e63946] text-left space-y-3.5 shadow-lg">
                              <div className="flex justify-between items-center">
                                <div>
                                  <h6 className="text-base font-extrabold text-[#e63946]">{seoulQuizMatch.name}</h6>
                                  <span className="text-xs text-slate-400 font-mono">({seoulQuizMatch.koName})</span>
                                </div>
                                <div className="text-right">
                                  <span className="text-xs font-bold font-mono text-white">₩{seoulQuizMatch.price.toLocaleString()}</span>
                                  <span className="block text-[9px] text-slate-400 font-mono">≈ NT$ {(seoulQuizMatch.price * 0.025).toLocaleString()}</span>
                                </div>
                              </div>
                              
                              <p className="text-[11px] text-slate-300 leading-relaxed font-sans">{seoulQuizMatch.intro}</p>
                              
                              <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 space-y-1 text-[10px] text-slate-400 font-sans">
                                <div>📍 <strong>經典代表：</strong><span className="text-white">{seoulQuizMatch.recommendPlace}</span></div>
                                <div>⏰ <strong>避排隊時段：</strong><span className="text-[#e63946] font-bold">{seoulQuizMatch.bestTime}</span></div>
                                <div>💡 <strong>專家吃法：</strong><span className="text-orange-400">{seoulQuizMatch.tips}</span></div>
                              </div>
                            </div>

                            <div className="flex items-center justify-center gap-4 pt-2">
                              <button
                                onClick={resetSeoulQuiz}
                                className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold rounded-lg transition-all cursor-pointer"
                              >
                                重新測驗 🔄
                              </button>
                              <button
                                onClick={() => {
                                  setSeoulDistrict(seoulQuizMatch.district);
                                  setSeoulCategory(seoulQuizMatch.category);
                                  // Scroll to filters
                                  const mapEl = document.getElementById('planner');
                                  if (mapEl) mapEl.scrollIntoView({ behavior: 'smooth' });
                                }}
                                className="px-4 py-2 bg-[#e63946] hover:bg-[#C1121F] text-white text-xs font-bold rounded-lg transition-all shadow-md cursor-pointer"
                              >
                                在地圖中查看 🗺️
                              </button>
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                )}

                {/* --- 13. 花蓮台東三天兩夜專屬互動規劃介面 --- */}
                {page.id === 'hualien-taitung' && (
                  <div className="space-y-6 animate-fade-in text-slate-800">
                    {/* Intro Hero banner */}
                    <div className="bg-gradient-to-r from-teal-600 to-emerald-700 p-6 md:p-8 rounded-3xl text-white shadow-md relative overflow-hidden">
                      <div className="absolute right-0 bottom-0 opacity-10 pointer-events-none transform translate-y-12 translate-x-12">
                        <Compass size={280} />
                      </div>
                      <div className="relative z-10 max-w-2xl space-y-2">
                        <span className="bg-white/20 backdrop-blur-md px-3 py-1 rounded-full text-[10px] tracking-widest uppercase font-bold text-white">
                          HUALIEN & TAITUNG PLANNER 2026
                        </span>
                        <h3 className="font-serif font-extrabold text-2xl md:text-3xl leading-snug">
                          花東山海慢旅智慧規劃對焦儀
                        </h3>
                        <p className="text-xs text-slate-100 leading-relaxed max-w-lg">
                          點擊左側地圖中的山海地標探尋深度的景點、地道小吃與海景住宿，或是使用右側的「三天兩夜智慧規劃器」一鍵量身生成專屬的慢活路線，甚至還能精算旅行經費與同步到您的隨行備忘錄！
                        </p>
                      </div>
                    </div>

                    {/* Quick Statistics Grid */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-teal-50 flex items-center justify-center text-teal-600 shrink-0">
                          <Flame size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">慢遊名勝</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">12 大指標地標</span>
                        </div>
                      </div>
                      
                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-blue-50 flex items-center justify-center text-blue-500 shrink-0">
                          <MapPin size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">四大分區</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">橫跨山海縱谷</span>
                        </div>
                      </div>

                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-emerald-50 flex items-center justify-center text-emerald-500 shrink-0">
                          <Coins size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">費用經費</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">智慧經費精算</span>
                        </div>
                      </div>

                      <div className="bg-white p-4 rounded-2xl border border-tiffany-ice/40 shadow-xs flex items-center gap-3">
                        <div className="w-10 h-10 rounded-xl bg-amber-50 flex items-center justify-center text-amber-500 shrink-0">
                          <Sparkles size={20} />
                        </div>
                        <div>
                          <span className="block text-[10px] text-slate-400 font-bold uppercase tracking-wider font-display">行程輸出</span>
                          <span className="block text-sm font-bold text-slate-900 font-display">一鍵複製/同步</span>
                        </div>
                      </div>
                    </div>

                    {/* Main Interaction Layout */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-6" id="planner">
                      
                      {/* Left Column: Interactive Map */}
                      <div className="lg:col-span-5 bg-slate-50 p-5 rounded-3xl border border-slate-200/50 space-y-4">
                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-200 pb-3">
                          <div>
                            <h4 className="font-serif font-extrabold text-slate-900 text-sm flex items-center gap-1.5">
                              🗺️ 花東山海慢旅地圖
                            </h4>
                            <p className="text-[10px] text-slate-400">點擊點位看詳細介紹與避坑提示</p>
                          </div>
                          {/* Map Reset */}
                          <button 
                            onClick={() => { setHtDistrict('all'); setHtCategory('all'); setHtSelectedPoi(null); }}
                            className="text-[10px] font-bold text-[#e63946] hover:text-[#C1121F] underline cursor-pointer self-start sm:self-auto"
                          >
                            重設地圖
                          </button>
                        </div>

                        {/* District Filter Badges */}
                        <div className="flex flex-wrap gap-1">
                          {[
                            { id: 'all', name: '全部分區' },
                            { id: 'hualien', name: '花蓮/太魯閣' },
                            { id: 'coast', name: '台11線海岸' },
                            { id: 'valley', name: '台9線縱谷' },
                            { id: 'taitung', name: '台東市/多良' }
                          ].map(d => (
                            <button
                              key={d.id}
                              onClick={() => setHtDistrict(d.id)}
                              className={`px-2.5 py-1 rounded-full text-[10px] font-bold transition-all cursor-pointer ${
                                htDistrict === d.id 
                                  ? 'bg-slate-900 text-white shadow-xs' 
                                  : 'bg-white border border-slate-200 text-slate-500 hover:bg-slate-100'
                              }`}
                            >
                              {d.name}
                            </button>
                          ))}
                        </div>

                        {/* Map Visual Stage */}
                        <div className="relative aspect-[320/460] w-full max-w-[320px] mx-auto bg-gradient-to-b from-sky-100 to-blue-50 rounded-2xl border border-slate-200 shadow-inner overflow-hidden">
                          {/* Ocean Text */}
                          <div className="absolute right-4 top-1/2 -translate-y-1/2 text-[9px] font-bold tracking-widest text-blue-300 uppercase [writing-mode:vertical-lr] select-none pointer-events-none opacity-60">
                            Pacific Ocean 太平洋
                          </div>
                          
                          {/* Mountains Path */}
                          <div className="absolute left-0 top-0 bottom-0 w-1/3 bg-emerald-800/5 select-none pointer-events-none rounded-l-2xl" />
                          <div className="absolute left-2 top-10 text-[9px] font-bold text-slate-300 [writing-mode:vertical-lr] select-none pointer-events-none uppercase tracking-wider">
                            Central Range 中央山脈
                          </div>

                          {/* Highway 9 & 11 Guide Lines */}
                          <svg className="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 100 100" preserveAspectRatio="none">
                            {/* Highway 9 (Valley) */}
                            <path d="M 38 10 Q 33 40 33 90" fill="none" stroke="#FBBF24" strokeWidth="1" strokeDasharray="2,2" opacity="0.6" />
                            {/* Highway 11 (Coast) */}
                            <path d="M 48 10 Q 56 45 40 90" fill="none" stroke="#3B82F6" strokeWidth="1" strokeDasharray="2,2" opacity="0.6" />
                          </svg>

                          {/* Interactive Hotspots */}
                          {hualienTaitungPois.map(poi => {
                            const isDimmed = (htDistrict !== 'all' && poi.district !== htDistrict) || 
                                             (htCategory !== 'all' && poi.category !== htCategory);
                            const isSelected = htSelectedPoi === poi.id;
                            
                            let markerColor = 'bg-teal-500';
                            if (poi.category === 'food') markerColor = 'bg-orange-500';
                            if (poi.category === 'stay') markerColor = 'bg-indigo-500';

                            return (
                              <button
                                key={poi.id}
                                onClick={() => setHtSelectedPoi(poi.id)}
                                className={`absolute transform -translate-x-1/2 -translate-y-1/2 z-10 transition-all cursor-pointer ${
                                  isDimmed ? 'opacity-20 scale-75' : 'opacity-100 scale-100 hover:scale-110'
                                }`}
                                style={{ left: `${poi.x}%`, top: `${poi.y}%` }}
                              >
                                {/* Selected Ring / Wave */}
                                {isSelected && (
                                  <span className="absolute -inset-2 rounded-full bg-slate-900/10 animate-ping" />
                                )}
                                
                                {/* Marker Dot */}
                                <div className={`w-5 h-5 rounded-full ${markerColor} border-2 border-white shadow-md flex items-center justify-center text-white font-bold text-[9px]`}>
                                  {poi.category === 'spot' ? '⛰' : poi.category === 'food' ? '🍜' : '🏠'}
                                </div>

                                {/* Label tooltip */}
                                <div className={`absolute left-6 top-1/2 -translate-y-1/2 bg-slate-900/90 text-white text-[8px] font-bold px-1.5 py-0.5 rounded shadow-sm whitespace-nowrap transition-all ${
                                  isSelected ? 'opacity-100 scale-100' : 'opacity-0 scale-75 group-hover:opacity-100 pointer-events-none'
                                }`}>
                                  {poi.name.split(' ')[0]}
                                </div>
                              </button>
                            );
                          })}
                        </div>

                        {/* Selected POI Details Card */}
                        <div className="min-h-[140px] bg-white p-4 rounded-2xl border border-slate-200/60 shadow-xs flex flex-col justify-between">
                          {htSelectedPoi ? (
                            (() => {
                              const poi = hualienTaitungPois.find(p => p.id === htSelectedPoi);
                              if (!poi) return null;
                              return (
                                <div className="space-y-3 animate-fade-in text-slate-800">
                                  <div className="flex justify-between items-start gap-2">
                                    <div>
                                      <div className="flex items-center gap-1.5">
                                        <span className={`px-2 py-0.5 rounded text-[8px] font-bold text-white ${
                                          poi.category === 'spot' ? 'bg-teal-500' : poi.category === 'food' ? 'bg-orange-500' : 'bg-indigo-500'
                                        }`}>
                                          {poi.categoryName}
                                        </span>
                                        <span className="text-[10px] text-slate-400 font-bold">{poi.districtName}</span>
                                      </div>
                                      <h5 className="font-serif font-extrabold text-slate-900 text-sm mt-1">{poi.name}</h5>
                                    </div>
                                    <button 
                                      onClick={() => setHtSelectedPoi(null)}
                                      className="p-1 hover:bg-slate-100 rounded text-slate-400 cursor-pointer"
                                    >
                                      <X size={14} />
                                    </button>
                                  </div>
                                  
                                  <p className="text-[11px] text-slate-600 leading-relaxed">{poi.intro}</p>
                                  
                                  <div className="bg-slate-50 p-3 rounded-xl border border-slate-100 space-y-1 text-[10px] text-slate-500 font-sans">
                                    <div>💡 <strong>避坑提示：</strong><span className="text-slate-800">{poi.tips}</span></div>
                                    <div className="grid grid-cols-2 gap-2 pt-1 border-t border-slate-200/50 mt-1">
                                      <div>⏰ <strong>建議停留：</strong><span className="text-slate-800 font-bold">{poi.recommendTime}</span></div>
                                      <div>💰 <strong>預算預估：</strong><span className="text-slate-800 font-bold">{poi.budgetEst}</span></div>
                                    </div>
                                  </div>
                                </div>
                              );
                            })()
                          ) : (
                            <div className="h-full flex flex-col items-center justify-center text-center py-6 text-slate-400 space-y-1">
                              <Compass size={24} className="text-slate-300 animate-pulse" />
                              <span className="text-[11px] font-bold">尚未選擇點位</span>
                              <p className="text-[10px] text-slate-400 max-w-xs">請點擊上方手繪地圖上的各個彩色氣泡，解鎖對應景點、海味與希臘風住宿的特搜筆記！</p>
                            </div>
                          )}
                        </div>
                      </div>

                      {/* Right Column: Smart Budget & Route Generator */}
                      <div className="lg:col-span-7 bg-white p-5 rounded-3xl border border-slate-200/50 space-y-5">
                        <div className="border-b border-slate-200 pb-3">
                          <h4 className="font-serif font-extrabold text-slate-900 text-sm flex items-center gap-1.5">
                            ⚙️ 三天兩夜智慧客製規劃器
                          </h4>
                          <p className="text-[10px] text-slate-400">客製專屬行程、精算花費與同步我的隨行備忘錄</p>
                        </div>

                        {/* Controls */}
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                          {/* Travel Style */}
                          <div className="space-y-1.5">
                            <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">旅程風格偏好</label>
                            <div className="grid grid-cols-2 gap-1.5">
                              {[
                                { id: 'relax', label: '🌊 看海慢活' },
                                { id: 'trek', label: '⛰️ 戶外徒步' },
                                { id: 'food', label: '🍜 吃貨掃街' },
                                { id: 'culture', label: '🎨 文青打卡' }
                              ].map(style => (
                                <button
                                  key={style.id}
                                  onClick={() => setHtStyle(style.id)}
                                  className={`px-3 py-2 rounded-xl text-left text-xs font-bold transition-all flex items-center justify-between cursor-pointer ${
                                    htStyle === style.id
                                      ? 'bg-slate-900 text-white shadow-xs'
                                      : 'bg-slate-50 border border-slate-200 text-slate-600 hover:bg-slate-100'
                                  }`}
                                >
                                  <span>{style.label}</span>
                                </button>
                              ))}
                            </div>
                          </div>

                          {/* Transport Type */}
                          <div className="space-y-1.5">
                            <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">首選交通工具</label>
                            <div className="space-y-1.5">
                              {[
                                { id: 'scooter', label: '🏍️ 火車 + 租機車', desc: 'NT$500/天，超高自由度，停車超簡便' },
                                { id: 'car', label: '🚗 全家自駕開車', desc: 'NT$1800/天，遮風避雨，全家或帶長輩首選' },
                                { id: 'charter', label: '🚐 專屬包車導覽', desc: 'NT$5500/天，在地老司機帶路，不操心開車' }
                              ].map(trans => (
                                <button
                                  key={trans.id}
                                  onClick={() => setHtTransport(trans.id)}
                                  className={`w-full px-3 py-1.5 rounded-xl text-left text-xs font-bold transition-all cursor-pointer border flex flex-col justify-center ${
                                    htTransport === trans.id
                                      ? 'bg-slate-900 text-white border-slate-900 shadow-xs'
                                      : 'bg-slate-50 border-slate-200 text-slate-600 hover:bg-slate-100'
                                  }`}
                                >
                                  <span>{trans.label}</span>
                                  <span className={`text-[9px] font-medium block mt-0.5 ${htTransport === trans.id ? 'text-slate-300' : 'text-slate-400'}`}>
                                    {trans.desc}
                                  </span>
                                </button>
                              ))}
                            </div>
                          </div>
                        </div>

                        {/* Slider for Budget Goal */}
                        <div className="bg-slate-50 p-4 rounded-2xl border border-slate-100 space-y-2">
                          <div className="flex justify-between items-center">
                            <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">
                              我的每人預算目標 (理想上限)
                            </label>
                            <span className="text-xs font-bold font-mono text-teal-600 bg-teal-50 px-2.5 py-1 rounded-md">
                              NT$ {htBudget.toLocaleString()} 元
                            </span>
                          </div>
                          <input
                            type="range"
                            min="3000"
                            max="25000"
                            step="500"
                            value={htBudget}
                            onChange={(e) => setHtBudget(Number(e.target.value))}
                            className="w-full h-1.5 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-slate-900"
                          />
                          <div className="flex justify-between text-[8px] font-mono text-slate-400">
                            <span>$3k (省錢小資)</span>
                            <span>$10k (奢享慢旅)</span>
                            <span>$25k (極致包車)</span>
                          </div>
                        </div>

                        {/* Itinerary Output Cards - 3 Days Tabbed or Staggered */}
                        <div className="space-y-4">
                          <div className="flex justify-between items-center">
                            <span className="text-[11px] font-extrabold text-slate-500 uppercase tracking-wider">
                              📅 動態行程對焦：三天兩夜客製方案
                            </span>
                            <div className="flex gap-2">
                              {/* Sync and Copy actions */}
                              <button
                                onClick={() => handleCopyHtItinerary(getHtItinerary(htStyle, htTransport), calcHtBudget().total)}
                                className="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-800 text-[10px] font-bold rounded-lg transition-all flex items-center gap-1 cursor-pointer"
                              >
                                {htShowSuccess ? (
                                  <>
                                    <Check size={11} className="text-[#10B981]" />
                                    已複製！
                                  </>
                                ) : (
                                  '📋 複製行程'
                                )}
                              </button>
                              <button
                                onClick={() => handleSyncHtToNotes(getHtItinerary(htStyle, htTransport), calcHtBudget().total)}
                                className="px-3 py-1.5 bg-[#e63946] hover:bg-[#C1121F] text-white text-[10px] font-bold rounded-lg transition-all flex items-center gap-1 cursor-pointer"
                              >
                                {htSyncSuccess ? (
                                  <>
                                    <Check size={11} />
                                    已同步！
                                  </>
                                ) : (
                                  '💾 同步至備忘錄'
                                )}
                              </button>
                            </div>
                          </div>

                          {/* Staggered Timeline for Days */}
                          <div className="space-y-4 max-h-[320px] overflow-y-auto pr-1">
                            {getHtItinerary(htStyle, htTransport).map((day, dIdx) => (
                              <div key={dIdx} className="border-l-2 border-slate-200 pl-4 relative space-y-3">
                                {/* Day Circle Marker */}
                                <div className="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-slate-900 text-white flex items-center justify-center font-bold text-[8px] border-2 border-white shadow-xs">
                                  {dIdx + 1}
                                </div>
                                
                                <div>
                                  <span className="text-[9px] font-bold tracking-widest text-[#e63946] uppercase block">DAY 0{dIdx + 1}</span>
                                  <h5 className="font-serif font-extrabold text-slate-900 text-xs mt-0.5">{day.title}</h5>
                                </div>

                                <div className="space-y-2.5">
                                  {day.spots.map((spot, sIdx) => (
                                    <div key={sIdx} className="bg-slate-50 p-2.5 rounded-xl border border-slate-100 text-[11px] space-y-1">
                                      <div className="flex justify-between items-center text-[10px] text-slate-400 font-mono">
                                        <span>🕒 {spot.time}</span>
                                      </div>
                                      <div className="font-bold text-slate-900">{spot.name}</div>
                                      <p className="text-[10px] text-slate-500 leading-relaxed font-sans">{spot.desc}</p>
                                    </div>
                                  ))}
                                </div>
                              </div>
                            ))}
                          </div>
                        </div>

                        {/* Budget Analysis Dashboard */}
                        <div className="p-4 bg-slate-900 text-slate-300 rounded-2xl space-y-3 shadow-md">
                          <div className="border-b border-slate-800 pb-2 flex justify-between items-center">
                            <span className="text-[10px] font-bold tracking-wider text-[#e63946] uppercase">💰 智慧經費對焦試算</span>
                            <span className="text-[10px] text-slate-400 font-mono">每人平均花費</span>
                          </div>

                          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-[10px] text-slate-400">
                            <div className="bg-slate-950/40 p-2 rounded-xl border border-slate-800/40">
                              <span className="block text-[8px]">交通(油車/機車)</span>
                              <span className="block font-bold text-white mt-0.5">NT$ {calcHtBudget().transportCost.toLocaleString()}</span>
                            </div>
                            <div className="bg-slate-950/40 p-2 rounded-xl border border-slate-800/40">
                              <span className="block text-[8px]">住宿(2晚估)</span>
                              <span className="block font-bold text-white mt-0.5">NT$ {calcHtBudget().stayCost.toLocaleString()}</span>
                            </div>
                            <div className="bg-slate-950/40 p-2 rounded-xl border border-slate-800/40">
                              <span className="block text-[8px]">餐飲小吃</span>
                              <span className="block font-bold text-white mt-0.5">NT$ {calcHtBudget().foodCost.toLocaleString()}</span>
                            </div>
                            <div className="bg-slate-950/40 p-2 rounded-xl border border-slate-800/40">
                              <span className="block text-[8px]">門票/活動/雜費</span>
                              <span className="block font-bold text-white mt-0.5">NT$ {(calcHtBudget().actCost + calcHtBudget().miscCost).toLocaleString()}</span>
                            </div>
                          </div>

                          {/* Total Vs Budget Progress Bar */}
                          <div className="space-y-1.5 pt-1 border-t border-slate-800">
                            <div className="flex justify-between items-center text-xs">
                              <span className="font-bold text-white">智慧預估每人總花費：</span>
                              <span className="font-mono font-extrabold text-[#e63946] text-sm">
                                NT$ {calcHtBudget().total.toLocaleString()} 元
                              </span>
                            </div>

                            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden relative">
                              <div 
                                className={`h-full rounded-full transition-all duration-500 ${
                                  calcHtBudget().total > htBudget ? 'bg-orange-500' : 'bg-emerald-500'
                                }`}
                                style={{ width: `${Math.min(100, (calcHtBudget().total / htBudget) * 100)}%` }}
                              />
                            </div>

                            {/* Comparison and Tip from editor */}
                            <div className="text-[10px] text-slate-400 pt-1 flex items-start gap-1">
                              <span className="shrink-0">💡</span>
                              <p className="font-sans leading-relaxed">
                                {calcHtBudget().total > htBudget ? (
                                  <>
                                    <strong className="text-orange-400">預估超支 NT$ {(calcHtBudget().total - htBudget).toLocaleString()} 元。</strong>
                                    建議將交通工具切換為「火車+租機車」，或選擇更經濟的在地小食（如炸蛋蔥油餅與公正包子），即可完美把控預算喔！
                                  </>
                                ) : (
                                  <>
                                    <strong className="text-emerald-400 font-bold">預算非常充裕！餘額 NT$ {(htBudget - calcHtBudget().total).toLocaleString()} 元。</strong>
                                    恭喜您！您的預算十分充沛，建議到台東後直接升級都蘭灣第一排的海景下午茶，或多挑選一些阿美族精美的編織手工伴手禮！
                                  </>
                                )}
                              </p>
                            </div>
                          </div>
                        </div>

                      </div>
                    </div>
                  </div>
                )}

                {/* 其他目的地頁面通用提示 */}
                {!['power-plug-guide', 'miles-calculator', 'tax-refund-calculator', 'packing-list', 'esim-comparison', 'notion-travel-template', 'travel-tools', 'tokyo-accommodation', 'japan-drugstore-checklist', 'japan-budget-guide', 'korea-budget', 'kenting', 'seoul-food-map', 'hualien-taitung'].includes(page.id) && (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-4 text-center py-10">
                    <div className="w-16 h-16 bg-[#e63946]/10 rounded-full flex items-center justify-center mx-auto text-[#e63946] mb-4">
                      <Compass size={28} className="animate-spin-slow" />
                    </div>
                    <h4 className="font-serif font-extrabold text-slate-900 text-base">本篇讀者專屬電子票證工具正與官方聯動中</h4>
                    <p className="text-xs text-slate-500 max-w-md mx-auto leading-relaxed">
                      我們正在為這篇專題《{page.title}》對接當地的火車卡、優惠券及即時匯率接口。在此期間，歡迎在左側分頁閱讀完整攻略，或在下方「慢遊筆記」中保存您的旅程備份！
                    </p>
                  </div>
                )}
              </motion.div>
            )}

            {/* 慢遊筆記 / 聯絡我們反饋 */}
            {activeTab === 'notes' && (
              <motion.div 
                initial={{ opacity: 0, y: 15 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
              >
                {/* 意見反饋與聯絡 */}
                {page.id === 'about' ? (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-4">
                    <h4 className="font-serif font-extrabold text-slate-900 text-lg">聯絡我們 & 意見反饋</h4>
                    <p className="text-xs text-slate-500">歡迎與我們的 slow-travel 團隊交流您的漫遊故事或提供改進建議：</p>
                    
                    {feedbackSent ? (
                      <div className="p-8 text-center bg-tiffany-cream/40 rounded-xl border border-tiffany-ice/60 space-y-2">
                        <Check className="mx-auto text-[#e63946] h-8 w-8" />
                        <span className="font-bold text-slate-950 block text-sm">您的心聲我們收到囉！</span>
                        <p className="text-xs text-slate-500">感謝您的支持，慢旅團隊將於 3 個工作日內給您回信。</p>
                      </div>
                    ) : (
                      <form onSubmit={handleSendFeedback} className="space-y-4">
                        <div className="grid grid-cols-2 gap-4">
                          <div className="space-y-1.5">
                            <label className="text-xs font-bold text-slate-500">姓名</label>
                            <input 
                              type="text" required value={feedbackName} onChange={(e) => setFeedbackName(e.target.value)}
                              className="w-full bg-slate-50 border border-slate-200 rounded-lg px-3 py-2 text-xs font-semibold focus:outline-none focus:border-[#e63946]" 
                            />
                          </div>
                          <div className="space-y-1.5">
                            <label className="text-xs font-bold text-slate-500">電子郵件</label>
                            <input 
                              type="email" required value={feedbackEmail} onChange={(e) => setFeedbackEmail(e.target.value)}
                              className="w-full bg-slate-50 border border-slate-200 rounded-lg px-3 py-2 text-xs font-semibold focus:outline-none focus:border-[#e63946]" 
                            />
                          </div>
                        </div>
                        <div className="space-y-1.5">
                          <label className="text-xs font-bold text-slate-500">反饋內容</label>
                          <textarea 
                            required rows={4} value={feedbackMsg} onChange={(e) => setFeedbackMsg(e.target.value)}
                            className="w-full bg-slate-50 border border-slate-200 rounded-lg px-3 py-2 text-xs font-semibold focus:outline-none focus:border-[#e63946]" 
                            placeholder="輸入您的建議或任何想與我們說的話..."
                          />
                        </div>
                        <button 
                          type="submit"
                          className="px-6 py-3 bg-[#e63946] hover:bg-[#C1121F] text-white text-xs font-bold tracking-widest uppercase rounded-lg transition-all flex items-center justify-center gap-2 cursor-pointer"
                        >
                          <Send size={14} /> 送出反饋
                        </button>
                      </form>
                    )}
                  </div>
                ) : (
                  <div className="bg-white p-6 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-4">
                    <h4 className="font-serif font-extrabold text-slate-900 text-lg">您的隨行漫遊備忘錄</h4>
                    <p className="text-xs text-slate-500">在閱讀專題時，順手記下您在《{page.title}》中最感興趣的景點、美食或待辦清單：</p>
                    
                    <textarea 
                      className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-xs font-semibold leading-relaxed focus:outline-none focus:border-[#e63946]"
                      rows={8}
                      value={memoText}
                      onChange={(e) => setMemoText(e.target.value)}
                      placeholder="例如：
- 下次去東京一定要住由緣溫泉旅館，提早 3 個月訂！
- 藥妝店記得要滿 3 萬日圓才可以拿到松本清 10%+7% 折扣。
- 晚上 8 點以後一定要去一次日本超市，搶半價生魚片便當..."
                    />
                    
                    <div className="flex justify-between items-center pt-2">
                      <span className="text-[10px] font-mono text-slate-400">備忘錄將自動保存於您的瀏覽器快取中。</span>
                      <button 
                        onClick={handleSaveMemo}
                        className="px-4 py-2 bg-[#e63946] hover:bg-[#C1121F] text-white rounded-lg text-xs font-bold transition-all flex items-center gap-1.5"
                      >
                        {memoSavedStatus ? (
                          <>
                            <Check size={14} className="text-[#10B981]" />
                            已成功保存！
                          </>
                        ) : '手動保存筆記'}
                      </button>
                    </div>
                  </div>
                )}
              </motion.div>
            )}
          </div>
        </div>

        {/* 右側資訊側欄（高奢風） */}
        <aside className="lg:col-span-4 space-y-6">
          <div className="bg-slate-950 text-slate-200 p-6 rounded-2xl border border-slate-800/50 space-y-6 shadow-sm">
            <div className="border-b border-slate-800 pb-4">
              <span className="text-[#e63946] text-[9px] font-mono font-bold tracking-widest uppercase block">SLOW MAGAZINE</span>
              <h4 className="font-serif font-extrabold text-white text-base mt-1">漫漫旅刊編輯部</h4>
            </div>

            <div className="space-y-4">
              <div className="flex gap-4 items-center">
                <div className="w-10 h-10 rounded-full overflow-hidden bg-slate-800">
                  <img src="/images/ollie_yu_avatar_custom_1782353799678.jpg" alt="Editor Avatar" className="w-full h-full object-cover" referrerPolicy="no-referrer" />
                </div>
                <div>
                  <span className="text-xs font-serif font-extrabold text-white block">Ollie Yu</span>
                  <span className="text-[10px] text-slate-400 block">慢遊專欄首席編輯</span>
                </div>
              </div>

              <p className="text-xs text-slate-400 leading-relaxed font-sans">
                「我們為那些不僅僅是造訪、而是傾聽地方靈魂的人而寫。希望每一篇精細考證的慢遊專題，都能成為您探尋大地低語的專屬指南。」
              </p>
            </div>

            <div className="border-t border-slate-800 pt-4 space-y-3">
              <div className="flex justify-between items-center text-xs font-bold text-slate-300">
                <span>專欄刊登：</span>
                <span className="text-white">2026年夏季號</span>
              </div>
              <div className="flex justify-between items-center text-xs font-bold text-slate-300">
                <span>適合對象：</span>
                <span className="text-[#e63946]">極簡/深度旅人</span>
              </div>
              <div className="flex justify-between items-center text-xs font-bold text-slate-300">
                <span>更新頻率：</span>
                <span className="text-white">週四常規更新</span>
              </div>
            </div>
          </div>

          {/* 推薦閱讀卡片 */}
          <div className="bg-white p-5 rounded-2xl border border-tiffany-ice/40 shadow-xs space-y-4">
            <h5 className="font-serif font-bold text-slate-900 text-xs tracking-widest uppercase border-b border-slate-100 pb-2">本期其他推薦專欄</h5>
            
            <div className="space-y-3.5">
              {[
                { id: 'tokyo-5days', title: '東京5天4夜經典行程', category: '日本自由行' },
                { id: 'seoul-food', title: '首爾必吃美食攻略', category: '韓國自由行' },
                { id: 'travel-tools', title: '精選慢旅工具箱', category: '旅遊工具' }
              ].filter(x => x.id !== page.id).slice(0, 2).map((rec, i) => {
                const targetPage = customPages.find(p => p.id === rec.id);
                const coverImg = targetPage ? targetPage.coverImage : '/images/default.webp';
                const urlPath = targetPage ? `/${targetPage.url}` : '#';
                return (
                  <a 
                    key={i} 
                    href={urlPath}
                    className="flex gap-3 group items-center cursor-pointer block"
                  >
                    <div className="w-16 h-10 rounded-md overflow-hidden shrink-0 bg-slate-100 border border-slate-200/50">
                      <img 
                        src={coverImg} 
                        alt={rec.title} 
                        referrerPolicy="no-referrer"
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                      />
                    </div>
                    <div className="min-w-0">
                      <span className="text-[9px] text-[#e63946] font-bold block">{rec.category}</span>
                      <span className="text-xs font-serif font-bold text-slate-800 group-hover:text-[#e63946] transition-all truncate block mt-0.5">{rec.title}</span>
                    </div>
                  </a>
                );
              })}
            </div>
          </div>
        </aside>

      </main>
    </div>
  );
};
