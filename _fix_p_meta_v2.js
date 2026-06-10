const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let fixed = 0;

files.forEach(file => {
  const full = path.join(dir, file);
  let content = fs.readFileSync(full, 'utf8');
  const original = content;

  // Fix 1: Remove <p> wrapping meta/link tags (the broken structure)
  // Matches: <body><p><meta...<link...>  →  <body><meta...<link...>
  // Excludes any &gt; that was left as orphaned text between tags
  content = content.replace(
    /<body><p>((?:(?!<\/p>)[\s\S])*?<link )/g,
    '<body>$1'
  );

  // Fix 2: Remove any orphan &gt; that appears between meta tags or meta/link
  // These are leftover from broken <p>&gt;... structure
  content = content.replace(/&gt;(\s*<meta)/g, '$1');
  content = content.replace(/&gt;(\s*<link)/g, '$1');
  content = content.replace(/&gt;(\s*<!--)/g, '$1');

  // Fix 3: Clean up any remaining <p>&gt;</p> empty tags
  content = content.replace(/<p>&gt;<\/p>/g, '');

  if (content !== original) {
    fs.writeFileSync(full, content, 'utf8');
    fixed++;
    console.log('Fixed: ' + file);
  }
});

console.log('\nDone: ' + fixed + ' files fixed');