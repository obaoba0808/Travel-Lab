# Google Apps Script — Email Auto-Reply for golightly.fun Lead Magnet

## 步驟 1：建立 Google Apps Script

1. 前往 https://script.google.com 並用你的 Google 帳號登入
2. 點左上角「+ 新增指令碼」
3. 刪除預設程式碼，複製下面整段程式碼貼進去

```javascript
// ============================================================
// 均在路上 (golightly.fun) — 自動回覆程式碼
// ============================================================

const PDF_LINKS = {
  'bangkok-food-map':       'https://golightly.fun/downloads/bangkok-food-map.pdf',
  'seoul-food-map':         'https://golightly.fun/downloads/seoul-food-map.pdf',
  'osaka-food-map':         'https://golightly.fun/downloads/osaka-food-map.pdf',
  'taipei-food-map':       'https://golightly.fun/downloads/taipei-food-map.pdf',
  'tainan-food-map':        'https://golightly.fun/downloads/tainan-food-map.pdf',
  'tokyo-metro-map':        'https://golightly.fun/downloads/tokyo-metro-map.pdf',
  'usj-quick-pass':         'https://golightly.fun/downloads/usj-quick-pass.pdf',
  'busan-capsule-guide':    'https://golightly.fun/downloads/busan-capsule-guide.pdf',
  'chiang-mai-guide':       'https://golightly.fun/downloads/chiang-mai-guide.pdf',
  'danang-map':             'https://golightly.fun/downloads/danang-map.pdf',
  'jeju-driving-route':     'https://golightly.fun/downloads/jeju-driving-route.pdf',
  'okinawa-driving-map':    'https://golightly.fun/downloads/okinawa-driving-map.pdf',
  'kyoto-momiji-schedule':  'https://golightly.fun/downloads/kyoto-momiji-schedule.pdf',
  'kansai-pass-calculator': 'https://golightly.fun/downloads/kansai-pass-calculator.pdf',
  'japan-budget-sheet':    'https://golightly.fun/downloads/japan-budget-sheet.pdf',
  'korea-budget-sheet':    'https://golightly.fun/downloads/korea-budget-sheet.pdf',
  'sea-budget-sheet':      'https://golutely.fun/downloads/sea-budget-sheet.pdf',
  'hokkaido-packing-list':  'https://golightly.fun/downloads/hokkaido-packing-list.pdf',
  'packing-checklist':      'https://golightly.fun/downloads/packing-checklist.pdf',
  'emergency-contact-card':'https://golightly.fun/downloads/emergency-contact-card.pdf',
  'jiufen-guide':           'https://golightly.fun/downloads/jiufen-guide.pdf',
  'kenting-night-market':   'https://golightly.fun/downloads/kenting-night-market.pdf',
  'hualien-itinerary':      'https://golightly.fun/downloads/hualien-itinerary.pdf',
  'bangkok-massage-map':    'https://golightly.fun/downloads/bangkok-massage-map.pdf',
  'taiwan-travel':          'https://golightly.fun/downloads/taipei-food-map.pdf',
  'esim-comparison':        'https://golightly.fun/downloads/packing-checklist.pdf',
  'packing-list':           'https://golightly.fun/downloads/packing-checklist.pdf',
};

const PAGE_TITLES = {
  'bangkok-food-map':       '曼谷美食地圖',
  'seoul-food-map':         '首爾美食地圖',
  'osaka-food-map':         '大阪美食地圖',
  'taipei-food-map':        '台北美食地圖',
  'tainan-food-map':        '台南美食地圖',
  'tokyo-metro-map':        '東京地鐵攻略',
  'usj-quick-pass':         '大阪環球影城攻略',
  'busan-capsule-guide':    '釜山膠囊住宿指南',
  'chiang-mai-guide':       '清邁遊牧攻略',
  'danang-map':             '越南峴港地圖',
  'jeju-driving-route':      '濟州島自駕路線',
  'okinawa-driving-map':    '沖繩自駕地圖',
  'kyoto-momiji-schedule':  '京都紅葉攻略',
  'kansai-pass-calculator': '關西周遊券計算機',
  'japan-budget-sheet':     '日本預算表',
  'korea-budget-sheet':     '韓國預算表',
  'sea-budget-sheet':       '東南亞預算表',
  'hokkaido-packing-list':   '北海道行李清單',
  'packing-checklist':      '出發前檢查清單',
  'emergency-contact-card': '緊急聯絡卡',
  'jiufen-guide':           '九份十分一日遊',
  'kenting-night-market':  '墾丁夜市攻略',
  'hualien-itinerary':      '花蓮三日遊',
  'bangkok-massage-map':    '曼谷按摩地圖',
  'taiwan-travel':          '台灣自由行攻略',
  'esim-comparison':        'eSIM比較攻略',
  'packing-list':           '行李清單',
};

function doPost(e) {
  const data = JSON.parse(e.postData.contents);
  const email = data.email;
  const resource = data.resource || 'bangkok-food-map';

  if (!email || !email.includes('@')) {
    return HtmlService.createHtmlOutput(JSON.stringify({error: 'Invalid email'}), 400)
      .setContent('{\"error\":\"Invalid email\"}');
  }

  const pdfLink = PDF_LINKS[resource] || PDF_LINKS['bangkok-food-map'];
  const title = PAGE_TITLES[resource] || '旅遊攻略工具包';

  const htmlBody = `
    <div style="font-family:'Noto Sans TC','Microsoft JhengHei',sans-serif;max-width:600px;margin:0 auto;padding:20px">
      <div style="background:linear-gradient(135deg,#0ABAB5,#764ba2);color:white;border-radius:16px 16px 0 0;padding:28px;text-align:center">
        <h1 style="margin:0;font-size:24px;font-weight:700">✈️ 感謝訂閱均在路上！</h1>
        <p style="margin:8px 0 0;font-size:14px;opacity:0.9">你的免費攻略已備好</p>
      </div>
      <div style="border:1px solid #e8ecf0;border-top:none;border-radius:0 0 16px 16px;padding:28px;background:#fff">
        <p style="font-size:16px;color:#333;line-height:1.8;margin:0 0 20px">
          你好！👋<br>
          感謝你訂閱 <strong>均在路上</strong> 的旅遊攻略內容 ❤️<br>
          以下是你專屬的免費資源：
        </p>
        <div style="background:linear-gradient(135deg,#f0fafa,#e8f8f8);border-left:4px solid #0ABAB5;padding:20px 24px;border-radius:0 12px 12px 0;margin:20px 0">
          <div style="font-size:40px;text-align:center;margin-bottom:12px">📥</div>
          <h3 style="color:#0ABAB5;margin:0 0 12px;font-size:18px">${title}</h3>
          <a href="${pdfLink}" style="display:inline-block;background:linear-gradient(135deg,#0ABAB5,#764ba2);color:#fff;padding:12px 32px;border-radius:50px;text-decoration:none;font-size:15px;font-weight:700">
            ⬇️ 點此下載 PDF
          </a>
          <p style="font-size:13px;color:#888;margin:12px 0 0">連結直達下載頁面，無需註冊</p>
        </div>
        <p style="font-size:14px;color:#888;line-height:1.8;border-top:1px solid #eee;padding-top:20px;margin:20px 0 0">
          💡 小提醒：我們會不定時寄送最新旅遊攻略給你，可隨時退訂。<br>
          🌏 期待與你一起探索世界<br>
          — 均在路上 小編
        </p>
      </div>
    </div>`;

  try {
    GmailApp.sendEmail(email,
      `📬 你的「${title}」已備好！均在路上免費送`,
      '請使用 HTML 郵件客戶端查看此郵件（感謝訂閱均在在路上）',
      {
        htmlBody: htmlBody,
        name: '均在路上 Travel Lab'
      }
    );
    return HtmlService.createHtmlOutput(JSON.stringify({ok: true, resource: title}));
  } catch (err) {
    return HtmlService.createHtmlOutput(JSON.stringify({error: err.message}), 500);
  }
}

// 測試用（部署前點此測試）
function testEmail() {
  const testEmails = ['your-email@gmail.com']; // 改成你的測試 email
  testEmails.forEach(email => {
    const htmlBody = '<p>測試成功！</p>';
    GmailApp.sendEmail(email, '均在路上 測試郵件', '請用 HTML 客戶端查看', {htmlBody, name: '均在在路上'});
  });
}
```

