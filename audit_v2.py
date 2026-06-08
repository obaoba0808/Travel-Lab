"""Fix audit script: read files properly as UTF-8, fix E-E-A-T."""
import re, os

BASE = "https://golightly.fun/"

def audit_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    fname = os.path.basename(path)
    ok = []
    issues = []

    # Title
    t = re.search(r"<title>(.*?)</title>", content)
    title = t.group(1).strip() if t else "(missing)"
    if len(title) < 15:
        issues.append(f"title_short: {title[:60]}")
    elif "均在路上" not in title and "Travel Lab" not in title:
        issues.append(f"title_no_brand: {title[:60]}")
    else:
        ok.append("title")

    # Meta description
    d = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
    desc = d.group(1) if d else ""
    if not desc:
        issues.append("no_meta_desc")
    elif len(desc) < 50:
        issues.append(f"desc_short:{len(desc)}ch")
    else:
        ok.append("meta_desc")

    # Canonical
    c = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', content)
    if c and BASE in c.group(1):
        ok.append("canonical")
    elif c:
        issues.append(f"canonical_bad:{c.group(1)[:60]}")
    else:
        issues.append("no_canonical")

    # OG
    has_og = all([
        re.search(r'<meta\s+property="og:title"\s+content="[^"]+"', content),
        re.search(r'<meta\s+property="og:description"\s+content="[^"]+"', content),
        re.search(r'<meta\s+property="og:image"\s+content="[^"]+"', content),
        re.search(r'<meta\s+property="og:url"\s+content="[^"]+"', content),
    ])
    if has_og:
        ok.append("og")
    else:
        issues.append("og_incomplete")

    # Twitter Card
    if 'name="twitter:card"' in content:
        ok.append("twitter")
    else:
        issues.append("no_twitter")

    # JSON-LD
    ld = re.findall(r'"@type"\s*:\s*"([^"]+)"', content)
    if ld:
        ok.append("jsonld")
    else:
        issues.append("no_jsonld")

    # Images alt
    imgs = re.findall(r"<img[^>]+>", content)
    bad_imgs = [i for i in imgs if 'alt=' not in i]
    if bad_imgs and len(imgs) > 3:
        issues.append(f"imgs_no_alt:{len(bad_imgs)}/{len(imgs)}")
    elif imgs:
        ok.append("imgs")
    else:
        ok.append("no_imgs")

    # hreflang
    if "hreflang" in content:
        ok.append("hreflang")
    else:
        issues.append("no_hreflang")

    # Author / E-E-A-T
    if any(x in content for x in ['rel="author"', 'itemprop="author"', 'class="author"', 'class="author-line"']):
        ok.append("author")
    else:
        issues.append("no_author")

    return {"file": fname, "ok": ok, "issues": issues, "title": title[:70]}


results = []
for f in sorted(os.listdir(".")):
    if f.endswith(".html") and f not in ["404.html", "_live_index.html"]:
        results.append(audit_file(f))

results.sort(key=lambda x: len(x["issues"]), reverse=True)

print(f"{'File':<35} {'Issues':<5} {'Details'}")
print("-" * 100)
for r in results:
    print(f"{r['file']:<35} {len(r['issues']):<5} {', '.join(r['issues'])[:55]}")

print()
print("=== FULLY CLEAN ===")
clean = [r for r in results if not r["issues"]]
print(f"  {len(clean)} / {len(results)} files")
for r in clean:
    print(f"  - {r['file']}")

print()
print("=== NEEDS WORK ===")
needs = [r for r in results if r["issues"]]
for r in needs:
    print(f"\n  {r['file']}:")
    for iss in r["issues"]:
        print(f"    - {iss}")