const fs = require('fs');
const path = require('path');
const BASE = __dirname;

function read(f) { return fs.readFileSync(path.join(BASE, f), 'utf8'); }
function write(f, c) { fs.writeFileSync(path.join(BASE, f), c, 'utf8'); }

const exclude = new Set(['404.html','index.html','about.html','contact.html','disclaimer.html','privacy.html','terms.html','monthly-review.html']);
const htmlFiles = fs.readdirSync(BASE).filter(f => f.endsWith('.html') && fs.statSync(path.join(BASE, f)).isFile() && !exclude.has(f));

let fixedCount = 0;

for (const file of htmlFiles) {
  let content = read(file);
  const origLen = content.length;
  
  // Remove ALL old 延伸閱讀 sections that are NOT the correct card-style
  // Strategy: remove everything between any 延伸閱讀 heading (h2/h3/h4) and the footer,
  // EXCEPT the correct card-style section (h2.section-title + related-list + related-card)
  
  // Step 1: Remove any <h4>延伸閱讀 or <h3>延伸閱讀 blocks (these are always the old list style)
  content = content.replace(/<h[34][^>]*>[^<]*延伸閱讀[^<]*<\/h[34]>[\s\S]*?(?=\s*<div class="cta-box"|\s*<footer|\s*<!-- FOOTER|\s*<!-- GA|$)/gi, '');
  
  // Step 2: Remove any <h2>延伸閱讀 that is NOT section-title (old card-style without proper class)
  content = content.replace(/<h2[^>]*>[^<]*延伸閱讀[^<]*<\/h2>(?!\s*<div class="related-list">)[\s\S]*?(?=\s*<div class="cta-box"|\s*<footer|\s*<!-- FOOTER|\s*<!-- GA|$)/gi, '');
  
  // Step 3: Remove "日本自由行延伸閱讀" or other variations inside h4/h3
  content = content.replace(/<h[34][^>]*>[^<]*延伸閱讀[^<]*<\/h[34]>[\s\S]*?(?=\s*<div class="cta-box"|\s*<footer|\s*<!-- FOOTER|\s*<!-- GA|$)/gi, '');
  
  // Step 4: Remove any remaining old-style blocks (div.info-box containing 延伸閱讀)
  content = content.replace(/<div class="info-box">[\s\S]*?延伸閱讀[\s\S]*?<\/div>\s*<\/div>/gi, '');
  
  // Step 5: Remove remaining 延伸閱讀 that's just a comment
  content = content.replace(/<!--\s*延伸閱讀[\s\S]*?-->/gi, '');
  
  // Step 6: Remove the "延伸閱讀 -->" line in footer (leftover)
  content = content.replace(/延伸閱讀\s*-->\s*/g, '');
  
  // Step 7: Clean up multiple trailing </div> before footer (from removed sections)
  // Don't over-aggressively remove, just reduce consecutive ones
  content = content.replace(/(<\/div>\s*){4,}(?=\s*(?:<footer|<!-- FOOTER|<!-- GA))/gi, '</div>\n');
  
  if (content.length !== origLen) {
    write(file, content);
    fixedCount++;
    console.log(`CLEANED: ${file} (${origLen} -> ${content.length})`);
  }
}

console.log(`\nCleaned ${fixedCount} pages`);
