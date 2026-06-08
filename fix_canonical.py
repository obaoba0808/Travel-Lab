import re, sys
sys.stdout.reconfigure(encoding="utf-8")

with open("contact.html", "r", encoding="utf-8") as f:
    c = f.read()

# Add canonical after robots meta
canonical_tag = '<link rel="canonical" href="https://golightly.fun/contact.html">'
c = re.sub(r'(<meta\s+name="robots"[^>]*/?>)', r'\1\n' + canonical_tag, c, count=1)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(c)

# Verify
with open("contact.html", "r", encoding="utf-8") as f:
    v = f.read()
print(f"canonical present: {'canonical' in v}")
print(f"author-line present: {'author-line' in v}")
print(f"hreflang present: {'hreflang' in v}")