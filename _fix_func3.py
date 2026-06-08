# -*- coding: utf-8 -*-
import re

with open('restructure_travel_v3.py', 'r', encoding='utf-8') as f:
    c = f.read()

new_func = r'''def find_topbar_end(content):
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

    # Pattern 2: any </nav> after <body>
    nav_end = content.find("</nav>", body_idx)
    if nav_end >= 0:
        return nav_end + 6

    # Pattern 3: pages with unclosed nav — find </div>\n    </div>\n<section or </div>\n      </div>\n<section
    hero_match = re.search(r'</div>\s*</div>\s*(<section class="hero)', content[body_idx:])
    if hero_match:
        # Find the two </div> positions
        start = body_idx
        # Find the first </div> before <section
        section_start = body_idx + hero_match.start(1)
        # Go back to find </div></div> before <section
        before_section = content[section_start-60:section_start]
        # Return position right after the last </div> before <section
        last_div_pos = content.rfind("</div>", body_idx, section_start)
        if last_div_pos >= 0:
            return last_div_pos + 6

    return -1'''

old_pattern = r'def find_topbar_end\(content\):.*?(?=\ndef find_existing)'
m = re.search(old_pattern, c, re.DOTALL)
if m:
    c = c[:m.start()] + new_func + '\n\n' + c[m.end():]
    with open('restructure_travel_v3.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Replaced function at {m.start()}-{m.end()}")
else:
    print("ERROR: pattern not found")
