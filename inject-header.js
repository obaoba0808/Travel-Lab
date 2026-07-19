import fs from 'fs';
import path from 'path';

const rootDir = process.cwd();

// Find all HTML files in root (except index.html)
const files = fs.readdirSync(rootDir)
  .filter(file => file.endsWith('.html') && file !== 'index.html');

console.log(`Found ${files.length} HTML files to process.`);

files.forEach(file => {
  const filePath = path.join(rootDir, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  let modified = false;

  // 1. Update any existing global-header.js script tags to include the new cache-buster
  const existingScriptRegex = /<script[^>]*src=["']\/global-header\.js(?:\?v=[^"'\s]+)?["'][^>]*><\/script>/g;
  if (existingScriptRegex.test(content)) {
    content = content.replace(existingScriptRegex, '<!-- UNIFIED HEADER -->\n<script src="/global-header.js?v=20260627_v4" defer></script>');
    modified = true;
    console.log(`[${file}] Updated existing global-header.js reference to cache-busted version.`);
  }

  // 2. Remove older styled headers: <!-- TOP BAR NAVIGATION --> ... site-topbar
  // Let's use a very robust regex to match the site-topbar block
  const topbarRegex = /<!-- TOP BAR NAVIGATION -->[\s\S]*?<\/div>\s*<\/div>/g;
  if (topbarRegex.test(content)) {
    content = content.replace(topbarRegex, '<!-- UNIFIED HEADER -->\n<script src="/global-header.js?v=20260627_v4" defer></script>');
    modified = true;
    console.log(`[${file}] Replaced older site-topbar navigation block.`);
  } else {
    // If no comment, check for raw <div class="site-topbar">
    const rawTopbarRegex = /<div class="site-topbar">[\s\S]*?<\/div>\s*<\/div>/g;
    if (rawTopbarRegex.test(content)) {
      content = content.replace(rawTopbarRegex, '<!-- UNIFIED HEADER -->\n<script src="/global-header.js?v=20260627_v4" defer></script>');
      modified = true;
      console.log(`[${file}] Replaced raw site-topbar block.`);
    }
  }

  // 3. Remove newer glassmorphic headers: <!-- GLASSMORPHIC HEADER --> ... </header>
  const glassmorphicRegex = /<!-- GLASSMORPHIC HEADER -->[\s\S]*?<\/header>/g;
  if (glassmorphicRegex.test(content)) {
    content = content.replace(glassmorphicRegex, '<!-- UNIFIED HEADER -->\n<script src="/global-header.js?v=20260627_v4" defer></script>');
    modified = true;
    console.log(`[${file}] Replaced newer glassmorphic header block.`);
  } else {
    // Check for raw <header ...> ... </header>
    const rawHeaderRegex = /<header[^>]*>[\s\S]*?<\/header>/g;
    if (rawHeaderRegex.test(content)) {
      content = content.replace(rawHeaderRegex, '<!-- UNIFIED HEADER -->\n<script src="/global-header.js?v=20260627_v4" defer></script>');
      modified = true;
      console.log(`[${file}] Replaced raw header block.`);
    }
  }

  // If the file was not modified because none of the headers matched, let's inject it at the beginning of body
  if (!modified && !content.includes('global-header.js')) {
    if (content.includes('<body>')) {
      content = content.replace('<body>', '<body>\n<!-- UNIFIED HEADER -->\n<script src="/global-header.js?v=20260627_v4" defer></script>');
      modified = true;
      console.log(`[${file}] Injected script right after <body>.`);
    } else if (content.includes('<body')) {
      // Handle <body class="...">
      content = content.replace(/<body([^>]*)>/, '<body$1>\n<!-- UNIFIED HEADER -->\n<script src="/global-header.js?v=20260627_v4" defer></script>');
      modified = true;
      console.log(`[${file}] Injected script right after matched <body>.`);
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`[${file}] Successfully updated file.`);
  } else {
    console.log(`[${file}] No changes needed.`);
  }
});

console.log("All files processed!");
