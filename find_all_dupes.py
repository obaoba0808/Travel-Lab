import os
import re
from collections import defaultdict
import itertools

def extract_text(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'<script[^>]*>.*?</script>', ' ', c, flags=re.DOTALL)
    c = re.sub(r'<style[^>]*>.*?</style>', ' ', c, flags=re.DOTALL)
    c = re.sub(r'<[^>]+>', ' ', c)
    c = re.sub(r'\s+', ' ', c)
    return c.strip()

# Load all pages
pages = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('_')]
print(f"Checking {len(pages)} pages for near-duplicate pairs...\n")

# Extract text for all pages
texts = {}
for p in pages:
    texts[p] = extract_text(p)

# Compare all pairs
near_dupes = []
for i, p1 in enumerate(pages):
    for p2 in pages[i+1:]:
        words1 = set(texts[p1].split())
        words2 = set(texts[p2].split())
        if len(words1) == 0 or len(words2) == 0:
            continue
        overlap = len(words1 & words2) / len(words1 | words2) * 100
        if overlap > 60:
            near_dupes.append((p1, p2, overlap))

# Sort by similarity
near_dupes.sort(key=lambda x: -x[2])

print(f"Found {len(near_dupes)} near-duplicate pairs (similarity > 60%):\n")
for p1, p2, sim in near_dupes[:15]:  # Show top 15
    print(f"  {sim:.1f}%: {p1} <-> {p2}")
