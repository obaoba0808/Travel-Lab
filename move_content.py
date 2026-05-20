with open('japan-travel.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the new content block we inserted (between hero block and <!-- MAIN CONTENT -->)
import re

# The new content starts with <section style="max-width:900px;...>
# and ends with </section> (before <!-- MAIN CONTENT -->)
new_content_pattern = r'\n<section style="max-width:900px;margin:0 auto;padding:0 20px 40px;">.*?</section>\n'
m = re.search(new_content_pattern, c, re.S)
if not m:
    print('ERROR: Could not find the inserted content block')
else:
    new_content = m.group(0)
    # Remove the content from its current position
    c2 = c.replace(new_content, '\n', 1)
    
    # Now insert it INSIDE <main>, after the first <div class="section-divider"> (which contains the trip promo banner)
    main_start = c2.find('<main class="site-content"')
    if main_start < 0:
        print('ERROR: Could not find <main>')
    else:
        # Find the end of the section-divider (trip promo banner + h2)
        divider_end = c2.find('</div>\n  <div class="card-grid">', main_start)
        if divider_end < 0:
            # Try alternative pattern
            divider_end = c2.find('<div class="card-grid">', main_start)
        if divider_end >= 0:
            # Insert new content before card-grid
            c2 = c2[:divider_end] + new_content + '\n  ' + c2[divider_end:]
            with open('japan-travel.html', 'w', encoding='utf-8') as f:
                f.write(c2)
            print('Moved content inside <main> successfully!')
        else:
            print('ERROR: Could not find insertion point inside <main>')
