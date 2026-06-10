const fs = require('fs');

const FORMSPREE_ID = 'xredjjgb';
const files = ['esim-comparison.html', 'taiwan-travel.html'];

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  const original = content;

  // Remove lead-inline CSS block
  content = content.replace(/<style>\s*\.lead-inline[\s\S]*?<\/style>\n?/g, '');

  // New formspree form HTML
  const newForm = `<form action="https://formspree.io/f/${FORMSPREE_ID}" method="POST" style="display:flex;flex-direction:column;align-items:center;gap:10px;max-width:360px;margin:0 auto;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border-radius:16px;padding:32px 24px">
  <p style="color:#fff;font-size:15px;margin:0 0 4px">🗺️ 小編獨家攻略 價值$299，限時免費送</p>
  <input type="email" name="email" placeholder="輸入你的 Email" required style="width:100%;padding:12px 18px;border:none;border-radius:50px;font-size:14px;box-sizing:border-box">
  <input type="hidden" name="resource" value="${file.replace('.html', '')}">
  <button type="submit" style="background:#fff;color:#764ba2;padding:12px 36px;border:none;border-radius:50px;font-size:15px;font-weight:700;cursor:pointer;width:100%">免費領取攻略 PDF</button>
  <p style="font-size:12px;color:rgba(255,255,255,0.7);margin:8px 0 0">🔒 不會垃圾郵件，隨時可取消訂閱</p>
</form>`;

  // Remove old form + leadMsg + lead-note block
  const oldPattern = /<form onsubmit="submitLeadForm\(event\);return false">[\s\S]*?<\/form>\s*<div id="leadMsg"[\s\S]*?<\/div>\s*<p class="lead-note"[\s\S]*?<\/p>\s*/;
  content = content.replace(oldPattern, newForm);

  // Also remove any remaining worker URL/script refs
  content = content.replace(/\/\* PDF download URL per page \*\/[\s\S]*?getResourceKey\(\)[\s\S]*?<\/script>/, '');

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    console.log('Fixed:', file);
  } else {
    console.log('No change:', file);
  }
});
