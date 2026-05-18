import os
import re

html_dir = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"
css_link = '  <link rel="stylesheet" href="beautify-overrides.css">\n'

count = 0
for fname in os.listdir(html_dir):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(html_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'beautify-overrides.css' in content:
        print(f"  Skip (already has link): {fname}")
        continue
    # Insert after style.css link
    new_content = re.sub(
        r'(<link rel="stylesheet" href="style\.css">)',
        r'\1\n' + css_link.strip(),
        content
    )
    if new_content == content:
        print(f"  WARN: style.css link not found in {fname}")
        continue
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    count += 1
    print(f"  Updated: {fname}")

print(f"\nDone! Updated {count} files.")