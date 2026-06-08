"""Full performance audit for golightly.fun - check all common issues."""
import os, re, sys

sys.stdout.reconfigure(encoding="utf-8")

issues = []

# 1. Check image sizes and formats
print("=== IMAGE AUDIT ===")
img_total = 0
img_count = 0
no_webp = []
large_imgs = []

for f in sorted(os.listdir(".")):
    if not f.endswith(".html"):
        continue
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    for m in re.finditer(r'src=["\']([^"\']+\.(?:jpg|jpeg|png|gif|webp))["\']', c, re.I):
        src = m.group(1)
        img_count += 1
        # Check if webp
        if not src.lower().endswith(".webp") and "images/" in src:
            no_webp.append((f, src))

print("Total images referenced: " + str(img_count))
print("Non-WebP images (potential optimization): " + str(len(no_webp)))
for page, src in no_webp[:10]:
    print("  " + page + ": " + src)
if len(no_webp) > 10:
    print("  ... and " + str(len(no_webp) - 10) + " more")

# 2. Check for inline CSS/JS (should be external or minified)
print("\n=== INLINE CSS/JS SIZE ===")
for f in ["index.html"]:
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    # Inline style blocks
    styles = re.findall(r'<style[^>]*>(.*?)</style>', c, re.DOTALL)
    style_size = sum(len(s) for s in styles)
    
    # Inline script blocks
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', c, re.DOTALL)
    script_size = sum(len(s) for s in scripts)
    
    # External CSS files
    css_files = re.findall(r'<link[^>]*href=["\']([^"\']+\.css)["\']', c, re.I)
    
    # External JS files
    js_files = re.findall(r'<script[^>]*src=["\']([^"\']+\.js)["\']', c, re.I)
    
    print("index.html:")
    print("  Inline CSS: " + str(style_size) + " bytes (" + str(len(styles)) + " blocks)")
    print("  Inline JS: " + str(script_size) + " bytes (" + str(len(scripts)) + " blocks)")
    print("  External CSS: " + ", ".join(css_files))
    print("  External JS: " + ", ".join(js_files))
    
    total_inline = style_size + script_size
    if total_inline > 50000:
        issues.append(("P0", "Large inline CSS/JS on index.html (" + str(total_inline) + " bytes)", f))

# 3. Check for render-blocking resources
print("\n=== RENDER-BLOCKING RESOURCES ===")
for f in ["index.html"]:
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    blocking_css = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', c)
    blocking_js = re.findall(r'<script[^>]*src=["\'][^"\']+["\'][^>]*(?!.*async)(?!.*defer)[^>]*>', c)
    
    print("Render-blocking CSS: " + str(len(blocking_css)))
    for b in blocking_css[:5]:
        print("  " + b.strip())
    
    print("Render-blocking JS (no async/defer): " + str(len(blocking_js)))
    for b in blocking_js[:5]:
        print("  " + b.strip())

# 4. Check for missing lazy loading on images below fold
print("\n=== LAZY LOADING CHECK ===")
for f in ["index.html"]:
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    imgs = re.findall(r'<img[^>]+>', c, re.I)
    no_lazy = []
    for img in imgs:
        if 'loading=' not in img.lower() and 'src=' in img.lower():
            src_m = re.search(r'src=["\']([^"\']+)["\']', img, re.I)
            if src_m:
                no_lazy.append(src_m.group(1))
    
    print("Images without lazy loading: " + str(len(no_lazy)) + "/" + str(len(imgs)))

# 5. Check HTML file sizes
print("\n=== FILE SIZES ===")
sizes = []
for f in sorted(os.listdir(".")):
    if f.endswith(".html"):
        sz = os.path.getsize(f)
        sizes.append((f, sz))
        
sizes.sort(key=lambda x: -x[1])
for f, sz in sizes[:10]:
    status = ""
    if sz > 100000:
        status = " *** LARGE"
    elif sz > 50000:
        status = " ** MEDIUM"
    print("  " + f + ": " + str(sz // 1024) + "KB" + status)

# 6. Check for duplicate/unnecessary meta tags
print("\n=== META TAG AUDIT ===")
with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

meta_tags = re.findall(r'<meta[^>]+>', c)
print("Meta tags count: " + str(len(meta_tags)))

# Check for viewport
if 'viewport' in c:
    print("  Viewport: OK")
else:
    issues.append(("P0", "Missing viewport meta tag", "index.html"))

# Check for charset early
charset_pos = c.find('charset')
head_end = c.find('</head>')
if charset_pos > 0 and charset_pos < head_end:
    print("  Charset: OK (in head)")
else:
    issues.append(("P0", "Charset not in <head>", "index.html"))

# 7. Summary
print("\n=== ISSUES SUMMARY ===")
if issues:
    for priority, desc, file in issues:
        print("[" + priority + "] " + file + ": " + desc)
else:
    print("No critical issues found from static analysis.")
    print("For full PageSpeed diagnosis, use Lighthouse or PageSpeed Insights API.")

print("\nDone!")
