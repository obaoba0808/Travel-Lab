# osaka-usj.html 排版修復記錄

## 問題
補充內容（p5-expand、p5-expand2、FAQ、Form、Lead Magnet）出現在兩欄布局之外（全寬區域），而非右側 `.col-center` 內。

## 根因
- `</div><!-- /article-container -->` 和 `</div>`（關閉 col-center）被放在補充內容**之前**
- `<div class="three-col-wrapper">` 從未被關閉
- 導致補充內容脫離兩欄布局，跑到全寬區域

## 修復方法
### 原始結構：
```
...文章內容...
</div><!-- /article-container -->
<!-- FOOTER -->
</div> ← col-center close

<div id="p5-expand">...</div>
<div id="p5-expand2">...FAQ...form...</div>
<!-- EMAIL LEAD MAGNET -->...
...（以上內容全在布局之外）...
<footer>
```

### 修復後結構：
```
...文章內容...
<div id="p5-expand">...</div>
<div id="p5-expand2">...FAQ...form...</div>
<!-- EMAIL LEAD MAGNET -->...
</div><!-- /article-container -->
</div> ← col-center close
</div> ← three-col-wrapper close
<footer>
```

## 方法
Python 字串剪接：
1. 找到 `</div><!-- /article-container -->` 位置（15891）
2. 找到 `<footer>` 位置（22138）
3. 提取兩者之間的內容
4. 移除 `</div><!-- /article-container -->` + `<!-- FOOTER -->` + col-center close
5. 將剩餘內容插入 article-container 結束之前
6. 正確關閉 col-center 和 three-col-wrapper

## 驗證
- ✅ p5-expand INSIDE article-container
- ✅ FAQ INSIDE article-container  
- ✅ Lead Magnet INSIDE article-container
- ✅ 所有 2 個表單都在 article-container 內
- ✅ three-col-wrapper 正確關閉
- ✅ 僅移動結構，未改動任何內容文字

## Commit
`ff085a5` — osaka-usj.html (3 insertions, 9 deletions)
已推送到 GitHub，Cloudflare Pages 正在部署中。
