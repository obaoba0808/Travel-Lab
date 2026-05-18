import os
import re

html_dir = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"

count = 0
for fname in os.listdir(html_dir):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(html_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix: add defer if missing, and ensure it's present
    new_content = re.sub(
        r'<script src="js/monetization\.js"></script>',
        r'<script src="js/monetization.js" defer></script>',
        content
    )
    
    if new_content == content:
        # Already has defer or not present
        if 'monetization.js' in content and 'defer' not in content:
            print(f"  WARN: monetization.js exists but defer not added in {fname}")
        continue
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    count += 1
    print(f"  Fixed: {fname}")

print(f"\nDone! Fixed {count} files.")