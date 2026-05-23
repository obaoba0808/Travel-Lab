import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != '_live_index.html']

print(f"{'File':<30} {'Total iframes':<15} {'Before FAQ':<15} {'After FAQ':<15}")
print("="*80)

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Find ALL iframes
    all_iframes = list(re.finditer(r'<iframe.*?</iframe>', content, re.DOTALL))
    
    if not all_iframes:
        continue
    
    # Find FAQ section
    faq_match = re.search(r'<section[^>]*class="faq-section"', content)
    
    if not faq_match:
        print(f'{filename:<30} {len(all_iframes):<15} No FAQ section')
        continue
    
    faq_start = faq_match.start()
    
    # Find end of FAQ
    faq_end_match = re.search(r'</section>', content[faq_match.end():])
    if faq_end_match:
        faq_end = faq_match.end() + faq_end_match.start()
    else:
        faq_end = faq_match.end() + 500
    
    # Count iframes before and after FAQ
    before_count = sum(1 for m in all_iframes if m.start() < faq_start)
    after_count = sum(1 for m in all_iframes if m.start() > faq_end)
    
    if before_count > 0 or after_count > 0:
        print(f'{filename:<30} {len(all_iframes):<15} {before_count:<15} {after_count:<15}')
