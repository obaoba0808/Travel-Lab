const fs = require('fs');
const path = require('path');

// Fix pages where footer is INSIDE article-container instead of outside
// The pattern: footer should have </div><!-- /article-container --> before it

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f !== '404.html');

let fixed = 0;

for (const file of files) {
  let html = fs.readFileSync(path.join(dir, file), 'utf-8');
  
  // Check if </div><!-- /article-container --> exists before footer
  const footerIdx = html.indexOf('<footer class="site-footer">');
  if (footerIdx === -1) continue;
  
  const beforeFooter = html.substring(footerIdx - 200, footerIdx);
  
  if (!beforeFooter.includes('/article-container')) {
    // Missing article-container close. Add it.
    // Find the last </div> before footer and add closing div + comment after it
    const lastDivClose = html.lastIndexOf('</div>', footerIdx);
    html = html.substring(0, lastDivClose + 6) + '\n</div><!-- /article-container -->\n<!-- FOOTER -->\n' + html.substring(footerIdx);
    fs.writeFileSync(path.join(dir, file), html, 'utf-8');
    console.log(`FIXED: ${file}`);
    fixed++;
  }
}

console.log(`\nTotal fixed: ${fixed}`);