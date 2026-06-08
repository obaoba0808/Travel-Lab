# -*- coding: utf-8 -*-
import re

with open('restructure_travel_v3.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix the broken escape sequences
old = "        while pos < len(content) and content[pos] in ('\n', '\r', ' ', '\t'):\n            pos += 1"
# Check what's actually there
idx = c.find("while pos < len(content) and content[pos] in (")
if idx >= 0:
    chunk = c[idx:idx+100]
    print(f"Found at {idx}: repr={repr(chunk)}")
    # Replace with proper escapes
    new_chunk = "while pos < len(content) and content[pos] in ('\\n', '\\r', ' ', '\\t'):\n            pos += 1"
    c = c[:idx] + new_chunk + c[idx+len(chunk):]
    with open('restructure_travel_v3.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed!")
else:
    print("Not found")
