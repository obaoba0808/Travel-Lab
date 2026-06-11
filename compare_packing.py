import re

def extract_text(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    # Remove script/style
    c = re.sub(r'<script[^>]*>.*?</script>', '', c, flags=re.DOTALL)
    c = re.sub(r'<style[^>]*>.*?</style>', '', c, flags=re.DOTALL)
    # Remove all HTML tags
    c = re.sub(r'<[^>]+>', ' ', c)
    # Normalize whitespace
    c = re.sub(r'\s+', ' ', c)
    return c.strip()

t1 = extract_text('packing-list.html')
t2 = extract_text('packing-list-online.html')

print("packing-list.html text length:", len(t1))
print("packing-list-online.html text length:", len(t2))
print()

# Compare first 500 chars
print("=== First 300 chars comparison ===")
print("packing-list.html:", t1[:300])
print()
print("packing-list-online.html:", t2[:300])
print()

# Check similarity
if t1 == t2:
    print("RESULT: IDENTICAL content - these are DUPLICATE pages!")
elif t1 in t2 or t2 in t1:
    print("RESULT: One page's content is a subset of the other - NEAR DUPLICATE!")
else:
    # Calculate similarity
    words1 = set(t1.split())
    words2 = set(t2.split())
    overlap = len(words1 & words2) / len(words1 | words2) * 100
    print(f"RESULT: Content similarity: {overlap:.1f}%")
    if overlap > 80:
        print("  -> HIGH similarity - likely DUPLICATE content")
