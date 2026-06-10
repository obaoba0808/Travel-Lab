import re

# Read file
with open('chiang-mai.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add extra content before FAQ section
extra = '''
<div style="margin:20px 0;padding:16px;background:#f0fdf4;border-left:4px solid #0ABAB5;border-radius:0 8px 8px 0;">
<h3 style="margin-top:0;color:#0ABAB5;">💡 小編真心話：清邁旅遊小撇步</h3>
<p>清邁旺季是 11-2 月（涼季），這時候天氣最舒服。4 月潑水節很有趣但要準備防水袋。週日夜市（週日）比週六夜市大很多，建議留整天在古城。泰式按摩一次才 NT$200 左右，便宜到哭。</p>
</div>
'''

# Insert before FAQ section
faq_pattern = '<section class="faq-section"'
if re.search(faq_pattern, content):
    content = re.sub(faq_pattern, extra + '\n<section class="faq-section"', content, count=1)
    print('OK: Added extra content to chiang-mai.html')
else:
    print('ERROR: FAQ section not found')

# Write back
with open('chiang-mai.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Check count
with open('chiang-mai.html', 'r', encoding='utf-8') as f:
    c = f.read()
chinese = re.findall(r'[\u4e00-\u9fff]', c)
print(f'New count: {len(chinese)} Chinese chars')
