// -*- coding: utf-8 -*-
// fix_homepage_seo.cjs - Add comprehensive OG/Twitter/JSON-LD to index.html
const fs = require('fs');
const path = require('path');

const indexPath = path.join(__dirname, 'index.html');
let html = fs.readFileSync(indexPath, 'utf-8');

// --- 1. Title (already present, just ensure it's optimal) ---
const currentTitle = html.match(/<title>(.*?)<\/title>/);
console.log('Current title:', currentTitle ? currentTitle[1] : 'NOT FOUND');

// --- 2. Meta description (already present) ---
const currentDesc = html.match(/<meta name="description" content="([^"]*)"/);
console.log('Current desc:', currentDesc ? currentDesc[1].substring(0, 60) + '...' : 'NOT FOUND');

// --- 3. Check if OG tags already exist ---
if (html.includes('og:title') && html.includes('og:image')) {
    console.log('OG tags already present - skipping');
} else {
    // Add comprehensive OG + Twitter tags before </head>
    const ogTags = `
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://golightly.fun/" />
    <meta property="og:title" content="均在路上 Travel Lab｜用最少預算走最多地方的實戰旅遊攻略" />
    <meta property="og:description" content="日本、韓國、東南亞自由行攻略，含真實行程規劃、交通教學、美食推薦與實際花費分享。每篇攻略由實地走訪者撰寫，助你省錢玩遍亞洲。" />
    <meta property="og:image" content="https://golightly.fun/images/hero-golightly.webp" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:site_name" content="均在路上 Travel Lab" />
    <meta property="og:locale" content="zh_TW" />
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@golightlyfun" />
    <meta name="twitter:title" content="均在路上 Travel Lab｜用最少預算走最多地方的實戰旅遊攻略" />
    <meta name="twitter:description" content="日本、韓國、東南亞自由行攻略，含真實行程規劃、交通教學、美食推薦與實際花費分享。" />
    <meta name="twitter:image" content="https://golightly.fun/images/hero-golightly.webp" />
`;

    // Insert before </head>
    html = html.replace('</head>', ogTags + '\n  </head>');
    console.log('Added OG + Twitter tags');
}

// --- 4. Check if WebSite JSON-LD exists ---
if (html.includes('"@type":"WebSite"')) {
    console.log('WebSite JSON-LD already present - skipping');
} else {
    const jsonLd = `
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "均在路上 Travel Lab",
  "url": "https://golightly.fun/",
  "description": "台港旅客省錢自由行攻略平台，涵蓋日本、韓國、東南亞實戰旅遊指南",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://golightly.fun/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "均在路上 Travel Lab",
  "url": "https://golightly.fun/",
  "logo": "https://golightly.fun/images/travel-lab-logo.png",
  "sameAs": [
    "https://instagram.com/golightlyfun",
    "https://facebook.com/golightlyfun"
  ]
}
</script>
`;

    html = html.replace('</head>', jsonLd + '\n  </head>');
    console.log('Added WebSite + Organization JSON-LD');
}

// --- 5. Add H1 to body if missing ---
if (html.includes('<h1')) {
    console.log('H1 already present - skipping');
} else {
    // Find the <body> opening and add H1 after it
    html = html.replace(/<body[^>]*>/, (match) => {
        return match + `
    <h1 class="sr-only">均在路上 Travel Lab — 台港旅客省錢自由行攻略平台</h1>
`;
    });
    console.log('Added sr-only H1 to body');
}

fs.writeFileSync(indexPath, html, 'utf-8');
console.log('\nindex.html updated successfully!');
