import re

for f in ["korea-budget-travel-guide.html", "seasia-budget-travel-guide.html", "taiwan-travel-guide.html"]:
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    d = re.search(r'<meta name="description" content="([^"]+)"', c)
    desc = d.group(1) if d else "MISSING"
    t = re.search(r"<title>(.*?)</title>", c)
    title = t.group(1).strip() if t else "?"
    print(f"FILE: {f}")
    print(f"  DESC ({len(desc)}ch): {desc}")
    print(f"  TITLE: {title}")
    print()