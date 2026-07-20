import React from 'react';

// category → 地區入口對應（與 vite.config.ts 的 CATEGORY_PORTAL 一致）
const CATEGORY_PORTAL: Record<string, { label: string; url: string }> = {
  '日本自由行': { label: '日本自由行', url: 'https://golightly.fun/japan-travel.html' },
  '韓國自由行': { label: '韓國自由行', url: 'https://golightly.fun/korea-travel.html' },
  '台灣旅遊': { label: '台灣旅遊', url: 'https://golightly.fun/taiwan-travel.html' },
  '台灣自由行': { label: '台灣旅遊', url: 'https://golightly.fun/taiwan-travel.html' },
  '東南亞自由行': { label: '東南亞自由行', url: 'https://golightly.fun/southeast-asia.html' },
  '旅遊工具': { label: '旅遊工具', url: 'https://golightly.fun/travel-tools.html' },
  '關於我們': { label: '關於我們', url: 'https://golightly.fun/about.html' },
};

interface BreadcrumbProps {
  title: string;
  category?: string;
}

export const Breadcrumb: React.FC<BreadcrumbProps> = ({ title, category }) => {
  const portal = category ? CATEGORY_PORTAL[category] : undefined;
  return (
    <nav aria-label="麵包屑導覽" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-4 pb-1 text-sm text-slate-500">
      <ol className="flex flex-wrap items-center gap-x-1.5 gap-y-1">
        <li>
          <a href="https://golightly.fun/" className="hover:text-tiffany transition-colors">首頁</a>
        </li>
        {portal && (
          <li className="flex items-center gap-1.5">
            <span className="text-slate-300" aria-hidden="true">/</span>
            <a href={portal.url} className="hover:text-tiffany transition-colors">{portal.label}</a>
          </li>
        )}
        <li className="flex items-center gap-1.5">
          <span className="text-slate-300" aria-hidden="true">/</span>
          <span className="text-slate-700 font-medium" aria-current="page">{title}</span>
        </li>
      </ol>
    </nav>
  );
};
