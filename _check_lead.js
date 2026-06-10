const fs = require('fs');
const files = ['MEMORY.md', 'memory/2026-06-09.md', 'memory/2026-06-10.md'];
files.forEach(f => {
  try {
    const c = fs.readFileSync(f, 'utf8');
    const idx = c.indexOf('Email Lead Magnet');
    if (idx !== -1) {
      console.log('File:', f, 'idx:', idx, ':', c.slice(idx, idx + 500));
    } else {
      console.log('Not found in:', f);
    }
  } catch (e) {
    console.log('Not found:', f);
  }
});

// Also check for email list related terms
const terms = ['email list', '信箱名單', 'RESEND_API', 'lead list', 'email名單', '名單'];
files.forEach(f => {
  try {
    const c = fs.readFileSync(f, 'utf8');
    terms.forEach(term => {
      const idx = c.indexOf(term);
      if (idx !== -1) {
        console.log('Found "' + term + '" in', f, 'at', idx, ':', c.slice(Math.max(0, idx-50), idx + 200));
      }
    });
  } catch (e) {}
});
