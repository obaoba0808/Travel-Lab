import os
import re
from collections import defaultdict

# Extract H2 headings from HTML
def extract_h2s(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove script/style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    # Extract H2 text
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
    # Clean HTML tags from H2 text
    h2s = [re.sub(r'<[^>]+>', '', h2).strip() for h2 in h2s]
    return h2s

# Build H2 -> pages mapping
h2_map = defaultdict(list)
all_h2s = {}

for fname in os.listdir('.'):
    if fname.endswith('.html') and not fname.startswith('_'):
        h2s = extract_h2s(fname)
        all_h2s[fname] = h2s
        for h2 in h2s:
            if len(h2) > 5:  # Ignore very short headings
                h2_map[h2].append(fname)

# Find duplicate H2s
print("=== Duplicate H2 headings (possible duplicate content) ===\n")
dup_count = 0
for h2, pages in h2_map.items():
    if len(pages) > 1:
        dup_count += 1
        print(f"  H2: '{h2}'")
        print(f"    Found in: {', '.join(pages)}\n")

print(f"Total duplicate H2s: {dup_count}")

# Also check for very similar content (same H2 count = similar structure)
print("\n=== Pages with identical H2 count (possible template duplication) ===\n")
from collections import Counter
h2_count_map = defaultdict(list)
for fname, h2s in all_h2s.items():
    h2_count_map[len(h2s)].append(fname)

for count, pages in h2_count_map.items():
    if len(pages) > 5:  # Many pages with same H2 count = likely template
        print(f"  {count} H2s: {len(pages)} pages")
        for p in pages[:10]:
            print(f"    - {p}")
        if len(pages) > 10:
            print(f"    ... and {len(pages)-10} more")
        print()
