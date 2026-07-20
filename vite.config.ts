import path from 'path';
import fs from 'fs';
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import { travelArticles } from './data/articles';
import { customPages } from './data/customPages';

// 靜態 HTML 生成插件
function staticHtmlGenerator() {
  return {
    name: 'static-html-generator',
    closeBundle() {
      const distDir = path.resolve(__dirname, 'dist');
      const indexPath = path.join(distDir, 'index.html');
      
      if (!fs.existsSync(indexPath)) {
        console.log('跳過靜態 HTML 生成：未找到 dist/index.html。');
        return;
      }
      
      const template = fs.readFileSync(indexPath, 'utf-8');
      
      // 讀取 metadata.json 作為預設備用值
      const metadataPath = path.resolve(__dirname, 'metadata.json');
      let metadataName = '均在路上 Travel Lab';
      let metadataDescription = '一個實戰旅遊攻略網站，專注於日本、韓國、台灣、東南亞自由行攻略。每篇內容都經過實地走訪驗證，提供具體的行程規劃、交通教學、美食推薦和預算參考。';
      
      if (fs.existsSync(metadataPath)) {
        try {
          const metaObj = JSON.parse(fs.readFileSync(metadataPath, 'utf-8'));
          if (metaObj.name) metadataName = metaObj.name;
          if (metaObj.description) metadataDescription = metaObj.description;
        } catch (err) {
          console.error('讀取 metadata.json 失敗，使用預設值：', err);
        }
      }
      
      // 確保 dist/articles 目錄存在
      const articlesDir = path.join(distDir, 'articles');
      if (!fs.existsSync(articlesDir)) {
        fs.mkdirSync(articlesDir, { recursive: true });
      }
      
      // 輔助函式：置換 SEO Meta 標籤（Title / Description / Canonical / OG / Twitter）
      const replaceMeta = (html: string, title: string, description: string, imageUrl: string, canonicalUrl: string, keywords: string) => {
        let h = html;
        
        // 1. 替換 Title
        const titleRegex = /<title>.*?<\/title>/;
        const newTitle = `<title>${title}</title>`;
        if (titleRegex.test(h)) {
          h = h.replace(titleRegex, newTitle);
        } else {
          h = h.replace('</head>', `${newTitle}\n</head>`);
        }
        
        // 2. 替換 Description
        const descRegex = /<meta\s+name="description"\s+content="[^"]*"\s*\/?>/i;
        const newDesc = `<meta name="description" content="${description}" />`;
        if (descRegex.test(h)) {
          h = h.replace(descRegex, newDesc);
        } else {
          h = h.replace('</head>', `${newDesc}\n</head>`);
        }
        
        // 3. 替換 Canonical
        const canonicalRegex = /<link\s+rel="canonical"\s+href="[^"]*"\s*\/?>/i;
        const newCanonical = `<link rel="canonical" href="${canonicalUrl}" />`;
        if (canonicalRegex.test(h)) {
          h = h.replace(canonicalRegex, newCanonical);
        } else {
          h = h.replace('</head>', `${newCanonical}\n</head>`);
        }
        
        // 4. 注入其他 Meta 標籤 (OG, Twitter, Keywords, Robots)
        const ogTitleRegex = /<meta\s+property="og:title"\s+content="[^"]*"\s*\/?>/i;
        const ogDescRegex = /<meta\s+property="og:description"\s+content="[^"]*"\s*\/?>/i;
        const twitterTitleRegex = /<meta\s+name="twitter:title"\s+content="[^"]*"\s*\/?>/i;
        const twitterDescRegex = /<meta\s+name="twitter:description"\s+content="[^"]*"\s*\/?>/i;

        if (ogTitleRegex.test(h)) {
          h = h.replace(ogTitleRegex, `<meta property="og:title" content="${title}" />`);
        }
        if (ogDescRegex.test(h)) {
          h = h.replace(ogDescRegex, `<meta property="og:description" content="${description}" />`);
        }
        if (twitterTitleRegex.test(h)) {
          h = h.replace(twitterTitleRegex, `<meta name="twitter:title" content="${title}" />`);
        }
        if (twitterDescRegex.test(h)) {
          h = h.replace(twitterDescRegex, `<meta name="twitter:description" content="${description}" />`);
        }

        const additionalTags = [
          !h.includes('name="keywords"') ? `<meta name="keywords" content="${keywords}" />` : '',
          !h.includes('name="robots"') ? `<meta name="robots" content="index, follow" />` : '',
          !ogTitleRegex.test(html) ? `<meta property="og:title" content="${title}" />` : '',
          !ogDescRegex.test(html) ? `<meta property="og:description" content="${description}" />` : '',
          imageUrl && !h.includes('property="og:image"') ? `<meta property="og:image" content="${imageUrl}" />` : '',
          !h.includes('property="og:url"') ? `<meta property="og:url" content="${canonicalUrl}" />` : '',
          !h.includes('property="og:type"') ? `<meta property="og:type" content="article" />` : '',
          !h.includes('name="twitter:card"') ? `<meta name="twitter:card" content="summary_large_image" />` : '',
          !twitterTitleRegex.test(html) ? `<meta name="twitter:title" content="${title}" />` : '',
          !twitterDescRegex.test(html) ? `<meta name="twitter:description" content="${description}" />` : '',
          imageUrl && !h.includes('name="twitter:image"') ? `<meta name="twitter:image" content="${imageUrl}" />` : '',
        ].filter(Boolean).join('\n    ');
        
        if (additionalTags) {
          h = h.replace('</head>', `${additionalTags}\n</head>`);
        }
        
        return h;
      };

      // 移除所有既有的 JSON-LD 腳本（改由生成器統一管理，避免重複與不一致）
      const stripJsonLd = (html: string): string => {
        return html.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/gi, '');
      };

      // 從 HTML 中解析頁面專屬的 FAQPage 結構化資料（保留既有問答，避免遺失）
      const extractFaqPage = (html: string): any | null => {
        const matches = html.match(/<script type="application\/ld\+json">[\s\S]*?<\/script>/gi);
        if (!matches) return null;
        for (const m of matches) {
          try {
            const jsonStr = m.replace(/<script[^>]*>/i, '').replace(/<\/script>/i, '');
            const data = JSON.parse(jsonStr);
            const arr = Array.isArray(data) ? data : [data];
            for (const d of arr) {
              if (d && d['@type'] === 'FAQPage' && Array.isArray(d.mainEntity) && d.mainEntity.length > 0) {
                return d;
              }
            }
          } catch (e) { /* 解析失敗則忽略，不阻斷建置 */ }
        }
        return null;
      };

      // 分類 → 地區入口頁對應（用於 BreadcrumbList 中間層）
      const CATEGORY_PORTAL: Record<string, { label: string; url: string }> = {
        '日本自由行': { label: '日本自由行', url: 'https://golightly.fun/japan-travel.html' },
        '韓國自由行': { label: '韓國自由行', url: 'https://golightly.fun/korea-travel.html' },
        '台灣旅遊': { label: '台灣旅遊', url: 'https://golightly.fun/taiwan-travel.html' },
        '台灣自由行': { label: '台灣旅遊', url: 'https://golightly.fun/taiwan-travel.html' },
        '東南亞自由行': { label: '東南亞自由行', url: 'https://golightly.fun/southeast-asia.html' },
        '旅遊工具': { label: '旅遊工具', url: 'https://golightly.fun/travel-tools.html' },
        '關於我們': { label: '關於我們', url: 'https://golightly.fun/about.html' },
      };

      // 建立 BreadcrumbList 結構化資料（首頁 → 地區入口 → 當前頁）
      const buildBreadcrumb = (pageUrl: string, pageTitle: string, category?: string): any => {
        const items: any[] = [
          { '@type': 'ListItem', position: 1, name: '首頁', item: 'https://golightly.fun/' }
        ];
        if (category && CATEGORY_PORTAL[category]) {
          const p = CATEGORY_PORTAL[category];
          items.push({ '@type': 'ListItem', position: items.length + 1, name: p.label, item: p.url });
        }
        items.push({ '@type': 'ListItem', position: items.length + 1, name: pageTitle, item: pageUrl });
        return {
          '@context': 'https://schema.org',
          '@type': 'BreadcrumbList',
          itemListElement: items
        };
      };

      // 建立 Article / AboutPage 主結構化資料
      const buildPageSchema = (page: any, canonicalUrl: string, title: string, description: string, imageUrl: string, siteName: string): any => {
        const isAbout = page.id === 'about';
        return {
          '@context': 'https://schema.org',
          '@type': isAbout ? 'AboutPage' : 'Article',
          '@id': `${canonicalUrl}#article`,
          'headline': page.title,
          'image': imageUrl || 'https://golightly.fun/images/logo.webp',
          'datePublished': '2026-06-25',
          'dateModified': '2026-07-20',
          'author': { '@type': 'Organization', 'name': siteName },
          'publisher': {
            '@type': 'Organization',
            'name': siteName,
            'url': 'https://golightly.fun',
            'logo': { '@type': 'ImageObject', 'url': 'https://golightly.fun/images/logo.webp' }
          },
          'mainEntityOfPage': { '@type': 'WebPage', '@id': canonicalUrl },
          'articleSection': page.category || '旅遊攻略',
          'keywords': `${page.title}, 自由行, 旅遊攻略, 均在路上`,
          'description': description
        };
      };

      // 在 </head> 前注入多個 JSON-LD 區塊
      const injectJsonLd = (html: string, blocks: any[]): string => {
        let h = html;
        for (const block of blocks) {
          const script = `  <script type="application/ld+json">\n${JSON.stringify(block, null, 2)}\n  </script>`;
          h = h.replace('</head>', `${script}\n</head>`);
        }
        return h;
      };
      
      // 可見麵包屑 HTML（與 JSON-LD 麵包屑共用 CATEGORY_PORTAL 邏輯）
      const buildBreadcrumbHtml = (pageUrl: string, pageTitle: string, category?: string): string => {
        const portal = category ? CATEGORY_PORTAL[category] : undefined;
        const items: string[] = [
          `<li><a href="https://golightly.fun/" class="hover:text-tiffany transition-colors">首頁</a></li>`
        ];
        if (portal) {
          items.push(`<li class="flex items-center gap-1.5"><span class="text-slate-300" aria-hidden="true">/</span><a href="${portal.url}" class="hover:text-tiffany transition-colors">${portal.label}</a></li>`);
        }
        items.push(`<li class="flex items-center gap-1.5"><span class="text-slate-300" aria-hidden="true">/</span><span class="text-slate-700 font-medium" aria-current="page">${pageTitle}</span></li>`);
        return `  <nav aria-label="麵包屑導覽" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-4 pb-1 text-sm text-slate-500">\n    <ol class="flex flex-wrap items-center gap-x-1.5 gap-y-1">\n      ${items.join('\n      ')}\n    </ol>\n  </nav>`;
      };
      
      // 將可見麵包屑注入實體頁（global-header.js 之後、hero 之前；SPA 頁由 React 元件處理，此處不注入）
      const injectBreadcrumbHtml = (html: string, navHtml: string): string => {
        const m = html.match(/<script src="\/global-header\.js[^>]*>\s*<\/script>/);
        if (m) {
          return html.replace(m[0], `${m[0]}\n\n${navHtml}`);
        }
        return html;
      };
      
      // 統一注入 hreflang（先移除既有，再補 zh-Hant / zh-TW / x-default）
      const injectHreflang = (html: string, canonicalUrl: string): string => {
        let h = html.replace(/<link[^>]*\shreflang[^>]*\/?>/gi, '');
        const tags = [
          `<link href="${canonicalUrl}" hreflang="zh-Hant" rel="alternate"/>`,
          `<link href="${canonicalUrl}" hreflang="zh-TW" rel="alternate"/>`,
          `<link href="${canonicalUrl}" hreflang="x-default" rel="alternate"/>`
        ].join('\n  ');
        return h.replace('</head>', `  ${tags}\n</head>`);
      };
      
      // 生成文章專題靜態頁面
      travelArticles.forEach(article => {
        const title = `${article.title}｜${metadataName}`;
        const description = article.intro || article.subtitle || metadataDescription;
        const imageUrl = article.heroImage || '';
        const canonicalUrl = `https://golightly.fun/articles/${article.id}.html`;
        const keywords = `${article.title}, ${article.country}旅遊, 自由行, 旅遊攻略, 均在路上`;
        
        const jsonLd = {
          "@context": "https://schema.org",
          "@type": "BlogPosting",
          "@id": `${canonicalUrl}#article`,
          "headline": article.title,
          "image": imageUrl || "https://golightly.fun/images/logo.webp",
          "genre": article.category || "旅遊攻略",
          "keywords": keywords,
          "publisher": {
            "@type": "Organization",
            "name": metadataName,
            "url": "https://golightly.fun",
            "logo": {
              "@type": "ImageObject",
              "url": "https://golightly.fun/images/logo.webp"
            }
          },
          "url": canonicalUrl,
          "mainEntityOfPage": { "@type": "WebPage", "@id": canonicalUrl },
          "datePublished": article.publishDate || "2026-06-25",
          "dateModified": "2026-07-20",
          "author": {
            "@type": "Person",
            "name": article.author?.name || "Kristian Sigurd"
          },
          "description": description
        };
        
        // 文章麵包屑：首頁 → 國家入口（若有）→ 文章
        const breadcrumb = buildBreadcrumb(canonicalUrl, article.title, article.country ? `${article.country}自由行` : undefined);
        
        let articleHtml = replaceMeta(template, title, description, imageUrl, canonicalUrl, keywords);
        articleHtml = stripJsonLd(articleHtml);
        articleHtml = injectJsonLd(articleHtml, [jsonLd, breadcrumb]);
        articleHtml = injectHreflang(articleHtml, canonicalUrl);
        const articlePath = path.join(articlesDir, `${article.id}.html`);
        fs.writeFileSync(articlePath, articleHtml, 'utf-8');
        console.log(`[Static Generator] 已成功為文章《${article.title}》生成靜態 HTML 檔：/articles/${article.id}.html`);
      });
      
      // 生成自訂功能分頁靜態頁面
      customPages.forEach(page => {
        const pagePath = path.join(distDir, `${page.id}.html`);
        const title = `${page.title}｜${metadataName}`;
        const description = page.intro || page.description || metadataDescription;
        const imageUrl = page.coverImage || '';
        const canonicalUrl = `https://golightly.fun/${page.id}.html`;
        const keywords = `${page.title}, 自由行, 旅遊攻略, 均在路上`;

        const physicalPath = path.resolve(__dirname, page.url || `${page.id}.html`);
        if (fs.existsSync(physicalPath)) {
          const physicalContent = fs.readFileSync(physicalPath, 'utf-8');
          // 保留實體 HTML 中既有的 FAQPage 問答（若有）
          const faq = extractFaqPage(physicalContent);
          const jsonLd = buildPageSchema(page, canonicalUrl, title, description, imageUrl, metadataName);
          const breadcrumb = buildBreadcrumb(canonicalUrl, page.title, page.category);
          const blocks = [jsonLd, breadcrumb];
          if (faq) blocks.push(faq);
          // 透過 replaceMeta 將實體 HTML 內部的 SEO 欄位對齊 page 資料物件，並由生成器統一注入 JSON-LD
          let optimizedHtml = replaceMeta(physicalContent, title, description, imageUrl, canonicalUrl, keywords);
          optimizedHtml = stripJsonLd(optimizedHtml);
          optimizedHtml = injectJsonLd(optimizedHtml, blocks);
          optimizedHtml = injectHreflang(optimizedHtml, canonicalUrl);
          const visibleBreadcrumb = buildBreadcrumbHtml(canonicalUrl, page.title, page.category);
          optimizedHtml = injectBreadcrumbHtml(optimizedHtml, visibleBreadcrumb);
          fs.writeFileSync(pagePath, optimizedHtml, 'utf-8');
          console.log(`[Static Generator] 已成功複製並優化實體《${page.title}》靜態 HTML 至：/dist/${page.id}.html`);
          return;
        }
        
        const jsonLd = buildPageSchema(page, canonicalUrl, title, description, imageUrl, metadataName);
        const breadcrumb = buildBreadcrumb(canonicalUrl, page.title, page.category);
        let pageHtml = replaceMeta(template, title, description, imageUrl, canonicalUrl, keywords);
        pageHtml = stripJsonLd(pageHtml);
        pageHtml = injectJsonLd(pageHtml, [jsonLd, breadcrumb]);
        pageHtml = injectHreflang(pageHtml, canonicalUrl);
        fs.writeFileSync(pagePath, pageHtml, 'utf-8');
        console.log(`[Static Generator] 已成功為功能頁《${page.title}》生成靜態 HTML 檔：/${page.id}.html`);
      });

      // === 動態生成 sitemap.xml ===
      const sitemapPath = path.join(distDir, 'sitemap.xml');
      const today = new Date().toISOString().split('T')[0];
      const urls = new Set<string>();
      
      // 1. 首頁
      urls.add('https://golightly.fun/');

      // 2. 加入 customPages 設定檔中的所有頁面（static generator 必定會複製到 dist）
      customPages.forEach(page => {
        urls.add(`https://golightly.fun/${page.url || `${page.id}.html`}`);
      });

      // 3. 加入動態產生的 travelArticles 文章專題頁面
      travelArticles.forEach(article => {
        urls.add(`https://golightly.fun/articles/${article.id}.html`);
      });
      
      let sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>\n`;
      sitemapContent += `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;
      
      urls.forEach(url => {
        const priority = url === 'https://golightly.fun/' ? '1.0' : 
                         url.includes('/articles/') ? '0.6' : '0.8';
        const changefreq = url === 'https://golightly.fun/' ? 'daily' : 'weekly';
        
        sitemapContent += `  <url>\n`;
        sitemapContent += `    <loc>${url}</loc>\n`;
        sitemapContent += `    <lastmod>${today}</lastmod>\n`;
        sitemapContent += `    <changefreq>${changefreq}</changefreq>\n`;
        sitemapContent += `    <priority>${priority}</priority>\n`;
        sitemapContent += `  </url>\n`;
      });
      
      sitemapContent += `</urlset>\n`;
      fs.writeFileSync(sitemapPath, sitemapContent, 'utf-8');
      console.log(`[Static Generator] 成功生成 sitemap.xml 至 /dist/sitemap.xml (共 ${urls.size} 個網址)`);

      // === 動態生成 robots.txt ===
      const robotsPath = path.join(distDir, 'robots.txt');
      const robotsContent = `User-agent: *\nAllow: /\n\nSitemap: https://golightly.fun/sitemap.xml\n`;
      fs.writeFileSync(robotsPath, robotsContent, 'utf-8');
      console.log(`[Static Generator] 成功生成 robots.txt 至 /dist/robots.txt`);
    }
  };
}

