"""Add lazy loading to images that are missing it on index.html."""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Find images without loading attribute
imgs = list(re.finditer(r'<img([^>]+)>', c, re.I))
fixed = 0

for m in imgs:
    img_tag = m.group(0)
    attrs = m.group(1)
    
    # Skip if already has loading
    if 'loading=' in img_tag.lower():
        continue
    
    # Find src
    src_m = re.search(r'src=["\']([^"\']+)["\']', attrs, re.I)
    if not src_m:
        continue
    
    src = src_m.group(1)
    
    # Add lazy loading (insert before >)
    new_img = img_tag.replace('>', ' loading="lazy" decoding="async">', 1)
    c = c.replace(img_tag, new_img, 1)
    fixed += 1
    print("  Added lazy: " + src)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)

print("\nFixed " + str(fixed) + " images")
