"""Fix contact.html properly: CP950 body decode + add hreflang + author byline."""
import re, sys, os

sys.stdout.reconfigure(encoding="utf-8")

# Decode body as CP950, head as UTF-8
with open("contact.html", "rb") as f:
    raw = f.read()

body_start = raw.find(b"<body>")
head_bytes = raw[:body_start]
body_bytes = raw[body_start:]

head_text = head_bytes.decode("utf-8", errors="replace")
body_text = body_bytes.decode("cp950", errors="replace")

full = head_text + body_text

# Fix canonical (currently wrong: points to seoul-food.html)
# Remove bad canonical from body
full = re.sub(r'<link\s+rel="canonical"\s+href="https://golightly\.fun/seoul-food\.html"\s*/?>', '', full)

# Add hreflang block (if not present)
if "hreflang" not in full:
    block = """<link rel="alternate" hreflang="zh-Hant" href="https://golightly.fun/contact.html">
<link rel="alternate" hreflang="zh-TW" href="https://golightly.fun/contact.html">
<link rel="alternate" hreflang="x-default" href="https://golightly.fun/contact.html">"""
    full = re.sub(r'(<meta\s+name="robots"[^>]*/?>)', r'\1\n' + block, full, count=1)

# Add author byline after </h1> (handle potential CP950 corruption in surrounding text)
AUTHOR = '<p class="author-line" style="color:#888;font-size:13px;margin:8px 0 16px;">📝 均在路上 Travel Lab 編輯部 · 更新於 2026 年</p>'

# Try raw bytes approach: find the </h1> sequence in CP950 body
h1_close_cp950 = b"</h1>"
idx = body_text.find("</h1>")
if idx >= 0:
    insert_pos = len(head_text) + idx + len("</h1>")
    full = full[:insert_pos] + "\n" + AUTHOR + full[insert_pos:]
    print(f"  Inserted author at position {insert_pos}")
else:
    # Find the bytes position directly
    h1_close_bytes = b"</h1>"
    byte_pos = raw.find(h1_close_bytes)
    if byte_pos >= 0:
        # Reconstruct with author
        before = raw[:byte_pos + len(h1_close_bytes)]
        after = raw[byte_pos + len(h1_close_bytes):]
        body_decoded = after.decode("cp950")
        full = head_text + before[body_start:].decode("utf-8", errors="replace") + "\n" + AUTHOR + body_decoded
        print(f"  Inserted author via bytes at {byte_pos}")

# Write as UTF-8
with open("contact.html", "w", encoding="utf-8") as f:
    f.write(full)
print("  Written contact.html (UTF-8)")

# Verify
with open("contact.html", "r", encoding="utf-8") as f:
    v = f.read()
has_author = 'author-line' in v
has_hreflang = 'hreflang' in v
print(f"\nVerify: author-line={has_author}, hreflang={has_hreflang}")
if has_author:
    t = re.search(r"<title>(.*?)</title>", v)
    print(f"  Title: {t.group(1).strip() if t else '?'}")
    print(f"  OK - contact.html fully fixed!")
else:
    print("  WARNING: author not added")