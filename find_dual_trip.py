import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != '_live_index.html']

print(f"{'File':<30} {'Before FAQ':<20} {'After FAQ':<20}")
print("="*70)

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Find FAQ section
    faq_match = re.search(r'<section[^>]*class="faq-section"', content)
    if not faq_match:
        continue
    
    faq_start = faq_match.start()
    
    # Find end of FAQ section (next </section> after FAQ start)
    faq_end_match = re.search(r'</section>', content[faq_match.end():])
    if faq_end_match:
        faq_end = faq_match.end() + faq_end_match.start()
    else:
        faq_end = faq_match.end() + 500  # approximate
    
    # Find all trip-promo-inline or trip-dynamic-banner positions
    trip_patterns = [
        r'<div class="trip-promo-inline">',
        r'<div class="trip-dynamic-banner">',
        r'<iframe.*?trip\.com'
    ]
    
    before_faq = []
    after_faq = []
    
    for pattern in trip_patterns:
        matches = list(re.finditer(pattern, content))
        for match in matches:
            pos = match.start()
            if pos < faq_start:
                before_faq.append((pattern, pos))
            elif pos > faq_end:
                after_faq.append((pattern, pos))
    
    if before_faq or after_faq:
        print(f'{filename:<30} {len(before_faq)} before{"":>15} {len(after_faq)} after')
