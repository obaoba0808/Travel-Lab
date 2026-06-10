const fs = require('fs');
const files = ['esim-comparison.html', 'taiwan-travel.html'];
files.forEach(f => {
  const c = fs.readFileSync(f, 'utf8');
  console.log('=== ' + f + ' ===');
  console.log('size:', c.length);
  // Find all occurrences
  ['submitLeadForm', 'leadEmail', 'leadMsg', 'WORKER_URL', 'leadSent'].forEach(t => {
    const idx = c.indexOf(t);
    if (idx !== -1) console.log(t, 'at', idx, ':', c.slice(Math.max(0,idx-30), idx+100));
  });
});
