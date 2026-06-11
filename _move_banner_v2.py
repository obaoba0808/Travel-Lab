"""
Move <!-- CHARTER BANNER --> block INSIDE three-col-wrapper for all pages.
Strategy: find <!-- CHARTER BANNER --> ... <div class="three-col-wrapper">,
move the banner block inside the wrapper after its opening <div>.
"""
import os, re

pages = [f for f in os.listdir('.') if f.endswith('.html') and f != 'tokyo-5days.html']

for fname in sorted(pages):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find the whole charter banner block: comment + wrapping div + a+img + closing div
    # Pattern: <!-- CHARTER BANNER --> ... <div class="three-col-wrapper">
    banner_pat = re.compile(
        r'(<!--\s*CHARTER\s*BANNER\s*-->\s*'
        r'<div[^>]*max-width:\s*900px[^>]*>\s*'
        r'<a[^>]*>.*?</a>\s*'
        r'</div>)',
        re.DOTALL
    )
    m_banner = banner_pat.search(content)
    tcw_open = re.search(r'<div class="three-col-wrapper">', content)

    if not m_banner or not tcw_open:
        continue

    banner_start = m_banner.start()
    banner_end = m_banner.end()
    tcw_pos = tcw_open.start()

    # Only fix if banner is BEFORE three-col-wrapper
    if banner_start >= tcw_pos:
        continue  # already inside or after

    # Extract banner block
    banner_block = m_banner.group(1)

    # Build new content: remove banner from original position
    new_content = content[:banner_start] + content[banner_end:]

    # Find three-col-wrapper opening in the new content (no banner now)
    tcw_open2 = re.search(r'<div class="three-col-wrapper">', new_content)
    if not tcw_open2:
        continue
    insert_after = tcw_open2.end()

    # Insert banner right after <div class="three-col-wrapper">
    new_content = new_content[:insert_after] + '\n' + banner_block + new_content[insert_after:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'Fixed: {fname}')

print('Done.')