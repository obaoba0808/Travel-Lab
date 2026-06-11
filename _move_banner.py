"""
Move charter-banner INSIDE three-col-wrapper for all pages.
tokyo-5days.html is already correct (INSIDE), skip it.
"""
import os, re

pages = [f for f in os.listdir('.') if f.endswith('.html') and f != 'tokyo-5days.html']

for fname in sorted(pages):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find banner <a>...</a> (charter-banner)
    banner_match = re.search(
        r'(<a [^>]*charter-banner[^>]*>.*?</a>)',
        content, re.DOTALL
    )
    if not banner_match:
        continue

    banner_html = banner_match.group(1)
    banner_start = banner_match.start()
    banner_end = banner_match.end()

    # Only fix if banner is OUTSIDE three-col-wrapper
    tcw_pos = content.find('three-col-wrapper')
    if tcw_pos == -1 or banner_start > tcw_pos:
        continue  # already inside or no wrapper

    # Find the closing > of the three-col-wrapper opening div
    # e.g. <div class="three-col-wrapper">
    tcw_open_match = re.search(r'<div class="three-col-wrapper">', content)
    if not tcw_open_match:
        continue
    tcw_open_end = tcw_open_match.end()  # position right after ">"

    # Build new content: remove banner from original position, insert after three-col-wrapper opening
    new_content = content[:banner_start] + content[banner_end:]
    insert_pos = new_content.find('three-col-wrapper')
    # find the closing > of that same div
    tcw_open2 = re.search(r'<div class="three-col-wrapper">', new_content)
    if not tcw_open2:
        continue
    insert_after = tcw_open2.end()

    new_content = new_content[:insert_after] + '\n' + banner_html + new_content[insert_after:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'Fixed: {fname}')

print('Done.')