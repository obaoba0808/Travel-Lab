"""Final fix: add hreflang to resource pages, author byline to contact.html."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

HREFLANG_BLOCK = """<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/{filename}">
<link rel="alternate" hreflang="zh-TW" href="https://golightly.fun/{filename}">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/{filename}">"""

AUTHOR_HTML = '<p class="author-line" style="color:#888;font-size:13px;margin:8px 0 16px;">📝 均在路上 Travel Lab 編輯部 · 更新於 2026 年</p>'

def add_hreflang(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    if "hreflang" in c:
        return False
    fname = os.path.basename(path)
    block = HREFLANG_BLOCK.format(filename=fname)
    # Insert after <meta name="robots"
    new_c = re.sub(
        r'(<meta\s+name="robots"[^>]*/?>)',
        r'\1\n' + block,
        c,
        count=1
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_c)
    return True


def add_author_to_contact(path):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    if "author-line" in c:
        return False
    # Find </h1> or <h2>
    if re.search(r"</h1>", c):
        new_c = re.sub(r"(</h1>)", rf"\1\n{AUTHOR_HTML}", c, count=1)
    else:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_c)
    return True


# Resource pages missing hreflang
for f in ["korea-budget-travel-guide.html", "seasia-budget-travel-guide.html", "taiwan-travel-guide.html"]:
    if os.path.exists(f):
        ok = add_hreflang(f)
        print(f"{'FIXED' if ok else 'SKIP '} hreflang: {f}")

# contact.html missing author byline
if os.path.exists("contact.html"):
    ok = add_author_to_contact("contact.html")
    print(f"{'FIXED' if ok else 'SKIP '} author: contact.html")

print("Done.")