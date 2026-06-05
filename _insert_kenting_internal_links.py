import re

# 读取文件
with open('kenting.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 内部链接区块 HTML
internal_links = '''
<!-- 相關文章推薦 -->
<div style="background:#f5f5f5;padding:20px;border-radius:12px;margin:24px 0;">
  <h4 style="margin:0 0 12px;color:#333;">📖 台灣自由行延伸閱讀</h4>
  <ul style="margin:0;padding-left:20px;line-height:1.8;">
    <li><a href="hualien-taitung.html" style="color:#078E8A;font-weight:600;">花東三天兩夜｜太魯閣×台11線攻略</a></li>
    <li><a href="tainan-food.html" style="color:#078E8A;font-weight:600;">台南美食牛肉湯攻略｜台南小吃推薦</a></li>
    <li><a href="taipei-food.html" style="color:#078E8A;font-weight:600;">台北美食地圖｜夜市×餐廳推薦</a></li>
    <li><a href="jiufen.html" style="color:#078E8A;font-weight:600;">九份老街攻略｜黃金博物館×茶坊</a></li>
  </ul>
</div>
'''

# 在 FAQ 前插入内部链接区块
# 找到 </section> 结束标签前的 FAQ 区块
pattern = r'(<section class="faq-section">)'
replacement = internal_links + r'\1'
content = re.sub(pattern, replacement, content, count=1)

# 写入文件
with open('kenting.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已在 kenting.html 的 FAQ 前插入「相關文章推薦」區塊')
print('   內部連結：4 個描述性錨文本')
print('   位置：<section class="faq-section"> 之前')