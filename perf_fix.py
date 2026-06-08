"""Performance fix for golightly.fun - fix all PageSpeed issues."""
import os, re, sys

sys.stdout.reconfigure(encoding="utf-8")

fix_count = 0
fixed_files = []

for f in sorted(os.listdir(".")):
    if not f.endswith(".html"):
        continue
    
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    original = c
    
    # FIX 1: Add media="print" to Google Fonts to make it non-render-blocking
    # Then use JS to enable it on load
    old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">'
    new_fonts = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet"></noscript>'''
    
    if old_fonts in c:
        c = c.replace(old_fonts, new_fonts)
        print("  [FIX 1] Fonts non-render-blocking: " + f)
    
    # FIX 2: Add async to GA4 gtag if missing
    # Already has async, skip
    
    # FIX 3: Ensure monetization.js has defer
    if 'src="js/monetization.js"' in c and 'defer' not in c.split('src="js/monetization.js"')[0].split('<script')[-1]:
        c = c.replace('src="js/monetization.js"', 'src="js/monetization.js" defer')
        print("  [FIX 3] Added defer to monetization.js: " + f)
    
    if c != original:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(c)
        fix_count += 1
        fixed_files.append(f)

print("\nFixed " + str(fix_count) + " files")
