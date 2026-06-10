import re

# Read file
with open('korea-travel.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add extra content before FAQ section
extra = '''
<div style="margin:20px 0;padding:16px;background:#f0fdf4;border-left:4px solid #0ABAB5;border-radius:0 8px 8px 0;">
<h3 style="margin-top:0;color:#0ABAB5;">💡 小編真心話：韓國旅遊秘訣</h3>
<p>韓國四季分明，春天（4-5月）櫻花、秋天（10-11月）楓葉最美。明洞換錢要去民間換書所，匯率比機場好。釜山海雲台海水浴場夏天很棒，但人超多，建議平日去。</p>
</div>
'''

# Insert before FAQ section
faq_pattern = '<section class="faq-section"'
if re.search(faq_pattern, content):
    content = re.sub(faq_pattern, extra + '\n<section class="faq-section"', content, count=1)
    print('OK: Added extra content to korea-travel.html')
else:
    print('ERROR: FAQ section not found')

# Write back
with open('korea-travel.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Check count
with open('korea-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()
chinese = re.findall(r'[\u4e00-\u9fff]', c)
print(f'New count: {len(chinese)} Chinese chars')
