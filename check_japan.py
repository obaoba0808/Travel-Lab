import re

with open('japan-travel.html', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

for i, line in enumerate(lines, 1):
    s = line.strip().lower()
    if any(kw in s for kw in ['<main', '</main>', '<footer', 'faq', '常見問題']):
        print(f'L{i}: {line.rstrip()[:150]}')
