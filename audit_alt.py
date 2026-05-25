"""Audit image alt tags across all HTML files."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

results = []

for f in sorted(os.listdir(".")):
    if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
        continue
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()

    imgs = re.findall(r'<img[^>]+>', c)
    if not imgs:
        continue

    no_alt = []
    short_alt = []
    good_alt = []

    for img in imgs:
        alt_m = re.search(r'alt="([^"]*)"', img)
        src_m = re.search(r'src="([^"]*)"', img)
        src = src_m.group(1) if src_m else "?"

        if not alt_m:
            no_alt.append(src.split("/")[-1][:40])
        else:
            alt = alt_m.group(1).strip()
            if len(alt) < 5:
                short_alt.append((src.split("/")[-1][:30], alt))
            else:
                good_alt.append(src.split("/")[-1][:40])

    if no_alt or short_alt:
        results.append({
            "file": f,
            "no_alt": no_alt,
            "short_alt": short_alt,
            "good_alt": good_alt,
            "total": len(imgs)
        })

print(f"{'File':<35} {'Total':>5} {'NoAlt':>5} {'Short':>5} {'Good':>5}")
print("-" * 60)
for r in results:
    print(f"{r['file']:<35} {r['total']:>5} {len(r['no_alt']):>5} {len(r['short_alt']):>5} {len(r['good_alt']):>5}")

print()
print("=== DETAILS ===")
for r in results:
    if r["no_alt"] or r["short_alt"]:
        print(f"\n{r['file']}:")
        for src in r["no_alt"]:
            print(f"  ❌ NO ALT: {src}")
        for src, alt in r["short_alt"]:
            print(f"  ⚠️  SHORT ALT ({len(alt)}ch): alt=\"{alt}\" — {src}")