import sys; sys.stdout.reconfigure(encoding='utf-8')
c = open('japan-travel.html', 'r', encoding='utf-8').read()
import re
# Find all img tags
for i, m in enumerate(re.finditer(r'<img[^>]+>', c)):
    src = re.search(r'src="([^"]+)"', m.group())
    cls = re.search(r'class="([^"]+)"', m.group())
    print(f'[{i}] class={cls.group(1) if cls else "none"} src={src.group(1) if src else "none"}')
