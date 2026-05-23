import re
import os

# List all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != '_live_index.html']

removed_count = 0

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Check if file has trip-promo-inline
    if 'trip-promo-inline' not in content:
        continue
    
    # Find FAQ section start
    faq_match = re.search(r'<section[^>]*class="faq-section"', content)
    
    # Remove all trip-promo-inline divs
    # Pattern matches: <div class="trip-promo-inline">...</div>
    pattern = r'<div class="trip-promo-inline">.*?</div>\s*</a>\s*</div>'
    
    # Actually, let me use a simpler pattern that matches the entire div block
    # The structure is: <div class="trip-promo-inline"><a ...><img ...></a></div>
    pattern = r'<div class="trip-promo-inline">\s*<a[^>]*>\s*<img[^>]*>\s*</a>\s*</div>'
    
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Check if anything was removed
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        removed_count += 1
        print(f'[OK] Removed trip-promo-inline from: {filename}')
    else:
        # Try alternative pattern (maybe different whitespace)
        pattern2 = r'<div class="trip-promo-inline">.*?</div>'
        new_content2 = re.sub(pattern2, '', content, flags=re.DOTALL)
        if new_content2 != content:
            with open(filename, 'w', encoding='utf-8') as fp:
                fp.write(new_content2)
            removed_count += 1
            print(f'[OK] Removed trip-promo-inline from: {filename} (alt pattern)')
        else:
            print(f'[SKIP] Could not find trip-promo-inline pattern in: {filename}')

print(f'\n{"="*60}')
print(f'Total files processed: {removed_count}')
print(f'{"="*60}')
