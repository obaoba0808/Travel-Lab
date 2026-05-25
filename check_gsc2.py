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
        # extract content value
        m = re.search(r'google-site-verification[^>]*content=["\']([^"\']+)["\']', c, re.I)
        if m:
            found.append((f, m.group(1)))
        else:
            found.append((f, "FOUND_BUT_NO_CONTENT"))
    else:
        not_found.append(f)

print("=== PAGES WITH GSC VERIFICATION TAG ===")
for f, v in found:
    print("  " + f + ": " + v[:50])

print()
print("=== PAGES WITHOUT GSC VERIFICATION TAG ===")
for f in not_found:
    print("  " + f)

print()
print("Total: " + str(len(found)) + " with tag, " + str(len(not_found)) + " without")
