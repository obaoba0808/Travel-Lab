"""Check footer and contact page for social links."""
import re, sys
sys.stdout.reconfigure(encoding="utf-8")

with open("contact.html", "r", encoding="utf-8") as f:
    c = f.read()

# Find footer
m = re.search(r"<footer", c, re.IGNORECASE)
if m:
    footer_start = m.start()
    print("=== Footer section (first 1000 chars) ===")
    print(c[footer_start:footer_start+1000])
else:
    print("No <footer> found")

print("\n=== All links in contact.html ===")
links = re.findall(r'href="([^"]+)"', c)
for link in links:
    if any(x in link for x in ["facebook", "line.me", "instagram", "twitter", "youtube", "social"]):
        print(f"  Social: {link}")
    elif "http" in link or link.startswith("#") or link.startswith("/"):
        pass

print("\n=== Check if facebook/line already in any html ===")
for fname in ["index.html", "contact.html", "about.html"]:
    try:
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        if "facebook" in content.lower() or "line.me" in content:
            print(f"  {fname}: has facebook/line link")
        else:
            print(f"  {fname}: NO social links")
    except:
        pass