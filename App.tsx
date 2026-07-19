import React, { useState, useEffect } from 'react';
import { travelArticles } from './data/articles';
import { customPages } from './data/customPages';
import { HomeView } from './components/HomeView';
import { ArticleView } from './components/ArticleView';
import { CustomPageView } from './components/CustomPageView';
import { Footer } from './components/Footer';
import { 
  Menu, X, Heart, Bookmark, ArrowRight, Trash2, Clock, Star, ChevronDown 
} from 'lucide-react';

const App: React.FC = () => {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const [activeArticleId, setActiveArticleId] = useState<string | null>(null);
  const [activeCustomPageId, setActiveCustomPageId] = useState<string | null>(null);
  
  // 珍藏清單狀態
  const [savedTripIds, setSavedTripIds] = useState<string[]>([]);
  const [bookmarksDrawerOpen, setBookmarksDrawerOpen] = useState(false);

  // 選單下拉狀態
  const [activeDropdown, setActiveDropdown] = useState<string | null>(null);
  const [activeMobileAccordion, setActiveMobileAccordion] = useState<string | null>(null);


  // 滾動與載入本地快取
  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 80);
    window.addEventListener('scroll', handleScroll);
    
    const saved = localStorage.getItem('travel_bookmarks');
    if (saved) {
      setSavedTripIds(JSON.parse(saved));
    }

    // 1. 初始化解析 URL 載入對應頁面
    const path = window.location.pathname;
    if (path.includes('/articles/')) {
      const match = path.match(/\/articles\/([^/.]+)/);
      if (match && match[1]) {
        const articleId = match[1];
        if (travelArticles.some(art => art.id === articleId)) {
          setActiveArticleId(articleId);
          setActiveCustomPageId(null);
        }
      }
    } else {
      const filename = path.split('/').pop();
      if (filename && filename.endsWith('.html') && filename !== 'index.html') {
        const pageId = filename.replace('.html', '');
        if (customPages.some(page => page.id === pageId)) {
          setActiveCustomPageId(pageId);
          setActiveArticleId(null);
        }
      }
    }

    // 2. 監聽瀏覽器上一頁/下一頁 (popstate)
    const handlePopState = () => {
      const currentPath = window.location.pathname;
      if (currentPath === '/' || currentPath === '' || currentPath.endsWith('index.html')) {
        setActiveArticleId(null);
        setActiveCustomPageId(null);
      } else if (currentPath.includes('/articles/')) {
        const match = currentPath.match(/\/articles\/([^/.]+)/);
        if (match && match[1]) {
          const articleId = match[1];
          if (travelArticles.some(art => art.id === articleId)) {
            setActiveArticleId(articleId);
            setActiveCustomPageId(null);
          }
        }
      } else {
        const filename = currentPath.split('/').pop();
        if (filename && filename.endsWith('.html') && filename !== 'index.html') {
          const pageId = filename.replace('.html', '');
          if (customPages.some(page => page.id === pageId)) {
            setActiveCustomPageId(pageId);
            setActiveArticleId(null);
            return;
          }
        }
        setActiveArticleId(null);
        setActiveCustomPageId(null);
      }
    };

    window.addEventListener('popstate', handlePopState);

    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('popstate', handlePopState);
    };
  }, []);

  // 珍藏/取消珍藏處理
  const handleToggleSaveTrip = (id: string) => {
    let updated: string[];
    if (savedTripIds.includes(id)) {
      updated = savedTripIds.filter(tid => tid !== id);
    } else {
      updated = [...savedTripIds, id];
    }
    setSavedTripIds(updated);
    localStorage.setItem('travel_bookmarks', JSON.stringify(updated));
  };

  const handleSelectArticle = (id: string) => {
    // 連結到資料夾對應的靜態頁面html
    window.location.href = `/articles/${id}.html`;
  };

  const handleSelectCustomPage = (id: string) => {
    // 連結到資料夾對應的靜態頁面html
    const page = customPages.find(p => p.id === id);
    if (page) {
      window.location.href = `/${page.url}`;
    } else {
      window.location.href = `/${id}.html`;
    }
  };

  const getCategoryUrl = (key: string) => {
    switch (key) {
      case 'japan': return '/japan-travel.html';
      case 'korea': return '/korea-travel.html';
      case 'taiwan': return '/taiwan-travel.html';
      case 'southeast': return '/southeast-asia.html';
      case 'tools': return '/travel-tools.html';
      default: return '/';
    }
  };

  const handleBackToHome = () => {
    setActiveArticleId(null);
    setActiveCustomPageId(null);
    window.scrollTo({ top: 0, behavior: 'instant' });
    // 回到首頁，更新網址列
    window.history.pushState(null, '', '/');
  };

  const activeArticle = travelArticles.find(art => art.id === activeArticleId);
  const activeCustomPage = customPages.find(page => page.id === activeCustomPageId);
  const bookmarkedArticles = travelArticles.filter(art => savedTripIds.includes(art.id));

  return (
    <div className="min-h-screen bg-tiffany-cream text-slate-800 selection:bg-[#e63946] selection:text-white flex flex-col font-sans transition-colors duration-300">
      
      <nav className={`fixed top-0 left-0 right-0 z-[100] transition-all duration-500 ${
        scrolled 
          ? 'bg-tiffany-cream/90 backdrop-blur-md shadow-xs border-b border-tiffany-ice/50 py-3.5' 
          : activeArticleId || activeCustomPageId
            ? 'bg-tiffany-cream/90 backdrop-blur-md border-b border-tiffany-ice/50 py-4'
            : 'bg-transparent py-6 text-white'
      }`}>
        <div className="container mx-auto px-6 max-w-7xl flex justify-between items-center">
          
          {/* 品牌標誌與標題 */}
          <div 
            className="flex items-center gap-3.5 cursor-pointer group" 
            onClick={handleBackToHome}
          >
            <div className="w-9 h-9 bg-[#e63946] rounded-full flex items-center justify-center text-white font-serif font-bold text-lg shadow-inner pb-0.5 group-hover:scale-105 transition-transform">
              α
            </div>
            <span className={`font-serif font-bold text-lg tracking-[0.25em] ${
              scrolled || activeArticleId || activeCustomPageId ? 'text-slate-900' : 'text-slate-50'
            }`}>
              均在路上
            </span>
          </div>
          
          {/* 桌機選單 */}
          <div className="hidden lg:flex items-center gap-10 text-xs font-semibold tracking-[0.2em] uppercase">
            
            {/* 首頁 */}
            <button 
              onClick={handleBackToHome}
              className={`hover:text-[#e63946] transition-colors cursor-pointer ${
                !activeArticleId && !activeCustomPageId
                  ? 'text-[#e63946] font-bold' 
                  : scrolled || activeArticleId || activeCustomPageId
                    ? 'text-slate-800' 
                    : 'text-slate-200'
              }`}
            >
              首頁
            </button>

            {/* 自由行分類下拉選單 */}
            {[
              { label: '日本自由行', key: 'japan' },
              { label: '韓國自由行', key: 'korea' },
              { label: '台灣旅遊', key: 'taiwan' },
              { label: '東南亞自由行', key: 'southeast' },
              { label: '旅遊工具', key: 'tools' }
            ].map((cat) => {
              const pages = customPages.filter(p => p.category === cat.label);
              const isActive = activeCustomPage?.category === cat.label;
              return (
                <div 
                  key={cat.key}
                  className="relative py-2"
                  onMouseEnter={() => setActiveDropdown(cat.key)}
                  onMouseLeave={() => setActiveDropdown(null)}
                >
                  <a 
                    href={getCategoryUrl(cat.key)}
                    className={`flex items-center gap-1 hover:text-[#e63946] transition-colors cursor-pointer ${
                      isActive 
                        ? 'text-[#e63946] font-bold' 
                        : scrolled || activeArticleId || activeCustomPageId
                          ? 'text-slate-800' 
                          : 'text-slate-200'
                    }`}
                  >
                    <span>{cat.label}</span>
                    <ChevronDown size={11} className={`transition-transform duration-300 ${activeDropdown === cat.key ? 'rotate-180' : ''}`} />
                  </a>

                  {activeDropdown === cat.key && (
                    <div className="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-[420px] bg-white border border-tiffany-ice/60 rounded-xl shadow-xl py-3 z-[110] text-slate-800 normal-case tracking-normal animate-fade-in max-h-[580px] overflow-y-auto custom-scrollbar">
                      <div className="px-4 py-1.5 text-[10px] font-bold text-slate-400 uppercase tracking-widest border-b border-slate-100 mb-2 flex justify-between items-center">
                        <span>{cat.label} 專欄</span>
                        <a 
                          href={getCategoryUrl(cat.key)}
                          className="text-[9px] text-[#e63946] font-bold hover:underline"
                        >
                          查看全部 ➡️
                        </a>
                      </div>
                      {pages.map((p) => (
                        <a
                          key={p.id}
                          href={`/${p.url}`}
                          onClick={() => {
                            setActiveDropdown(null);
                          }}
                          className="w-full text-left px-4 py-2 hover:bg-tiffany-cream/60 transition-colors flex gap-3 group/item cursor-pointer block"
                        >
                          <div className="w-20 h-12 rounded-md overflow-hidden shrink-0 bg-slate-100 border border-slate-200/50">
                            <img 
                              src={p.coverImage} 
                              alt={p.title} 
                              referrerPolicy="no-referrer"
                              className="w-full h-full object-cover group-hover/item:scale-105 transition-transform duration-300"
                            />
                          </div>
                          <div className="flex flex-col justify-center min-w-0">
                            <span className="text-[8px] text-[#e63946] font-bold tracking-wider uppercase">{p.category}</span>
                            <span className="text-[11px] font-bold text-slate-900 group-hover/item:text-[#e63946] transition-colors line-clamp-1 mt-0.5">
                              {p.title}
                            </span>
                          </div>
                        </a>
                      ))}
                    </div>
                  )}
                </div>
              );
            })}

            {/* 關於我們 */}
            <a 
              href="/about.html"
              className={`hover:text-[#e63946] transition-colors cursor-pointer ${
                activeCustomPageId === 'about'
                  ? 'text-[#e63946] font-bold' 
                  : scrolled || activeArticleId || activeCustomPageId
                    ? 'text-slate-800' 
                    : 'text-slate-200'
              }`}
            >
              關於我們
            </a>
          </div>

          {/* 行動裝置選單觸發器 */}
          <div className="flex items-center gap-3 lg:hidden">
            <button 
              className={`p-2.5 rounded-full transition-colors ${
                scrolled || activeArticleId || activeCustomPageId ? 'text-slate-900 bg-slate-100' : 'text-white bg-white/10'
              }`} 
              onClick={() => setMenuOpen(!menuOpen)}
            >
              {menuOpen ? <X size={18} /> : <Menu size={18} />}
            </button>
          </div>

        </div>
      </nav>

      {/* 2. 行動裝置選單下拉選單 */}
      {menuOpen && (
        <div className="fixed inset-x-0 top-[60px] bottom-0 z-[95] bg-tiffany-cream/95 backdrop-blur-md shadow-xl flex flex-col p-8 gap-4 text-sm font-bold tracking-widest uppercase text-slate-700 animate-fade-in lg:hidden overflow-y-auto">
          
          {/* 首頁 */}
          <a 
            href="/index.html"
            onClick={() => {
              setMenuOpen(false);
            }}
            className="text-left py-2 border-b border-slate-200/50 hover:text-[#e63946]"
          >
            首頁
          </a>

          {/* 自由行分類摺疊 */}
          {[
            { label: '日本自由行', key: 'japan' },
            { label: '韓國自由行', key: 'korea' },
            { label: '台灣旅遊', key: 'taiwan' },
            { label: '東南亞自由行', key: 'southeast' },
            { label: '旅遊工具', key: 'tools' }
          ].map((cat) => {
            const pages = customPages.filter(p => p.category === cat.label);
            return (
              <div key={cat.key} className="flex flex-col border-b border-slate-200/50 pb-1.5">
                <button 
                  onClick={() => setActiveMobileAccordion(activeMobileAccordion === cat.key ? null : cat.key)}
                  className="text-left py-2 hover:text-[#e63946] flex justify-between items-center w-full"
                >
                  <span>{cat.label}</span>
                  <ChevronDown size={14} className={`transition-transform duration-300 ${activeMobileAccordion === cat.key ? 'rotate-180' : ''} text-[#e63946]`} />
                </button>
                
                {activeMobileAccordion === cat.key && (
                  <div className="pl-4 pb-2 pt-1 flex flex-col gap-3 normal-case tracking-normal animate-fade-in">
                    <a
                      href={getCategoryUrl(cat.key)}
                      onClick={() => setMenuOpen(false)}
                      className="text-left py-1.5 text-xs font-bold text-[#e63946] hover:underline pl-3.5 flex items-center gap-1 cursor-pointer"
                    >
                      <span>➡️ 查看全部 {cat.label} 攻略</span>
                    </a>
                    {pages.map((p) => (
                      <a
                        key={p.id}
                        href={`/${p.url}`}
                        onClick={() => {
                          setMenuOpen(false);
                        }}
                        className="text-left py-1.5 text-xs font-serif text-slate-600 hover:text-[#e63946] border-l-2 border-slate-200 hover:border-[#e63946] pl-3.5 transition-all flex items-center justify-between cursor-pointer block"
                      >
                        <span className="font-bold line-clamp-1 pr-2">{p.title}</span>
                      </a>
                    ))}
                  </div>
                )}
              </div>
            );
          })}

          {/* 關於我們 */}
          <a 
            href="/about.html"
            onClick={() => {
              setMenuOpen(false);
            }}
            className="text-left py-2 border-b border-slate-200/50 hover:text-[#e63946]"
          >
            關於我們
          </a>

          <a 
            href="/index.html#magazine-section"
            onClick={() => {
              setMenuOpen(false);
            }}
            className="text-left py-2 hover:text-[#e63946]"
          >
            探索熱門目的地
          </a>

        </div>
      )}

      {/* 3. 右側滑出式珍藏抽屜 */}
      <div className={`fixed inset-y-0 right-0 z-[150] w-full sm:w-110 bg-white shadow-2xl border-l border-slate-200 transform transition-transform duration-500 ease-out flex flex-col ${
        bookmarksDrawerOpen ? 'translate-x-0' : 'translate-x-full'
      }`}>
        {/* 抽屜標頭 */}
        <div className="p-6 md:p-8 border-b border-slate-100 flex justify-between items-center bg-slate-50">
          <div className="flex items-center gap-2">
            <Bookmark className="text-[#e63946]" size={18} />
            <span className="font-serif font-bold text-lg text-slate-900 tracking-wide">我的珍藏清單</span>
          </div>
          <button 
            onClick={() => setBookmarksDrawerOpen(false)}
            className="p-2 hover:bg-slate-200 rounded-full transition-colors text-slate-400 hover:text-slate-800 cursor-pointer"
          >
            <X size={18} />
          </button>
        </div>

        {/* 抽屜內容 */}
        <div className="p-6 md:p-8 overflow-y-auto flex-grow space-y-6 custom-scrollbar">
          {bookmarkedArticles.length === 0 ? (
            <div className="text-center py-16 space-y-4">
              <div className="w-16 h-16 bg-slate-50 rounded-full flex items-center justify-center mx-auto text-slate-300">
                <Heart size={28} />
              </div>
              <p className="text-slate-500 font-serif italic text-sm">
                「您的慢旅珍藏庫目前是空的。在探索時，點擊愛心即可珍藏指南。」
              </p>
            </div>
          ) : (
            bookmarkedArticles.map((art) => (
              <div 
                key={art.id}
                className="group flex gap-4 bg-slate-50/50 border border-slate-150 p-4 rounded-xl shadow-2xs hover:border-[#e63946]/40 hover:bg-white transition-all duration-300"
              >
                {/* 縮圖 */}
                <div className="w-20 h-20 rounded-lg overflow-hidden shrink-0 bg-slate-200">
                  <img 
                    src={art.heroImage} 
                    alt={art.title}
                    referrerPolicy="no-referrer"
                    className="w-full h-full object-cover group-hover:scale-102 transition-transform duration-300"
                  />
                </div>

                <div className="space-y-1.5 flex-grow">
                  <div className="flex justify-between items-start">
                    <span className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">{art.country}</span>
                    
                    {/* 移除 */}
                    <button
                      onClick={() => handleToggleSaveTrip(art.id)}
                      className="text-slate-300 hover:text-red-500 transition-colors cursor-pointer"
                      title="移除珍藏"
                    >
                      <Trash2 size={12} />
                    </button>
                  </div>

                  <h4 
                    onClick={() => handleSelectArticle(art.id)}
                    className="font-serif text-sm font-bold text-slate-950 group-hover:text-[#e63946] transition-colors cursor-pointer line-clamp-2 leading-snug"
                  >
                    {art.title}
                  </h4>

                  <div className="flex gap-4 text-[10px] text-slate-400 font-mono pt-1">
                    <span className="flex items-center gap-0.5 text-tiffany-rating"><Star size={9} className="fill-tiffany-rating text-tiffany-rating" /> {art.rating}</span>
                    <span className="flex items-center gap-0.5"><Clock size={9} /> {art.readTime}</span>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>

        {/* 抽屜頁尾 */}
        {bookmarkedArticles.length > 0 && (
          <div className="p-6 md:p-8 bg-slate-50 border-t border-slate-100 flex flex-col gap-4">
            <div className="flex justify-between items-center text-xs text-slate-500">
              <span>已珍藏指南數：</span>
              <span className="font-mono font-bold text-slate-800">{bookmarkedArticles.length} 篇慢旅誌</span>
            </div>
            <button
              onClick={() => handleSelectArticle(bookmarkedArticles[0].id)}
              className="w-full py-3 bg-slate-950 hover:bg-[#e63946] text-white text-xs font-bold tracking-widest uppercase rounded-lg transition-colors flex items-center justify-center gap-2 cursor-pointer"
            >
              開始閱讀專欄 <ArrowRight size={13} />
            </button>
          </div>
        )}
      </div>

      {/* 遮罩背景 */}
      {bookmarksDrawerOpen && (
        <div 
          onClick={() => setBookmarksDrawerOpen(false)}
          className="fixed inset-0 z-[140] bg-black/40 backdrop-blur-xs transition-opacity duration-300"
        />
      )}

      {/* 4. 主要子檢視區 */}
      <div className="flex-grow">
        {activeCustomPageId && activeCustomPage ? (
          <CustomPageView 
            page={activeCustomPage}
            onBackToHome={handleBackToHome}
          />
        ) : activeArticleId && activeArticle ? (
          <ArticleView 
            article={activeArticle}
            onBackToHome={handleBackToHome}
            isSaved={savedTripIds.includes(activeArticle.id)}
            onToggleSave={() => handleToggleSaveTrip(activeArticle.id)}
          />
        ) : (
          <HomeView 
            articles={travelArticles}
            customPages={customPages}
            onSelectArticle={handleSelectArticle}
            onSelectCustomPage={handleSelectCustomPage}
            savedTripIds={savedTripIds}
            onToggleSaveTrip={handleToggleSaveTrip}
          />
        )}
      </div>

      {/* 5. 頁尾 */}
      <Footer />

    </div>
  );
};

export default App;
