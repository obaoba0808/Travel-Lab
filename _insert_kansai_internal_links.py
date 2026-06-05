import re

# 读取文件
with open('kansai-pass.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 内部链接区块 HTML
internal_links = '''
<!-- 相關文章推薦 -->
<div style="background:#f5f5f5;padding:20px;border-radius:12px;margin:24px 0;">
  <h4 style="margin:0 0 12px;color:#333;">📖 關西自由行延伸閱讀</h4>
  <ul style="margin:0;padding-left:20px;line-height:1.8;">
    <li><a href="kyoto-temples.html" style="color:#078E8A;font-weight:600;">京都寺廟散步地圖｜清水寺×金閣寺×嵐山竹林</a></li>
    <li><a href="osaka-food.html" style="color:#078E8A;font-weight:600;">大阪美食攻略｜道頓堀×黑門市場必吃清單</a></li>
    <li><a href="tokyo-5days.html" style="color:#078E8A;font-weight:600;">東京5天4夜行程｜地鐵教學×景點推薦</a></li>
    <li><a href="japan-budget-guide.html" style="color:#078E8A;font-weight:600;">日本旅遊預算指南｜機票+住宿+交通</a></li>
  </ul>
</div>
'''

# 在 FAQ 前插入内部链接区块
# 找到 </section> 结束标签前的 FAQ 区块
pattern = r'(<section class="faq-section">)'
replacement = internal_links + r'\1'
content = re.sub(pattern, replacement, content, count=1)

# 写入文件
with open('kansai-pass.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已在 kansai-pass.html 的 FAQ 前插入「相關文章推薦」區塊')
print('   內部連結：4 個描述性錨文本')
print('   位置：<section class="faq-section"> 之前')