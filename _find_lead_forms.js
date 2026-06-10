const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
const terms = ['submitLeadForm', 'leadEmail', 'WORKER_URL', 'leadSent', 'leadMsg', 'leadSubmitBtn'];

terms.forEach(term => {
  const matches = files.filter(f => {
    try { return fs.readFileSync(f, 'utf8').includes(term); }
    catch (e) { return false; }
  });
  if (matches.length > 0) {
    console.log('Term:"' + term + '" in: ' + matches.join(', '));
  }
});

// Also find files with the PDF lead magnet form structure
files.forEach(f => {
  try {
    const c = fs.readFileSync(f, 'utf8');
    if (c.includes('golightly-email') || c.includes('pdf-form')) {
      console.log('Has golightly-email or pdf-form:', f);
    }
  } catch (e) {}
});
