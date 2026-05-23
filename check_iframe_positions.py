import re
import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Find all iframe positions with trip.com
    iframes = list(re.finditer(r'<iframe.*?trip\.com/partners/ad.*?</iframe>', content, re.DOTALL))
    
    if not iframes:
        continue
    
    # Find FAQ section position
    faq_match = re.search(r'<section[^>]*class="faq-section"', content)
    faq_end = re.search(r'</section>', content[faq_match.end():]) if faq_match else None
    
    print(f'\n{"="*60}')
    print(f'File: {filename}')
    print(f'  Number of iframes: {len(iframes)}')
    
    for i, iframe_match in enumerate(iframes):
        iframe_pos = iframe_match.start()
        
        # Determine position relative to FAQ
        if faq_match:
            faq_start = faq_match.start()
            if faq_end:
                faq_end_pos = faq_match.end() + faq_end.start()
            else:
                faq_end_pos = faq_match.end() + 500  # approximate
            
            if iframe_pos < faq_start:
                position = "BEFORE FAQ"
            elif iframe_pos > faq_end_pos:
                position = "AFTER FAQ"
            else:
                position = "INSIDE FAQ"
        else:
            position = "NO FAQ FOUND"
        
        print(f'  Iframe {i+1}: {position} (pos {iframe_pos})')
        
        # Extract the banner ID
        id_match = re.search(r'id="(DB\d+)"', iframe_match.group())
        if id_match:
            print(f'    Banner ID: {id_match.group(1)}')
