const fs = require('fs');

const files = [
  'bangkok-3days.html', 'bangkok-massage.html', 'busan-capsule.html', 'chiang-mai.html',
  'hokkaido-winter.html', 'hualien-taitung.html', 'jeju-island.html', 'jiufen.html',
  'kansai-pass.html', 'kenting.html', 'korea-budget.html', 'kyoto-temples.html',
  'okinawa.html', 'osaka-food.html', 'osaka-usj.html', 'seoul-food.html',
  'tainan-food.html', 'taipei-food.html', 'tokyo-5days.html', 'vietnam-danang.html'
];

let fixed = 0;
files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  const original = content;

  // Fix: <p>&gt;\n<meta -> <p><meta (with any whitespace)
  content = content.replace(/<p>&gt;\s*<meta/g, '<p><meta');
  // Also fix standalone <p>&gt;</p>
  content = content.replace(/<p>&gt;<\/p>/g, '');

  if (content !== original) {
    fs.writeFileSync(file, content, 'utf8');
    fixed++;
    console.log('Fixed:', file);
  }
});

console.log('Total fixed:', fixed);