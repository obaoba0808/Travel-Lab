"""Add Facebook + LINE social links to footer-bottom of all HTML pages."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

FB_URL = "https://www.facebook.com/profile.php?id=61590076012361"
LINE_URL = "https://line.me/ti/g/NbNGnW4Eh6"

SOCIAL_BLOCK = (
    '    <div style="margin-top:12px;font-size:14px;">\n'
    '      <a href="' + FB_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;margin-right:16px;text-decoration:none;">\n'
    '        \xf0\x9f\x93\x98 Facebook \xe7\xb2\x89\xe5\xb0\x88</a>\n'
    '      <a href="' + LINE_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;text-decoration:none;">\n'
    '        \xf0\x9f\x92\xac LINE \xe7\xbe\xa4\xe7\xb5\x84</a>\n'
    '    </div>'
)

# Write social block as proper UTF-8
SOCIAL_BLOCK = (
    '    <div style="margin-top:12px;font-size:14px;">\n'
    '      <a href="' + FB_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;margin-right:16px;text-decoration:none;">\n'
    '        📘 Facebook 粉專</a>\n'
    '      <a href="' + LINE_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;text-decoration:none;">\n'
    '        💬 LINE 群組</a>\n'
    '    </div>'
)

count = 0
for fname in sorted(os.listdir(".")):
    if not fname.endswith(".html") or fname in ["404.html", "_live_index.html"]:
        continue
    with open(fname, "r", encoding="utf-8") as fh:
        c = fh.read()

    if FB_URL in c:
        print(f"  SKIP (FB exists): {fname}")
        continue

    # Find: closing </div> of footer-bottom, right before </footer>
    # Pattern: footer-bottom div ... </div> \n\n </footer>
    pat = re.compile(
        r'(<div class="footer-bottom">.*?)(\n  </div>\n        </footer>)',
        re.DOTALL
    )
    m = pat.search(c)
    if not m:
        # Try alternate whitespace
        pat2 = re.compile(
            r'(<div class="footer-bottom">.*?)(\n  </div>\n</footer>)',
            re.DOTALL
        )
        m2 = pat2.search(c)
        if not m2:
            print(f"  WARN (pattern mismatch): {fname}")
            continue
        new_c = c[:m2.start(2)] + "\n" + SOCIAL_BLOCK + c[m2.start(2):]
    else:
        new_c = c[:m.start(2)] + "\n" + SOCIAL_BLOCK + c[m.start(2):]

    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(new_c)
    count += 1
    print(f"  ADDED: {fname}")

print(f"\nTotal updated: {count} files")
