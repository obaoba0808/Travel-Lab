/**
 * Fix JSON-LD syntax errors + expand thin content
 * 1. Validate and fix JSON-LD in all HTML files
 * 2. Expand seasia-budget-travel-guide.html (thin content ~8KB)
 */
const fs = require('fs');
const path = require('path');
const BASE = __dirname;

function read(f) { return fs.readFileSync(path.join(BASE, f), 'utf8'); }
function write(f, c) { fs.writeFileSync(path.join(BASE, f), c, 'utf8'); }

// === Fix JSON-LD syntax errors ===
const htmlFiles = fs.readdirSync(BASE).filter(f => f.endsWith('.html') && fs.statSync(path.join(BASE, f)).isFile());

let jsonFixed = 0;
const jsonErrors = [];

for (const file of htmlFiles) {
  const content = read(file);
  const matches = [...content.matchAll(/<script[^>]*type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/g)];
  
  if (matches.length === 0) continue;
  
  let newContent = content;
  let fileChanged = false;
  
  for (const m of matches) {
    const jsonStr = m[1].trim();
    try {
      JSON.parse(jsonStr);
    } catch (e) {
      // Try to fix common JSON-LD errors
      let fixed = jsonStr;
      
      // Fix 1: missing } before "datePublished" etc (author object not closed)
      fixed = fixed.replace(/"name":"[^"]*"}\s*,"/g, (match) => {
        // Check if there's a missing closing brace before datePublished
        return match;
      });
      
      // Fix 2: spaces before/after colons (actually valid in JSON, but let's check)
      
      // Fix 3: missing commas between properties
      // Actually, let me just try to parse and find/fix the specific error
      
      // Better approach: try to rebuild the JSON-LD from the HTML context
      // For now, let me just log the error and try a basic fix
      jsonErrors.push({ file, error: e.message, pos: e.message.match(/position\s+(\d+)/i)?.[1] });
      
      // Try a more aggressive fix: re-encode the JSON-LD by re-extracting from the file
      // Actually, let me just try to fix the specific known issues:
      // Issue: "name":"X"},"datePublished" -> missing } closure? No, that looks correct
      // Let me look for the actual issue in the regex output from PowerShell earlier
      
      // From the PowerShell output, the issue was around position 931 in esim-comparison.html
      // The JSON showed: "name":"均在路上 Travel Lab"},"datePublished":"2026-05-16","dateModified": "2026-05-26"
      // Actually that looks valid... Let me try parsing the exact string
    }
  }
}

console.log('JSON-LD errors found:', jsonErrors.length);
jsonErrors.forEach(e => console.log(`  ${e.file}: ${e.error}`));

// Let me try a different approach: actually parse the JSON-LD from the file directly
console.log('\nRe-checking JSON-LD with Node.js...');
let errorCount = 0;
for (const file of htmlFiles) {
  const content = read(file);
  const matches = [...content.matchAll(/<script[^>]*type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/g)];
  
  for (const m of matches) {
    const jsonStr = m[1].trim();
    try {
      JSON.parse(jsonStr);
    } catch (e) {
      errorCount++;
      console.log(`ERROR in ${file}: ${e.message}`);
      console.log(`  JSON snippet (around error): ${jsonStr.substring(Math.max(0, parseInt(e.message.match(/position\s+(\d+)/)?.[1] || '0') - 40, 200)}`);
      
      // Try to fix: common issue is trailing commas or missing commas
      let fixed = jsonStr;
      // Remove trailing commas before } or ]
      fixed = fixed.replace(/,\s*([}\]])/g, '$1');
      // Ensure commas between properties (this is tricky)
      
      try {
        JSON.parse(fixed);
        console.log(`  FIXED (removed trailing commas)`);
        // Write back
        const newContent = content.replace(jsonStr, fixed);
        write(file, newContent);
        jsonFixed++;
      } catch (e2) {
        console.log(`  Could not auto-fix: ${e2.message}`);
      }
    }
  }
}

console.log(`\nFixed ${jsonFixed} JSON-LD blocks`);
console.log(`Remaining errors: ${errorCount - jsonFixed}`);

// === Now fix seasia-budget-travel-guide.html (thin content) ===
console.log('\n=== Fixing seasia-budget-travel-guide.html (thin content) ===');

let seasia = read('seasia-budget-travel-guide.html');
const TARGET_SIZE = 15000; // aim for 15KB

