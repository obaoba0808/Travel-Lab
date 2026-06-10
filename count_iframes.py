import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"{'File':<30} {'Iframe Count':<15}")
print("="*60)

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    iframes = re.findall(r'<iframe', content)
    count = len(iframes)
    
    if count > 0:
        print(f'{filename:<30} {count:<15}')
