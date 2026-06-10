const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
const terms = ['299', '獨家攻略', '索取', 'PDF下載', 'submitLeadForm', 'leadEmail'];
terms.forEach(t => {
  const matches = files.filter(f => fs.readFileSync(f, 'utf8').includes(t));
  if (matches.length > 0) {
    console.log('Term:"' + t + '" in: ' + matches.join(', '));
  }
});
