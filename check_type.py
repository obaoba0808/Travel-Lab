import re, os

articles = []
others = []

for f in sorted(os.listdir(".")):
    if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
        continue
    with open(f, "r", encoding="utf-8", errors="replace") as fh:
        c = fh.read()

    og = re.search(r"og:type.*?content=\"([^\"]+)\"", c, re.DOTALL)
    t = re.search(r"<title>(.*?)</title>", c)
    tp = og.group(1).strip() if og else "(missing)"
    title = t.group(1).strip()[:40] if t else "?"
    entry = f"{f} [{tp}] {title}"

    if tp == "article":
        articles.append(entry)
    else:
        others.append(entry)

print("ARTICLE pages:", len(articles))
for a in articles:
    print(" ", a)

print()
print("NON-ARTICLE pages:", len(others))
for o in others:
    print(" ", o)