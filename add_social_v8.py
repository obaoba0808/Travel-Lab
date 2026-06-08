#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Facebook + LINE social links to footer-bottom of all HTML pages."""
import os
import sys
import re

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

updated = 0
skipped = 0

for fname in sorted(os.listdir(".")):
    if not fname.endswith(".html"):
        continue
    if fname in ("404.html", "_live_index.html"):
        continue

    fpath = os.path.join(".", fname)
    with open(fpath, "r", encoding="utf-8") as fh:
        content = fh.read()

    if FB_URL in content:
        print("  SKIP (FB exists): " + fname)
        skipped += 1
        continue

    # Find: closing </div> of footer-bottom, right before </footer>
    # Pattern: footer-bottom div ... </div> \n </footer>
    # We insert social block BEFORE the </div> that closes footer-bottom
    footer_end = content.find("</footer>")
    if footer_end < 0:
        print("  WARN (no </footer>): " + fname)
        skipped += 1
        continue

    # Find the last </div> before </footer> (this closes footer-bottom)
    last_div_pos = content.rfind("</div>", 0, footer_end)
    if last_div_pos < 0:
        print("  WARN (no </div>): " + fname)
        skipped += 1
        continue

    # Insert social block before that </div>
    new_content = content[:last_div_pos] + "\n" + SOCIAL_BLOCK + "\n" + content[last_div_pos:]

    with open(fpath, "w", encoding="utf-8") as fh:
        fh.write(new_content)

    print("  ADDED: " + fname)
    updated += 1

print("")
print("Total updated: " + str(updated) + " files")
print("Total skipped: " + str(skipped) + " files")
