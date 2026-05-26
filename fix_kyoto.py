import re

# Read file
with open('kyoto-temples.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add extra content before FAQ section
extra = '''
<div style="margin:20px 0;padding:16px;background:#f0fdf4;border-left:4px solid #0ABAB5;border-radius:0 8px 8px 0;">
<h3 style="margin-top:0;color:#0ABAB5;">💡 小編真心話：京都寺廟參觀守則</h3>
<p>參觀寺廟時記得保持安靜，不要大聲喧嘩。拍照前先確認是否允許（有些區域禁拍）。春秋兩季人潮最多，建議早上 8 點開門就衝，可以拍到沒人的美景。金閣寺和清水寺建議平日去，假日真的擠不進去。</p>
</div>
'''

# Insert before FAQ section
faq_pattern = '<section class="faq-section"'
if re.search(faq_pattern, content):
    content = re.sub(faq_pattern, extra + '\n<section class="faq-section"', content, count=1)
    print('OK: Added extra content to kyoto-temples.html')
else:
    print('ERROR: FAQ section not found')

# Write back
with open('kyoto-temples.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Check count
with open('kyoto-temples.html', 'r', encoding='utf-8') as f:
    c = f.read()
chinese = re.findall(r'[\u4e00-\u9fff]', c)
print(f'New count: {len(chinese)} Chinese chars')
