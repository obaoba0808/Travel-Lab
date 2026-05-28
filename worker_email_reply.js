// Cloudflare Worker - Email Auto-Reply for golightly.fun
// 接收網站表單 → 自動寄送 PDF 下載連結到用戶信箱

const PDF_LINKS = {
 'tokyo-metro-map': 'https://golightly.fun/downloads/tokyo-metro-map.pdf',
 'kansai-pass-calculator':'https://golightly.fun/downloads/kansai-pass-calculator.pdf',
 'hokkaido-packing-list': 'https://golightly.fun/downloads/hokkaido-packing-list.pdf',
 'okinawa-driving-map': 'https://golightly.fun/downloads/okinawa-driving-map.pdf',
 'kyoto-momiji-schedule': 'https://golightly.fun/downloads/kyoto-momiji-schedule.pdf',
 'osaka-food-map': 'https://golightly.fun/downloads/osaka-food-map.pdf',
 'usj-quick-pass': 'https://golightly.fun/downloads/usj-quick-pass.pdf',
 'japan-budget-sheet': 'https://golightly.fun/downloads/japan-budget-sheet.pdf',
 'seoul-food-map': 'https://golightly.fun/downloads/seoul-food-map.pdf',
 'busan-capsule-guide': 'https://golightly.fun/downloads/busan-capsule-guide.pdf',
 'jeju-driving-route': 'https://golightly.fun/downloads/jeju-driving-route.pdf',
 'korea-budget-sheet': 'https://golightly.fun/downloads/korea-budget-sheet.pdf',
 'hualien-itinerary': 'https://golightly.fun/downloads/hualien-itinerary.pdf',
 'tainan-food-map': 'https://golightly.fun/downloads/tainan-food-map.pdf',
 'kenting-night-market': 'https://golightly.fun/downloads/kenting-night-market.pdf',
 'taipei-food-map': 'https://golightly.fun/downloads/taipei-food-map.pdf',
 'jiufen-guide': 'https://golightly.fun/downloads/jiufen-guide.pdf',
 'chiang-mai-guide': 'https://golightly.fun/downloads/chiang-mai-guide.pdf',
 'bangkok-food-map': 'https://golightly.fun/downloads/bangkok-food-map.pdf',
 'bangkok-massage-map': 'https://golightly.fun/downloads/bangkok-massage-map.pdf',
 'danang-map': 'https://golightly.fun/downloads/danang-map.pdf',
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

addEventListener('fetch', event => {
 event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
 // 支援 GET（URL參數）和 POST（JSON body）兩種方式
 let email, resource;

 if (request.method === 'POST') {
   try {
     const body = await request.json();
     email = body.email;
     resource = body.resource || body.pdfUrl;
   } catch (e) {
     return new Response(JSON.stringify({error: 'Invalid JSON'}), {
       status: 400,
       headers: {'Content-Type': 'application/json'}
     });
   }
 } else {
   const url = new URL(request.url);
   email = url.searchParams.get('email');
   resource = url.searchParams.get('resource') || url.searchParams.get('pdfUrl');
 }

 if (!email || !email.includes('@')) {
   return new Response(JSON.stringify({error: 'Invalid email'}), {
     status: 400,
     headers: {'Content-Type': 'application/json'}
   });
 }

 const pdfLink = PDF_LINKS[resource] || 'https://golightly.fun/downloads/旅遊攻略工具包.pdf';
 const title = PAGE_TITLES[resource] || '旅遊攻略工具包';

 const htmlBody = `
 <div style="font-family: 'Noto Sans TC', sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
 <div style="background: #0ABAB5; color: white; border-radius: 12px 12px 0 0; padding: 24px; text-align: center;">
 <h1 style="margin: 0; font-size: 22px;">✈️ 感謝訂閱均在路上！</h1>
 </div>
 <div style="border: 1px solid #eee; border-top: none; border-radius: 0 0 12px 12px; padding: 24px; background: white;">
 <p style="font-size: 16px; color: #333; line-height: 1.8;">
 你好！👋<br>
 感謝你訂閱 <strong>均在路上</strong> 的旅遊攻略！<br><br>
 以下是你要的免費資源：
 </p>
 <div style="background: #f0fafa; border-left: 4px solid #0ABAB5; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 20px 0;">
 <h3 style="color: #0ABAB5; margin: 0 0 8px;">📥 ${title}</h3>
 <a href="${pdfLink}" style="color: #0ABAB5; font-size: 14px;">點擊下載 PDF</a>
 </div>
 <p style="font-size: 14px; color: #888; line-height: 1.8;">
 💡 小提醒：我們未來會不定時寄送最新旅遊攻略給你，隨時可退訂。<br><br>
 期待與你一起探索世界 🌏<br>
 — 均在路上 小編
 </p>
 </div>
 </div>
 `;

 const resendKey = RESEND_API_KEY || 're_VB5NPTVx_2FB2g9v6H8qfDWTZouVZKdF3';

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
   return new Response(JSON.stringify({error: 'Resend API error', detail: result}), {
     status: 500,
     headers: {'Content-Type': 'application/json'}
   });
 }

 return new Response(JSON.stringify({ok: true, result}), {
   headers: {'Content-Type': 'application/json'}
 });
}
