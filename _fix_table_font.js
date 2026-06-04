const fs = require('fs');
const files = ['gen_korea_all.py', 'gen_taiwan_all.py', 'gen_sea_all.py'];
const old = "        ('FONTNAME', (0,0), (-1,0), 'MSJHB'),\n        ('FONTSIZE', (0,0), (-1,0), 11),\n        ('ALIGN', (0,0), (-1,-1), 'LEFT'),";
const nnew = "        ('FONTNAME', (0,0), (-1,0), 'MSJHB'),\n        ('FONTSIZE', (0,0), (-1,0), 11),\n        ('FONTNAME', (0,1), (-1,-1), 'MSJH'),\n        ('FONTSIZE', (0,1), (-1,-1), 10),\n        ('ALIGN', (0,0), (-1,-1), 'LEFT'),";
files.forEach(f => {
  let c = fs.readFileSync(f, 'utf8');
  if (c.includes(old)) {
    c = c.replace(old, nnew);
    fs.writeFileSync(f, c, 'utf8');
    console.log('Fixed: ' + f);
  } else {
    console.log('Not found in: ' + f);
  }
});