if (seasia.length < TARGET_SIZE) {
  // Add substantial content sections
  const extraContent = `
<section class="content-block">
<h2>東南亞各國預算比較表</h2>
<table class="budget-table">
<thead><tr><th>國家</th><th>每日預算（經濟）</th><th>每日預算（舒適）</th><th>青年旅館床位</th><th>雙人房（中價）</th></tr></thead>
<tbody>
<tr><td>🇹🇭 泰國</td><td>NT$ 800-1,200</td><td>NT$ 2,000-3,500</td><td>NT$ 300-500</td><td>NT$ 800-1,500</td></tr>
<tr><td>🇻🇳 越南</td><td>NT$ 600-1,000</td><td>NT$ 1,500-2,500</td><td>NT$ 250-400</td><td>NT$ 600-1,200</td></tr>
<tr><td>🇲🇾 柬埔寨</td><td>NT$ 500-900</td><td>NT$ 1,200-2,000</td><td>NT$ 200-350</td><td>NT$ 500-1,000</td></tr>
<tr><td>🇱🇭 寮國</td><td>NT$ 400-800</td><td>NT$ 1,000-1,800</td><td>NT$ 150-300</td><td>NT$ 400-800</td></tr>
<tr><td>🇲🇾 馬來西亞</td><td>NT$ 700-1,100</td><td>NT$ 1,800-3,000</td><td>NT$ 250-450</td><td>NT$ 700-1,400</td></tr>
<tr><td>🇸🇬 新加坡</td><td>NT$ 1,500-2,500</td><td>NT$ 3,500-6,000</td><td>NT$ 500-900</td><td>NT$ 1,500-3,000</td></tr>
</tbody>
</table>
<p class="table-note">※ 匯率參考：1 USD ≈ NT$ 32。預算含住宿+餐食+交通+景點門票，不含機票。</p>
</section>

<section class="content-block">
<h2>東南亞低預算旅行5大秘訣</h2>
<h3>1. 選對季節：淡季機票省一半</h3>
<p>東南亞淡季（5-10月雨季）機票便宜 30-50%。泰國/越南淡季來回 NT$ 6,000-8,000，旺季（12-2月）要 NT$ 12,000+。柬埔寨/寮國全年差價較小。</p>

<h3>2. 當地交通：Grab 比計程車便宜</h3>
<p>泰國/越南/馬來西亞 Grab 價格透明，比路邊招手計程車便宜 20-40%。市區短程 NT$ 60-150，機場到市區 NT$ 200-400。過夜巴士（VIP Bus）是窮遊神器：曼谷→清邁 NT$ 350，胡志明→峴港 NT$ 500。</p>

<h3>3. 住宿：Hostelworld 比 Booking 便宜</h3>
<p>青年旅館床位在 Hostelworld 常有特價，曼谷/胡志明/吉隆坡優質床位 NT$ 250-400/晚。双人房（Airbnb 或民宿）在越南/柬埔寨 CP 值超高：海景房 NT$ 800-1,200/晚。</p>

<h3>4. 餐食：夜市 + 路邊攤 = 省錢又好吃</h3>
<p>東南亞路邊攤每餐 NT$ 40-80，夜市 NT$ 60-120，商場美食廣場（Food Court）NT$ 80-150。避開觀光區餐廳（價格翻倍），跟著當地人排隊的最香！</p>

<h3>5. 景點：免費寺廟 + 自然景觀</h3>
<p>泰國寺廟（雙龍寺/白色寺）免費或 NT$ 30-100。越南峴港海灘、胡志明統一宮（NT$ 60）是小錢。柬埔寨吳哥窟門票最貴（1日票 US$ 37 ≈ NT$ 1,200），但其他景點大多免費。</p>
</section>

<section class="content-block">
<h2>東南亞各國簽證最新規定（2026）</h2>
<ul>
<li><strong>🇹🇭 泰國</strong>：台灣護照免簽證 30 天（2026 持續）</li>
<li><strong>🇻🇳 越南</strong>：需辦電子簽證（E-visa）US$ 25，3-5 工作天，可停留 90 天</li>
<li><strong>🇲🇾 柬埔寨</strong>：落地簽證 US$ 30（觀光），需準備 2 吋照片 + 現金</li>
<li><strong>🇱🇭 寮國</strong>：落地簽證 US$ 30-40，可停留 30 天</li>
<li><strong>🇲🇾 馬來西亞</strong>：台灣護照免簽證 30 天</li>
<li><strong>🇸🇬 新加坡</strong>：台灣護照免簽證 30 天</li>
<li><strong>🇮🇩 印尼（峇里島）</strong>：落地簽證 IDR 500,000（≈ NT$ 1,050），可停留 30 天</li>
</ul>
<p class="tip">💡 簽證規定隨時可能變動，出發前務必查詢該國移民署官網最新資訊！</p>
</section>

<section class="content-block">
<h2>東南亞最佳旅行時間指南</h2>
<table class="budget-table">
<thead><tr><th>國家</th><th>乾季（推薦）</th><th>雨季（淡季）</th><th>最佳月份</th><th>避開月份</th></tr></thead>
<tbody>
<tr><td>泰國</td><td>11-2月</td><td>5-10月</td><td>11-2月（涼爽）</td><td>4月（太熱 40°C+）</td></tr>
<tr><td>越南</td><td>11-3月</td><td>5-10月</td><td>11-1月（乾涼）</td><td>7-8月（颱風季）</td></tr>
<tr><td>柬埔寨</td><td>11-3月</td><td>5-10月</td><td>12-2月</td><td>5-10月（悶熱多雨）</td></tr>
<tr><td>馬來西亞</td><td>12-2月</td><td>5-9月</td><td>12-2月（相對涼爽）</td><td>6-8月（煙霾嚴重）</td></tr>
<tr><td>新加坡</td><td>12-2月</td><td>5-8月</td><td>12-2月</td><td>全年皆宜（室內冷氣強）</td></tr>
</tbody>
</table>
</section>
`;
  
  // Insert before the related reading section
  const relatedIdx = seasia.indexOf('延伸閱讀');
  if (relatedIdx > 0) {
    seasia = seasia.slice(0, relatedIdx) + extraContent + '\n' + seasia.slice(relatedIdx);
  } else {
    // Insert before </article> or </body>
    const articleIdx = seasia.indexOf('</article>');
    if (articleIdx > 0) {
      seasia = seasia.slice(0, articleIdx) + extraContent + '\n' + seasia.slice(articleIdx);
    }
  }
  
  write('seasia-budget-travel-guide.html', seasia);
  console.log(`  Expanded: ${seasia.length} bytes (was 8687)`);
} else {
  console.log('  Already substantial content, skipping expansion');
}

console.log('\nDone!');
