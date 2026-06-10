const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let fixed = 0, total = 0;

files.forEach(file => {
  const full = path.join(dir, file);
  let content = fs.readFileSync(full, 'utf8');
  const original = content;

  // Core fix: remove <p> that wraps only meta/link tags (the broken structure)
  // Pattern: <body><p><meta...<meta...<link...> → <body><meta...<meta...<link...>
  // The <p> is never closed, so we strip the opening <p> after <body>
  content = content.replace(/<body><p>(<meta[\s\S]*?)(<link[\s\S]*?>)/g, '<body>$1$2');

  // Also fix leftover orphan <p>&gt;</p> or <p>&gt; patterns
  content = content.replace(/<p>&gt;(\s*)<\/p>/g, '');

  // Fix any stray </p> after body that was left from broken <p> wrapping
  content = content.replace(/<body><\/p>/g, '<body>');

  if (content !== original) {
    fs.writeFileSync(full, content, 'utf8');
    fixed++;
    console.log('Fixed: ' + file);
  }
  total++;
});

console.log('\nDone: ' + fixed + '/' + total + ' files fixed');