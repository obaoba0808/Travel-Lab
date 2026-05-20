import re

# Check tokyo-5days.html structure
with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all H2 tags (section headers in articles)
h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL)
h2s_clean = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
print("=== H2 Headers in tokyo-5days.html ===")
for i, h in enumerate(h2s_clean[:15]):
    print(f"  {i+1}. {h}")

# Find all <p> tags with meaningful content (not empty)
paras = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
paras_clean = [re.sub(r'<[^>]+>', '', p).strip() for p in paras if re.sub(r'<[^>]+>', '', p).strip()]
print(f"\n=== Paragraph count: {len(paras_clean)} ===")
for i, p in enumerate(paras_clean[:5]):
    print(f"  [{i+1}] {p[:80]}...")
print(f"  ... ({len(paras_clean)} total paragraphs)")

# Count Chinese chars in all paragraphs
all_text = ' '.join(paras_clean)
chinese = len(re.findall(r'[\u4e00-\u9fff]', all_text))
print(f"\n=== Chinese chars in paragraphs: {chinese} ===")

# Also check what's inside <article> tag
article_match = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
if article_match:
    art = article_match.group(1)
    art_text = re.sub(r'<[^>]+>', ' ', art)
    art_text = re.sub(r'\s+', ' ', art_text).strip()
    art_chinese = len(re.findall(r'[\u4e00-\u9fff]', art_text))
    print(f"\n=== Inside <article> tag: {art_chinese} Chinese chars ===")
    print(f"  Preview: {art_text[:200]}...")
else:
    print("\n=== No <article> tag found ===")
