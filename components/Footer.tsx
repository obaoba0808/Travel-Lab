import React, { useState } from 'react';
import { Mail, Check, Compass, Facebook, MessageCircle, Heart } from 'lucide-react';

export const Footer: React.FC = () => {
  const [email, setEmail] = useState('');
  const [subscribed, setSubscribed] = useState(false);

  const handleSubscribe = (e: React.FormEvent) => {
    e.preventDefault();
    if (email.trim()) {
      setSubscribed(true);
      setEmail('');
      setTimeout(() => setSubscribed(false), 5000);
    }
  };

  return (
    <footer id="footer" className="bg-gradient-to-b from-[#020617] to-[#1e293b] text-slate-300 border-t border-slate-800/80 pt-20 pb-12 transition-all">
      <div className="container mx-auto px-6 max-w-7xl">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 pb-16 border-b border-slate-800/80">
          
          {/* Brand & Philosophy */}
          <div className="lg:col-span-4 space-y-6">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-[#e63946] rounded-full flex items-center justify-center text-white font-serif font-bold text-xl pb-0.5">
                α
              </div>
              <span className="font-serif font-bold text-xl tracking-widest text-white">
                均在路上
              </span>
            </div>
            <p className="text-slate-400 text-sm leading-relaxed">
              日本/韓國/台灣/東南亞自由行攻略平台 — 機票、住宿、交通、美食、預算一站式服務
            </p>
            <div className="space-y-2.5">
              <span className="text-[10px] font-bold uppercase tracking-widest text-slate-500 block">加入社群媒體</span>
              <div className="flex flex-wrap gap-2.5">
                <a 
                  href="https://www.facebook.com/profile.php?id=61590076012361" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="px-4 py-2 bg-[#020617]/40 border border-slate-800 hover:border-[#e63946] rounded-full hover:bg-[#e63946] hover:text-white transition-all text-slate-300 text-xs font-bold flex items-center gap-2"
                >
                  <Facebook size={14} className="shrink-0" /> Facebook 粉專
                </a>
                <a 
                  href="https://line.me/ti/g/NbNGnW4Eh6" 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="px-4 py-2 bg-[#020617]/40 border border-slate-800 hover:border-[#e63946] rounded-full hover:bg-[#e63946] hover:text-white transition-all text-slate-300 text-xs font-bold flex items-center gap-2"
                >
                  <MessageCircle size={14} className="shrink-0" /> LINE 群組
                </a>
              </div>
            </div>
          </div>

          {/* Quick Links */}
          <div className="lg:col-span-2 lg:col-start-6 space-y-6">
            <h4 className="text-xs font-bold uppercase tracking-[0.2em] text-[#e63946]">慢旅探索</h4>
            <ul className="space-y-3 text-sm text-slate-400">
              <li><a href="japan-travel.html" className="hover:text-white transition-colors">日本自由行</a></li>
              <li><a href="korea-travel.html" className="hover:text-white transition-colors">韓國自由行</a></li>
              <li><a href="taiwan-travel.html" className="hover:text-white transition-colors">台灣旅遊</a></li>
              <li><a href="southeast-asia.html" className="hover:text-white transition-colors">東南亞自由行</a></li>
              <li><a href="travel-tools.html" className="hover:text-white transition-colors">旅遊工具</a></li>
            </ul>
          </div>

          <div className="lg:col-span-2 space-y-6">
            <h4 className="text-xs font-bold uppercase tracking-[0.2em] text-[#e63946]">支援中心</h4>
            <ul className="space-y-3 text-sm text-slate-400">
              <li><a href="about.html" className="hover:text-white transition-colors">關於我們</a></li>
              <li><a href="contact.html" className="hover:text-white transition-colors">聯絡我們</a></li>
            </ul>
          </div>

          {/* Newsletter Input */}
          <div className="lg:col-span-3 space-y-6">
            <h4 className="text-xs font-bold uppercase tracking-[0.2em] text-[#e63946]">慢旅期刊</h4>
            <p className="text-sm text-slate-400 leading-relaxed">
              訂閱我們的極簡期刊，定期接收我們精心挑選的慢旅紀事、編輯推薦導航以及精品設計旅宿評測。
            </p>
            <form onSubmit={handleSubscribe} className="relative flex items-center">
              <input
                type="email"
                required
                placeholder="輸入您的電子信箱..."
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full bg-[#020617]/50 border border-slate-800 rounded-full px-5 py-3 pr-12 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-[#e63946] transition-all"
              />
              <button
                type="submit"
                className="absolute right-1.5 p-2 bg-[#e63946] hover:bg-[#b91c1c] text-white rounded-full transition-colors focus:outline-none"
              >
                {subscribed ? <Check size={16} /> : <Mail size={16} />}
              </button>
            </form>
            {subscribed && (
              <p className="text-xs text-[#e63946] animate-fade-in flex items-center gap-1">
                <Check size={12} /> 訂閱成功！感謝您加入我們的慢旅行列。
              </p>
            )}
          </div>

        </div>

        {/* Footer Bottom */}
        <div className="flex flex-col md:flex-row justify-between items-center pt-8 text-xs text-slate-500 gap-4">
          <div>
            © 2026 均在路上 Travel Lab.版權所有
          </div>
          <div className="flex items-center gap-1">
            Made with <Heart size={10} className="text-[#e63946] fill-[#e63946]" /> by 均在路上小編
          </div>
          <div className="flex gap-6">
            <a href="privacy.html" className="hover:text-slate-300 transition-colors">隱私權政策</a>
            <a href="terms.html" className="hover:text-slate-300 transition-colors">使用條款</a>
          </div>
        </div>
      </div>
    </footer>
  );
};
