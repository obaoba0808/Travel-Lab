import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. h1 color
c = c.replace(
    '.hero-landing h1{font-family:"Noto Serif TC",serif;font-size:42px;font-weight:700;margin-bottom:12px;position:relative}',
    '.hero-landing h1{font-family:"Noto Serif TC",serif;font-size:42px;font-weight:700;margin-bottom:12px;position:relative;color:#1a1a2e}'
)
print('1 h1 color')

# 2. sub text color
c = c.replace(
    'color:rgba(255,255,255,0.9);margin-bottom:8px;position:relative}',
    'color:#444;margin-bottom:8px;position:relative}'
)
print('2 sub color')

# 3. tagline color
c = c.replace(
    'color:rgba(255,255,255,0.7);margin-bottom:32px;position:relative}',
    'color:#666;margin-bottom:32px;position:relative}'
)
print('3 tagline color')

# 4. stat label color (first occurrence - the one in hero)
c = c.replace(
    '.hero-stat-label{font-size:12px;color:rgba(255,255,255,0.7)}',
    '.hero-stat-label{font-size:12px;color:#888}'
)
print('4 stat label')

# 5. secondary button
c = re.sub(
    r'\.hero-cta-secondary\{background:rgba\(255,255,255,0\.15\);color:#fff;border:2px solid rgba\(255,255,255,0\.4\)\}',
    '.hero-cta-secondary{background:transparent;color:#078E8A;border:2px solid #078E8A}',
    c
)
print('5 secondary btn')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done - hero background changed to white')
