import path from 'path';
import fs from 'fs';
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import { travelArticles } from './data/articles';
import { customPages } from './data/customPages';

import { cloudflare } from "@cloudflare/vite-plugin";

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
      
      // 輔助函式：置換 SEO Meta 標籤與注入 JSON-LD 結構化數據
      const generatePageHtml = (templateHtml: string, title: string, description: string, imageUrl: string, canonicalUrl: string, keywords: string, extraJsonLd: any = null) => {
        let html = templateHtml;
        
        // 1. 替換 Title
        const titleRegex = /<title>.*?<\/title>/;
        const newTitle = `<title>${title}</title>`;
        if (titleRegex.test(html)) {
          html = html.replace(titleRegex, newTitle);
        } else {
          html = html.replace('</head>', `${newTitle}\n</head>`);
        }
        
        // 2. 替換 Description
        const descRegex = /<meta\s+name="description"\s+content="[^"]*"\s*\/?>/i;
        const newDesc = `<meta name="description" content="${description}" />`;
        if (descRegex.test(html)) {
          html = html.replace(descRegex, newDesc);
        } else {
          html = html.replace('</head>', `${newDesc}\n</head>`);
        }
        
        // 3. 替換 Canonical
        const canonicalRegex = /<link\s+rel="canonical"\s+href="[^"]*"\s*\/?>/i;
        const newCanonical = `<link rel="canonical" href="${canonicalUrl}" />`;
        if (canonicalRegex.test(html)) {
          html = html.replace(canonicalRegex, newCanonical);
        } else {
          html = html.replace('</head>', `${newCanonical}\n</head>`);
        }
        
        // 4. 注入其他 Meta 標籤 (OG, Twitter, Keywords, Robots)
        const ogTitleRegex = /<meta\s+property="og:title"\s+content="[^"]*"\s*\/?>/i;
        const ogDescRegex = /<meta\s+property="og:description"\s+content="[^"]*"\s*\/?>/i;
        const twitterTitleRegex = /<meta\s+name="twitter:title"\s+content="[^"]*"\s*\/?>/i;
        const twitterDescRegex = /<meta\s+name="twitter:description"\s+content="[^"]*"\s*\/?>/i;

        if (ogTitleRegex.test(html)) {
          html = html.replace(ogTitleRegex, `<meta property="og:title" content="${title}" />`);
        }
        if (ogDescRegex.test(html)) {
          html = html.replace(ogDescRegex, `<meta property="og:description" content="${description}" />`);
        }
        if (twitterTitleRegex.test(html)) {
          html = html.replace(twitterTitleRegex, `<meta name="twitter:title" content="${title}" />`);
        }
        if (twitterDescRegex.test(html)) {
          html = html.replace(twitterDescRegex, `<meta name="twitter:description" content="${description}" />`);
        }

        const additionalTags = [
          !html.includes('name="keywords"') ? `<meta name="keywords" content="${keywords}" />` : '',
          !html.includes('name="robots"') ? `<meta name="robots" content="index, follow" />` : '',
          !ogTitleRegex.test(templateHtml) ? `<meta property="og:title" content="${title}" />` : '',
          !ogDescRegex.test(templateHtml) ? `<meta property="og:description" content="${description}" />` : '',
          imageUrl && !html.includes('property="og:image"') ? `<meta property="og:image" content="${imageUrl}" />` : '',
          !html.includes('property="og:url"') ? `<meta property="og:url" content="${canonicalUrl}" />` : '',
          !html.includes('property="og:type"') ? `<meta property="og:type" content="article" />` : '',
          !html.includes('name="twitter:card"') ? `<meta name="twitter:card" content="summary_large_image" />` : '',
          !twitterTitleRegex.test(templateHtml) ? `<meta name="twitter:title" content="${title}" />` : '',
          !twitterDescRegex.test(templateHtml) ? `<meta name="twitter:description" content="${description}" />` : '',
          imageUrl && !html.includes('name="twitter:image"') ? `<meta name="twitter:image" content="${imageUrl}" />` : '',
        ].filter(Boolean).join('\n    ');
        
        if (additionalTags) {
          html = html.replace('</head>', `${additionalTags}\n</head>`);
        }
        
        // 5. 注入頁面專屬的 JSON-LD 結構數據
        if (extraJsonLd && !html.includes('type="application/ld+json"')) {
          const jsonLdScript = `<script type="application/ld+json">\n${JSON.stringify(extraJsonLd, null, 2)}\n</script>`;
          html = html.replace('</head>', `${jsonLdScript}\n</head>`);
        }
        
        return html;
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
          "datePublished": article.publishDate || "2026-06-25",
          "author": {
            "@type": "Person",
            "name": article.author?.name || "Kristian Sigurd"
          },
          "description": description
        };
        
        const articleHtml = generatePageHtml(template, title, description, imageUrl, canonicalUrl, keywords, jsonLd);
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
        
        const jsonLd = {
          "@context": "https://schema.org",
          "@type": "WebPage",
          "name": title,
          "description": description,
          "publisher": {
            "@type": "Organization",
            "name": metadataName,
            "url": "https://golightly.fun"
          },
          "url": canonicalUrl
        };

        const physicalPath = path.resolve(__dirname, page.url || `${page.id}.html`);
        if (fs.existsSync(physicalPath)) {
          const physicalContent = fs.readFileSync(physicalPath, 'utf-8');
          // 透過 generatePageHtml 將實體 HTML 內部的 SEO 欄位完全對齊 article/page 資料物件，避免空值
          const optimizedHtml = generatePageHtml(physicalContent, title, description, imageUrl, canonicalUrl, keywords, jsonLd);
          fs.writeFileSync(pagePath, optimizedHtml, 'utf-8');
          console.log(`[Static Generator] 已成功複製並優化實體《${page.title}》靜態 HTML 至：/dist/${page.id}.html`);
          return;
        }
        
        const pageHtml = generatePageHtml(template, title, description, imageUrl, canonicalUrl, keywords, jsonLd);
        fs.writeFileSync(pagePath, pageHtml, 'utf-8');
        console.log(`[Static Generator] 已成功為功能頁《${page.title}》生成靜態 HTML 檔：/${page.id}.html`);
      });

      // === 動態生成 sitemap.xml ===
      const sitemapPath = path.join(distDir, 'sitemap.xml');
      const today = new Date().toISOString().split('T')[0];
      const urls = new Set<string>();
      
      // 1. 首頁
      urls.add('https://golightly.fun/');
      
      // 2. 掃描專案根目錄下所有實體存在的靜態 HTML 檔案 (除 index.html 外)
      const rootFiles = fs.readdirSync(__dirname);
      rootFiles.forEach(file => {
        if (file.endsWith('.html') && file !== 'index.html') {
          urls.add(`https://golightly.fun/${file}`);
        }
      });
      
      // 3. 加入 customPages 設定檔中的所有頁面
      customPages.forEach(page => {
        urls.add(`https://golightly.fun/${page.url || `${page.id}.html`}`);
      });
      
      // 4. 加入動態產生的 travelArticles 文章專題頁面
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
      plugins: [react(), staticHtmlGenerator(), devHtmlFallbackPlugin(), cloudflare()],
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