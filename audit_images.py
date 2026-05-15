import sys, re, glob
sys.stdout.reconfigure(encoding='utf-8')

print("=== HERO IMAGES (should be hero) ===")
for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    for m in re.finditer(r'class="hero-img"[^>]*src="([^"]+)"', c):
        print(f"  {f}: {m.group(1)}")

print("\n=== SIDEBAR IMAGES (should be sidebar) ===")
for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    for m in re.finditer(r'sb-hero-img[^>]*src="([^"]+)"', c):
        print(f"  {f}: {m.group(1)}")

print("\n=== POST-THUMB (related posts, should be hero) ===")
for f in sorted(glob.glob('*.html')):
    c = open(f, 'r', encoding='utf-8').read()
    for m in re.finditer(r'post-thumb[^>]*><img[^>]*src="([^"]+)"', c):
        print(f"  {f}: {m.group(1)}")

print("\n=== CATEGORY CARD IMAGES (should be hero) ===")
for f in ['japan-travel.html','korea-travel.html','taiwan-travel.html','southeast-asia.html','index.html']:
    c = open(f, 'r', encoding='utf-8').read()
    for m in re.finditer(r'<img src="images/([^"]+)"[^>]*width="1536"', c):
        print(f"  {f}: {m.group(1)}")
