import re

# ========================================
# File 1: 404.html - 完整的錯誤頁面
# ========================================

with open('404.html', 'r', encoding='utf-8') as f:
    content_404 = f.read()

extra_404 = '''
<div style="text-align:center;padding:40px 20px;">
<h2>😅 頁面找不到（404 Error）</h2>
<p>抱歉，您要找的頁面可能已經移動、刪除或網址輸入錯誤。</p>
<p>別擔心，這種情況每個旅人都會遇到（就像在京都迷路一樣，最後總會找到美景）。</p>
</div>

<h2>🔍 你可以這樣做</h2>
<ul>
<li><strong>檢查網址拼寫</strong>：有時候只是打錯字而已，檢查一下網址是否正確</li>
<li><strong>回到首頁</strong>：點擊上方「均在路上 Travel Lab」標題回到首頁</li>
<li><strong>搜尋想要的文章</strong>：使用搜尋功能找相關旅遊攻略</li>
<li><strong>聯絡我們</strong>：如果真的找不到，歡迎透過 <a href="contact.html">聯絡頁面</a> 告訴我們</li>
</ul>

<h2>🔥 熱門文章推薦</h2>
<p>與其繼續找找不到的頁面，不如看看這些熱門攻略：</p>
<ul>
<li>🇯🇵 <a href="japan-travel.html">日本旅遊攻略 2026</a> - 關東關西全面解析，附交通券、美食、景點推薦</li>
<li>🇰🇷 <a href="korea-travel.html">韓國旅遊攻略</a> - 首爾釜山濟州島完整指南</li>
<li>🇹🇼 <a href="taiwan-travel.html">台灣旅遊攻略</a> - 環島必去景點推薦</li>
<li>🍜 <a href="osaka-food.html">大阪美食地圖</a> -