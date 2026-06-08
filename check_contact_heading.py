import re, sys
sys.stdout.reconfigure(encoding="utf-8")

with open("contact.html", "r", encoding="utf-8") as fh:
    c = fh.read()

for tag in [r"<h1", r"<h2", r"<h3", r"class=", r"id=", r"<main"]:
    m = re.search(tag, c)
    if m:
        print(f"Found '{tag}': {repr(c[m.start():m.start()+100])}")
    else:
        print(f"NOT found: {tag}")