import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

# Check hero div images
for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    m = re.search(r'<div class="hero"><img[^>]*src="([^"]+)"', c)
    if m:
        print(f"  HERO: {f}: {m.group(1)}")
