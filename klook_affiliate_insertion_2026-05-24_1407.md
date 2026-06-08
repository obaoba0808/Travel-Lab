# Klook 聯盟連結插入任務 - 2026-05-24 14:07

## 任務目標

為 Travel Lab 網站的 **3 個旅遊頁面** 插入 **Klook 聯盟推薦卡片**，以「自然推薦」方式埋入文章，提升轉換率。

---

## 執行摘要

**狀態**：⏳ 待執行  
**頁面數**：3 個  
**Klook 聯盟 ID**：`aid=121592`  
**廣告 ID**：`aff_adid=1283452 / 1283449 / 1283447`  

---

## 完成的頁面清單

| 頁面 | 城市 | Klook 連結內容 | 插入位置 | 狀態 |
|------|------|----------------|----------|------|
| `osaka-usj.html` | 大阪 | USJ 普通票 + 快速通關 | 「🎢 USJ 遊樂設施推薦」後方 | ⏳ 待執行 |
| `kansai-pass.html` | 關西 | JR Pass 關西寬廣區域券（5日） | 「💰 票券選擇決策樹」後方 | ⏳ 待執行 |
| `tokyo-5days.html` | 東京 | Tokyo Subway Ticket（24/48/72小時） | 「🚇 東京都內交通」後方 | ⏳ 待執行 |

---

## Klook 聯盟連結詳細資訊

### 1. osaka-usj.html — USJ 門票（2 個連結）

#### USJ 普通票（QR Code 直接入場）

**原始連結**：
```
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry%2F
```

**解碼後**：
```
https://www.klook.com/zh-TW/activity/46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry/
```

**活動 ID**：`46604`  
**廣告 ID**：`aff_adid=1283452`  

#### USJ 快速通關券（Express Pass）

**原始連結**：
```
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F3407-universal-studios-japan-express-pass-osaka%2F
```

**解碼後**：
```
https://www.klook.com/zh-TW/activity/3407-universal-studios-japan-express-pass-osaka/
```

**活動 ID**：`3407`  
**廣告 ID**：`aff_adid=1283449`  

**插入位置**：  
- 普通票：插入在「🎢 USJ 遊樂設施推薦」章節後方  
- 快速通關：插入在「🎢 USJ 遊樂設施推薦」章節後方（普通票下方）  

**卡片設計**：  
- 使用 Klook 品牌色（#FF5722 橘色）  
- 背景：#FFF3E0（淺橘白）  
- 圓角：16px  
- 陰影：box-shadow: 0 4px 16px rgba(0,0,0,0.06)  
- Hover 效果：transform: translateY(-3px)  

---

### 2. kansai-pass.html — JR Pass 關西寬廣區域券

#### JR Pass 關西寬廣區域券（5日）

**原始連結**：
```
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-HK%2Factivity%2F3277-5-day-kansai-wide-area-jr-pass%2F
```

**解碼後**：
```
https://www.klook.com/zh-HK/activity/3277-5-day-kansai-wide-area-jr-pass/
```

**活動 ID**：`3277`  
**廣告 ID**：`aff_adid=1283449`  

**插入位置**：插入在「💰 票券選擇決策樹」章節後方（圖片 `ollieyu-kansai-pass.png` 下方）  

**卡片設計**：  
- 使用 JR 品牌色（#007B43 綠色）  
- 背景：#E8F8F7（淺薄荷白）  
- 圓角：16px  
- 陰影：box-shadow: 0 4px 16px rgba(0,0,0,0.06)  
- Hover 效果：transform: translateY(-3px)  

---

### 3. tokyo-5days.html — Tokyo Subway Pass 地鐵

#### Tokyo Subway Ticket（24/48/72小時）

**原始連結**：
```
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283447&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1552-subway-ticket-tokyo%2F
```

**解碼後**：
```
https://www.klook.com/zh-TW/activity/1552-subway-ticket-tokyo/
```

**活動 ID**：`1552`  
**廣告 ID**：`aff_adid=1283447`  

**插入位置**：插入在「🚇 東京都內交通」章節後方  

**卡片設計**：  
- 使用 Tokyo Metro 品牌色（#0078C8 藍色）  
- 背景：#E3F2FD（淺藍白）  
- 圓角：16px  
- 陰影：box-shadow: 0 4px 16px rgba(0,0,0,0.06)  
- Hover 效果：transform: translateY(-3px)  

---

## 卡片設計規格

### 配色方案（Klook 橘色）

```css
主色：#FF5722（Klook 橘）
背景：#FFF3E0（淺橘白）
文字深色：#1a1a2e
文字灰色：#666
邊框：5px solid #FF5722
```

### 樣式細節

```css
border-radius: 16px;
padding: 24px 28px;
margin: 36px 0;
box-shadow: 0 4px 16px rgba(0,0,0,0.06);
transition: transform 0.2s, box-shadow 0.2s;
```

### Hover 效果

```css
transform: translateY(-3px);
box-shadow: 0 6px 24px rgba(0,0,0,0.12);
```

### CTA 按鈕

```css
display: inline-block;
background: #FF5722;
color: #fff;
padding: 10px 22px;
border-radius: 8px;
text-decoration: none;
font-weight: 600;
font-size: 14px;
transition: background 0.2s;
```

Hover 時背景變深：`#F4511E`

---

## 插入位置邏輯

### osaka-usj.html

**位置**：「🎢 USJ 遊樂設施推薦」章節後方  

**原因**：  
- 讀者讀完 USJ 遊樂設施介紹後，正要考慮買票  
- 此時插入門票推薦，轉換率最高  
- 普通票 + 快速通關一起推薦，滿足不同需求  

