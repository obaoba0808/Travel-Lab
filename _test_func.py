# Test the fixed function
import re

def find_topbar_end(content):
    body_idx = content.find("<body")
    if body_idx < 0:
        return -1
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
    nav_end = content.find("</nav>", body_idx)
    if nav_end >= 0:
        return nav_end + 6
    hero_match = re.search(r'</div>\s*</div>\s*(<section class="hero)', content[body_idx:])
    if hero_match:
        section_start = body_idx + hero_match.start(1)
        last_div_pos = content.rfind("</div>", body_idx, section_start)
        if last_div_pos >= 0:
            return last_div_pos + 6
    return -1

for f in ['angkor-wat-2days.html','kualalumpur-3days.html','singapore-3days.html','bangkok-4days.html','seoul-5days.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    end = find_topbar_end(c)
    print(f"{f}: topbar_end={end}")
    if end > 0:
        print(f"  after topbar: [{c[end:end+80]}]")
