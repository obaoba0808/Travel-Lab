# golightly.fun 網站審計報告
**審計日期**: 2026-05-28  
**審計範圍**: SEO / UX / 變現設計  
**檔案數量**: 36 個 HTML 檔案

---

## 一、內容重複檢查

### 檢查方法
掃描所有 HTML 檔案（排除 index、about、contact、privacy、terms、disclaimer）的「實戰攻略精華」「小編真心話」「FAQ」區塊。

### 發現的問題

#### 1.1 區塊缺失不一致
以下是各文章包含的內容區塊統計：

| 檔案名稱 | 小編真心話 | 實戰攻略精華 | FAQ | Trip.com CTA | Klook CTA | 住宿推薦 |
|-----------|------------|--------------|-----|--------------|------------|----------|
| tokyo-5days.html | ❌ | ❌ | ✅ (6項) | ✅ (5處) | ✅ (2處) | ✅ |
| kansai-pass.html | ✅ | ❌ | ✅ (8項) | ✅ (1處) | ✅ (2處) | ❌ |
| osaka-food.html | ✅ | ✅ | ✅ (6項) | ✅ (1處) | ✅ (1處) | ✅ |
| seoul-food.html | ✅ | ❌ | ✅ (9項) | ✅ (4處) | ✅ (1處) | ✅ |
| bangkok-3days.html | ✅ | ❌ | ✅ (7項) | ✅ (1處) | ❌ | ✅ |

**問題**: 不是所有文章都有「小編真心話」和「實戰攻略精華」區塊，這會造成用戶體驗不一致。

#### 1.2 可能的重複內容
經比對內容雜湊值，目前未發現完全相同的段落。但發現以下潛在問題：
- **交通攻略說明**：多篇文章（如 tokyo-5days、kansai-pass）都有類似的地鐵/票券說明
- **免稅提醒**：多篇「小編真心話」提到免稅購物，文字相似度高
- **便利店推薦**：多篇提到 7-11、FamilyMart，內容重複

**建議**: 需要進一步用 Python + BeautifulSoup 詳細比對段落相似度。

---

## 二、UI 一致性審計

### 2.1 文章標題結構
**發現問題**:
- ✅ 大部分文章使用正確的 H1 → H2 → H3 階層
- ❌ 部分文章（如 `kansai-pass.html`）使用 inline style 而非統一 CSS 類別

**不一致範例**:
`kansai-pass.html` 第 190、256 行使用：
```html
<div style="margin:28px 0;padding:16px 20px;border-left:4px solid #0ABAB5;background:#f0fafa;border-radius:...">
```
應統一為：
```html
<div class="tip-box">
```

### 2.2 卡片風格一致性

| 元素 | 應有樣式 | 實際狀況 |
|------|----------|------------|
| `highlight-box-beautify` | 統一邊框、陰影、圓角 | ❌ 部分文章缺少此類別 |
| `day-card` | 統一日期標籤、標題樣式 | ✅ 大部分一致 |
| `tip-box` | Tiffany 藍邊框、淺藍背景 | ⚠️ `kansai-pass.html` 使用 inline style |
| `faq-item` | 統一點擊展開互動 | ✅ 大部分一致 |

**問題**: `kansai-pass.html` 未使用統一的 `tip-box` 類別，改用 inline style，導致樣式不一致。

### 2.3 CTA 位置一致性

#### Trip.com Banner 位置
- ❌ **不一致**: `tokyo-5days.html` 有 **5 處** Trip.com CTA，`seoul-food.html` 有 **4 處**
- ✅ **較佳**: `kansai-pass.html`、`osaka-food.html` 只有 **1 處**

**建議**: 每篇文章統一放置 **1 處** Trip.com 住宿推薦 CTA，位置統一在「延伸閱讀」之前。

#### Klook 動態橫幅位置
- ❌ **缺失**: `bangkok-3days.html`、`hokkaido-winter.html` 缺少 Klook CTA
- ✅ **統一**: 大部分文章放在 FAQ 區塊之前

### 2.4 小編真心話區塊樣式
**發現問題**:
- `kansai-pass.html` 使用 `<em>` 標籤
- `osaka-food.html` 使用 `<strong>` 標籤
- 部分文章使用 inline style 而非統一 CSS 類別

**建議**: 統一使用 `<div class="tip-box">` 並加上「小編真心話」標題。

### 2.5 FAQ 區塊樣式
✅ **一致性良好**: 所有 FAQ 區塊都使用 `<section class="faq-section">` 和 `<div class="faq-item">`，互動邏輯一致。

### 2.6 延伸閱讀樣式
❌ **缺失**: 部分文章（如 `packing-list.html`、`esim-comparison.html`）沒有「延伸閱讀」區塊。

### 2.7 Footer 社群連結
✅ **一致性良好**: 所有文章都包含完整的 footer 社群連結（Instagram、Facebook、LINE@、Email）。

---

## 三、Email 變現設計（Lead Magnet）

### 3.1 現有文章 Lead Magnet 設計

