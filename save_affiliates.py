import sys
sys.stdout.reconfigure(encoding='utf-8')

content = '''# 聯盟連結清單（Affiliate Links）

> 最後更新：2026-05-31
> 用途：PDF 推廣嵌入、網頁聯盟連結替換

---

## 🔗 Klook 聯盟連結（aid=121592）

### 1. Osaka USJ 門票
**Ad ID**: 1283452
**連結**:
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry%2F

### 2. Osaka USJ 快速通關（EXP）
**Ad ID**: 1283449
**連結**:
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F3407-universal-studios-japan-express-pass-osaka%2F

### 3. Kansai JR Pass
**Ad ID**: 1283449
**連結**:
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-HK%2Factivity%2F3277-5-day-kansai-wide-area-jr-pass%2F

### 4. Tokyo Subway Pass 地鐵
**Ad ID**: 1283447
**連結**:
https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283447&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1552-subway-ticket-tokyo%2F

---

## 🏨 Trip.com 聯盟連結

**Alliance ID**: 8237671
**SID**: 312406690
**廣告 ID**: DB17138130

**Base URL**:
https://tw.trip.com/partners/ad/DB17138130?Allianceid=8237671&SID=312406690&trip_sub1=

---

## 📊 Klook 動態橫幅 Widget

### 台北酒店
`html
<ins class="klk-aff-widget" data-adid="1282378" data-lang="zh-TW" data-currency="TWD" data-cardH="126" data-padding="92" data-lgH="470" data-edgeValue="655" data-prod="hotel_dynamic_widget"><a href="//www.klook.com/">Klook.com</a></ins>
<script type="text/javascript">
(function (d, sc, u) {
  var s = d.createElement(sc), p = d.getElementsByTagName(sc)[0];
  s.type = "text/javascript"; s.async = true;
  s.src = u; p.parentNode.insertBefore(s, p);
})(document, "script", "https://affiliate.klook.com/widget/fetch-iframe-init.js");
</script>
`

### 大阪酒店
`html
<ins class="klk-aff-widget" data-adid="1282013" data-lang="zh-TW" data-currency="TWD" data-cardH="126" data-padding="92" data-lgH="470" data-edgeValue="655" data-prod="hotel_dynamic_widget"><a href="//www.klook.com/">Klook.com</a></ins>
<script type="text/javascript">
(function (d, sc, u) {
  var s = d.createElement(sc), p = d.getElementsByTagName(sc)[0];
  s.type = "text/javascript"; s.async = true;
  s.src = u; p.parentNode.insertBefore(s, p);
})(document, "script", "https://affiliate.klook.com/widget/fetch-iframe-init.js");
</script>
`

### 東京酒店
`html
<ins class="klk-aff-widget" data-adid="1281998" data-lang="zh-TW" data-currency="TWD" data-cardH="126" data-padding="92" data-lgH="470" data-edgeValue="655" data-prod="hotel_dynamic_widget"><a href="//www.klook.com/">Klook.com</a></ins>
<script type="text/javascript">
(function (d, sc, u) {
  var s = d.createElement(sc), p = d.getElementsByTagName(sc)[0];
  s.type = "text/javascript"; s.async = true;
  s.src = u; p.parentNode.insertBefore(s, p);
})(document, "script", "https://affiliate.klook.com/widget/fetch-iframe-init.js");
</script>
`

### 京都酒店
`html
<ins class="klk-aff-widget" data-adid="1282006" data-lang="zh-TW" data-currency="TWD" data-cardH="126" data-padding="92" data-lgH="470" data-edgeValue="655" data-prod="hotel_dynamic_widget"><a href="//www.klook.com/">Klook.com</a></ins>
<script type="text/javascript">
(function (d, sc, u) {
  var s = d.createElement(sc), p = d.getElementsByTagName(sc)[0];
  s.type = "text/javascript"; s.async = true;
  s.src = u; p.parentNode.insertBefore(s, p);
})(document, "script", "https://affiliate.klook.com/widget/fetch-iframe-init.js");
</script>
`

---

## 📌 使用注意

1. **PDF 嵌入**：用 PyMuPDF 的 page.insert_link() 添加可點擊連結
2. **網頁嵌入**：直接複製上方 HTML 代碼貼到網頁
3. **連結檢查**：每次使用前建議用 browser 工具檢查連結是否仍有效
4. **GDPR 合規**：記得在網頁底部加上「聯盟連結聲明」

---

*此文件由 AI 自動生成，請定期檢查連結有效性*
'''

with open('affiliate-links.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Saved to affiliate-links.md')
