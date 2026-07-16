import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Search, ArrowRight, MapPin, Star, Clock, Sparkles, 
  Compass, Sliders, CheckCircle2, Map, Users, Heart 
} from 'lucide-react';
import { TravelArticle } from '../types';
import { CustomPageData } from '../data/customPages';

interface HomeViewProps {
  articles: TravelArticle[];
  customPages: CustomPageData[];
  onSelectArticle: (id: string) => void;
  onSelectCustomPage: (id: string) => void;
  savedTripIds: string[];
  onToggleSaveTrip: (id: string) => void;
}

export const HomeView: React.FC<HomeViewProps> = ({ 
  articles, 
  customPages,
  onSelectArticle, 
  onSelectCustomPage,
  savedTripIds, 
  onToggleSaveTrip 
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [heroIndex, setHeroIndex] = useState(0);
  const [showAllArticles, setShowAllArticles] = useState(false);

  // 當分類或搜尋關鍵字改變時，自動重置收合狀態
  useEffect(() => {
    setShowAllArticles(false);
  }, [selectedCategory, searchQuery]);
  
  // 互動測驗狀態
  const [quizStep, setQuizStep] = useState(1);
  const [quizAnswers, setQuizAnswers] = useState({
    vibe: '',
    pace: '',
    focus: ''
  });
  const [quizResult, setQuizResult] = useState<TravelArticle | null>(null);

  // 專屬行程狀態
  const [journeyDestination, setJourneyDestination] = useState('japan');
  const [journeyStyle, setJourneyStyle] = useState('Solo');
  const [journeyFocus, setJourneyFocus] = useState('Culture');

  // 輪播背景
  const heroBackgrounds = [
    {
      id: 'japan',
      title: '日本自由行',
      tagline: '東京、關西、北海道與沖繩深度旅遊指南',
      img: 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=1200&auto=format&fit=crop'
    },
    {
      id: 'korea',
      title: '韓國自由行',
      tagline: '首爾潮流、釜山海景與濟州島自然假期',
      img: 'https://images.unsplash.com/photo-1517154421773-0529f29ea451?q=80&w=1200&auto=format&fit=crop'
    },
    {
      id: 'taiwan',
      title: '台灣旅遊',
      tagline: '漫步阿里山雲海、日月潭湖光與台北巷弄美食',
      img: 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=1200&auto=format&fit=crop'
    },
    {
      id: 'southeast-asia',
      title: '東南亞自由行',
      tagline: '泰國曼谷清邁、新加坡與熱帶度假海島指南',
      img: 'https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?q=80&w=1200&auto=format&fit=crop'
    }
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setHeroIndex((prev) => (prev + 1) % heroBackgrounds.length);
    }, 8000);
    return () => clearInterval(timer);
  }, []);

  // 搜尋與分類過濾
  const filteredArticles = articles.filter(art => {
    const matchesSearch = art.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
                          art.country.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          art.subtitle.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          art.category.toLowerCase().includes(searchQuery.toLowerCase());
    
    const matchesCategory = selectedCategory === 'All' || art.category === selectedCategory;
    
    return matchesSearch && matchesCategory;
  });

  const filteredCustomPages = (customPages || []).filter(page => {
    if (page.category === '關於我們') return false;
    
    const matchesSearch = page.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
                          page.intro.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          page.category.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          page.tags.some(t => t.toLowerCase().includes(searchQuery.toLowerCase()));
    
    const matchesCategory = selectedCategory === 'All' || page.category === selectedCategory;
    
    return matchesSearch && matchesCategory;
  });

  const resetQuiz = () => {
    setQuizStep(1);
    setQuizAnswers({ vibe: '', pace: '', focus: '' });
    setQuizResult(null);
  };

  // 專屬行程生成邏輯 (翻譯與美化)
  const getJourneyContent = () => {
    const destName = 
      journeyDestination === 'japan' ? '日本' :
      journeyDestination === 'korea' ? '韓國' :
      journeyDestination === 'taiwan' ? '台灣' : '東南亞';

    const focusLabel = 
      journeyFocus === 'Culture' ? '人文歷史' :
      journeyFocus === 'Nature' ? '自然奇觀' :
      journeyFocus === 'Culinary' ? '在地美食' : '光影定格';

    const companionLabel = 
      journeyStyle === 'Solo' ? '個人省錢自由行' :
      journeyStyle === 'Couple' ? '雙人浪漫漫遊' : '家族舒適深度遊';

    const d1Activity = 
      journeyDestination === 'japan' ? (
        journeyFocus === 'Culture' ? '清晨參訪東京淺草寺、京都古老神社，並在百年茶屋中體驗傳統抹茶茶道。' :
        journeyFocus === 'Nature' ? '搭乘登山纜車前往大湧谷，漫步於富士山展望台呼吸阿爾卑斯純淨的晨曦空氣。' :
        journeyFocus === 'Culinary' ? '探訪築地場外市場或黑門市場，品嚐現剖海膽、玉子燒與現烤和牛串。' :
        '攜手攝影同好前往京都嵐山竹林或澀谷十字路口，捕捉晨曦初露與人潮動靜對比的光影畫面。'
      ) : journeyDestination === 'korea' ? (
        journeyFocus === 'Culture' ? '漫步北村韓屋村石牆路，穿著傳統韓服參訪景福宮，感受朝鮮王朝歷史氛圍。' :
        journeyFocus === 'Nature' ? '清晨搭乘海雲台藍線公園膠囊列車，俯瞰東海水天一色的純淨海岸晨光。' :
        journeyFocus === 'Culinary' ? '走訪首爾廣藏市場，品嚐最道地的綠豆煎餅、生拌牛肉與麻藥海苔飯捲。' :
        '在甘川洞文化村五彩斑斕的小屋間尋找「小王子」銅像，捕捉日出時分的山城奇妙光影。'
      ) : journeyDestination === 'taiwan' ? (
        journeyFocus === 'Culture' ? '深度漫步大稻埕迪化街歷史洋樓，並在傳統茶藝館中沖泡一杯台灣高山烏龍茶。' :
        journeyFocus === 'Nature' ? '漫步阿里山巨木群棧道，迎著清晨微風在祝山車站等待浩瀚的日出與雲海。' :
        journeyFocus === 'Culinary' ? '探訪台南國華街與保安路，品嚐清甜鮮美的牛肉湯、碗粿與虱目魚粥。' :
        '在晨光乍現時前往日月潭水社碼頭，捕捉湖面雲霧繚繞、如水墨畫般空靈縹緲的靜謐光影。'
      ) : (
        journeyFocus === 'Culture' ? '深度探訪清邁古城雙龍寺，參觀精緻的泰式木雕古蹟，感受蘭納王朝遺風。' :
        journeyFocus === 'Nature' ? '漫步在峇里島德哥拉朗絕美梯田，或探尋熱帶雨林深處鮮為人知的秘境瀑布。' :
        journeyFocus === 'Culinary' ? '在曼谷清晨前往安帕瓦水上市場，在船家旁品嚐現烤泰國蝦、酸辣冬蔭功與烤香蕉。' :
        '清晨在吳哥窟小吳哥的荷花池前，架設相機捕捉朝陽從五座石塔背後緩緩升起的經典史詩光影。'
      );

    const d2Activity = 
      journeyDestination === 'japan' ? (
        journeyFocus === 'Culture' ? '造訪東京下町的職人工坊，親自體驗古老的手作江戶切子玻璃雕刻或傳統藍染。' :
        journeyFocus === 'Nature' ? '漫步在鎌倉海岸線，搭乘江之電軌道電車，在夕陽下的湘南海岸放鬆身心。' :
        journeyFocus === 'Culinary' ? '入座隱密精緻的關西壽喜燒或懷石料理，品味一期一會的極致四季和風盛宴。' :
        '登上東京晴空塔或六本木新城展望台，使用慢速快門與長曝光技術拍下繁華都市的流光溢彩。'
      ) : journeyDestination === 'korea' ? (
        journeyFocus === 'Culture' ? '造訪首爾仁寺洞傳統工藝街，親自體驗韓紙捏製或製作專屬中文刻字印章。' :
        journeyFocus === 'Nature' ? '探尋濟州島城山日出峰，沿著風光秀麗的火山峭壁步道健行，俯瞰壯麗的太平洋。' :
        journeyFocus === 'Culinary' ? '享用熱騰騰的東大門一隻雞或神仙雪濃湯，晚餐安排正宗韓式木炭烤肉與冰啤酒。' :
        '前往東大門設計廣場 (DDP) 捕捉未來感極強的流線型建築與金屬光澤，實地練習極簡構圖。'
      ) : journeyDestination === 'taiwan' ? (
        journeyFocus === 'Culture' ? '走訪鶯歌陶瓷老街與手作工坊，親自拉胚並捏製專屬的復古手作茶杯。' :
        journeyFocus === 'Nature' ? '深入花蓮太魯閣國家公園，漫步砂卡礑或燕子口步道，讚嘆大自然鬼斧神工的峽谷。' :
        journeyFocus === 'Culinary' ? '前往士林夜市或逢甲夜市，品嚐黑糖珍珠鮮奶、起司大雞排與胡椒餅。' :
        '沿著淡水金色海岸或九份豎崎路石階，捕捉夕陽西下時，老街燈籠亮起那一瞬間的懷舊與溫柔光影。'
      ) : (
        journeyFocus === 'Culture' ? '在清邁手工藝村，親自體驗傳統泰式手繪紙傘、泰絲編織與銀器雕刻工法。' :
        journeyFocus === 'Nature' ? '乘船漫遊下龍灣奇峰怪石，或在熱帶潛水勝地與海龜及珊瑚礁一同在大海中遨遊。' :
        journeyFocus === 'Culinary' ? '參加泰式料理烹飪學校，跟隨大廚去市集認菜，實地學做正宗泰式炒河粉與綠咖哩。' :
        '深入峇里島烏布林間，在椰林與光芒交織的絕美午後捕捉光影，定格富有熱帶風情的人像。'
      );

    const d3Activity = 
      journeyDestination === 'japan' ? (
        journeyFocus === 'Culture' ? '前往下北澤或高圓寺的復古古著店街，探索東京最接地氣的青年流行文化與獨立書店。' :
        journeyFocus === 'Nature' ? '前往箱根或有馬溫泉，在群山環抱的露天風呂中舒緩疲勞，享受身心合一的平靜。' :
        journeyFocus === 'Culinary' ? '在新宿回憶橫丁或大阪道頓堀，享用美味的炸串、章魚燒與大杯冰鎮生啤酒。' :
        '在傍晚前往淺草雷門，拍攝燈火闌珊的紅色大燈籠與周邊復古人力車交疊的江戶時代風情。'
      ) : journeyDestination === 'korea' ? (
        journeyFocus === 'Culture' ? '前往弘大或聖水洞文創街區，探索當代韓國設計師品牌、獨立畫廊與文創咖啡廳。' :
        journeyFocus === 'Nature' ? '在首爾南山公園踏青，沿著古城牆步道散步至首爾塔，將整座城市的夜景盡收眼底。' :
        journeyFocus === 'Culinary' ? '在明洞小吃街品嚐雞蛋糕、烤起司串，晚餐享用極具特色的安東燉雞或韓式炸雞外送。' :
        '前往盤浦大橋或清溪川，使用腳架拍攝絢麗奪目的彩虹噴泉與城市水道交相輝映的動人夜景。'
      ) : journeyDestination === 'taiwan' ? (
        journeyFocus === 'Culture' ? '前往松山文創園區或華山 1914，參觀文創展覽與原創選物店，體驗台灣小清新生活美學。' :
        journeyFocus === 'Nature' ? '搭乘平溪線火車，漫步在十分老街鐵道旁，在夜空下施放一盞承載祈願的傳統天燈。' :
        journeyFocus === 'Culinary' ? '在台北永康街享用精緻著名的鼎泰豐小籠包，並以一碗堆疊厚實的芒果雪花冰完美收尾。' :
        '前往萬華龍山寺或大稻埕碼頭，在繚繞的香火或淡水河畔的落日餘暉中拍攝最富有人文溫度的剪影。'
      ) : (
        journeyFocus === 'Culture' ? '走訪新加坡牛車水與小印度，感受多元宗教與種族文化融合的街區風情與古老廟宇。' :
        journeyFocus === 'Nature' ? '漫步在新加坡濱海灣花園巨型超級樹 (Supertrees) 之中，體驗科技與自然交織的未來主義。' :
        journeyFocus === 'Culinary' ? '在新加坡麥士威熟食中心或吉隆坡亞羅街，享用香氣四溢的肉骨茶、海南雞飯與沙爹串。' :
        '在曼谷鄭王廟 (黎明寺) 暮色降臨時，在湄南河對岸捕捉整座白色佛塔染上黃金餘暉的史詩級日落畫面。'
      );

    return {
      title: `${companionLabel} · ${destName}${focusLabel}之旅`,
      days: [
        {
          day: 1,
          time: '清晨與上午',
          activity: d1Activity,
          cost: journeyStyle === 'Solo' ? '約 $35' : journeyStyle === 'Couple' ? '約 $70' : '約 $110'
        },
        {
          day: 2,
          time: '午後時光',
          activity: d2Activity,
          cost: journeyStyle === 'Solo' ? '約 $45' : journeyStyle === 'Couple' ? '約 $90' : '約 $140'
        },
        {
          day: 3,
          time: '暮色與夜晚',
          activity: d3Activity,
          cost: journeyStyle === 'Solo' ? '約 $60' : journeyStyle === 'Couple' ? '約 $120' : '約 $180'
        }
      ]
    };
  };

  const customJourney = getJourneyContent();

  return (
    <div className="bg-tiffany-cream min-h-screen text-slate-900 font-sans pb-16">
      
      {/* 1. HERO 輪播看板區 */}
      <section className="relative h-[95vh] flex items-center justify-center overflow-hidden bg-slate-950">
        
        {/* 背景圖片 AnimatePresence */}
        <div className="absolute inset-0 z-0">
          <AnimatePresence mode="wait">
            <motion.div
              key={heroIndex}
              initial={{ opacity: 0, scale: 1.05 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 1.5, ease: 'easeInOut' }}
              className="absolute inset-0 bg-cover bg-center bg-no-repeat"
              style={{ 
                backgroundImage: `url(${heroBackgrounds[heroIndex].img})`,
                filter: 'brightness(0.55)' 
              }}
            />
          </AnimatePresence>
          {/* 漸變覆蓋 */}
          <div className="absolute inset-0 bg-gradient-to-t from-[#f8fafc] via-transparent to-black/40 z-10 pointer-events-none" />
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_30%,#1c1917/30%_100%)] z-10 pointer-events-none" />
        </div>

        {/* 英雄區內容 */}
        <div className="relative z-20 container mx-auto px-6 max-w-7xl text-center text-white mt-12">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="space-y-6"
          >
            <div className="inline-flex items-center gap-2 px-4 py-1.5 border border-white/20 bg-white/10 backdrop-blur-md rounded-full text-xs font-bold tracking-[0.3em] uppercase text-[#e63946]">
              <Sparkles size={12} className="text-[#e63946] fill-[#e63946]" /> ✈ 用最少預算，走最多地方
            </div>
            
            <h1 className="font-serif tracking-tight leading-[1.1] drop-shadow-md flex flex-col items-center gap-2 md:gap-3">
              <span className="text-3xl md:text-5xl lg:text-6xl font-semibold text-slate-50">
                Go lightly
              </span>
              <span className="text-lg md:text-2xl lg:text-3xl font-sans font-medium tracking-[0.3em] text-[#e63946] uppercase">
                Travel
              </span>
            </h1>

            <p className="max-w-2xl mx-auto text-base md:text-lg text-slate-200 font-light leading-relaxed drop-shadow-sm">
              台港旅客省錢自由行攻略平台。日本、韓國、台灣、東南亞深度旅遊指南，含預算規劃、簽證、交通、住宿推薦與實際花費。
            </p>

            {/* 互動式搜尋列 */}
            <div className="max-w-2xl mx-auto mt-8 md:mt-12 bg-white/95 backdrop-blur-md rounded-full shadow-2xl border border-slate-200 p-1.5 md:p-2 flex flex-row items-center gap-1.5 md:gap-2">
              <div className="flex items-center gap-2 md:gap-3 w-full pl-3 md:pl-4 py-1 md:py-2 text-slate-700 min-w-0">
                <Search className="text-[#e63946] shrink-0" size={18} />
                <input 
                  type="text" 
                  placeholder="搜尋想去的景點或攻略？（例：東京、首爾、曼谷...）" 
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="bg-transparent w-full focus:outline-none text-slate-800 placeholder-slate-400 text-xs md:text-base min-w-0"
                />
              </div>
              <button 
                onClick={() => {
                  const el = document.getElementById('magazine-section');
                  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }}
                className="bg-[#e63946] hover:bg-[#C1121F] text-white font-medium text-xs md:text-sm tracking-wider md:tracking-widest uppercase px-4 md:px-8 py-2 md:py-3.5 rounded-full transition-all duration-300 flex items-center justify-center gap-1.5 shrink-0"
              >
                <span className="hidden sm:inline">探索日誌</span>
                <span className="inline sm:hidden">探索</span>
                <ArrowRight size={14} className="shrink-0" />
              </button>
            </div>

            {/* 輪播切換按鈕 */}
            <div className="grid grid-cols-2 sm:flex sm:flex-row justify-center gap-2 sm:gap-3 pt-6 max-w-[320px] sm:max-w-none mx-auto w-full px-4 sm:px-0">
              {heroBackgrounds.map((bg, idx) => {
                const getHref = (id: string) => {
                  switch (id) {
                    case 'japan': return '/japan-travel.html';
                    case 'korea': return '/korea-travel.html';
                    case 'taiwan': return '/taiwan-travel.html';
                    case 'southeast-asia': return '/southeast-asia.html';
                    default: return '#';
                  }
                };
                return (
                  <a
                    key={bg.id}
                    href={getHref(bg.id)}
                    className={`w-full sm:w-auto px-2 sm:px-4 py-2 sm:py-1.5 rounded-full text-[11px] sm:text-xs font-bold uppercase tracking-wider sm:tracking-widest transition-all duration-300 backdrop-blur-xs text-center flex items-center justify-center ${
                      heroIndex === idx 
                        ? 'bg-[#121e1e] text-white scale-105 shadow-md border border-[#121e1e]' 
                        : 'bg-white/15 hover:bg-white/30 text-white border border-white/20'
                    }`}
                  >
                    {bg.title}
                  </a>
                );
              })}
            </div>

          </motion.div>
        </div>
      </section>

      {/* 2. 靈魂慢旅測驗 (QUIZ) */}
      <section className="py-24 bg-white border-y border-slate-200">
        <div className="container mx-auto px-6 max-w-7xl">
          <div className="text-center max-w-2xl mx-auto mb-16">
            <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">靈智探針</span>
            <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">探索您的心靈歸屬之地</h2>
            <div className="w-12 h-1 bg-[#e63946] mx-auto mt-4 mb-6"></div>
            <p className="text-slate-500 font-light">
              花一分鐘回答三個關於您當下心境的探索，我們的心靈羅盤將為您指引最契合的慢旅歸宿。
            </p>
          </div>

          <div className="max-w-3xl mx-auto bg-slate-50 border border-slate-200 rounded-2xl p-8 md:p-12 shadow-sm relative overflow-hidden">
            
            {/* 背景微光 */}
            <div className="absolute top-0 right-0 w-64 h-64 bg-[#e63946]/5 rounded-full blur-3xl pointer-events-none" />

            {/* 測驗進度 */}
            <div className="flex justify-between items-center mb-8 border-b border-slate-200 pb-6">
              <span className="text-xs font-bold uppercase tracking-widest text-slate-400">
                {quizStep < 4 ? `心靈探問 ${quizStep} / 3` : '您的專屬契合地'}
              </span>
              <div className="flex gap-2">
                {[1, 2, 3].map((step) => (
                  <div 
                    key={step} 
                    className={`h-1 w-8 rounded-full transition-all duration-500 ${
                      quizStep >= step ? 'bg-[#e63946]' : 'bg-slate-200'
                    }`} 
                  />
                ))}
              </div>
            </div>

            <AnimatePresence mode="wait">
              {/* 步驟 1: 選擇氛圍 */}
              {quizStep === 1 && (
                <motion.div
                  key="step1"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ x: -20, opacity: 0 }}
                  className="space-y-6"
                >
                  <h3 className="font-serif text-2xl text-slate-900">1. 此刻，您的靈魂渴望沉浸在何種氛圍中？</h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4">
                    {[
                      { value: 'Zen', title: '靜謐與禪意', desc: '古老寺廟、翠綠青苔、枯山水、裊裊茶香與沉思。' },
                      { value: 'Scenic', title: '壯麗與遼闊', desc: '陡峭巍峨的花崗岩山峰、奔騰咆哮的瀑布與悠揚牛鈴。' },
                      { value: 'Epic', title: '神秘與原始', desc: '黑火山沙灘、粗獷的黑色岩石、蒸汽騰騰的地熱與北極光。' }
                    ].map((item) => (
                      <button
                        key={item.value}
                        onClick={() => {
                          setQuizAnswers(prev => ({ ...prev, vibe: item.value }));
                          setQuizStep(2);
                        }}
                        className="flex flex-col text-left p-6 bg-white border border-slate-200 hover:border-[#e63946] rounded-xl transition-all duration-300 group shadow-sm hover:shadow-md"
                      >
                        <span className="font-serif text-lg font-bold text-slate-800 group-hover:text-[#e63946] transition-colors">{item.title}</span>
                        <span className="text-xs text-slate-500 font-light mt-2 leading-relaxed">{item.desc}</span>
                        <div className="mt-4 text-xs font-bold text-[#e63946] uppercase tracking-widest flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                          選擇此項 <ArrowRight size={12} />
                        </div>
                      </button>
                    ))}
                  </div>
                </motion.div>
              )}

              {/* 步驟 2: 選擇節奏 */}
              {quizStep === 2 && (
                <motion.div
                  key="step2"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ x: -20, opacity: 0 }}
                  className="space-y-6"
                >
                  <h3 className="font-serif text-2xl text-slate-900">2. 您傾向於如何體驗時間的流逝？</h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4">
                    {[
                      { value: 'Slow', title: '極簡沉思', desc: '靜坐廊前，嗅聞葉香，徹底放慢呼吸與心靈。' },
                      { value: 'Balanced', title: '隨心遊走', desc: '搭乘景觀火車，在古樸村落小巷間無拘無束漫步。' },
                      { value: 'High', title: '極致探索', desc: '在曠野馳騁，攀越萬年冰川，追逐刺骨的北極寒風。' }
                    ].map((item) => (
                      <button
                        key={item.value}
                        onClick={() => {
                          setQuizAnswers(prev => ({ ...prev, pace: item.value }));
                          setQuizStep(3);
                        }}
                        className="flex flex-col text-left p-6 bg-white border border-slate-200 hover:border-[#e63946] rounded-xl transition-all duration-300 group shadow-sm hover:shadow-md"
                      >
                        <span className="font-serif text-lg font-bold text-slate-800 group-hover:text-[#e63946] transition-colors">{item.title}</span>
                        <span className="text-xs text-slate-500 font-light mt-2 leading-relaxed">{item.desc}</span>
                        <div className="mt-4 text-xs font-bold text-[#e63946] uppercase tracking-widest flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                          選擇此項 <ArrowRight size={12} />
                        </div>
                      </button>
                    ))}
                  </div>
                  <button 
                    onClick={() => setQuizStep(1)}
                    className="text-slate-400 hover:text-slate-700 text-xs font-bold uppercase tracking-widest mt-4 flex items-center gap-1"
                  >
                    ← 返回步驟 1
                  </button>
                </motion.div>
              )}

              {/* 步驟 3: 選擇焦點 */}
              {quizStep === 3 && (
                <motion.div
                  key="step3"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ x: -20, opacity: 0 }}
                  className="space-y-6"
                >
                  <h3 className="font-serif text-2xl text-slate-900">3. 哪一種深度體驗最能點燃您的熱情？</h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4">
                    {[
                      { value: 'Culture', title: '歷史、民俗與人文', desc: '數百年的民間傳說、極致匠人手藝與莊嚴神聖的儀式。' },
                      { value: 'Nature', title: '純淨的大自然奇觀', desc: '宏大磅礴的瀑布、深邃寧靜的高山松林與純淨冰川。' },
                      { value: 'Adventure', title: '地球運作的地質奧秘', desc: '活躍的地熱噴發、神秘的極黑苔原與晶瑩剔透的藍冰洞。' }
                    ].map((item) => (
                      <button
                        key={item.value}
                        onClick={() => {
                          const updatedAnswers = { ...quizAnswers, focus: item.value };
                          setQuizAnswers(updatedAnswers);
                          setTimeout(() => {
                            let targetId = 'kyoto';
                            if (updatedAnswers.vibe === 'Scenic' || updatedAnswers.focus === 'Nature') {
                              targetId = 'switzerland';
                            } else if (updatedAnswers.vibe === 'Epic' || updatedAnswers.pace === 'High' || updatedAnswers.focus === 'Adventure') {
                              targetId = 'iceland';
                            }
                            const matched = articles.find(art => art.id === targetId) || articles[0];
                            setQuizResult(matched);
                            setQuizStep(4);
                          }, 100);
                        }}
                        className="flex flex-col text-left p-6 bg-white border border-slate-200 hover:border-[#e63946] rounded-xl transition-all duration-300 group shadow-sm hover:shadow-md"
                      >
                        <span className="font-serif text-lg font-bold text-slate-800 group-hover:text-[#e63946] transition-colors">{item.title}</span>
                        <span className="text-xs text-slate-500 font-light mt-2 leading-relaxed">{item.desc}</span>
                        <div className="mt-4 text-xs font-bold text-[#e63946] uppercase tracking-widest flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                          揭曉心靈目的地 <ArrowRight size={12} />
                        </div>
                      </button>
                    ))}
                  </div>
                  <button 
                    onClick={() => setQuizStep(2)}
                    className="text-slate-400 hover:text-slate-700 text-xs font-bold uppercase tracking-widest mt-4 flex items-center gap-1"
                  >
                    ← 返回步驟 2
                  </button>
                </motion.div>
              )}

              {/* 步驟 4: 測驗結果 */}
              {quizStep === 4 && quizResult && (
                <motion.div
                  key="result"
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0 }}
                  className="space-y-6 text-center py-4"
                >
                  <div className="w-16 h-16 bg-[#e63946]/10 rounded-full flex items-center justify-center mx-auto text-[#e63946] animate-bounce mb-4">
                    <Compass size={32} />
                  </div>
                  <span className="text-slate-500 text-xs font-bold uppercase tracking-[0.2em]">羅盤為您指引的方向：</span>
                  
                  <h3 className="font-serif text-3xl md:text-5xl text-slate-900 font-semibold mt-2">{quizResult.country}</h3>
                  <p className="text-slate-500 font-serif italic text-base md:text-lg max-w-xl mx-auto px-4">
                    「{quizResult.title}」
                  </p>

                  <div className="flex flex-wrap justify-center gap-2 max-w-lg mx-auto pt-2">
                    <span className="px-3 py-1 bg-[#e63946]/10 text-[#e63946] text-xs font-bold tracking-wider uppercase rounded-full">
                      氛圍契合：{quizResult.vibe}
                    </span>
                    <span className="px-3 py-1 bg-slate-200 text-slate-700 text-xs font-bold tracking-wider uppercase rounded-full">
                      最佳季節：{quizResult.bestSeason}
                    </span>
                    <span className="px-3 py-1 bg-slate-200 text-slate-700 text-xs font-bold tracking-wider uppercase rounded-full">
                      體驗分類：{quizResult.category}
                    </span>
                  </div>

                  {/* 推薦必訪景點 */}
                  {quizResult.mapSpots && quizResult.mapSpots.length > 0 && (
                    <div className="pt-8 border-t border-slate-200/80 mt-8 text-left">
                      <h4 className="font-serif text-lg text-slate-900 font-bold mb-1 text-center md:text-left flex items-center justify-center md:justify-start gap-2">
                        <Sparkles size={16} className="text-[#e63946]" /> 心靈指引：專屬必訪景點
                      </h4>
                      <p className="text-xs text-slate-500 mb-6 text-center md:text-left font-light">
                        以下是羅盤特別為您挑選，高度契合此次探索心境的精選奇景：
                      </p>
                      
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {quizResult.mapSpots.map((spot, index) => (
                          <div 
                            key={index} 
                            onClick={() => onSelectArticle(quizResult.id)}
                            className="flex gap-4 bg-white p-3.5 rounded-xl border border-slate-200/60 shadow-xs hover:shadow-md hover:border-[#e63946] transition-all duration-300 group cursor-pointer"
                          >
                            <div className="w-20 h-20 rounded-lg overflow-hidden shrink-0 bg-slate-100 relative">
                              <img 
                                src={spot.image} 
                                alt={spot.name} 
                                className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                                referrerPolicy="no-referrer"
                              />
                              <div className="absolute top-1 left-1 w-5 h-5 rounded-full bg-[#e63946] text-white flex items-center justify-center text-[10px] font-bold shadow-xs">
                                {index + 1}
                              </div>
                            </div>
                            <div className="flex flex-col justify-between py-0.5 min-w-0">
                              <div>
                                <h5 className="font-serif text-sm font-bold text-slate-800 group-hover:text-[#e63946] transition-colors truncate">
                                  {spot.name}
                                </h5>
                                <p className="text-[11px] text-slate-500 font-light mt-1 line-clamp-2 leading-relaxed">
                                  {spot.description}
                                </p>
                              </div>
                              <div className="flex items-center gap-1 text-[9px] font-mono text-slate-400 mt-1">
                                <MapPin size={10} className="text-slate-400 shrink-0" />
                                <span className="truncate">{spot.lat}, {spot.lng}</span>
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  <div className="flex flex-col sm:flex-row justify-center items-center gap-4 pt-8">
                    <button
                      onClick={() => onSelectArticle(quizResult.id)}
                      className="w-full sm:w-auto px-8 py-4 bg-[#e63946] hover:bg-[#C1121F] text-white text-xs tracking-widest uppercase font-bold rounded-full transition-all duration-300 shadow-md flex items-center justify-center gap-2"
                    >
                      開啟深度指南 <ArrowRight size={14} />
                    </button>
                    <button
                      onClick={resetQuiz}
                      className="w-full sm:w-auto py-3 px-4 text-slate-500 hover:text-slate-800 text-xs font-bold uppercase tracking-widest underline decoration-[#e63946] underline-offset-4"
                    >
                      重新測驗
                    </button>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

          </div>
        </div>
      </section>

      {/* 3. 慢旅編輯推薦特輯 (JOURNAL GRID) */}
      <section id="magazine-section" className="py-24 max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-end mb-16 gap-6">
          <div>
            <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">慢旅深度紀事</span>
            <h2 className="font-serif text-4xl md:text-6xl font-semibold text-slate-900 tracking-tight leading-tight">精選探索專欄</h2>
            <div className="w-16 h-1 bg-[#06B6D4] mt-4"></div>
          </div>

          {/* 分類篩選藥丸 */}
          <div className="flex flex-wrap gap-2 pt-4">
            {[
              { id: 'All', label: '全部專欄' },
              { id: '日本自由行', label: '日本自由行' },
              { id: '韓國自由行', label: '韓國自由行' },
              { id: '台灣旅遊', label: '台灣旅遊' },
              { id: '東南亞自由行', label: '東南亞自由行' },
              { id: '旅遊工具', label: '旅遊工具' }
            ].map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(cat.id)}
                className={`px-5 py-2.5 rounded-full text-xs font-bold uppercase tracking-widest border transition-all duration-300 ${
                  selectedCategory === cat.id 
                    ? 'bg-[#1E293B] text-white border-[#1E293B] shadow-md' 
                    : 'bg-white text-slate-600 border-slate-200 hover:border-slate-400'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>

        {/* 搜尋無結果反饋 */}
        {filteredCustomPages.length === 0 && (
          <div className="text-center py-16 bg-slate-50 rounded-2xl border border-slate-200">
            <p className="text-slate-500 font-serif italic text-lg">「抱歉，沒有找到符合您搜尋條件的慢旅地標。試著用其他關鍵字探索看看。」</p>
            <button 
              onClick={() => { setSearchQuery(''); setSelectedCategory('All'); }}
              className="mt-4 px-6 py-2 bg-slate-900 text-white rounded-full text-xs tracking-widest uppercase font-bold"
            >
              重置篩選
            </button>
          </div>
        )}

        {/* 雜誌卡片網格 */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
          {(showAllArticles ? filteredCustomPages : filteredCustomPages.slice(0, 12)).map((page, idx) => {
            const isSaved = savedTripIds.includes(page.id);
            const region = page.category === '日本自由行' ? '日本' :
                           page.category === '韓國自由行' ? '韓國' :
                           page.category === '台灣旅遊' ? '台灣' :
                           page.category === '東南亞自由行' ? '東南亞' :
                           page.category === '旅遊工具' ? '工具箱' : '慢旅';

            // 動態估計閱讀時間
            const readTime = `${Math.max(3, Math.min(10, Math.ceil(page.title.length / 5)))} 分鐘`;

            // 動態產生一個高評分 (如 4.8, 4.9)
            const rating = (4.7 + (idx % 3) * 0.1).toFixed(1);

            return (
              <motion.article
                key={page.id}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-100px" }}
                transition={{ duration: 0.6, delay: idx * 0.1 }}
                className="group bg-white rounded-3xl border border-slate-200/50 shadow-sm hover:shadow-xl hover:border-[#e63946]/20 overflow-hidden flex flex-col h-[480px] transition-all duration-500"
              >
                {/* 封面圖片 */}
                <div className="relative h-48 overflow-hidden bg-slate-100 shrink-0">
                  <img
                    src={page.coverImage}
                    alt={page.title}
                    referrerPolicy="no-referrer"
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out"
                  />
                  {/* 省錢自由行標籤 */}
                  <div className="absolute top-4 left-4 z-10">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setSelectedCategory(page.category);
                        const el = document.getElementById('magazine-section');
                        if (el) {
                          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        }
                      }}
                      className="px-3 py-1 bg-slate-900/85 hover:bg-[#e63946] backdrop-blur-md text-slate-100 font-bold text-[10px] tracking-widest uppercase rounded-full transition-all duration-300 cursor-pointer hover:scale-105 active:scale-95 shadow-md"
                      title={`篩選 ${page.category}`}
                    >
                      {page.category}
                    </button>
                  </div>
                </div>

                {/* 卡片內容 */}
                <div className="p-6 flex flex-col flex-grow justify-between gap-4">
                  {/* 評分、國家 */}
                  <div className="flex justify-between items-center text-xs font-mono text-slate-500">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        const categoryMap: { [key: string]: string } = {
                          '日本': '日本自由行',
                          '韓國': '韓國自由行',
                          '台灣': '台灣旅遊',
                          '東南亞': '東南亞自由行',
                          '工具箱': '旅遊工具'
                        };
                        const targetCat = categoryMap[region] || 'All';
                        setSelectedCategory(targetCat);
                        const el = document.getElementById('magazine-section');
                        if (el) {
                          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        }
                      }}
                      className="flex items-center gap-1.5 px-2.5 py-1 bg-tiffany-cream hover:bg-[#e63946] text-slate-700 hover:text-white border border-slate-200/80 hover:border-[#e63946] rounded-full transition-all duration-300 font-bold tracking-wider cursor-pointer shadow-2xs hover:shadow-xs group/tag"
                      title={`篩選 ${region} 專欄`}
                    >
                      <MapPin size={11} className="text-[#e63946] group-hover/tag:text-white transition-colors duration-300" />
                      <span className="text-[10.5px] uppercase tracking-wider">{region}</span>
                    </button>
                    <span className="flex items-center gap-3">
                      <span className="flex items-center gap-0.5 text-[#FBBF24] font-bold"><Star size={11} className="fill-[#FBBF24] text-[#FBBF24]" /> {rating}</span>
                      <span className="w-1 h-1 bg-slate-300 rounded-full" />
                      <span className="flex items-center gap-1"><Clock size={11} /> 閱讀 {readTime}</span>
                    </span>
                  </div>

                  {/* 標題與副標題 */}
                  <h3 className="font-serif text-2xl font-bold leading-snug text-slate-950 group-hover:text-[#e63946] transition-colors line-clamp-2">
                    {page.title}
                  </h3>
                  
                  <p className="text-slate-500 text-sm font-light leading-relaxed line-clamp-3">
                    {page.intro}
                  </p>

                  <div className="pt-4 mt-auto border-t border-slate-100 flex items-center justify-between">
                    {/* 標籤 tags */}
                    <div className="flex items-center gap-1.5 overflow-hidden max-w-[65%]">
                      {page.tags.slice(0, 2).map(tag => {
                        const isHot = tag.includes('最新') || tag.includes('熱門') || tag.includes('推薦') || tag.includes('Hot');
                        return (
                          <span 
                            key={tag} 
                            className={`text-[9px] px-2 py-0.5 rounded-full font-medium whitespace-nowrap ${
                              isHot 
                                ? 'bg-[#FF6B35] text-white font-bold shadow-2xs' 
                                : 'bg-slate-100 text-slate-500'
                            }`}
                          >
                            #{tag}
                          </span>
                        );
                      })}
                    </div>

                    {/* 呼籲行動 */}
                    <button 
                      onClick={() => onSelectCustomPage(page.id)}
                      className="text-slate-900 group-hover:text-[#e63946] text-xs font-bold tracking-widest uppercase flex items-center gap-1 transition-all shrink-0"
                    >
                      開啟指南 <ArrowRight size={13} className="group-hover:translate-x-1 transition-transform" />
                    </button>
                  </div>

                </div>
              </motion.article>
            );
          })}
        </div>

        {/* 看更多按鈕 */}
        {filteredCustomPages.length > 12 && (
          <div className="flex justify-center mt-14">
            <button
              onClick={() => setShowAllArticles(!showAllArticles)}
              className="px-8 py-3.5 bg-[#e63946] hover:bg-[#C1121F] text-white font-bold text-xs tracking-widest uppercase rounded-full transition-all duration-300 shadow-md flex items-center gap-2 group cursor-pointer"
            >
              {showAllArticles ? '收合文章' : '看更多文章'}
              <ArrowRight size={14} className={`transition-transform duration-300 ${showAllArticles ? '-rotate-90' : 'group-hover:translate-x-1'}`} />
            </button>
          </div>
        )}
      </section>

      {/* 4. 互動式「專屬藍圖」行程策劃大師 */}
      <section className="py-24 bg-gradient-to-b from-[#020617] via-[#0d1527] to-[#1e293b] text-white overflow-hidden relative">
        <div className="absolute top-0 left-0 w-full h-full opacity-10 pointer-events-none">
          <div className="w-[500px] h-[500px] rounded-full bg-slate-800 blur-[130px] absolute top-[-100px] left-[-150px]"></div>
          <div className="w-[500px] h-[500px] rounded-full bg-[#e63946] blur-[150px] absolute bottom-[-150px] right-[-150px]"></div>
        </div>

        <div className="container mx-auto px-6 max-w-7xl relative z-10">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
            
            {/* 策劃控制面板 */}
            <div className="lg:col-span-5 space-y-8">
              <div>
                <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">慢旅智聯規劃師</span>
                <h2 className="font-serif text-3xl md:text-5xl font-semibold tracking-tight text-white leading-tight">量身定制您的省錢之旅</h2>
                <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
                <p className="text-slate-400 font-light text-sm leading-relaxed">
                  點選您有興趣目的地、旅伴模式與核心感官偏好，我們將即時計算出最合適的推薦預算與每日漫遊亮點。
                </p>
              </div>

              {/* 選擇 1: 目的地 */}
              <div className="space-y-3">
                <label className="text-xs font-bold uppercase tracking-widest text-[#e63946] block">1. 選擇夢想目的地</label>
                <div className="grid grid-cols-2 gap-2">
                  {[
                    { id: 'japan', name: '日本自由行' },
                    { id: 'korea', name: '韓國自由行' },
                    { id: 'taiwan', name: '台灣旅遊' },
                    { id: 'southeast-asia', name: '東南亞自由行' }
                  ].map((d) => (
                    <button
                      key={d.id}
                      onClick={() => setJourneyDestination(d.id)}
                      className={`px-4 py-3 rounded-xl text-xs font-bold uppercase tracking-widest border transition-all ${
                        journeyDestination === d.id
                          ? 'bg-[#e63946] text-white border-[#e63946] shadow-md scale-105'
                          : 'bg-slate-900 text-slate-400 border-slate-800 hover:border-slate-600'
                      }`}
                    >
                      {d.name}
                    </button>
                  ))}
                </div>
              </div>

              {/* 選擇 2: 同行對象 */}
              <div className="space-y-3">
                <label className="text-xs font-bold uppercase tracking-widest text-[#e63946] block">2. 伴侶模式與同行人數</label>
                <div className="grid grid-cols-3 gap-2">
                  {[
                    { id: 'Solo', name: '獨行探路' },
                    { id: 'Couple', name: '雙人漫步' },
                    { id: 'Family', name: '家族同行' }
                  ].map((st) => (
                    <button
                      key={st.id}
                      onClick={() => setJourneyStyle(st.id)}
                      className={`px-4 py-3 rounded-xl text-xs font-bold uppercase tracking-widest border transition-all ${
                        journeyStyle === st.id
                          ? 'bg-white text-slate-950 border-white shadow-md scale-105'
                          : 'bg-slate-900 text-slate-400 border-slate-800 hover:border-slate-600'
                      }`}
                    >
                      {st.name}
                    </button>
                  ))}
                </div>
              </div>

              {/* 選擇 3: 體驗核心 */}
              <div className="space-y-3">
                <label className="text-xs font-bold uppercase tracking-widest text-[#e63946] block">3. 核心感官探索主題</label>
                <div className="grid grid-cols-4 gap-2">
                  {[
                    { id: 'Culture', name: '人文印記' },
                    { id: 'Nature', name: '自然奇觀' },
                    { id: 'Culinary', name: '慢食美學' },
                    { id: 'Photos', name: '光影定格' }
                  ].map((fc) => (
                    <button
                      key={fc.id}
                      onClick={() => setJourneyFocus(fc.id)}
                      className={`px-1 py-3 rounded-xl text-[10px] font-bold uppercase tracking-wider border transition-all ${
                        journeyFocus === fc.id
                          ? 'bg-white text-slate-950 border-white shadow-md scale-105'
                          : 'bg-slate-900 text-slate-400 border-slate-800 hover:border-slate-600'
                      }`}
                    >
                      {fc.name}
                    </button>
                  ))}
                </div>
              </div>
            </div>

            {/* 生成的視覺行程藍圖 */}
            <div className="lg:col-span-7 bg-gradient-to-br from-[#1e293b] to-[#020617] border border-slate-800 p-8 md:p-12 rounded-2xl shadow-2xl relative">
              <div className="absolute top-4 right-4 flex items-center gap-1.5 px-3 py-1 bg-slate-800 rounded-full text-[10px] font-bold tracking-widest uppercase text-[#e63946]">
                <Map size={12} /> 方案構建中
              </div>
              
              <div className="space-y-6">
                <div>
                  <span className="text-xs font-mono text-slate-500 uppercase tracking-widest">慢旅定制藍圖編號 No. 2026</span>
                  <h3 className="font-serif text-2xl text-white font-bold mt-1">{customJourney.title}</h3>
                </div>

                <div className="relative border-l border-slate-800 pl-6 space-y-8 py-2">
                  {customJourney.days.map((day, idx) => (
                    <div key={idx} className="relative group">
                      {/* 節點 */}
                      <span className="absolute left-[-31px] top-1 w-4.5 h-4.5 bg-[#e63946] rounded-full border-4 border-slate-900 flex items-center justify-center text-[10px] text-white font-bold" />
                      
                      <div className="space-y-1.5">
                        <div className="flex justify-between items-center">
                          <span className="text-xs font-bold uppercase tracking-widest text-slate-400">{day.time} — DAY {day.day}</span>
                          <span className="text-xs font-mono text-[#e63946]">估計花費: {day.cost}</span>
                        </div>
                        <p className="text-sm font-medium text-slate-200 leading-relaxed">
                          {day.activity}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>

                <div className="pt-6 border-t border-slate-800 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500 block">整體預估在地開銷</span>
                    <span className="font-serif text-2xl font-bold text-[#e63946]">
                      {journeyDestination === 'japan' ? '約 25,000 日圓' : 
                       journeyDestination === 'korea' ? '約 240,000 韓元' : 
                       journeyDestination === 'taiwan' ? '約 4,800 台幣' : '約 4,200 泰銖 / 披索'}
                    </span>
                  </div>
                  <button 
                    onClick={() => {
                      const targetId = 
                        journeyDestination === 'japan' ? 'japan-budget-guide' : 
                        journeyDestination === 'korea' ? 'korea-budget' : 
                        journeyDestination === 'taiwan' ? 'taipei-food' : 'seasia-budget-travel-guide';
                      onSelectCustomPage(targetId);
                    }}
                    className="w-full sm:w-auto px-6 py-3 bg-[#e63946] hover:bg-[#C1121F] text-white text-xs font-bold tracking-widest uppercase rounded-full transition-all flex items-center justify-center gap-2"
                  >
                    載入完整探索指南 <ArrowRight size={13} />
                  </button>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>



    </div>
  );
};
