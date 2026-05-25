"""Add Facebook + LINE social links to footer-bottom of all HTML pages."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

FB_URL = "https://www.facebook.com/profile.php?id=61590076012361"
LINE_URL = "https://line.me/ti/g/NbNGnW4Eh6"

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

    # Strategy: find the closing </div> of footer-bottom, insert social block before it
    # footer-bottom ends right before </footer>
    footer_bottom_start = c.find('<div class="footer-bottom">')
    if footer_bottom_start < 0:
        print(f"  WARN (no footer-bottom): {fname}")
        continue

    footer_end = c.find("</footer>", footer_bottom_start)
    if footer_end < 0:
        print(f"  WARN (no </footer>): {fname}")
        continue

    # Find the </div> that closes footer-bottom (right before </footer>)
    # We need to find the correct closing </div> for footer-bottom
    # Simple heuristic: find the last </div> before </footer>
    last_div_before_footer = c.rfind("</div>", footer_bottom_start, footer_end)
    if last_div_before_footer < 0:
        print(f"  WARN (no closing </div>): {fname}")
        continue

    # Insert social block before that </div>
    new_c = c[:last_div_before_footer] + "\n" + SOCIAL_BLOCK + "\n" + c[last_div_before_footer:]

    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(new_c)
    count += 1
    print(f"  ADDED: {fname}")

print(f"\nTotal updated: {count} files")