### kansai-pass.html

**位置**：「💰 票券選擇決策樹」章節後方（圖片下方）  

**原因**：  
- 讀者已經知道要買哪種票券  
- 決策樹幫助他們做出選擇  
- 直接給連結，縮短購買路徑  

### tokyo-5days.html

**位置**：「🚇 東京都內交通」章節後方  

**原因**：  
- 讀者正要規劃東京地鐵移動  
- 此時推薦地鐵票券，需求最高  
- 交通章節後方是黃金位置  

---

## 遭遇問題與解決方案（預期）

### 問題 1：PowerShell 輸出 emoji 編碼錯誤

**錯誤訊息**（預期）：  
```
Cannot process the command because the value 128308 of the 'encoding' operand is not supported
```

**原因**：PowerShell console 使用 cp950（Big5），無法正確顯示 emoji（Unicode > U+FFFF）  

**解決方案**：  
- 腳本邏輯已執行成功，只是輸出時報錯  
- 使用 `Select-String` 驗證檔案內容確認插入成功 ✅  
- 改用純文字輸出（`[OK]`、`[SKIP]`、`[FAIL]`）避免 emoji  

### 問題 2：HTML 結構匹配問題

**原因**：HTML 標籤可能帶有 `style` 屬性或其他屬性  

**解決方案**：  
- 使用寬鬆正則：`r'(<h2[^>]*>🎢 USJ 遊樂設施推薦</h2>)'`  
- 使用 `re.search()` 而非精確字串匹配  
- 提高容錯性  

---

## 技術筆記

### Klook 聯盟連結解碼

**URL 編碼解碼**：  
```python
from urllib.parse import unquote

url = "https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry%2F"

params = parse_qs(urlparse(url).query)
k_site = unquote(params['k_site'][0])
print(k_site)
# 輸出：https://www.klook.com/zh-TW/activity/46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry/
```

**確認活動 ID**：  
- USJ 普通票：`46604`  
- USJ 快速通關：`3407`  
- JR Pass 關西寬廣：`3277`  
- Tokyo Subway：`1552`  

### Python 腳本處理中文內容的最佳實踐

1. **使用 `encoding="utf-8"` 開啟檔案**  
   ```python
   with open(fp, "r", encoding="utf-8") as f:
       content = f.read()
   ```

2. **正則表達式需考慮 HTML 屬性**  
   ```python
   # 錯誤：無法匹配帶有 style 屬性的標籤
   pattern = r'(<h2>🎢 USJ 遊樂設施推薦</h2>)'
   
   # 正確：使用寬鬆正則
   pattern = r'(<h2[^>]*>🎢 USJ 遊樂設施推薦</h2>)'
   ```

3. **使用 `re.search()` 而非精確字串匹配**  
   - 提高容錯性  
   - 處理 HTML 屬性變化  

### Klook 橘色配色在網頁設計的應用

- **主色 #FF5722**：Klook 橘，給人活力感、行動呼籲感，適合門票推薦  
- **背景 #FFF3E0**：淺橘白，與主色形成柔和對比  
- **Hover 效果**：微上浮 + 陰影加深，提升互動感  
- **圓角 16px**：現代感設計，避免尖角給人壓迫感  

---

## Git 操作記錄（預期）

```powershell
# 加入修改的檔案
git add osaka-usj.html kansai-pass.html tokyo-5days.html

# 提交
git commit -m "feat: 3頁面插入 Klook 聯盟推薦卡片（Klook 橘配色）`n`n自然埋入門票/票券推薦，含個人體驗文字+CTA 按鈕`n`n涵蓋：大阪USJ/關西JR Pass/東京地鐵"

# 推送
git push origin master
```

**預期 Commit hash**：待執行後生成  

---

## 部署狀態（預期）

- ⏳ Commit 已推送到 GitHub  
- ⏳ GitHub Pages 自動部署中（預計 1-3 分鐘）  
- ⏳ 所有卡片已上線（https://golightly.fun/）  
- ⏳ Klook 橘配色已生效  

---

## 待驗證項目

- [ ] 確認 https://golightly.fun/osaka-usj.html 卡片顯示正常  
- [ ] 確認 https://golightly.fun/kansai-pass.html 卡片顯示正常  
- [ ] 確認 https://golightly.fun/tokyo-5days.html 卡片顯示正常  
- [ ] 確認卡片圓角效果（border-radius: 16px）  
- [ ] 確認卡片陰影效果（box-shadow）  
- [ ] 確認 CTA 按鈕 hover 效果  
- [ ] 確認手機版顯示正常（max-width: 600px）  

---

## 下一步可以做的聯盟推薦

你目前已經完成：  
1. ✅ **① 住宿推薦（Trip.com）** — 10 個頁面  
2. ⏳ **② 門票/景點票券（Klook）** — 3 個頁面（待執行）  

如果你有其他的聯盟連結，可以繼續埋入：  

3. **③ eSIM/上網方案（Airalo/Nomad）** → 插入在「行前準備」清單內  
4. **④ 交通票券（JR Pass）** → 插入在關西/東京頁面的交通章節  
5. **⑤ 打包清單/購物推薦** → 插入在「行前準備」末端  
6. **⑥ 旅行保險** → 插入在 FAQ 前方或文末  

需要我繼續做嗎？把對應的聯盟連結給我即可 🔗

---

**最後更新**：2026-05-24 14:07 GMT+8  
**狀態**：⏳ Klook 聯盟連結已收到並記錄，等待執行插入任務
