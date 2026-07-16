import fs from 'fs';
import path from 'path';

const rootDir = process.cwd();
const files = fs.readdirSync(rootDir).filter(file => file.endsWith('.html'));

console.log(`Analyzing ${files.length} HTML files...`);

files.forEach(file => {
  const filePath = path.join(rootDir, file);
  const content = fs.readFileSync(filePath, 'utf-8');

  // Let's search for a top-level section that looks like a hero
  // It usually starts with <section ... and contains <h1 or has classes like relative, hero, or bg-
  // Let's find sections in the first 300 lines
  const lines = content.split('\n').slice(0, 300).join('\n');
  const sectionMatch = lines.match(/<section[^>]*?id="hero[^>]*?>([\s\S]*?)<\/section>|<section[^>]*?class="[^"]*?(?:relative bg-|hero-region)[^>]*?>([\s\S]*?)<\/section>/i);

  if (sectionMatch) {
    const fullSection = sectionMatch[0];
    const sectionBody = sectionMatch[1] || sectionMatch[2];
    
    // Extract H1
    const h1Match = fullSection.match(/<h1[^>]*?>([\s\S]*?)<\/h1>/i);
    const h1 = h1Match ? h1Match[1].replace(/<[^>]*>/g, '').trim() : 'N/A';

    // Extract image src
    const imgMatch = fullSection.match(/<img[^>]*?src=["']([^"']+)["']/i) || fullSection.match(/background-image:\s*url\(['"]?([^'")]+)['"]?\)/i);
    const imgSrc = imgMatch ? imgMatch[1] : 'N/A';

    console.log(`[${file}]: FOUND Hero Section`);
    console.log(`  H1: "${h1}"`);
    console.log(`  Img: "${imgSrc}"`);
  } else {
    // Check if it's a standard simple page like fukuoka-5days.html or esim-comparison.html
    const h1Match = lines.match(/<h1[^>]*?>([\s\S]*?)<\/h1>/i);
    if (h1Match) {
      const h1 = h1Match[1].replace(/<[^>]*>/g, '').trim();
      console.log(`[${file}]: Standard H1 only: "${h1}"`);
    } else {
      console.log(`[${file}]: No H1 or Hero found in first 300 lines.`);
    }
  }
});
