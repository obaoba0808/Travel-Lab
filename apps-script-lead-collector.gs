// Google Apps Script - Email Lead Collector for golightly.fun
// 部署為 Web App (Execute as: Me, Access: Anyone)

const SHEET_ID = 'YOUR_SHEET_ID_HERE'; // TODO: 替換為你的 Google Sheet ID

function doGet(e) {
  return handleRequest(e);
}

function doPost(e) {
  return handleRequest(e);
}

function handleRequest(e) {
  try {
    const params = e.parameter || {};
    const email = params.email;
    const resource = params.resource || '';
    const page = params.page || '';
    const timestamp = new Date().toLocaleString('zh-TW', { timeZone: 'Asia/Taipei' });

    if (!email || !email.includes('@')) {
      return ContentService.createTextOutput(JSON.stringify({error: 'Invalid email'}))
        .setMimeType(ContentService.MimeType.JSON)
        .setHeader('Access-Control-Allow-Origin', '*');
    }

    const ss = SpreadsheetApp.openById(SHEET_ID);
    let sheet = ss.getSheetByName('Leads');

    if (!sheet) {
      sheet = ss.insertSheet('Leads');
      sheet.appendRow(['Timestamp', 'Email', 'Resource', 'Page']);
      sheet.getRange(1, 1, 1, 4).setFontWeight('bold').setBackground('#0ABAB5').setFontColor('#ffffff');
    }

    sheet.appendRow([timestamp, email, resource, page]);

    return ContentService.createTextOutput(JSON.stringify({ok: true}))
      .setMimeType(ContentService.MimeType.JSON)
      .setHeader('Access-Control-Allow-Origin', '*');

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({error: err.message}))
      .setMimeType(ContentService.MimeType.JSON)
      .setHeader('Access-Control-Allow-Origin', '*');
  }
}
