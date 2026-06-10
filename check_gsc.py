"""Check if GSC verification tag is present in all HTML pages."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

found = []
not_found = []

for f in sorted(os.listdir(".")):
    if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
        continue
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    if "google-site-verification" in c.lower():
        m = re.search(r'google-site-verification[^"\\']*content=["\\']([^"\\']+)["\\']', c, re.I)
        found.append((f, m.group(1) if m else "FOUND_BUT_NO_CONTENT"))
    else:
        not_found.append(f)

print("=== PAGES WITH GSC VERIFICATION TAG ===")
for f, v in found:
    print(f"  {f}: {v[:40]}")

print()
print("=== PAGES WITHOUT GSC VERIFICATION TAG ===")
for f in not_found:
    print(f"  {f}")
    
print()
print(f"Total: {len(found)} with tag, {len(not_found)} without")
