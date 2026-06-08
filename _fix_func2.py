# -*- coding: utf-8 -*-
import re

with open('restructure_travel_v3.py', 'r', encoding='utf-8') as f:
    c = f.read()

new_func = '''def find_topbar_end(content):
    """Find where topbar ends. Try multiple patterns."""
    body_idx = content.find("<body")
    if body_idx < 0:
        return -1

    # Pattern 1: standard topbar with tagline
    marker = "\u7528\u6700\u5c11\u9810\u7b97\uff0c\u8d70\u6700\u591a\u5730\u65b9"
    idx = content.find(marker, body_idx)
    if idx >= 0:
        pos = idx + len(marker)
        divs_found = 0
        while divs_found < 3:
            next_div = content.find("</div>", pos)
            if next_div < 0:
                return -1
            divs_found += 1
            pos = next_div + 6
        return pos

    # Pattern 2: any </nav> after <body
    nav_end = content.find("</nav>", body_idx)
    if nav_end >= 0:
        pos = nav_end + 6
        return pos

    return -1'''

# Replace everything from "def find_topbar_end" to the next "def "
old_pattern = r'def find_topbar_end\(content\):.*?(?=\ndef find_existing)'
m = re.search(old_pattern, c, re.DOTALL)
if m:
    print(f"Found old function at {m.start()}-{m.end()}")
    c = c[:m.start()] + new_func + '\n\n' + c[m.end():]
    with open('restructure_travel_v3.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced successfully")
else:
    print("ERROR: pattern not found")
