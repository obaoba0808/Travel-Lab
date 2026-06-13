# golightly.fun FAQ 重複內容 SEO 審計報告
**日期：2026-06-13 | 受影響：35/62 頁（56%）**

---

## 🔴 問題本質

**FAQ 答案 = 文章內容逐字複製**

頁面結構：
```
[文章正文]
  └─ H2: 首爾5天4夜花多少錢？
        內容：不含機票約 NT$15,000-25,000...
  └─ H2: 首爾交通怎麼搭？
        內容：首選地鐵，購買T-money卡...

[常見問題]  ← FAQ 答案跟上面正文完全相同
  └─ Q: 首爾5天4夜花多少錢？
        A: 不含機票約 NT$15,000-25,000...（複製）
  └─ Q: 首爾交通怎麼搭？
        A: 首選地鐵，購買T-money卡...（複製）
```

---

## 📊 受影響頁面清單

| 頁面 | 重複數量 | 嚴重程度 |
|------|---------|---------|
| budget-airline-guide.html | 8 | 🔴嚴重 |
| busan-4days.html | 8 | 🔴嚴重 |
| credit-card-miles-guide.html | 8 | 🔴嚴重 |
| korea-transport.html | 8 | 🔴嚴重 |
| seoul-5days.html | 8 | 🔴嚴重 |
| seoul-food-map.html | 8 | 🔴嚴重 |
| singapore-3days.html | 8 | 🔴嚴重 |
| angkor-wat-2days.html | 5 | 🔴嚴重 |
| chiang-mai.html | 5 | 🔴嚴重 |
| japan-drugstore-checklist.html | 5 | 🔴嚴重 |
| jeju-island.html | 5 | 🔴嚴重 |
| kenting.html | 5 | 🔴嚴重 |
| okinawa.html | 5 | 🔴嚴重 |
| tax-refund-calculator.html | 6 | 🔴嚴重 |
| miles-calculator.html | 3 | 🟡中等 |
| fukuoka-5days.html | 2 | 🟡中等 |
| japan-money-saving-tips.html | 2 | 🟡中等 |
| japan-travel.html | 4 | 🟡中等 |
| taiwan-travel.html | 3 | 🟡中等 |
| bangkok-massage.html | 2 | 🟡中等 |
| osaka-food.html | 2 | 🟡中等 |
| japan-budget-guide.html | 2 | 🟡中等 |
| taipei-food.html | 2 | 🟡中等 |
| hokkaido-winter.html | 1 | 🟢輕微 |
| kansai-pass.html | 1 | 🟢輕微 |
| korea-budget.html | 1 | 🟢輕微 |
| kualalumpur-3days.html | 1 | 🟢輕微 |
| osaka-usj.html | 1 | 🟢輕微 |
| packing-list.html | 3 | 🟡中等 |
| seoul-food.html | 1 | 🟢輕微 |
| tainan-food.html | 1 | 🟢輕微 |
| travel-tools.html | 1 | 🟢輕微 |
| vietnam-danang.html | 1 | 🟢輕微 |
| busan-capsule.html | 1 | 🟢輕微 |

---

## 🧠 SEO 分析

### 負面影響
1. **關鍵字蠶食（Keyword Cannibalization）**：同一查詢有兩個相同答案區塊，稀釋相關性信號
2. **爬蟲預算浪費**：Google 爬完重複內容等於白爬
3. **淺層內容稀釋**：頁面字數看似多，實際獨特內容少
4. **用戶體驗差**：滾動到 FAQ 發現「這個內容我看過了」

### 不是問題的情況
- **H2 標題 = FAQ 問題**：這是正常結構，FAQ 答案展開 H2 的內容是標準 featured snippet 模式 ✅
- **真正有問題的是**：FAQ 答案跟在文章正文後，又把同樣內容複製一遍

---

## 💡 修復方案

### 方案 A：移除 FAQ 答案（最省力）
```
Q: 首爾5天4夜花多少錢？
A: [刪除答案，讓文章內容自己回答]
```
**優點**：最省力，一次腳本完成
**缺點**：FAQ 區只有問題沒有答案，看起來空洞

### 方案 B：濃縮 FAQ 答案（推薦）⭐
```
Q: 首爾5天4夜花多少錢？
A: 不含機票 NT$15,000-25,000/人，詳見上文「花費預算」章節。

Q: 首爾交通怎麼搭？
A: T-money 卡全韓通用，地鐵為主，詳見上文「市內交通」章節。
```
**優點**：FAQ 有實質答案，用內部連結導引到文章詳細內容
**缺點**：仍需逐頁調整腳本

### 方案 C：AI 重寫答案（最佳但最慢）
用 AI 將每個 FAQ 答案改寫為「一句話結論 + 數據 + 導引連結」
**優點**：內容價值最高，有機會拿下 featured snippet
**缺點**：需要逐頁執行，成本高

---

## ⚡ 快速修復腳本（方案 A 簡化版）

移除 FAQ 答案中與文章重複的內容，改為「詳見上文」格式：
- 提取每個 FAQ 的 H2 標題
- 在文章中找到對應的 H2 段落，獲取前 50 字作為濃縮答案
- 將「完整答案」改為「濃縮結論句 + 連結」

---

## 🎯 建議行動

1. **立即行動（一次 script）**：方案 B 濃縮答案，35 頁一次修復
2. **中期（手動精修）**：針對高流量頁面（seoul-5days/bangkok-4days/okinawa）用方案 C 重寫
3. **長期**：建立內容模板，FAQ 答案必須是文章中**未涵蓋**的補充資訊

---

*掃描腳本：check_answer_dupes.py（已保存在 Travel-Lab 目錄）*
*影響範圍：35 頁 | 重複答案總數：~180 處*