/**
 * Optimize page speed: apply index.html's non-blocking loading to all inner pages
 * 1. Google Fonts: media="print" onload="this.media='all'" + <noscript> fallback
 * 2. style.css: preload + onload swap + <noscript> fallback  
 */
const fs = require('fs');
const path = require('path');
const BASE = __dirname;

const exclude = new Set(['404.html','index.html','about.html','contact.html','disclaimer.html','privacy.html','terms.html','monthly-review.html']);
const htmlFiles = fs.readdirSync(BASE).filter(f => f.endsWith('.html') && fs.statSync(path.join(BASE, f)).isFile() && !exclude.has(f));

let fixedCount = 0;

for (const file of htmlFiles) {
  let content = fs.readFileSync(path.join(BASE, file), 'utf8');
  let changed = false;
  
  // 1. Fix Google Fonts loading (make non-blocking)
  const fontRegex = /<link[^>]+href="https:\/\/fonts\.googleapis\.com\/css2\?[^"]+"[^>]*rel="stylesheet"\s*\/?>/g;
  const fontMatch = content.match(fontRegex);
  
  if (fontMatch) {
    for (const match of fontMatch) {
      if (!match.includes('media="print"')) {
        const optimized = match
          .replace(/\/?>$/, '') // Remove trailing />
          .replace('rel="stylesheet"', 'media="print" onload="this.media=\'all\'" rel="stylesheet"')
          + '>\n<noscript>' + match + '</noscript>';
        content = content.replace(match, optimized);
        changed = true;
      }
    }
  }
  
  // 2. Fix style.css loading (preload + onload swap)
  const cssRegex = /<link[^>]+href="style\.css"[^>]*rel="stylesheet"\s*\/?>/g;
  const cssMatch = content.match(cssRegex);
  
  if (cssMatch) {
    for (const match of cssMatch) {
      if (!match.includes('as="style"')) {
        const optimized = '<link as="style" href="style.css" onload="this.onload=null;this.rel=\'stylesheet\'" rel="preload"/>\n<noscript>' + match + '</noscript>';
        content = content.replace(match, optimized);
        changed = true;
      }
    }
  }
  
  // 3. Ensure beautify-overrides.css and beautify.css are loaded after style.css (order matters)
  // (skip for now - they're small)
  
  if (changed) {
    fs.writeFileSync(path.join(BASE, file), content, 'utf8');
    fixedCount++;
    console.log(`FIXED: ${file}`);
  } else {
    console.log(`OK: ${file}`);
  }
}

console.log(`\n=== Summary ===`);
console.log(`Fixed: ${fixedCount}/${htmlFiles.length} pages`);
console.log(`Skipped: ${htmlFiles.length - fixedCount}/${htmlFiles.length} pages (already optimized)`);
