import re

with open('esim-comparison.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add ~250 characters before FAQ section
extra = '''
<div style=\"margin:20px 0;padding:16px;background:#f0fdf4;border-left:4px solid #0ABAB5;border-radius:0 8px 8px 0;\">
<h3 style=\"margin-top:0;color:#0ABAB5;\">💡 小編真心話：eSIM 選購要點</h3>
<p>買 eSIM 前一定要確認手機是否支援 eSIM（iPhone XS 以後都支援，Android 手機要查型號）。另外，有些 eSIM 方案不能熱點分享，如果需要分享網路給同伴，記得選支援熱點的方案。Airalo 和 Nomad 都有中文客服，遇到問題比較好溝通。</p>
</div>
'''

# Insert before FAQ section
faq_pattern = '<section class=\"faq-section\"'
if re.search(faq_pattern, content):
    content = re.sub(faq_pattern, extra + '\n<section class=\"faq-section\"', content, count=1)
    print('OK: Added extra content to esim-comparison.html')
else:
    print('ERROR: FAQ section not found')

with open('esim-comparison.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Check count
with open('esim-comparison.html', 'r', encoding='utf-8') as f:
    c = f.read()
chinese = re.findall(r'[\u4e00-\u9fff]', c)
print(f'New count: {len(chinese)} Chinese chars')
