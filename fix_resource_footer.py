"""Fix 3 resource pages: add social links to simple footer."""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

FB_URL = "https://www.facebook.com/profile.php?id=61590076012361"
LINE_URL = "https://line.me/ti/g/NbNGnW4Eh6"

SOCIAL = (
    '  <div style="margin-top:12px;font-size:14px;">\n'
    '    <a href="' + FB_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;margin-right:16px;text-decoration:none;">\n'
    '      📘 Facebook 粉專</a>\n'
    '    <a href="' + LINE_URL + '" target="_blank" rel="noopener" '
    'style="color:inherit;text-decoration:none;">\n'
    '      💬 LINE 群組</a>\n'
    '  </div>\n'
)

FILES = [
    "korea-budget-travel-guide.html",
    "seasia-budget-travel-guide.html",
    "taiwan-travel-guide.html",
]

for fname in FILES:
    if not os.path.exists(fname):
        print(f"  NOT FOUND: {fname}")
        continue
    with open(fname, "r", encoding="utf-8") as fh:
        c = fh.read()

    if FB_URL in c:
        print(f"  SKIP (FB exists): {fname}")
        continue

    # Insert before </footer>
    idx = c.find("</footer>")
    if idx < 0:
        print(f"  WARN (no </footer>): {fname}")
        continue

    new_c = c[:idx] + SOCIAL + c[idx:]

    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(new_c)
    print(f"  FIXED: {fname}")

print("\nDone.")