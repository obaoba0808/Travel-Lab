"""Fix render-blocking CSS - make style.css load asynchronously."""
import os, re, sys

sys.stdout.reconfigure(encoding="utf-8")

# For index.html specifically - the main page that PageSpeed tests
with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# FIX: Make main stylesheet non-render-blocking
# Replace blocking stylesheet with preload + async load pattern
old_css = '<link rel="stylesheet" href="style.css">'
new_css = '''<link rel="preload" href="style.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="style.css"></noscript>'''

if old_css in c:
    c = c.replace(old_css, new_css)
    print("Made style.css non-render-blocking on index.html")
else:
    print("style.css pattern not found, checking alternatives...")
    # Check what's actually there
    for m in re.finditer(r'<link[^>]*stylesheet[^>]*>', c):
        print("  Found: " + m.group(0)[:100])

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Done!")
