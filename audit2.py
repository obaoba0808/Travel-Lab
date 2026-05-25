import re, os
BASE = "https://golightly.fun/"

need_canonical = []
need_og = []
need_jsonld = []
need_twitter = []
good = []

for f in sorted(os.listdir(".")):
    if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
        continue
    with open(f, "r", encoding="utf-8", errors="replace") as fh:
        c = fh.read()

    issues = []
    if 'rel="canonical"' not in c:
        issues.append("no_canonical")
    if "og:title" not in c:
        issues.append("no_og")
    if "name=" in c and 'name="twitter:card"' not in c:
        issues.append("no_twitter")
    if '"@type"' not in c:
        issues.append("no_jsonld")

    if not issues:
        good.append(f)
    else:
        print(f"  {f}: {', '.join(issues)}")

print(f"\nFully clean ({len(good)} files): {', '.join(good)}")