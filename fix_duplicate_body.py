#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove duplicate <body> tags from all HTML files in travel-lab."""

import os
import re

HTML_DIR = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Match <body> with or without attributes: <body>, <body class="x">, etc.
    body_tags = list(re.finditer(r'<body[^>]*>', content))

    if len(body_tags) <= 1:
        return False  # No duplicate, skip

    # Keep first <body>, remove the rest (work from end to preserve indices)
    for match in reversed(body_tags[1:]):
        start = match.start()
        end = match.end()
        content = content[:start] + content[end:]

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    files = [f for f in os.listdir(HTML_DIR) if f.endswith('.html')]
    fixed = []
    for fname in sorted(files):
        fpath = os.path.join(HTML_DIR, fname)
        if fix_file(fpath):
            fixed.append(fname)

    if fixed:
        print("[OK] Fixed duplicate <body> in %d files:" % len(fixed))
        for f in fixed:
            print("  - %s" % f)
    else:
        print("[i] No duplicate <body> tags found.")

if __name__ == '__main__':
    main()
