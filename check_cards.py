import sys; sys.stdout.reconfigure(encoding='utf-8')
c = open('japan-travel.html', 'r', encoding='utf-8').read()
import re
for m in re.finditer(r'card-img[^>]*src="([^"]+)"', c):
    print(m.group(0))
