import sys; sys.stdout.reconfigure(encoding='utf-8')
c = open('japan-travel.html', 'r', encoding='utf-8').read()
import re
# Find all img tags in the article cards section
for m in re.finditer(r'<img[^>]+>', c):
    src = re.search(r'src="([^"]+)"', m.group())
    cls = re.search(r'class="([^"]+)"', m.group())
    if src and ('card' in (cls.group(1) if cls else '') or 'article' in (cls.group(1) if cls else '') or 'thumb' in (cls.group(1) if cls else '')):
        print(m.group()[:150])
