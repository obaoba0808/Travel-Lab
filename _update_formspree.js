const fs = require('fs');

// Map page -> resource name for formspree
const RESOURCE_MAP = {
  'tokyo-5days.html': 'tokyo-5days',
  'kansai-pass.html': 'kansai-pass',
  'hokkaido-winter.html': 'hokkaido-winter',
  'okinawa.html': 'okinawa',
  'kyoto-temples.html': 'kyoto-temples',
  'osaka-food.html': 'osaka-food',
  'osaka-usj.html': 'osaka-usj',
  'japan-budget-guide.html': 'japan-budget-guide',
  'seoul-food.html': 'seoul-food',
  'busan-capsule.html': 'busan-capsule',
  'jeju-island.html': 'jeju-island',
  'korea-budget.html': 'korea-budget',
  'hualien-taitung.html': 'hualien-taitung',
  'tainan-food.html': 'tainan-food',
  'kenting.html': 'kenting',
  'taipei-food.html': 'taipei-food',
  'jiufen.html': 'jiufen',
  'chiang-mai.html': 'chiang-mai',
  'bangkok-3days.html': 'bangkok-3days',
  'bangkok-massage.html': 'bangkok-massage',
  'vietnam-danang.html': 'vietnam-danang',
};

const FORMSPREE_ID = 'xredjjgb';

const PDF_FORM_HTML = (resource) => `
<!-- PDF Lead Magnet -->
<div style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:16px;padding:40px 24px;margin:48px 0;text-align:center;color:#fff">
  <div style="font-size:40px;margin-bottom:12px">🗺️</div>
  <h2 style="font-size:24px;margin:0 0 8px;color:#fff">小編獨家攻略 價值$299</h2>
  <p style="margin:0 0 24px;opacity:0.9;font-size:16px">填Email免費領取完整攻略 PDF，出发前印出来对照更方便</p>
  <form action="https://formspree.io/f/${FORMSPREE_ID}" method="POST" style="display:flex;flex-direction:column;align-items:center;gap:10px;max-width:360px;margin:0 auto">
    <input type="email" name="email" placeholder="輸入你的 Email" required style="width:100%;padding:14px 20px;border:none;border-radius:50px;font-size:15px;box-sizing:border-box">
    <input type="hidden" name="resource" value="${resource}">
    <button type="submit" style="background:#fff;color:#764ba2;padding:14px 40px;border:none;border-radius:50px;font-size:16px;font-weight:700;cursor:pointer;width:100%">免費領取攻略 PDF</button>
  </form>
  <p style="font-size:13px;margin:12px 0 0;opacity:0.7">🔒 不會垃圾郵件，隨時可取消訂閱</p>
</div>
`;

let fixed = 0;
let skipped = 0;

Object.entries(RESOURCE_MAP).forEach(([file, resource]) => {
  try {
    let content = fs.readFileSync(file, 'utf8');

    // Skip if already has formspree
    if (content.includes('formspree.io/f/' + FORMSPREE_ID)) {
      skipped++;
      console.log('Skip (already has formspree):', file);
      return;
    }

    // Insert before </footer> (at end of page content, before site footer)
    const footerIdx = content.lastIndexOf('</footer>');
    if (footerIdx === -1) {
      console.log('No footer found:', file);
      return;
    }

    // Insert the PDF form
    const formHtml = PDF_FORM_HTML(resource);
    content = content.slice(0, footerIdx) + formHtml + content.slice(footerIdx);

    fs.writeFileSync(file, content, 'utf8');
    fixed++;
    console.log('Updated:', file, '-> resource:', resource);
  } catch (e) {
    console.log('Error:', file, e.message);
  }
});

console.log('\nDone: ' + fixed + ' files updated, ' + skipped + ' skipped (already had formspree)');
