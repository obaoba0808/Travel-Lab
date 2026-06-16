# golightly.fun Portal 首頁完整修復

**時間**：2026-06-14 01:07-01:20 GMT+8

## 問題

用戶截圖顯示 `index.html` 首頁完全沒有 Portal 樣式。

## 根因分析

**兩層問題**：

### 第一層（01:07）：CSS 載入
- Portal 樣式在 `index-inline.css` 獨立檔案中
- 合併到主 `style.css`（commit `df72bf7`）解決載入順序問題

### 第二層（01:07-01:20）：Tailwind 幻影類別
- `#p5-expand` 到 `#p5-expand5` 全部使用 **Tailwind CSS utility classes**（`mt-12`、`grid`、`rounded-2xl`、`shadow-sm`、`text-gray-700`、`bg-gradient-to-br`、`from-teal-50` 等）
- **網站從未載入 Tailwind CSS**，所有這些類別都是無效的
- 這是全站唯一使用 Tailwind 的頁面，之前可能是從別的模板複製過來的

## 修復方案

將 5 個 `#p5-expand` 區塊全部重建：

| 區塊 | 原始 | 修復後 |
|------|------|--------|
| p5-expand | `<div class="mt-12...">` 熱門攻略精選 | `<section class="region-section">` + inline styles grid |
| p5-expand2 | `<div class="mt-8...">` 為什麼選擇 | `<section class="region-section">` + gradient bg |
| p5-expand3 | `<div class="mt-6...">` 保險須知 | `<section>` + card with left border accent |
| p5-expand4 | `<div class="mt-4...">` 旅行理念 | `<section>` + gradient bg card |
| p5-expand5 | `<div class="mt-4...">` 免費宣言 | `<section>` + gradient bg card |

**樣式策略**：
- 全部使用 inline styles（不依賴 CSS 檔案）
- Tiffany 綠 `#0ABAB5` 作為強調色
- Grid 布局用 `display:grid` inline
- Hover 效果用 `onmouseover/onmouseout`

## 同步修復
- 清理 `<body>` 內 dead comments（`<!-- TRIP.COM PROMO -->` 等 6 行）
- 修復 `portal-content` div 缺失閉合（差 1 個 `</div>`）
- Div 平衡驗證：117/117 ✓

## 結果
- Commit `7c418fa`
- 全站零 Tailwind 類別殘留
- Cloudflare Pages 自動部署中
