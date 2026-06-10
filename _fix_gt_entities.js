const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let fixed = 0;

files.forEach(file => {
  const full = path.join(dir, file);
  let content = fs.readFileSync(full, 'utf8');
  const original = content;

  // Fix: Remove orphan &gt; (HTML entity >) between tag closings and openings
  // This is leftover from <p>>>>>>>...</p> wrapping meta/link tags
  content = content.replace(/>&gt;(\s*<meta)/g, '>$1');
  content = content.replace(/>&gt;(\s*<link)/g, '>$1');
  content = content.replace(/>&gt;(\s*<!--)/g, '>$1');
  content = content.replace(/>&gt;(\s*<script)/g, '>$1');
  content = content.replace(/>&gt;(\s*<style)/g, '>$1');

  // Also fix any orphan &gt; that appears standalone in the body (between tags)
  content = content.replace(/>&gt;(\s*<\/)/g, '>$1');
  content = content.replace(/&gt;(\s*<)/g, '>$1');

  // Clean up any <p>&gt;</p> empty remnants
  content = content.replace(/<p>&gt;<\/p>/g, '');
  // Clean up <p>&gt; followed by non-tag
  content = content.replace(/<p>&gt;(\s*)/g, '$1');

  if (content !== original) {
    fs.writeFileSync(full, content, 'utf8');
    fixed++;
    console.log('Fixed: ' + file);
  }
});

console.log('\nDone: ' + fixed + ' files fixed');