// 開發伺服器 HTML 導向插件：在開發模式下將所有未實際存在的 *.html 與 /articles/*.html 導向至 index.html
function devHtmlFallbackPlugin() {
  return {
    name: 'dev-html-fallback',
    configureServer(server: any) {
      server.middlewares.use((req: any, res: any, next: any) => {
        const url = req.url ? req.url.split('?')[0] : '';
        
        if (url.endsWith('.html') && url !== '/index.html' && !url.includes('/@') && !url.includes('/node_modules/')) {
          const filename = url.split('/').pop() || '';
          const pageId = filename.replace('.html', '');
          
          const isCustomPage = customPages.some(page => page.id === pageId);
          const isArticle = url.startsWith('/articles/') && travelArticles.some(art => art.id === pageId);
          
          // Check if there is a physical file in the workspace root
          const hasPhysicalFile = fs.existsSync(path.resolve(__dirname, filename)) || (isCustomPage && (() => {
            const page = customPages.find(p => p.id === pageId);
            return page && fs.existsSync(path.resolve(__dirname, page.url));
          })());
          
          // 若為自訂功能分頁且「無」實體存在的 HTML 檔案，或文章專頁，則在開發伺服器重導向至 index.html
          if ((isCustomPage && !hasPhysicalFile) || isArticle) {
            req.url = '/index.html';
          }
        }
        next();
      });
    }
  };
}

// 遞迴複製目錄函數，確保所有圖片都能從 public/images 被存取
function copyDirRecursive(src: string, dest: string) {
  if (!fs.existsSync(src)) return;
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// 在伺服器啟動或打包時自動同步圖片
const srcImages = path.resolve(__dirname, 'src/assets/images');
const destImages = path.resolve(__dirname, 'public/images');
copyDirRecursive(srcImages, destImages);
console.log('[Image Sync] Copied images from src/assets/images to public/images');

export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, '.', '');
    return {
      server: {
        port: 3000,
        host: '0.0.0.0',
      },
      plugins: [react(), staticHtmlGenerator(), devHtmlFallbackPlugin()],
      define: {
        'process.env.API_KEY': JSON.stringify(env.GEMINI_API_KEY),
        'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY)
      },
      resolve: {
        alias: {
          '@': path.resolve(__dirname, '.'),
        }
      }
    };
});
