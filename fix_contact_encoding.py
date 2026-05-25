"""Fix contact.html CP950 body + add hreflang + author byline."""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

# Read the file as raw bytes and split into head (UTF-8) and body (CP950)
with open("contact.html", "rb") as f:
    raw = f.read()

body_start = raw.find(b"<body>")
head_bytes = raw[:body_start]
body_bytes = raw[body_start:]

try:
    head_text = head_bytes.decode("utf-8")
except:
    head_text = head_bytes.decode("cp950", errors="replace")

try:
    body_text = body_bytes.decode("cp950")
except:
    body_text = body_bytes.decode("utf-8", errors="replace")

full = head_text + body_text

# Check if already fixed
if 'class="author-line"' in full:
    print("contact.html: already has author-line, skipping")

    # Still add hreflang if missing
    if "hreflang" not in full:
        block = """<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/contact.html">
<link rel="alternate" hreflang="zh-TW" href="https://golightly.fun/contact.html">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/contact.html">"""
        full = re.sub(
            r'(<meta\s+name="robots"[^>]*/?>)',
            r'\1\n' + block,
            full,
            count=1
        )
        with open("contact.html", "w", encoding="utf-8") as f:
            f.write(full)
        print("  Added hreflang")
    else:
        print("  Already has hreflang")
else:
    # Fix body encoding first (already done from CP950)
    # Now add author byline after </h1>
    author_html = '<p class="author-line" style="color:#888;font-size:13px;margin:8px 0 16px;">📝 均在路上 Travel Lab 編輯部 · 更新於 2026 年</p>'

    if re.search(r"</h1>", full):
        new_full = re.sub(r"(</h1>)", r"\1\n" + author_html, full, count=1)
        print("  Added author after </h1>")
    else:
        new_full = full
        print("  WARNING: no </h1> found")

    # Add hreflang
    block = """<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/contact.html">
<link rel="alternate" hreflang="zh-TW" href="https://golightly.fun/contact.html">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/contact.html">"""
    new_full = re.sub(
        r'(<meta\s+name="robots"[^>]*/?>)',
        r'\1\n' + block,
        new_full,
        count=1
    )
    print("  Added hreflang")

    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(new_full)
    print("  Written to contact.html")

# Verify
with open("contact.html", "r", encoding="utf-8") as f:
    verify = f.read()
has_author = 'author-line' in verify
has_hreflang = 'hreflang' in verify
print(f"\nVerification: author-line={has_author}, hreflang={has_hreflang}")
if has_author:
    # Print title from head section
    head_end = verify.find("</head>")
    head = verify[:head_end]
    t = re.search(r"<title>(.*?)</title>", head)
    print(f"  Title: {t.group(1).strip() if t else '?'}")
    # Print author line
    m = re.search(r'<p class="author-line"[^>]+>', verify)
    print(f"  Author: {m.group(0)[:80] if m else '?'}")