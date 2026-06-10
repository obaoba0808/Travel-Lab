#!/usr/bin/env python3
"""Fix 'defer defer' to 'defer' in all HTML files."""
import re, glob, os

dir_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"
count = 0
for f in glob.glob(os.path.join(dir_path, "*.html")):
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    new = content.replace('defer defer', 'defer')
    if new != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new)
        print(f"Fixed: {os.path.basename(f)}")
        count += 1

print(f"\nTotal fixed: {count} files")