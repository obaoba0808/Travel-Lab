import re
with open('seoul-food.html', encoding='utf-8') as f:
    c = f.read()
text = re.sub(r'<[^>]+>', '', c)
chinese = re.sub(r'[^\u4e00-\u9fff]', '', text)
h2s = re.findall(r'<h2[^>]*>([^<]+)</h2>', c)
faqs = len(re.findall(r'faq-item', c))
print(f'seoul-food.html: {len(c)} bytes, ~{len(chinese)} Chinese chars, {len(h2s)} H2s, {faqs} FAQs')
for h in h2s:
    print(' -', h.strip())
