"""Add Facebook + LINE social links to footer-bottom of all HTML pages."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

FB_URL = "https://www.facebook.com/profile.php?id=61590076012361"
LINE_URL = "https://line.me/ti/g/NbNGnW4Eh6"

# Social block to insert
SOCIAL = (
    '    <div style="margin-top:12px;font-size:14px;">\n'
    '      <a href="' + FB_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;margin-right:16px;text-decoration:none;">\n'
    '        \xf0\x9f\x93\x98 Facebook \xe7\xb2\x89\xe5\xb0\x88</a>\n'
    '      <a href="' + LINE_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;text-decoration:none;">\n'
    '        \xf0\x9f\x92\xac LINE \xe7\xbe\xa4\xe7\xb5\x84</a>\n'
    '    </div>'
)

# Decode to proper UTF-8 string with emojis
SOCIAL = (
    '    <div style="margin-top:12px;font-size:14px;">\n'
    '      <a href="' + FB_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;margin-right:16px;text-decoration:none;">\n'
    '        \xf0\x9f\x93\x98 Facebook \xe7\xb2\x89\xe5\xb0\x88</a>\n'
    '      <a href="' + LINE_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;text-decoration:none;">\n'
    '        \xf0\x9f\x92\xac LINE \xe7\xbe\xa4\xe7\xb5\x84</a>\n'
    '    </div>'
)

# Write as proper UTF-8
SOCIAL = (
    '    <div style="margin-top:12px;font-size:14px;">\n'
    '      <a href="' + FB_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;margin-right:16px;text-decoration:none;">\n'
    '        \xe2\xad\x90 Facebook \xe7\xb2\x89\xe5\xb0\x88</a>\n'
    '      <a href="' + LINE_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;text-decoration:none;">\n'
    '        \xf0\x9f\x92\xac LINE \xe7\xbe\xa4\xe7\xb5\x84</a>\n'
    '    </div>'
)

# Let me just write the social block as a raw string with actual UTF-8 characters
# I'll encode it properly
social_bytes = (
    '    <div style="margin-top:12px;font-size:14px;">\n'
    '      <a href="' + FB_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;margin-right:16px;text-decoration:none;">\n'
    '        \xf0\x9f\x93\x98 Facebook \xe7\xb2\x89\xe5\xb0\x88</a>\n'
    '      <a href="' + LINE_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;text-decoration:none;">\n'
    '        \xf0\x9f\x92\xac LINE \xe7\xbe\xa4\xe7\xb5\x84</a>\n'
    '    </div>'
).encode("utf-8")

SOCIAL = social_bytes.decode("utf-8")

count = 0
for fname in sorted(os.listdir(".")):
    if not fname.endswith(".html") or fname in ["404.html", "_live_index.html"]:
        continue
    with open(fname, "r", encoding="utf-8") as fh:
        c = fh.read()
    if FB_URL in c:
        print(f"  SKIP (FB exists): {fname}")
        continue
    # Find last </div> before </footer>
    footer_end = c.find("</footer>")
    if footer_end < 0:
        print(f"  WARN (no </footer>): {fname}")
        continue
    last_div = c.rfind("</div>", 0, footer_end)
    if last_div < 0:
        print(f"  WARN (no </div>): {fname}")
        continue
    new_c = c[:last_div] + "\n" + SOCIAL + "\n" + c[last_div:]
    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(new_c)
    count += 1
    print(f"  ADDED: {fname}")

print(f"\nTotal updated: {count} files")
