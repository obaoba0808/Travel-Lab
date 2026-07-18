// -*- coding: utf-8 -*-
// fix_broken_og.cjs - Fix &amp; entities in Unsplash URLs + busan-capsule missing image
const fs = require('fs');
const path = require('path');

const __dirname = process.cwd();

// 1. Fix &amp; entities in Unsplash URLs (physical HTML files)
const filesWithAmp = [
    'angkor-wat-2days.html',
    'kualalumpur-3days.html',
    'singapore-3days.html',
];

let fixedAmp = 0;
for (const fname of filesWithAmp) {
    const fpath = path.join(__dirname, fname);
    if (!fs.existsSync(fpath)) { console.log(`NOT FOUND: ${fname}`); continue; }
    let html = fs.readFileSync(fpath, 'utf-8');
    const before = html;
    // Decode &amp; in og:image URL only
    html = html.replace(
        /(<meta\s+property="og:image"\s+content=")([^"]*)&amp;([^"]*)("\s*\/?>)/gi,
        (match, open, beforeAmp, close) => {
            return open + beforeAmp.replace(/&amp;/g, '&') + close;
        }
    );
    // Simpler approach: just replace all &amp; in og:image tags
    html = html.replace(/(<meta\s+property="og:image"[^>]*content=")([^"]+)(")/gi, (m, prefix, url, suffix) => {
        if (url.includes('&amp;')) {
            return prefix + url.replace(/&amp;/g, '&') + suffix;
        }
        return m;
    });
    if (html !== before) {
        fs.writeFileSync(fpath, html, 'utf-8');
        fixedAmp++;
        console.log(`Fixed &amp; in: ${fname}`);
    } else {
        console.log(`No &amp; found: ${fname}`);
    }
}

// 2. Fix customPages.ts - busan-capsule coverImage
const cpPath = path.join(__dirname, 'data/customPages.ts');
if (fs.existsSync(cpPath)) {
    let content = fs.readFileSync(cpPath, 'utf-8');
    let fixed = 0;

    // busan-capsule-train.webp → busan-hero.webp
    if (content.includes('busan-capsule-train.webp')) {
        content = content.replace(/busan-capsule-train\.webp/g, 'busan-hero.webp');
        fixed++;
        console.log('Replaced busan-capsule-train.webp → busan-hero.webp in customPages.ts');
    }

    if (fixed > 0) {
        fs.writeFileSync(cpPath, content, 'utf-8');
        console.log(`Updated customPages.ts: ${fixed} replacement(s)`);
    } else {
        console.log('No changes needed in customPages.ts');
    }
}

console.log(`\nDone. Fixed ${fixedAmp} HTML files with &amp; encoding.`);
