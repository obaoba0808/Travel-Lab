with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '.hero-landing h1{font-family:"Noto Serif TC",serif;font-size:42px;font-weight:700;margin-bottom:12px;position:relative;color:#1a1a2e}',
    '.hero-landing h1{font-family:"Noto Serif TC",serif;font-size:42px;font-weight:700;margin-bottom:12px;position:relative;color:#0ABAB5}'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('OK - h1 color changed to Tiffany #0ABAB5')