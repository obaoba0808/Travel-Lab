import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  ArrowLeft, Calendar, Clock, Star, Heart, Check, ChevronDown,
  Info, Plus, MessageSquare, Trash2, MapPin, Globe, Share2, Compass, 
  Sun, Leaf, Snowflake, Flower, Camera, CloudSun
} from 'lucide-react';
import { TravelArticle, Comment } from '../types';
import { Breadcrumb } from './Breadcrumb';

interface ArticleViewProps {
  article: TravelArticle;
  onBackToHome: () => void;
  isSaved: boolean;
  onToggleSave: () => void;
}

export const ArticleView: React.FC<ArticleViewProps> = ({
  article,
  onBackToHome,
  isSaved,
  onToggleSave
}) => {
  const [scrollProgress, setScrollProgress] = useState(0);
  const [activeSection, setActiveSection] = useState('intro');
  const [expandedDay, setExpandedDay] = useState<number | null>(1);
  const [selectedMapSpot, setSelectedMapSpot] = useState<number>(0);
  
  // Budget Customizer states
  const [daysCount, setDaysCount] = useState<number>(3);
  const [hotelTier, setHotelTier] = useState<'budget' | 'boutique' | 'luxury'>('boutique');
  const [diningTier, setDiningTier] = useState<'street' | 'bistro' | 'fine'>('bistro');
  
  // Packing list state
  const [packingItems, setPackingItems] = useState<{ id: string; text: string; checked: boolean; category: string }[]>([]);
  const [newItemText, setNewItemText] = useState('');
  const [newItemCategory, setNewItemCategory] = useState('Essentials');

  // Comments state
  const [comments, setComments] = useState<Comment[]>([]);
  const [newCommentName, setNewCommentName] = useState('');
  const [newCommentRating, setNewCommentRating] = useState(5);
  const [newCommentText, setNewCommentText] = useState('');
  const [commentSuccess, setCommentSuccess] = useState(false);
  const [hoveredStar, setHoveredStar] = useState<number | null>(null);

  // Photo Lightbox state
  const [lightboxIndex, setLightboxIndex] = useState<number | null>(null);
  
  // Copy Link State
  const [copiedLink, setCopiedLink] = useState(false);

  // Dynamic Table of Contents (TOC) states
  const mainContentRef = useRef<HTMLDivElement>(null);
  const [toc, setToc] = useState<{ id: string; text: string }[]>([]);
  const [activeHeadingId, setActiveHeadingId] = useState<string>('');
  const [isMobileTocOpen, setIsMobileTocOpen] = useState(false);

  // Refs for scroll tracking
  const sectionsRef = {
    intro: useRef<HTMLDivElement>(null),
    itinerary: useRef<HTMLDivElement>(null),
    routemap: useRef<HTMLDivElement>(null),
    budget: useRef<HTMLDivElement>(null),
    weather: useRef<HTMLDivElement>(null),
    packing: useRef<HTMLDivElement>(null),
    comments: useRef<HTMLDivElement>(null),
  };

  // Generate Table of Contents from h2 tags dynamically
  useEffect(() => {
    const timer = setTimeout(() => {
      if (mainContentRef.current) {
        const headings = mainContentRef.current.querySelectorAll('h2');
        const items: { id: string; text: string }[] = [];
        headings.forEach((heading, index) => {
          let id = heading.id;
          if (!id) {
            id = `article-h2-${index}`;
            heading.id = id;
          }
          items.push({
            id,
            text: heading.textContent || ''
          });
        });
        setToc(items);
        if (items.length > 0) {
          setActiveHeadingId(items[0].id);
        }
      }
    }, 150);

    return () => clearTimeout(timer);
  }, [article.id]);

  // Track scroll position to update active TOC heading
  useEffect(() => {
    const handleHeadingScroll = () => {
      if (!mainContentRef.current || toc.length === 0) return;
      const headings = mainContentRef.current.querySelectorAll('h2');
      const scrollPosition = window.scrollY + 120; // Offset for sticky headers and padding

      let currentActiveId = '';
      for (let i = 0; i < headings.length; i++) {
        const heading = headings[i];
        if (heading.offsetTop <= scrollPosition) {
          currentActiveId = heading.id;
        } else {
          break;
        }
      }

      if (currentActiveId) {
        setActiveHeadingId(currentActiveId);
      }
    };

    window.addEventListener('scroll', handleHeadingScroll);
    return () => window.removeEventListener('scroll', handleHeadingScroll);
  }, [toc]);

  // 動態 SEO Head 標籤與結構化數據 (JSON-LD) 注入
  useEffect(() => {
    const originalTitle = document.title;
    document.title = `${article.title}｜均在路上 Travel Lab`;

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
    setMetaTag('name', 'description', article.intro || '');
    setMetaTag('name', 'robots', 'index, follow');

    // 設定關鍵字
    const pageKeywords = `${article.title}, ${article.country}旅遊, 自由行, 旅遊攻略, 均在路上`;
    setMetaTag('name', 'keywords', pageKeywords);

    // 設定 Canonical
    const originalCanonicalElement = document.querySelector('link[rel="canonical"]');
    const originalCanonical = originalCanonicalElement ? originalCanonicalElement.getAttribute('href') : '';
    const pageUrl = `https://golightly.fun/articles/${article.id}.html`;
    setLinkTag('canonical', pageUrl);

    // 設定 Open Graph 標籤
    setMetaTag('property', 'og:title', `${article.title}｜均在路上 Travel Lab`);
    setMetaTag('property', 'og:description', article.intro || '');
    setMetaTag('property', 'og:image', article.heroImage || '');
    setMetaTag('property', 'og:url', pageUrl);
    setMetaTag('property', 'og:type', 'article');

    // 設定 Twitter 標籤
    setMetaTag('name', 'twitter:card', 'summary_large_image');
    setMetaTag('name', 'twitter:title', `${article.title}｜均在路上 Travel Lab`);
    setMetaTag('name', 'twitter:description', article.intro || '');
    setMetaTag('name', 'twitter:image', article.heroImage || '');

    // 移除舊的動態 JSON-LD
    const existingJsonLd = document.getElementById('dynamic-jsonld');
    if (existingJsonLd) {
      existingJsonLd.remove();
    }

    // 插入新動態 JSON-LD
    const script = document.createElement('script');
    script.id = 'dynamic-jsonld';
    script.type = 'application/ld+json';

    const jsonLdContent = {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": article.title,
      "image": article.heroImage || "https://golightly.fun/images/logo.webp",
      "genre": article.category || "旅遊攻略",
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
      "datePublished": article.publishDate || "2026-06-25",
      "author": {
        "@type": "Person",
        "name": article.author?.name || "Kristian Sigurd"
      },
      "description": article.intro || ""
    };

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
  }, [article]);

  // Initialize and load persistent user state
  useEffect(() => {
    window.scrollTo({ top: 0 });

    const handleScroll = () => {
      const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
      if (totalScroll > 0) {
        setScrollProgress((window.scrollY / totalScroll) * 100);
      }

      const scrollPos = window.scrollY + 200;
      for (const [key, ref] of Object.entries(sectionsRef)) {
        const el = ref.current;
        if (el) {
          const top = el.offsetTop;
          const height = el.offsetHeight;
          if (scrollPos >= top && scrollPos < top + height) {
            setActiveSection(key);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);

    // Load packing list
    const savedPacking = localStorage.getItem(`packing_${article.id}`);
    if (savedPacking) {
      setPackingItems(JSON.parse(savedPacking));
    } else {
      const defaults = article.packingList.flatMap(cat => 
        cat.items.map((item, idx) => ({
          id: `${cat.category}_${idx}`,
          text: item,
          checked: false,
          category: cat.category
        }))
      );
      setPackingItems(defaults);
      localStorage.setItem(`packing_${article.id}`, JSON.stringify(defaults));
    }

    // Load Comments
    const savedComments = localStorage.getItem(`comments_${article.id}`);
    if (savedComments) {
      setComments(JSON.parse(savedComments));
    } else {
      // Seed initial reviews in Traditional Chinese
      const seeded: Comment[] = [
        {
          id: 's1',
          userName: 'Charlotte Dubois',
          rating: 5,
          content: `絕佳的慢旅深度指南！我幾乎一字不差地遵循了這個三日行程，真的讓我們的旅程無比輕鬆而充實。每日的地圖與地標推薦省去了我們大量的規劃時間，特別是提早起床前往 ${article.id === 'kyoto' ? '嵐山竹林' : article.id === 'switzerland' ? '施陶巴赫瀑布' : '塞里雅蘭瀑布'} 的建議，讓我們避開了擁擠人潮，捕捉到了最神聖、寧靜的光影。強烈推薦！`,
          date: '2026年5月28日'
        },
        {
          id: 's2',
          userName: '佐藤 健治',
          rating: 4,
          content: `這篇指南裡提到的攝影建議完全精準。SVG 互動式地圖上的經緯度坐標與地景非常符合實際。感謝推薦在地旅宿防坑技巧，真的是背包客的救星。`,
          date: '2026年6月10日'
        }
      ];
      setComments(seeded);
      localStorage.setItem(`comments_${article.id}`, JSON.stringify(seeded));
    }

    return () => window.removeEventListener('scroll', handleScroll);
  }, [article.id]);

  // Handle Packing List Toggle
  const handleTogglePacking = (id: string) => {
    const updated = packingItems.map(item => 
      item.id === id ? { ...item, checked: !item.checked } : item
    );
    setPackingItems(updated);
    localStorage.setItem(`packing_${article.id}`, JSON.stringify(updated));
  };

  // Add Custom Packing Item
  const handleAddPackingItem = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newItemText.trim()) return;

    const newItem = {
      id: `custom_${Date.now()}`,
      text: newItemText.trim(),
      checked: false,
      category: newItemCategory
    };

    const updated = [...packingItems, newItem];
    setPackingItems(updated);
    localStorage.setItem(`packing_${article.id}`, JSON.stringify(updated));
    setNewItemText('');
  };

  // Delete Packing Item
  const handleDeletePackingItem = (id: string) => {
    const updated = packingItems.filter(item => item.id !== id);
    setPackingItems(updated);
    localStorage.setItem(`packing_${article.id}`, JSON.stringify(updated));
  };

  // Handle Comment Submission
  const handleAddComment = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newCommentName.trim() || !newCommentText.trim()) return;

    const newComment: Comment = {
      id: `comm_${Date.now()}`,
      userName: newCommentName.trim(),
      rating: newCommentRating,
      content: newCommentText.trim(),
      date: new Date().toLocaleDateString('zh-TW', { year: 'numeric', month: 'long', day: 'numeric' })
    };

    const updated = [newComment, ...comments];
    setComments(updated);
    localStorage.setItem(`comments_${article.id}`, JSON.stringify(updated));
    
    setNewCommentName('');
    setNewCommentText('');
    setNewCommentRating(5);
    setCommentSuccess(true);
    setTimeout(() => setCommentSuccess(false), 4000);
  };

  const handleDeleteComment = (id: string) => {
    const updated = comments.filter(c => c.id !== id);
    setComments(updated);
    localStorage.setItem(`comments_${article.id}`, JSON.stringify(updated));
  };

  // Copy Link Action
  const handleCopyLink = () => {
    navigator.clipboard.writeText(window.location.href);
    setCopiedLink(true);
    setTimeout(() => setCopiedLink(false), 3000);
  };

  // Budget calculations
  const calculateBudget = () => {
    const hotelRates = { budget: 45, boutique: 130, luxury: 290 };
    const diningRates = { street: 15, bistro: 40, fine: 110 };
    const baseActivityRate = article.budgetEstimates.activityBudget;

    const hotelTotal = daysCount * hotelRates[hotelTier];
    const diningTotal = daysCount * diningRates[diningTier];
    const activityTotal = daysCount * baseActivityRate;
    const flightTotal = article.budgetEstimates.flightBudget;

    const total = hotelTotal + diningTotal + activityTotal + flightTotal;

    return {
      hotel: hotelTotal,
      dining: diningTotal,
      activities: activityTotal,
      flights: flightTotal,
      total
    };
  };

  const budgetBreakdown = calculateBudget();

  // Scroll smoothly to section
  const scrollToSection = (sectionName: string) => {
    const element = sectionsRef[sectionName as keyof typeof sectionsRef]?.current;
    if (element) {
      const headerOffset = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  };

  // Scroll smoothly to specific dynamic heading
  const scrollToHeading = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      const headerOffset = 90;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
      setActiveHeadingId(id);
    }
  };

  // Packing list stats
  const getPackingStats = () => {
    if (packingItems.length === 0) return 0;
    const checkedCount = packingItems.filter(item => item.checked).length;
    return Math.round((checkedCount / packingItems.length) * 100);
  };

  const packingProgress = getPackingStats();

  // Photos for Lightbox
  const galleryPhotos = [
    article.heroImage,
    ...article.itinerary.map(day => day.image),
    ...article.mapSpots.map(spot => spot.image)
  ].filter((v, i, a) => a.indexOf(v) === i);

  return (
    <div className="bg-tiffany-cream min-h-screen text-slate-800 pb-12 relative">
      <Breadcrumb title={article.title} category={article.country ? `${article.country}自由行` : undefined} />
      
      {/* 頂部 Tiffany 綠進度條 */}
      <div 
        className="fixed top-0 left-0 h-1 bg-[#e63946] z-50 transition-all duration-100 ease-out" 
        style={{ width: `${scrollProgress}%` }}
      />

      {/* 左側懸浮目錄導航 (僅桌機顯示) */}
      <aside className="hidden xl:block fixed left-6 top-24 z-40 w-64 p-5 bg-white/85 backdrop-blur-md rounded-2xl border border-slate-200/60 shadow-lg space-y-4 max-h-[75vh] overflow-y-auto">
        <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#e63946] block border-b border-slate-100 pb-2">文章大綱目錄</span>
        <nav className="flex flex-col gap-3 text-xs font-medium tracking-wide text-slate-500">
          {toc.length > 0 ? (
            toc.map((item, idx) => (
              <button
                key={item.id}
                onClick={() => scrollToHeading(item.id)}
                className={`text-left transition-all duration-300 cursor-pointer relative py-1 pl-3 leading-relaxed border-l-2 ${
                  activeHeadingId === item.id 
                    ? 'text-slate-950 border-[#e63946] font-semibold font-sans' 
                    : 'hover:text-slate-800 border-transparent hover:border-slate-300'
                }`}
              >
                <span className="font-mono text-[9px] opacity-65 block mb-0.5">0{idx + 1}.</span>
                {item.text}
              </button>
            ))
          ) : (
            [
              { id: 'intro', label: '1. 深度序章' },
              { id: 'itinerary', label: '2. 三日行程藍圖' },
              { id: 'routemap', label: '3. 地理坐標地圖' },
              { id: 'budget', label: '4. 智慧預算規劃' },
              { id: 'weather', label: '5. 氣候與季節建議' },
              { id: 'packing', label: '6. 出行裝備清單' },
              { id: 'comments', label: '7. 旅人評價反饋' }
            ].map((sec) => (
              <button
                key={sec.id}
                onClick={() => scrollToSection(sec.id)}
                className={`text-left transition-all duration-300 cursor-pointer relative py-1.5 pl-3 leading-relaxed border-l-2 ${
                  activeSection === sec.id 
                    ? 'text-slate-950 border-[#e63946] font-semibold' 
                    : 'hover:text-slate-800 border-transparent hover:border-slate-300'
                }`}
              >
                {sec.label}
              </button>
            ))
          )}
        </nav>
      </aside>

      {/* 導航列 */}
      <nav className="sticky top-0 bg-tiffany-cream/90 backdrop-blur-md z-45 border-b border-tiffany-ice/40 py-4">
        <div className="container mx-auto px-6 max-w-7xl flex justify-between items-center">
          <button 
            onClick={onBackToHome}
            className="flex items-center gap-2 text-slate-600 hover:text-slate-900 transition-colors text-xs font-bold uppercase tracking-widest cursor-pointer"
          >
            <ArrowLeft size={16} /> 返回探索日誌
          </button>
          
          <div className="flex items-center gap-4">
            <button
              onClick={handleCopyLink}
              className="p-2 border border-slate-200 rounded-full hover:bg-slate-100 transition-colors text-slate-600 cursor-pointer"
              title="複製指南連結"
            >
              <Share2 size={16} />
            </button>
            <button
              onClick={onToggleSave}
              className={`flex items-center gap-2 px-5 py-2.5 rounded-full text-xs font-bold uppercase tracking-widest border transition-all duration-300 cursor-pointer ${
                isSaved 
                  ? 'bg-[#e63946] border-[#e63946] text-white' 
                  : 'bg-white border-slate-200 text-slate-600 hover:border-[#e63946]/50 hover:text-[#e63946]'
              }`}
            >
              <Heart size={14} className={isSaved ? 'fill-white' : ''} /> {isSaved ? '已珍藏' : '珍藏指南'}
            </button>
          </div>
        </div>
      </nav>

      {/* 複製連結反饋 */}
      <AnimatePresence>
        {copiedLink && (
          <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="fixed top-18 left-1/2 transform -translate-x-1/2 z-50 bg-[#020617] text-white text-xs tracking-wider uppercase font-bold px-6 py-3 rounded-full shadow-lg"
          >
            指南連結已成功複製到剪貼簿。
          </motion.div>
        )}
      </AnimatePresence>

      {/* 沉浸式文章巨幕 - 無裁剪整張顯示 */}
      <header className="relative w-full bg-slate-950 overflow-hidden">
        {/* HERO IMAGE - FULLY UNMASKED */}
        <div className="w-full overflow-hidden bg-slate-950">
          <img 
            alt={article.title} 
            src={article.heroImage} 
            className="w-full h-auto block mx-auto object-cover hover:scale-[1.01] transition-transform duration-700"
            style={{ filter: 'brightness(0.85)', objectFit: 'cover' }}
          />
        </div>
        
        {/* HERO CONTENT BLOCK */}
        <div className="py-8 px-6 md:py-10 md:px-12 text-center bg-white space-y-5 border-b border-slate-100">
          <div className="flex flex-wrap items-center justify-center gap-2 md:gap-3">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 bg-slate-50 border border-slate-200 rounded-full text-[10px] font-bold tracking-[0.15em] uppercase text-[#e63946]">
              <Globe size={11} /> 沉浸慢旅期刊 • {article.country.toUpperCase()}
            </span>
            <span className="inline-flex items-center gap-1.5 px-3 py-1 bg-teal-50 border border-teal-100 rounded-full text-[10px] font-bold tracking-[0.15em] uppercase text-teal-700">
              <Compass size={11} /> 體驗 • {article.category}
            </span>
            <span className="inline-flex items-center gap-1.5 px-3 py-1 bg-amber-50 border border-amber-100 rounded-full text-[10px] font-bold tracking-[0.15em] uppercase text-amber-700">
              <Sun size={11} /> 季節 • {article.bestSeason}
            </span>
            <span className="inline-flex items-center gap-1.5 px-3 py-1 bg-indigo-50 border border-indigo-100 rounded-full text-[10px] font-bold tracking-[0.15em] uppercase text-indigo-700">
              <Leaf size={11} /> 氛圍 • {article.vibe}
            </span>
          </div>
          
          <h1 className="font-serif text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-wide leading-tight text-slate-900 max-w-4xl mx-auto">
            {article.title}
          </h1>

          {article.subtitle && (
            <p className="text-sm md:text-base text-slate-500 max-w-2xl mx-auto italic font-serif leading-relaxed">
              {article.subtitle}
            </p>
          )}

          {/* 作者與屬性資料列 */}
          <div className="flex flex-wrap items-center justify-center gap-6 pt-4 text-slate-500 border-t border-slate-100 pb-2">
            <div className="flex items-center gap-3">
              <img 
                src={article.author.avatar} 
                alt={article.author.name}
                referrerPolicy="no-referrer"
                className="w-10 h-10 rounded-full object-cover border border-[#e63946]"
              />
              <div className="text-left">
                <p className="text-xs font-bold text-slate-800">{article.author.name}</p>
                <p className="text-[10px] text-slate-400 tracking-wider uppercase">{article.author.role}</p>
              </div>
            </div>

            <div className="h-8 w-px bg-slate-200 hidden sm:block" />

            <div className="flex gap-6 text-xs font-mono">
              <span className="flex items-center gap-1.5 text-slate-600">
                <Calendar size={13} className="text-[#e63946]" /> {article.publishDate}
              </span>
              <span className="flex items-center gap-1.5 text-slate-600">
                <Clock size={13} className="text-[#e63946]" /> {article.readTime}
              </span>
              <span className="flex items-center gap-1.5 text-slate-600">
                <Star size={13} className="fill-[#FBBF24] text-[#FBBF24]" /> {article.rating}
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* 核心佈局區域 */}
      <main ref={mainContentRef} className="container mx-auto px-6 max-w-5xl py-12">
        {/* Mobile/Tablet Table of Contents Card (Visible below xl screen) */}
        {toc.length > 0 && (
          <div className="xl:hidden bg-white border border-slate-200/80 rounded-2xl p-5 shadow-md mb-8">
            <button 
              onClick={() => setIsMobileTocOpen(!isMobileTocOpen)}
              className="w-full flex justify-between items-center text-xs font-bold uppercase tracking-wider text-slate-800 cursor-pointer"
            >
              <span className="flex items-center gap-2">
                <Compass size={14} className="text-[#e63946] animate-spin-slow" />
                快速導覽目錄 ({toc.length} 個章節)
              </span>
              <span className="text-[10px] text-slate-500 font-mono">
                {isMobileTocOpen ? '收合 [-]' : '展開 [+]'}
              </span>
            </button>
            
            <AnimatePresence>
              {isMobileTocOpen && (
                <motion.div
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: 'auto', opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  transition={{ duration: 0.25 }}
                  className="overflow-hidden"
                >
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-4 mt-3 border-t border-slate-100">
                    {toc.map((item, idx) => (
                      <button
                        key={item.id}
                        onClick={() => {
                          scrollToHeading(item.id);
                          setIsMobileTocOpen(false);
                        }}
                        className={`text-left p-2.5 rounded-xl text-xs transition-all flex items-center gap-2 cursor-pointer border ${
                          activeHeadingId === item.id
                            ? 'bg-red-50 border-red-150 text-[#e63946] font-semibold'
                            : 'bg-slate-50/50 border-slate-150 text-slate-600 hover:bg-slate-100'
                        }`}
                      >
                        <span className="font-mono text-[9px] text-[#e63946] bg-[#e63946]/10 px-1.5 py-0.5 rounded-sm">
                          {idx + 1}
                        </span>
                        <span className="truncate flex-1">{item.text}</span>
                      </button>
                    ))}
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        )}

        <div className="grid grid-cols-1 gap-16">
          
          {/* 1. 深度序章區 */}
          <section id="intro" ref={sectionsRef.intro} className="space-y-8 scroll-mt-24">
            <div className="prose prose-stone max-w-none text-tiffany-obsidian/90 leading-relaxed text-lg md:text-xl font-light space-y-6">
              <p>
                <span className="text-6xl md:text-7xl float-left mr-3 mt-1 font-serif text-[#e63946] font-bold leading-[0.8] border border-tiffany-ice p-2.5 bg-tiffany-cream rounded-lg">
                  {article.intro.charAt(0)}
                </span>
                {article.intro.slice(1)}
              </p>
              
              {article.content.slice(0, 2).map((para, idx) => (
                <p key={idx} className="text-tiffany-obsidian/95 leading-relaxed">{para}</p>
              ))}
            </div>

            {/* 引述區 */}
            <div className="border-l-4 border-[#e63946] bg-white p-8 md:p-12 rounded-r-2xl my-10 relative overflow-hidden shadow-xs border-y border-r border-tiffany-ice/30">
              <div className="absolute top-2 right-4 font-serif text-9xl text-tiffany-ice/30 pointer-events-none">”</div>
              <blockquote className="font-serif italic text-xl md:text-2xl text-tiffany-obsidian leading-relaxed max-w-3xl relative z-10">
                「{article.quote}」
              </blockquote>
              <cite className="block text-xs font-bold uppercase tracking-widest text-[#e63946] mt-4 font-mono">
                — {article.quoteAuthor} · 現場行紀
              </cite>
            </div>

            <div className="prose prose-stone max-w-none text-tiffany-obsidian/90 leading-relaxed text-lg md:text-xl font-light">
              <p className="text-tiffany-obsidian/95 leading-relaxed">{article.content[2]}</p>
            </div>

            {/* 慢旅高光特色卡片 */}
            <div className="bg-white border border-tiffany-ice rounded-2xl p-8 md:p-10 shadow-xs mt-8">
              <span className="text-[10px] font-bold uppercase tracking-[0.25em] text-[#e63946] block mb-4">探索高光時刻</span>
              <h3 className="font-serif text-2xl text-tiffany-obsidian font-bold mb-6">不容錯過的感官體驗</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {article.highlights.map((high, idx) => (
                  <div key={idx} className="flex gap-3 items-start bg-tiffany-cream/50 p-4 rounded-xl border border-tiffany-ice/40">
                    <span className="p-1 bg-[#e63946]/10 rounded-full text-[#e63946] shrink-0">
                      <Check size={14} />
                    </span>
                    <span className="text-tiffany-obsidian/90 text-sm font-medium leading-snug">{high}</span>
                  </div>
                ))}
              </div>
            </div>
          </section>

          {/* 2. 三日行程藍圖 */}
          <section id="itinerary" ref={sectionsRef.itinerary} className="space-y-8 scroll-mt-24">
            <div className="border-t border-slate-200 pt-16">
              <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">精心編製路線</span>
              <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">三日深度探索藍圖</h2>
              <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
              <p className="text-slate-500 font-light max-w-2xl text-base leading-relaxed">
                我們為您精心策劃了一條穿梭於 {article.country} 的深度慢旅路線。展開每一天查看具體推薦、預算估算及不容錯過的攝影機位與獨家旅行秘訣。
              </p>
            </div>

            {/* 摺疊面板 */}
            <div className="space-y-4">
              {article.itinerary.map((day) => {
                const isOpen = expandedDay === day.day;
                return (
                  <div 
                    key={day.day}
                    className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-xs transition-all duration-300"
                  >
                    <button
                      onClick={() => setExpandedDay(isOpen ? null : day.day)}
                      className="w-full flex justify-between items-center p-6 md:p-8 text-left focus:outline-none hover:bg-slate-50/50 cursor-pointer"
                    >
                      <div className="flex items-center gap-4">
                        <span className="w-10 h-10 rounded-full bg-slate-900 text-white font-mono flex items-center justify-center font-bold text-sm">
                          {day.day}
                        </span>
                        <div>
                          <span className="text-[10px] font-bold tracking-widest text-[#e63946] uppercase block">第 {day.day} 天 · 慢旅日誌</span>
                          <h3 className="font-serif text-xl md:text-2xl font-bold text-slate-950 mt-0.5">{day.title}</h3>
                        </div>
                      </div>
                      <ChevronDown 
                        size={20} 
                        className={`text-slate-400 transition-transform duration-300 ${isOpen ? 'transform rotate-180 text-[#e63946]' : ''}`} 
                      />
                    </button>

                    <AnimatePresence initial={false}>
                      {isOpen && (
                        <motion.div
                          initial={{ height: 0 }}
                          animate={{ height: 'auto' }}
                          exit={{ height: 0 }}
                          transition={{ duration: 0.3, ease: 'easeInOut' }}
                          className="overflow-hidden border-t border-slate-100 bg-slate-50/40"
                        >
                          <div className="p-6 md:p-8 grid grid-cols-1 md:grid-cols-12 gap-8 items-start">
                            
                            <div className="md:col-span-7 space-y-6">
                              <p className="text-slate-600 text-sm md:text-base leading-relaxed">
                                {day.description}
                              </p>

                              {/* 今日目的地標籤 */}
                              <div className="space-y-2">
                                <span className="text-[10px] font-bold uppercase tracking-widest text-slate-400 block">今日探索地標</span>
                                <div className="flex flex-wrap gap-2">
                                  {day.spots.map((spot, sidx) => (
                                    <span key={sidx} className="inline-flex items-center gap-1 px-3 py-1 bg-white border border-slate-200 text-slate-700 text-xs font-semibold rounded-lg shadow-2xs">
                                      <MapPin size={11} className="text-[#e63946]" /> {spot}
                                    </span>
                                  ))}
                                </div>
                              </div>

                              {/* 深度私房秘訣 */}
                              <div className="p-4 bg-[#F59E0B]/10 border-l-2 border-[#F59E0B] rounded-r-xl space-y-1">
                                <span className="text-[10px] font-bold uppercase tracking-widest text-[#F59E0B] flex items-center gap-1"><Info size={12} /> 深度旅行秘訣</span>
                                <p className="text-xs text-slate-700 leading-relaxed font-medium">{day.tips}</p>
                              </div>

                              <div className="flex justify-between items-center text-xs font-mono border-t border-slate-100 pt-4 text-slate-500">
                                <span>今日在地開銷估計: <strong className="text-[#e63946]">{day.costEstimate}</strong></span>
                              </div>
                            </div>

                            {/* 今日精選照片 */}
                            <div className="md:col-span-5 relative rounded-xl overflow-hidden aspect-[4/3] shadow-inner bg-slate-200">
                              <img 
                                src={day.image} 
                                alt={day.title}
                                referrerPolicy="no-referrer"
                                className="w-full h-full object-cover hover:scale-105 transition-transform duration-500 cursor-pointer"
                                onClick={() => {
                                  const photoIdx = galleryPhotos.indexOf(day.image);
                                  if (photoIdx !== -1) setLightboxIndex(photoIdx);
                                }}
                              />
                              <div className="absolute bottom-3 right-3 bg-black/60 px-2.5 py-1 rounded-full text-[10px] text-white flex items-center gap-1.5 pointer-events-none">
                                <Camera size={10} /> 放大看圖
                              </div>
                            </div>

                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                );
              })}
            </div>
          </section>

          {/* 3. 互動式 SVGTopographical 地圖 */}
          <section id="routemap" ref={sectionsRef.routemap} className="space-y-8 scroll-mt-24">
            <div className="border-t border-slate-200 pt-16">
              <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">實地導航</span>
              <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">互動式地理坐標地圖</h2>
              <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
              <p className="text-slate-500 font-light max-w-2xl text-base leading-relaxed">
                點擊標記在 {article.country} 地形圖上的坐標節點，即刻預覽景點實景相片、確切的經緯度坐標以及前往探索時的關鍵防坑指南。
              </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center bg-white border border-slate-200 rounded-3xl p-6 md:p-8 shadow-xs">
              
              {/* 地圖畫布 */}
              <div className="lg:col-span-7 relative bg-slate-900 rounded-2xl aspect-square overflow-hidden p-6 border border-slate-850 shadow-inner flex items-center justify-center">
                <div className="absolute inset-0 bg-[radial-gradient(#e63946/10_1px,transparent_1px)] [background-size:16px_16px] pointer-events-none" />
                <div className="absolute inset-0 bg-linear-to-b from-slate-900 via-transparent to-slate-950 pointer-events-none" />
                
                {/* 路線連線 */}
                <svg className="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 100 100" preserveAspectRatio="none">
                  <path 
                    d={article.mapSpots.reduce((acc, spot, idx) => {
                      return acc + `${idx === 0 ? 'M' : 'L'} ${spot.x} ${spot.y} `;
                    }, '')}
                    fill="none" 
                    stroke="#EF4444" 
                    strokeWidth="0.85" 
                    strokeDasharray="3, 3"
                    className="animate-pulse"
                  />
                </svg>

                {/* 坐標點 */}
                {article.mapSpots.map((spot, idx) => {
                  const isSelected = selectedMapSpot === idx;
                  return (
                    <button
                      key={idx}
                      onClick={() => setSelectedMapSpot(idx)}
                      className="absolute group z-10 transition-transform duration-300 transform -translate-x-1/2 -translate-y-1/2 cursor-pointer focus:outline-none"
                      style={{ left: `${spot.x}%`, top: `${spot.y}%` }}
                    >
                      <span className={`absolute inset-[-12px] rounded-full border bg-transparent transition-all ${
                        isSelected 
                          ? 'border-[#EF4444] animate-ping opacity-70' 
                          : 'border-transparent group-hover:border-white/30 scale-75'
                      }`} />

                      <span className={`w-8 h-8 rounded-full flex items-center justify-center font-bold text-xs border transition-all shadow-md ${
                        isSelected 
                          ? 'bg-[#EF4444] text-white border-white scale-110' 
                          : 'bg-slate-950 text-slate-300 border-slate-800 group-hover:bg-[#0EA5E9] group-hover:text-white group-hover:border-[#0EA5E9]'
                      }`}>
                        {idx + 1}
                      </span>

                      <span className="absolute bottom-10 left-1/2 transform -translate-x-1/2 pointer-events-none opacity-0 group-hover:opacity-100 bg-slate-950 text-white text-[10px] font-bold tracking-wider uppercase px-2 py-1 rounded-sm shadow-md whitespace-nowrap border border-slate-800 transition-opacity z-20">
                        {spot.name}
                      </span>
                    </button>
                  );
                })}

                <div className="absolute top-2 left-4 text-[9px] text-slate-600 font-mono tracking-widest uppercase">地形坐標圖 v3.0</div>
                <div className="absolute bottom-2 right-4 text-[9px] text-slate-600 font-mono">LAT: {article.mapSpots[selectedMapSpot].lat}</div>
              </div>

              {/* 側邊資訊同步面板 */}
              <div className="lg:col-span-5 space-y-6">
                <div className="space-y-1">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-[#e63946] block">
                    地標節點 {selectedMapSpot + 1} / {article.mapSpots.length}
                  </span>
                  <h3 className="font-serif text-2xl md:text-3xl text-slate-950 font-bold">
                    {article.mapSpots[selectedMapSpot].name}
                  </h3>
                  <div className="flex gap-4 text-xs text-slate-400 font-mono mt-1">
                    <span>緯度: {article.mapSpots[selectedMapSpot].lat}</span>
                    <span>經度: {article.mapSpots[selectedMapSpot].lng}</span>
                  </div>
                </div>

                <div className="relative rounded-xl overflow-hidden aspect-[16/10] bg-slate-100 shadow-xs">
                  <img 
                    src={article.mapSpots[selectedMapSpot].image} 
                    alt={article.mapSpots[selectedMapSpot].name}
                    referrerPolicy="no-referrer"
                    className="w-full h-full object-cover hover:scale-102 transition-transform duration-300"
                  />
                </div>

                <div className="space-y-4">
                  <p className="text-slate-600 text-sm leading-relaxed">
                    {article.mapSpots[selectedMapSpot].description}
                  </p>
                  
                  <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl flex items-start gap-2.5">
                    <Info size={14} className="text-[#0EA5E9] shrink-0 mt-0.5" />
                    <div>
                      <span className="text-[10px] font-bold uppercase tracking-wider text-slate-500 block">漫遊探索建議</span>
                      <p className="text-xs text-slate-600 leading-normal mt-0.5">
                        建議在此停留至少 1.5 小時。這是捕捉黃金時刻或絕美日出、晨霧長曝光風景攝影的絕佳機位。
                      </p>
                    </div>
                  </div>
                </div>

                {/* 節點快速導航 */}
                <div className="flex justify-between items-center pt-2 border-t border-slate-100">
                  <span className="text-xs text-slate-500">快速切換：</span>
                  <div className="flex gap-1.5">
                    {article.mapSpots.map((_, idx) => (
                      <button
                        key={idx}
                        onClick={() => setSelectedMapSpot(idx)}
                        className={`w-7 h-7 rounded-full text-xs font-bold transition-all cursor-pointer ${
                          selectedMapSpot === idx 
                            ? 'bg-slate-900 text-white' 
                            : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                        }`}
                      >
                        {idx + 1}
                      </button>
                    ))}
                  </div>
                </div>

              </div>

            </div>
          </section>

          {/* 4. 智慧預算自訂工具 */}
          <section id="budget" ref={sectionsRef.budget} className="space-y-8 scroll-mt-24">
            <div className="border-t border-slate-200 pt-16">
              <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">花費計算器</span>
              <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">智慧預算自訂工具</h2>
              <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
              <p className="text-slate-500 font-light max-w-2xl text-base leading-relaxed">
                即時估計您的慢旅開銷。自由調整拉桿來自訂停留天數，選擇您偏好的住宿等級與飲食風格，隨即查看動態更新、完全同步的預算細項圖表。
              </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-stretch bg-white border border-slate-200 rounded-3xl p-6 md:p-10 shadow-xs">
              
              {/* 控制與調整參數 */}
              <div className="lg:col-span-6 space-y-8 flex flex-col justify-between">
                
                {/* 1. 天數 Slider */}
                <div className="space-y-3">
                  <div className="flex justify-between items-center text-xs font-bold uppercase tracking-widest text-slate-500">
                    <label>慢旅總天數</label>
                    <span className="text-[#e63946] font-mono text-sm">{daysCount} 天</span>
                  </div>
                  <input 
                    type="range" 
                    min={1} 
                    max={14} 
                    value={daysCount}
                    onChange={(e) => setDaysCount(parseInt(e.target.value))}
                    className="w-full accent-[#e63946] cursor-pointer h-1.5 bg-slate-100 rounded-lg appearance-none"
                  />
                  <div className="flex justify-between text-[10px] text-slate-400 font-mono">
                    <span>1 天</span>
                    <span>7 天</span>
                    <span>14 天</span>
                  </div>
                </div>

                {/* 2. 住宿層級 */}
                <div className="space-y-3">
                  <label className="text-xs font-bold uppercase tracking-widest text-slate-500 block">住宿等級偏好</label>
                  <div className="grid grid-cols-3 gap-2">
                    {[
                      { tier: 'budget', name: '溫馨青旅/民宿', desc: '$45 / 晚' },
                      { tier: 'boutique', name: '精品設計旅宿', desc: '$130 / 晚' },
                      { tier: 'luxury', name: '極致奢華酒店', desc: '$290 / 晚' }
                    ].map((h) => (
                      <button
                        key={h.tier}
                        onClick={() => setHotelTier(h.tier as any)}
                        className={`flex flex-col text-left p-4 rounded-xl border transition-all cursor-pointer ${
                          hotelTier === h.tier
                            ? 'bg-[#e63946]/10 border-[#e63946] text-slate-900'
                            : 'bg-slate-50 border-slate-200/80 text-slate-500 hover:border-slate-400'
                        }`}
                      >
                        <span className="text-xs font-bold tracking-wider uppercase">{h.name}</span>
                        <span className="text-[10px] font-mono mt-1 font-semibold">{h.desc}</span>
                      </button>
                    ))}
                  </div>
                </div>

                {/* 3. 飲食餐飲 */}
                <div className="space-y-3">
                  <label className="text-xs font-bold uppercase tracking-widest text-slate-500 block">餐飲美學風格</label>
                  <div className="grid grid-cols-3 gap-2">
                    {[
                      { tier: 'street', name: '在地街頭慢食', desc: '$15 / 天' },
                      { tier: 'bistro', name: '慢旅餐酒館/食堂', desc: '$40 / 天' },
                      { tier: 'fine', name: '星級主廚私房菜', desc: '$110 / 天' }
                    ].map((d) => (
                      <button
                        key={d.tier}
                        onClick={() => setDiningTier(d.tier as any)}
                        className={`flex flex-col text-left p-4 rounded-xl border transition-all cursor-pointer ${
                          diningTier === d.tier
                            ? 'bg-[#e63946]/10 border-[#e63946] text-slate-900'
                            : 'bg-slate-50 border-slate-200/80 text-slate-500 hover:border-slate-400'
                        }`}
                      >
                        <span className="text-xs font-bold tracking-wider uppercase">{d.name}</span>
                        <span className="text-[10px] font-mono mt-1 font-semibold">{d.desc}</span>
                      </button>
                    ))}
                  </div>
                </div>

                <div className="p-4 bg-slate-50 border border-slate-150 rounded-xl flex gap-2 items-center text-xs text-slate-500 italic font-light mt-4">
                  <Info size={14} className="text-[#0EA5E9] shrink-0" />
                  機票費用以固定平均往返航班 ${article.budgetEstimates.flightBudget} 納入估計。
                </div>

              </div>

              {/* 預算圖表分析 */}
              <div className="lg:col-span-6 bg-slate-50/50 border border-slate-150 p-6 md:p-8 rounded-2xl flex flex-col justify-between shadow-xs">
                
                <div className="space-y-6">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-slate-400 block">旅行開銷預估</span>
                    <h3 className="font-serif text-3xl font-bold text-slate-950 mt-1">預算細目分析</h3>
                  </div>

                  <div className="space-y-4">
                    {[
                      { label: '精緻住宿開銷', amount: budgetBreakdown.hotel, color: 'bg-amber-600', max: 4000 },
                      { label: '餐飲感官預算', amount: budgetBreakdown.dining, color: 'bg-emerald-600', max: 1540 },
                      { label: '景點門票與嚮導', amount: budgetBreakdown.activities, color: 'bg-blue-600', max: 1680 },
                      { label: '往返航線平均', amount: budgetBreakdown.flights, color: 'bg-[#e63946]', max: 1200 }
                    ].map((bar, bidx) => {
                      const pct = Math.min((bar.amount / budgetBreakdown.total) * 100, 100);
                      return (
                        <div key={bidx} className="space-y-1.5">
                          <div className="flex justify-between items-center text-xs text-slate-600">
                            <span className="font-semibold">{bar.label}</span>
                            <span className="font-mono font-bold">${bar.amount}</span>
                          </div>
                          <div className="w-full h-2.5 bg-slate-200/80 rounded-full overflow-hidden">
                            <div 
                              className={`h-full ${bar.color} rounded-full transition-all duration-500 ease-out`} 
                              style={{ width: `${pct}%` }}
                            />
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>

                <div className="pt-8 mt-8 border-t border-slate-200/80 flex justify-between items-end">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500 block">預估慢旅總預算</span>
                    <span className="font-serif text-3xl md:text-4xl font-bold text-[#e63946]">${budgetBreakdown.total}</span>
                  </div>
                  
                  {/* 省錢小建議 */}
                  <div className="text-right max-w-xs hidden sm:block">
                    <span className="text-[10px] font-bold text-[#e63946] uppercase tracking-widest block">慢旅省錢攻略</span>
                    <p className="text-[11px] text-slate-500 leading-normal font-light mt-0.5">
                      {hotelTier === 'luxury' 
                        ? '於週中預訂日式百年町家民宿，可為極致奢華等級的住宿節省高達 25% 的開銷。'
                        : hotelTier === 'boutique' 
                          ? '將在地交通週遊券與精品旅宿套裝包裹在一起，能巧妙繞過針對散客的地區旅遊溢價。'
                          : '溫馨青旅是結識世界各國自由行背包客、並加入在地免費導覽健行路線的絕佳窗口。'}
                    </p>
                  </div>
                </div>

              </div>

            </div>
          </section>

          {/* 5. 氣候與季節建議 */}
          <section id="weather" ref={sectionsRef.weather} className="space-y-8 scroll-mt-24">
            <div className="border-t border-slate-200 pt-16">
              <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">最佳起程時節</span>
              <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">四季氣候特性與穿搭指南</h2>
              <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
              <p className="text-slate-500 font-light max-w-2xl text-base leading-relaxed">
                {article.country} 的四季更迭展現著截然不同的壯麗之美。查看我們特別為您整理的季節溫度、特色氣候與行李穿搭指南，規劃最適合您的美學氣候。
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {article.weatherForecast.map((w, idx) => {
                const getIcon = (name: string) => {
                  switch (name) {
                    case 'flower': return <Flower className="text-pink-400" size={24} />;
                    case 'sun': return <Sun className="text-amber-400" size={24} />;
                    case 'leaf': return <Leaf className="text-amber-600" size={24} />;
                    case 'snowflake': return <Snowflake className="text-blue-300" size={24} />;
                    case 'cloud-rain': return <CloudSun className="text-slate-400" size={24} />;
                    case 'wind': return <Compass className="text-[#e63946]" size={24} />;
                    default: return <Sun className="text-[#e63946]" size={24} />;
                  }
                };

                return (
                  <div key={idx} className="bg-white border border-slate-200 rounded-2xl p-6 shadow-2xs space-y-4 hover:border-[#e63946]/30 transition-all flex flex-col justify-between">
                    <div className="space-y-3">
                      <div className="flex justify-between items-start">
                        {getIcon(w.iconName)}
                        <span className="font-mono text-xs font-bold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-sm">{w.temp}</span>
                      </div>
                      
                      <div>
                        <h4 className="font-serif text-lg font-bold text-slate-950">{w.season}</h4>
                        <p className="text-xs text-slate-500 leading-relaxed font-light mt-1">{w.description}</p>
                      </div>
                    </div>

                    <div className="pt-4 border-t border-slate-100 mt-4">
                      <span className="text-[9px] font-bold uppercase tracking-widest text-slate-400 block">探索適宜度</span>
                      <p className="text-[11px] font-medium text-slate-700 leading-normal mt-0.5">{w.suitability}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </section>

          {/* 6. 行李打包清單 */}
          <section id="packing" ref={sectionsRef.packing} className="space-y-8 scroll-mt-24">
            <div className="border-t border-slate-200 pt-16">
              <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">起程前裝備核對</span>
              <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">起程前裝備打包清單</h2>
              <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
              <p className="text-slate-500 font-light max-w-2xl text-base leading-relaxed">
                在您整理行李時逐項勾選打包。您的選擇將安全地儲存在瀏覽器的緩存中，即便關閉網頁也不會丟失。您還可以針對相機鏡頭、戶外登山設備自行添加專屬裝備。
              </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
              
              {/* 打包進度與自訂欄位 */}
              <div className="lg:col-span-4 space-y-6 bg-white border border-slate-200 p-6 md:p-8 rounded-2xl shadow-sm">
                
                <div className="text-center space-y-3">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-slate-400 block">行李打包進度</span>
                  
                  {/* 圓形進度圖 */}
                  <div className="relative w-28 h-28 mx-auto flex items-center justify-center">
                    <svg className="w-full h-full transform -rotate-90">
                      <circle 
                        cx="56" cy="56" r="48" 
                        stroke="#e5e5e5" strokeWidth="8" fill="transparent"
                      />
                      <circle 
                        cx="56" cy="56" r="48" 
                        stroke="#10B981" strokeWidth="8" fill="transparent"
                        strokeDasharray={2 * Math.PI * 48}
                        strokeDashoffset={(2 * Math.PI * 48) * (1 - packingProgress / 100)}
                        className="transition-all duration-500 ease-out"
                      />
                    </svg>
                    <span className="font-serif text-2xl font-bold text-slate-950">{packingProgress}%</span>
                  </div>

                  <p className="text-xs text-slate-600 font-medium">
                    {packingProgress === 100 ? '✨ 打包完成！隨時可以出發！' : '繼續打包，漫遊者！'}
                  </p>
                </div>

                {/* 添加自訂行李項的表單 */}
                <form onSubmit={handleAddPackingItem} className="pt-6 border-t border-slate-100 space-y-3">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500 block">添加自訂裝備設備</span>
                  <input
                    type="text"
                    required
                    placeholder="例如：Sony a7R 鏡頭、三腳架..."
                    value={newItemText}
                    onChange={(e) => setNewItemText(e.target.value)}
                    className="w-full text-xs border border-slate-200 focus:border-[#e63946] focus:outline-none rounded-lg px-4 py-3 bg-slate-50"
                  />
                  
                  <div className="flex gap-2">
                    <select
                      value={newItemCategory}
                      onChange={(e) => setNewItemCategory(e.target.value)}
                      className="w-full text-[10px] uppercase font-bold tracking-wider border border-slate-200 rounded-lg px-3 py-2 bg-slate-50 text-slate-600 cursor-pointer"
                    >
                      <option value="Essentials">必備物資</option>
                      <option value="Clothing">衣物防寒</option>
                      <option value="Electronics">數位與攝影</option>
                    </select>

                    <button
                      type="submit"
                      className="px-4 py-2 bg-[#1E293B] hover:bg-[#334155] text-white rounded-lg text-xs font-bold transition-colors flex items-center gap-1.5 shrink-0 cursor-pointer"
                    >
                      添加
                    </button>
                  </div>
                </form>

              </div>

              {/* 打包清單內容 */}
              <div className="lg:col-span-8 bg-white border border-slate-200 rounded-2xl p-6 md:p-8 shadow-sm space-y-6">
                
                {[
                  { id: 'Essentials', label: '必備物資' },
                  { id: 'Clothing', label: '衣物防寒' },
                  { id: 'Electronics', label: '數位與攝影' }
                ].map((cat) => {
                  const catItems = packingItems.filter(item => item.category.toLowerCase().startsWith(cat.id.toLowerCase().slice(0, 3)));
                  
                  return (
                    <div key={cat.id} className="space-y-3 pb-4 border-b border-slate-100 last:border-b-0 last:pb-0">
                      <h4 className="text-xs font-bold uppercase tracking-widest text-[#e63946] border-b border-slate-50 pb-1.5">
                        {cat.label}
                      </h4>

                      {catItems.length === 0 ? (
                        <p className="text-xs text-slate-400 italic">此分類目前沒有裝備項目。</p>
                      ) : (
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                          {catItems.map((item) => (
                            <div 
                              key={item.id}
                              className={`flex items-center justify-between p-3 border rounded-xl transition-all ${
                                item.checked 
                                  ? 'bg-slate-50/50 border-slate-200/40 opacity-60' 
                                  : 'bg-white border-slate-200 hover:border-slate-300'
                              }`}
                            >
                              <button
                                onClick={() => handleTogglePacking(item.id)}
                                className="flex items-start gap-3 text-left w-full focus:outline-none cursor-pointer"
                              >
                                <span className={`w-4 h-4 rounded-md border flex items-center justify-center shrink-0 mt-0.5 transition-all ${
                                  item.checked 
                                    ? 'bg-[#10B981] border-[#10B981] text-white' 
                                    : 'border-slate-300 bg-white'
                                }`}>
                                  {item.checked && <Check size={10} strokeWidth={3} />}
                                </span>
                                <span className={`text-xs font-medium text-slate-800 ${item.checked ? 'line-through text-slate-400' : ''}`}>
                                  {item.text}
                                </span>
                              </button>

                              {item.id.startsWith('custom_') && (
                                <button
                                  onClick={() => handleDeletePackingItem(item.id)}
                                  className="text-slate-300 hover:text-red-500 transition-colors p-1 cursor-pointer"
                                >
                                  <Trash2 size={13} />
                                </button>
                              )}
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  );
                })}

              </div>

            </div>
          </section>

          {/* 7. 旅人真實寫真幻燈片入口 */}
          <section className="space-y-8">
            <div className="border-t border-slate-200 pt-16">
              <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">實景寫真</span>
              <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">旅人視覺影像藝廊</h2>
              <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
              <p className="text-slate-500 font-light max-w-2xl text-base leading-relaxed">
                點擊任何由前線探索撰稿旅人現場拍攝的高解析度真實相片，即可開啟滿版大圖燈箱幻燈片播放模式。
              </p>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              {galleryPhotos.map((photo, pidx) => (
                <div 
                  key={pidx} 
                  className="relative group rounded-xl overflow-hidden aspect-square bg-slate-200 shadow-xs cursor-pointer"
                  onClick={() => setLightboxIndex(pidx)}
                >
                  <img 
                    src={photo} 
                    alt={`慢旅寫真地標 ${pidx + 1}`}
                    referrerPolicy="no-referrer"
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                  />
                  <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                    <span className="px-3 py-1 bg-white/90 text-slate-950 text-[10px] font-bold tracking-widest uppercase rounded-sm shadow-md">
                      放大預覽
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* 8. 旅人之聲討論板 */}
          <section id="comments" ref={sectionsRef.comments} className="space-y-8 scroll-mt-24">
            <div className="border-t border-slate-200 pt-16">
              <span className="text-[#e63946] text-xs font-bold tracking-[0.2em] uppercase block mb-3">旅人之聲討論板</span>
              <h2 className="font-serif text-3xl md:text-5xl font-semibold text-slate-900 leading-tight">旅人體驗反饋與評分</h2>
              <div className="w-12 h-1 bg-[#06B6D4] mt-4 mb-6"></div>
              <p className="text-slate-500 font-light max-w-2xl text-base leading-relaxed">
                留下您的專屬旅行印記，或細細讀讀過去曾造訪 {article.country} 幽靜竹林、極致山脈或深藍冰川的漫遊探險家們留下的最真實反饋。
              </p>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
              
              {/* 發布評鑑日誌 */}
              <div className="lg:col-span-5 bg-white border border-slate-200 p-6 md:p-8 rounded-2xl shadow-sm space-y-6">
                <div>
                  <h4 className="font-serif text-xl font-bold text-slate-950">寫下您的慢旅評鑑</h4>
                  <p className="text-xs text-slate-500 font-light mt-1">
                    分享最真實的實地勘查，能協助未來的漫遊者們獲得更準確、安全的旅行資訊。
                  </p>
                </div>

                <form onSubmit={handleAddComment} className="space-y-4">
                  <div className="space-y-1.5">
                    <label className="text-xs font-bold uppercase tracking-widest text-slate-500">探險家大名</label>
                    <input
                      type="text"
                      required
                      placeholder="例如：徐志摩"
                      value={newCommentName}
                      onChange={(e) => setNewCommentName(e.target.value)}
                      className="w-full text-xs border border-slate-200 focus:border-[#e63946] focus:outline-none rounded-lg px-4 py-3 bg-slate-50"
                    />
                  </div>

                  {/* 評分 */}
                  <div className="space-y-1.5">
                    <label className="text-xs font-bold uppercase tracking-widest text-slate-500 block">給予評分</label>
                    <div className="flex gap-1.5 pt-1">
                      {[1, 2, 3, 4, 5].map((star) => {
                        const isFilled = (hoveredStar ?? newCommentRating) >= star;
                        return (
                          <button
                            key={star}
                            type="button"
                            onMouseEnter={() => setHoveredStar(star)}
                            onMouseLeave={() => setHoveredStar(null)}
                            onClick={() => setNewCommentRating(star)}
                            className="focus:outline-none transition-transform active:scale-110 cursor-pointer"
                          >
                            <Star 
                              size={22} 
                              className={`transition-colors ${
                                isFilled 
                                  ? 'fill-[#FBBF24] text-[#FBBF24]' 
                                  : 'text-slate-300'
                              }`} 
                            />
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  <div className="space-y-1.5">
                    <label className="text-xs font-bold uppercase tracking-widest text-slate-500">旅人點評心得</label>
                    <textarea
                      required
                      rows={4}
                      placeholder="分享您的實地感官體驗、最新路況更新、或者值得推薦的秘境旅宿..."
                      value={newCommentText}
                      onChange={(e) => setNewCommentText(e.target.value)}
                      className="w-full text-xs border border-slate-200 focus:border-[#e63946] focus:outline-none rounded-lg px-4 py-3 bg-slate-50"
                    />
                  </div>

                  <button
                    type="submit"
                    className="w-full py-4 bg-[#e63946] hover:bg-[#C1121F] text-white text-xs font-bold tracking-widest uppercase rounded-lg transition-colors shadow-sm flex items-center justify-center gap-2 cursor-pointer"
                  >
                    發布評鑑日誌 <MessageSquare size={13} />
                  </button>
                </form>

                {commentSuccess && (
                  <p className="text-xs text-emerald-500 text-center animate-fade-in font-medium">
                    ✨ 您的點評日誌已成功同步儲存！
                  </p>
                )}
              </div>

              {/* 評論 Feed */}
              <div className="lg:col-span-7 bg-white border border-slate-200 rounded-2xl p-6 md:p-8 shadow-sm space-y-6">
                <div className="flex justify-between items-center pb-4 border-b border-slate-100">
                  <span className="text-xs font-bold uppercase tracking-widest text-[#e63946]">真實評價看板</span>
                  <span className="text-xs font-mono text-slate-400">{comments.length} 篇真實評鑑已登錄</span>
                </div>

                <div className="space-y-6 max-h-[500px] overflow-y-auto pr-2 custom-scrollbar">
                  {comments.map((comm) => (
                    <div 
                      key={comm.id}
                      className="pb-6 border-b border-slate-100 last:border-b-0 last:pb-0 space-y-3 relative group"
                    >
                      <div className="flex justify-between items-start">
                        <div className="space-y-0.5">
                          <h5 className="font-serif text-base font-bold text-slate-950">{comm.userName}</h5>
                          <span className="text-[10px] font-mono text-slate-400 block">{comm.date}</span>
                        </div>
                        
                        <div className="flex gap-0.5 text-[#FBBF24]">
                          {Array.from({ length: 5 }).map((_, sidx) => (
                            <Star 
                              key={sidx} 
                              size={12} 
                              className={sidx < comm.rating ? 'fill-[#FBBF24] text-[#FBBF24]' : 'text-slate-200'} 
                            />
                          ))}
                        </div>
                      </div>

                      <p className="text-xs text-slate-600 leading-relaxed font-light">
                        {comm.content}
                      </p>

                      {!comm.id.startsWith('s') && (
                        <button
                          onClick={() => handleDeleteComment(comm.id)}
                          className="absolute bottom-1 right-1 opacity-0 group-hover:opacity-100 text-slate-300 hover:text-red-500 transition-all p-1 text-[10px] font-bold uppercase tracking-wider flex items-center gap-1 cursor-pointer"
                        >
                          <Trash2 size={11} /> 刪除
                        </button>
                      )}
                    </div>
                  ))}
                </div>

              </div>

            </div>
          </section>

        </div>
      </main>

      {/* 燈箱投影片檢視 overlay */}
      <AnimatePresence>
        {lightboxIndex !== null && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 bg-black/95 backdrop-blur-md flex flex-col justify-between p-6"
            onClick={() => setLightboxIndex(null)}
          >
            <div className="flex justify-between items-center text-white" onClick={(e) => e.stopPropagation()}>
              <span className="text-xs font-mono text-slate-400">
                慢旅視覺影像 {lightboxIndex + 1} / {galleryPhotos.length}
              </span>
              <button 
                onClick={() => setLightboxIndex(null)}
                className="p-2 border border-white/10 hover:border-white/30 rounded-full transition-colors text-white text-xs font-bold uppercase tracking-widest cursor-pointer"
              >
                關閉 (Esc)
              </button>
            </div>

            <div 
              className="flex justify-between items-center w-full max-w-5xl mx-auto flex-grow"
              onClick={(e) => e.stopPropagation()}
            >
              <button
                onClick={() => setLightboxIndex((prev) => (prev !== null && prev > 0) ? prev - 1 : galleryPhotos.length - 1)}
                className="p-3 bg-white/10 text-white hover:bg-white/20 rounded-full text-xs font-bold tracking-widest uppercase shrink-0 cursor-pointer"
              >
                上一張
              </button>

              <div className="max-h-[75vh] max-w-[80vw] overflow-hidden rounded-xl bg-slate-900 border border-white/5 flex items-center justify-center">
                <img 
                  src={galleryPhotos[lightboxIndex]} 
                  alt="景致放大視圖" 
                  referrerPolicy="no-referrer"
                  className="max-h-[70vh] max-w-[75vw] object-contain"
                />
              </div>

              <button
                onClick={() => setLightboxIndex((prev) => (prev !== null && prev < galleryPhotos.length - 1) ? prev + 1 : 0)}
                className="p-3 bg-white/10 text-white hover:bg-white/20 rounded-full text-xs font-bold tracking-widest uppercase shrink-0 cursor-pointer"
              >
                下一張
              </button>
            </div>

            <div className="text-center text-white pb-6" onClick={(e) => e.stopPropagation()}>
              <p className="text-sm font-serif italic text-slate-300">「定格 {article.country} 最壯麗而溫柔、安靜的角落。」</p>
            </div>

          </motion.div>
        )}
      </AnimatePresence>

    </div>
  );
};
export default ArticleView;
