const fs = require('fs');
const terms = ['formspree', 'Formspree', 'FORM_ID', 'form-id', 'lead-email', 'leadSent'];
const files = ['MEMORY.md', 'memory/2026-06-09.md', 'memory/2026-06-10.md'];
files.forEach(f => {
  try {
    const c = fs.readFileSync(f, 'utf8');
    terms.forEach(term => {
      const idx = c.indexOf(term);
      if (idx !== -1) {
        console.log('Found "' + term + '" in', f, 'at', idx);
        console.log(c.slice(Math.max(0, idx-100), idx + 300));
        console.log('---');
      }
    });
  } catch (e) {}
});

// Search HTML files for formspree
const htmlFiles = fs.readdirSync('.').filter(f => f.endsWith('.html'));
htmlFiles.forEach(f => {
  const c = fs.readFileSync(f, 'utf8');
  if (c.includes('formspree') || c.includes('FORM_ID') || c.includes('form-id')) {
    console.log('Formspree in:', f);
    const idx = c.indexOf('formspree');
    console.log(c.slice(Math.max(0, idx-50), idx + 200));
    console.log('---');
  }
});