| 文章檔案 | Lead Magnet 名稱 | 誘餌文案 | 放置位置 | CTA 按鈕文字 |
|----------|-------------------|----------|----------|----------------|
| **tokyo-5days.html** | 東京5天地鐵路線圖PDF | 下載離線可用地鐵圖，搭車不迷路 | Day 3 之後 | 「免費下載東京地鐵圖」 |
| **kansai-pass.html** | 關西票券省錢試算表 | 輸入行程自動計算最省票券組合 | 票券比較表之後 | 「獲取我的省錢試算表」 |
| **hokkaido-winter.html** | 北海道冬季穿搭清單 | 氣溫對照表 + 必帶保暖裝備清單 | 穿衣指南之後 | 「下載穿搭清單PDF」 |
| **okinawa.html** | 沖繩自駕地圖與停車攻略 | 景點停車場收費 + 路邊停車技巧 | 自駕注意事項之後 | 「獲取自駕地圖」 |
| **kyoto-temples.html** | 京都賞楓時間表2026 | 即時紅葉預測 + 最佳攝影時間 | 賞楓景點介紹之後 | 「下載2026紅葉時間表」 |
| **osaka-food.html** | 大阪美食地圖PDF | 23家必吃餐廳位置 + 預約連結 | 美食推薦之後 | 「免費獲取美食地圖」 |
| **osaka-usj.html** | USJ快速通關攻略 | 遊樂設施等待時間 + 快速通關購買教學 | 行程規劃之後 | 「下載USJ攻略PDF」 |
| **japan-budget-guide.html** | 日本7天預算表 | Excel 可編輯預算表 + 花費分類 | 預算解析之後 | 「獲取預算試算表」 |
| **seoul-food.html** | 首爾美食地圖 | 明洞/弘大/江南餐廳分布圖 | 美食介紹之後 | 「下載首爾美食地圖」 |
| **busan-capsule.html** | 釜山膠囊列車預約教學 | 預約步驟截圖 + 付款教學 | 預約指南之後 | 「獲取預約教學PDF」 |
| **jeju-island.html** | 濟州島自駕環島路線 | 3天2夜自駕路線圖 + 加油站位置 | 自駕路線之後 | 「下載環島路線圖」 |
| **korea-budget.html** | 韓國5天預算表 | 首爾/釜山/濟州花費對照 | 預算指南之後 | 「獲取預算表」 |
| **hualien-taitung.html** | 花東三天兩夜行程表 | 太魯閣+七星潭+伯朗大道完整行程 | 行程規劃之後 | 「下載行程表PDF」 |
| **tainan-food.html** | 台南牛肉湯地圖 | 17家牛肉湯店位置 + 營業時間 | 美食推薦之後 | 「獲取牛肉湯地圖」 |
| **kenting.html** | 墾丁夜市美食清單 | 墾丁街邊小吃 + 夜市必吃推薦 | 夜市介紹之後 | 「下載美食清單」 |
| **taipei-food.html** | 台北美食地圖 | 士林/寧夏/遼寧夜市必吃清單 | 美食介紹之後 | 「下載台北美食地圖」 |
| **jiufen.html** | 九份老街攻略 | 老街店家推薦 + 避坑指南 | 老街導覽之後 | 「下載九份攻略PDF」 |
| **chiang-mai.html** | 清邁數位遊牧簽證指南 | 泰國簽證申請步驟 + 長期住宿推薦 | 簽證介紹之後 | 「獲取簽證指南」 |
| **bangkok-3days.html** | 曼谷美食地圖 | 嘟嘟車司機推薦隱藏美食 | 美食介紹之後 | 「下載曼谷美食地圖」 |
| **bangkok-massage.html** | 曼谷按摩地圖 | 22家合法按摩店位置 + 價格對照 | 按摩推薦之後 | 「下載按摩地圖PDF」 |
| **vietnam-danang.html** | 峴港景點地圖 | 巴拿山+美溪沙灘+山茶半島路線 | 景點介紹之後 | 「下載峴港地圖」 |

### 3.2 Lead Magnet 實作建議
1. **彈出視窗時機**: 用戶捲動到文章 60% 時觸發
2. **Email 收取工具**: 使用 Mailchimp 或 ConvertKit
3. **交付方式**: 填寫 Email 後自動發送 PDF 下載連結
4. **A/B 測試**: 測試不同 CTA 按鈕文字的轉換率

---

## 四、修正優先級

### P0（必須修）- 嚴重影響 UX/SEO
1. ❌ **修復 `kansai-pass.html` 的 inline style** → 改用統一 CSS 類別 `tip-box`
2. ❌ **統一 CTA 位置** → 每篇文章只留 1 處 Trip.com + 1 處 Klook，位置統一
3. ❌ **補齊缺失的「小編真心話」區塊** → 所有文章都應包含此區塊

### P1（應該修）- 影響專業度
1. ⚠️ **統一「小編真心話」樣式** → 全部使用 `<div class="tip-box">` + 標題
2. ⚠️ **補齊缺失的 Klook CTA** → `bangkok-3days.html`、`hokkaido-winter.html`
3. ⚠️ **新增 Lead Magnet 彈出視窗** → 所有文章都應有 Email 蒐集機制

### P2（可以修）- 優化體驗
1. 💡 **新增「延伸閱讀」區塊** → `packing-list.html`、`esim-comparison.html`
2. 💡 **優化 FAQ 區塊** → 部分文章 FAQ 過少（如 `tainan-food.html` 只有 1 題）
3. 💡 **內容去重複** → 用 Python 腳本詳細比對相似段落

---

## 五、執行計畫

### 階段一（本週完成）
- [ ] 修復 `kansai-pass.html` inline style 問題
- [ ] 統一所有文章的 CTA 位置
- [ ] 補齊「小編真心話」區塊

### 階段二（下週完成）
- [ ] 設計 Lead Magnet 彈出視窗
- [ ] 製作 21 個免費資源 PDF
- [ ] 串接 Email 收取工具

### 階段三（兩週內完成）
- [ ] 內容去重複檢查
- [ ] SEO 優化（metadata、結構化標記）
- [ ] 速度優化（圖片壓縮、快取設定）

---

**報告產出者**: 跨境SEO炼金师  
**報告日期**: 2026-05-28  
**檔案位置**: `C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\golightly_audit_20260528.md`
