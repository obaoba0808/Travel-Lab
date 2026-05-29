// Cloudflare Worker - Email Auto-Reply for golightly.fun
// 接收網站表單 → 自動寄送 PDF 下載連結到用戶信箱

const PDF_LINKS = {
 'tokyo-metro-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/tokyo-metro-map.pdf',
 'kansai-pass-calculator':'https://obaoba0808.github.io/Travel-Lab/downloads/kansai-pass-calculator.pdf',
 'hokkaido-packing-list': 'https://obaoba0808.github.io/Travel-Lab/downloads/hokkaido-packing-list.pdf',
 'okinawa-driving-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/okinawa-driving-map.pdf',
 'kyoto-momiji-schedule': 'https://obaoba0808.github.io/Travel-Lab/downloads/kyoto-momiji-schedule.pdf',
 'osaka-food-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/osaka-food-map.pdf',
 'usj-quick-pass': 'https://obaoba0808.github.io/Travel-Lab/downloads/usj-quick-pass.pdf',
 'japan-budget-sheet': 'https://obaoba0808.github.io/Travel-Lab/downloads/japan-budget-sheet.pdf',
 'seoul-food-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/seoul-food-map.pdf',
 'busan-capsule-guide': 'https://obaoba0808.github.io/Travel-Lab/downloads/busan-capsule-guide.pdf',
 'jeju-driving-route': 'https://obaoba0808.github.io/Travel-Lab/downloads/jeju-driving-route.pdf',
 'korea-budget-sheet': 'https://obaoba0808.github.io/Travel-Lab/downloads/korea-budget-sheet.pdf',
 'hualien-itinerary': 'https://obaoba0808.github.io/Travel-Lab/downloads/hualien-itinerary.pdf',
 'tainan-food-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/tainan-food-map.pdf',
 'kenting-night-market': 'https://obaoba0808.github.io/Travel-Lab/downloads/kenting-night-market.pdf',
 'taipei-food-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/taipei-food-map.pdf',
 'jiufen-guide': 'https://obaoba0808.github.io/Travel-Lab/downloads/jiufen-guide.pdf',
 'chiang-mai-guide': 'https://obaoba0808.github.io/Travel-Lab/downloads/chiang-mai-guide.pdf',
 'bangkok-food-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/bangkok-food-map.pdf',
 'bangkok-massage-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/bangkok-massage-map.pdf',
 'danang-map': 'https://obaoba0808.github.io/Travel-Lab/downloads/danang-map.pdf',
};

const PAGE_TITLES = {
 'tokyo-metro-map': '東京5天地鐵攻略',
 'kansai-pass-calculator':'關西票券省錢秘籍',
 'hokkaido-packing-list': '北海道冬季穿搭攻略',
 'okinawa-driving-map': '沖繩自駕必備地圖',
 'kyoto-momiji-schedule': '京都賞楓時間表2026',
 'osaka-food-map': '大阪美食地圖',
 'usj-quick-pass': 'USJ快速通關攻略',
 'japan-budget-sheet': '日本7天預算表',
 'seoul-food-map': '首爾美食地圖',
 'busan-capsule-guide': '釜山膠囊列車預約攻略',
 'jeju-driving-route': '濟州島自駕路線圖',
 'korea-budget-sheet': '韓國5天預算表',
 'hualien-itinerary': '花東三天行程表',
 'tainan-food-map': '台南牛肉湯地圖',
 'kenting-night-market': '墾丁夜市美食清單',
 'taipei-food-map': '台北美食地圖',
 'jiufen-guide': '九份老街攻略',
 'chiang-mai-guide': '清邁數位遊牧指南',
 'bangkok-food-map': '曼谷美食地圖',
 'bangkok-massage-map': '曼谷按摩地圖',
 'danang-map': '峴港景點地圖',
};

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': '*'
};

function jsonResp(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...CORS, 'Content-Type': 'application/json' }
  });
}

addEventListener('fetch', event => {
 event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
 // Handle CORS preflight
 if (request.method === 'OPTIONS') {
   return new Response(null, { headers: CORS });
 }

 // Support GET (URL params) and POST (JSON body)
 let email, resource;

 if (request.method === 'POST') {
   try {
     const body = await request.json();
     email = body.email;
     resource = body.resource || body.pdfUrl;
   } catch (e) {
     return jsonResp({error: 'Invalid JSON'}, 400);
   }
 } else {
   const url = new URL(request.url);
   email = url.searchParams.get('email');
   resource = url.searchParams.get('resource') || url.searchParams.get('pdfUrl');
 }

 if (!email || !email.includes('@')) {
   return jsonResp({error: 'Invalid email'}, 400);
 }

 const pdfLink = PDF_LINKS[resource] || 'https://golightly.fun/downloads/travel-guide-pack.pdf';
 const title = PAGE_TITLES[resource] || '旅遊攻略工具包';

 const htmlBody = `
<div style="font-family:'Noto Sans TC',sans-serif;max-width:600px;margin:0 auto;padding:20px">
<div style="background:#0ABAB5;color:white;border-radius:12px 12px 0 0;padding:24px;text-align:center">
<h1 style="margin:0;font-size:22px">✈️ 感謝訂閱均在路上！</h1>
</div>
<div style="border:1px solid #eee;border-top:none;border-radius:0 0 12px 12px;padding:24px;background:#fff">
<p style="font-size:16px;color:#333;line-height:1.8">你好！👋<br>感謝你訂閱 <strong>均在路上</strong> 的旅遊攻略！<br><br>以下是你要的免費資源：</p>
<div style="background:#f0fafa;border-left:4px solid #0ABAB5;padding:16px 20px;border-radius:0 8px 8px 0;margin:20px 0">
<h3 style="color:#0ABAB5;margin:0 0 8px">📥 ${title}</h3>
<a href="${pdfLink}" style="color:#0ABAB5;font-size:14px">點擊下載 PDF</a>
</div>
<p style="font-size:14px;color:#888;line-height:1.8">💡 小提醒：我們未來會不定時寄送最新旅遊攻略給你，隨時可退訂。<br><br>期待與你一起探索世界 🌏<br>— 均在路上 小編</p>
</div>
</div>`;

 const resendKey = RESEND_API_KEY || 're_EHikPqyc_Fe4PASKP8t9Nvtveg1z7DxUx';

 const res = await fetch('https://api.resend.com/emails', {
   method: 'POST',
   headers: {
     'Authorization': `Bearer ${resendKey}`,
     'Content-Type': 'application/json'
   },
   body: JSON.stringify({
     from: '均在路上 <noreply@golightly.fun>',
     to: email,
     subject: `📬 你的「${title}」已備好！均在路上免費送`,
     html: htmlBody
   })
 });

 const result = await res.json();

 if (!res.ok) {
   return jsonResp({error: 'Resend API error', detail: result}, 500);
 }

 return jsonResp({ok: true, result});
}
