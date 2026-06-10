const fs = require('fs');
const path = require('path');
const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f !== '404.html');

let ok = 0, bad = 0;
for (const file of files) {
  const html = fs.readFileSync(path.join(dir, file), 'utf-8');
  const footerIdx = html.indexOf('<footer class="site-footer">');
  if (footerIdx === -1) continue;
  const before = html.substring(footerIdx - 100, footerIdx);
  if (before.includes('/article-container')) {
    ok++;
  } else {
    bad++;
    console.log(`BAD: ${file}`);
  }
}
console.log(`OK: ${ok}, BAD: ${bad}`);