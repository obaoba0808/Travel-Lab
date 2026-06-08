"""Fix: add brand suffix to article titles + og:image for legal pages."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

BRAND = "｜均在路上 Travel Lab"

def add_brand_to_title(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    t = re.search(r"<title>(.*?)</title>", c)
    if not t:
        return False
    title = t.group(1).strip()
    if "均在路上" in title or "Travel Lab" in title:
        return False  # already has brand

    new_title = title + BRAND
    new_c = re.sub(r"<title>.*?</title>", f"<title>{new_title}</title>", c, count=1)

    # Also update og:title and twitter:title
    new_c = re.sub(
        r'(<meta\s+(?:property|name)="(?:og:title|twitter:title)"\s+content=")[^"]*(")',
        lambda m: m.group(1) + new_title + m.group(2),
        new_c
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_c)
    return True


def fix_og_image(path):
    """Add og:image if missing for disclaimer/terms pages."""
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    if 'property="og:image"' in c:
        return False
    # Use the about-hero image as fallback
    og_img_tag = '<meta property="og:image" content="https://golightly.fun/images/about-hero.webp">'
    # Insert after og:description tag
    new_c = re.sub(
        r'(<meta\s+property="og:description"\s+content="[^"]+"\s*/?>)',
        r'\1\n' + og_img_tag,
        c,
        count=1
    )
    if new_c == c:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_c)
    return True


ARTICLE_FILES = [
    "bangkok-massage.html", "esim-comparison.html", "japan-budget-guide.html",
    "jiufen.html", "korea-budget.html", "osaka-food.html", "osaka-usj.html",
    "taipei-food.html",
]

print("=== Adding brand suffix to article titles ===")
count = 0
for f in ARTICLE_FILES:
    if os.path.exists(f) and add_brand_to_title(f):
        print(f"  FIXED: {f}")
        count += 1
    else:
        print(f"  SKIP:  {f}")
print(f"  Total fixed: {count}")

print()
print("=== Fixing og:image for legal pages ===")
for f in ["disclaimer.html", "terms.html"]:
    if os.path.exists(f) and fix_og_image(f):
        print(f"  FIXED: {f}")
    else:
        print(f"  SKIP:  {f}")

print()
print("Done.")