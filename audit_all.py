import os, re

BASE = "https://golightly.fun/"

def audit_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    filename = os.path.basename(path)
    issues = []
    ok = []

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
        issues.append(f"desc_short: {len(desc)}chars")
    else:
        ok.append("meta_desc")

    # Canonical
    if 'rel="canonical"' in content:
        c = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', content)
        if c and BASE in c.group(1):
            ok.append("canonical")
        else:
            issues.append(f"canonical_bad: {c.group(1) if c else 'found'}")
    else:
        issues.append("no_canonical")

    # OG
    has_og = all(f'in content' for f in [
        re.search(r'<meta\s+property="og:title"\s+content="', content),
        re.search(r'<meta\s+property="og:description"\s+content="', content),
        re.search(r'<meta\s+property="og:image"\s+content="', content),
        re.search(r'<meta\s+property="og:url"\s+content="', content),
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
    ld_types = re.findall(r'@type"\s*:\s*"([^"]+)"', content)
    if ld_types:
        ok.append(f"jsonld:{','.join(set(ld_types))}")
    else:
        issues.append("no_jsonld")

    # Alt text on images
    imgs = re.findall(r'<img[^>]+>', content)
    imgs_no_alt = [i for i in imgs if 'alt=' not in i]
    if imgs_no_alt and len(imgs) > 3:
        issues.append(f"imgs_no_alt:{len(imgs_no_alt)}/{len(imgs)}")
    elif imgs:
        ok.append(f"imgs_ok:{len(imgs)}")
    else:
        ok.append("no_imgs")

    # hreflang
    if 'hreflang' in content:
        ok.append("hreflang")
    else:
        issues.append("no_hreflang")

    # Author / E-E-A-T
    if any(k in content for k in ['rel="author"', 'itemprop="author"', 'class="author"']):
        ok.append("author")
    else:
        issues.append("no_author")

    return {
        "file": filename,
        "ok": ok,
        "issues": issues,
        "title": title[:70]
    }

results = []
for f in sorted(os.listdir(".")):
    if f.endswith(".html"):
        r = audit_file(f)
        results.append(r)

# Sort by issue count
results.sort(key=lambda x: len(x["issues"]), reverse=True)

# Print summary
print(f"{'File':<35} {'Issues':<5} {'Issue Details'}")
print("-" * 100)
for r in results:
    issue_str = ", ".join(r["issues"])
    print(f"{r['file']:<35} {len(r['issues']):<5} {issue_str[:60]}")

print()
print("=== CRITICAL ISSUES ===")
crit = [r for r in results if len(r["issues"]) >= 3]
for r in crit:
    print(f"\n{r['file']}:")
    for iss in r["issues"]:
        print(f"  - {iss}")