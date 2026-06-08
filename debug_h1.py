"""Debug: find </h1> in raw bytes."""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("contact.html", "rb") as f:
    raw = f.read()

body_start = raw.find(b"<body>")
body_bytes = raw[body_start:]
body_text_cp950 = body_bytes.decode("cp950", errors="replace")

# Search for h1 close in both raw bytes and decoded text
h1_raw = raw.find(b"</h1>")
h1_cp950 = body_text_cp950.find("</h1>")
h1_utf8 = body_text_cp950.encode("utf-8", errors="replace").find(b"</h1>")

print(f"</h1> in raw bytes at: {h1_raw}")
print(f"</h1> in CP950 decoded body at: {h1_cp950}")
print(f"</h1> in UTF-8 re-encoded body at: {h1_utf8}")
print()

# Show context around raw position
if h1_raw > 0:
    ctx = raw[max(0, h1_raw-10):h1_raw+20]
    print(f"Context (raw): {repr(ctx)}")
    print(f"Hex: {ctx.hex()}")

# Check: is </h1> actually in body_bytes as-is?
print(f"</h1> in body_bytes: {b'</h1>' in body_bytes}")
print(f"</H1> in body_bytes: {b'</H1>' in body_bytes}")

# Show first 200 bytes of body section  
print(f"\nFirst 200 body bytes: {repr(body_bytes[:200])}")
print(f"First 200 body hex: {body_bytes[:200].hex()}")