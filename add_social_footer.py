"""Add Facebook + LINE social links to footer-bottom of all HTML pages."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

FB_URL = "https://www.facebook.com/profile.php?id=61590076012361"
LINE_URL = "https://line.me/ti/g/NbNGnW4Eh6"

SOCIAL_HTML = f'''    <div style="margin-top:8px;">
      <a href="{FB_URL}" target="_blank" rel="noopener" style="color:inherit;margin-right:16px;text-decoration:none;">📘 Facebook</a>
      <a href="{LINE_URL}" target="_blank" rel="noopener" style="color:inherit;text-decoration:none;">💬 LINE 群組</a>
    </div>'''

count = 0
for f in sorted(os.listdir(".")):
    if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
        continue
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()

    # Skip if already has this Facebook URL
    if FB_URL in c:
        print(f"  SKIP (FB exists): {f}")
        continue

    # Find footer-bottom div and add social links before </div> of footer-bottom
    # Pattern: <div class="footer-bottom"> ... </div> (the last </div>)
    fb = re.search(r'<div class="footer-bottom">', c, re.IGNORECASE)
    if not fb:
        print(f"  WARN (no footer-bottom): {f}")
        continue

    # Find the closing </div> of footer-bottom
    # Insert before the closing </div> of footer-bottom
    # Strategy: find the footer-bottom div, then find the last </div> before </footer>
    footer_start = fb.start()
    footer_end = c.find("</footer>", footer_start)
    if footer_end < 0:
        print(f"  WARN (no </footer>): {f}")
        continue

    # Find the last </div> before </footer> (this closes footer-bottom)
    # Actually, let me just insert before the footer-bottom's closing tags
    # The structure is: <div class="footer-bottom"> ... <p>...</p> <div>...</div> </div>
    # I want to insert BEFORE the final </div> of footer-bottom

    # Simpler: insert after the legal links div inside footer-bottom
    # Find: <div style="margin-top:8px;...">...</div> followed by </div> (closing footer-bottom)
    # Actually, let me just add after the existing footer-bottom content

    # Find: the line with footer-bottom's inner <div> with legal links
    # And add social links after it

    # Simple approach: find the closing </div> of "footer-bottom" section
    # Insert social HTML before the last </div> inside footer-bottom

    # Let me use a simpler pattern: insert before </div>\n  </footer>
    pattern = r'(  </div>\n  <div class="footer-bottom">.*?)(</div>\n        </footer>)'
    # Actually this is getting complex. Let me use a simpler string replacement.

    # The footer-bottom typically looks like:
    #   <div class="footer-bottom">
    #     <p>© 2026 ...</p>
    #     <div style="margin-top:8px;">...</div>
    #   </div>
    # I want to add social links after the legal links div.

    # Let me just append to the footer-bottom content
    target = '    </div>\n        </footer>'
    replacement = '    </div>\n' + SOCIAL_HTML + '\n        </footer>'
    new_c = c.replace(target, replacement, 1)

    if new_c == c:
        # Try alternate pattern
        # Some files may have different indentation
        target2 = '  </div>\n        </footer>'
        replacement2 = '  </div>\n' + SOCIAL_HTML + '\n        </footer>'
        new_c2 = c.replace(target2, replacement2, 1)
        if new_c2 == c:
            print(f"  WARN (pattern not matched): {f}")
            continue
        new_c = new_c2

    with open(f, "w", encoding="utf-8") as fh:
        fh.write(new_c)
    count += 1
    print(f"  ADDED: {f}")

print(f"\nTotal updated: {count} files")