import sys, re
sys.stdout.reconfigure(encoding='utf-8')
c = open('kansai-pass.html', 'r', encoding='utf-8').read()
# find all post-thumb src values
for m in re.finditer(r'post-thumb[^>]*><img[^>]*src="([^"]+)"', c):
    print(m.group(1))