4. 點「+ 新增指令碼」建立第二個檔案，名稱改為 `Config`（或貼在同檔案頂部），貼入以下：
（上面那段已經含在主要程式碼中了，可以跳過這步）

5. 點上方 **🔔 部署 → + 新增部署**，選擇「網頁應用程式」：
   - 執行身份：**_我_**
   - 可存取人士：**任何人**
   - 確認後複製產生的 **Web App URL**

---

## 步驟 2：修改網站表單

把每個攻略頁的表單 action 從：
```
https://formspree.io/f/xredjjgb
```
改成你剛複製的 Web App URL（長這樣）：
```
https://script.google.com/macros/s/AKfycbxxxxxxx/exec
```

**快速替換指令（在我這裡執行）：**
提供給我 Web App URL，我幫你一次性更新全站 46 個表單 action。

---

## 步驟 3：測試
1. 用瀏覽器打開 `https://script.google.com` 的部署設定
2. 點「測試」或直接在網站填一次表單
3. 檢查 Gmail 寄件備份應收到自動回覆郵件（含下載連結）

---

## 流程
```
用戶填表 → Google Apps Script 接收 → 自動回覆 email（含 PDF 下載連結）→ 用戶點連結下載
```

**完全免費，Gmail 每天可寄 100 封**，足夠旅遊網站使用。