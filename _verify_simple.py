# -*- coding: utf-8 -*-
import re

# Read tokyo-5days.html
with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check 1: SlideShare iframe
if 'slideshare.net' in content:
    print('[PASS] Found SlideShare embed')
    
    # Find all SlideShare URLs
    matches = re.findall(r'https://www\.slideshare\.net[^\s"\'<>]+', content)
    print(f'   Found {len(matches)} SlideShare URL(s)')
    for i, url in enumerate(matches[:3], 1):
        print(f'   [{i}] {url[:80]}')
else:
    print('[FAIL] SlideShare embed NOT found')

# Check 2: Formspree form
if 'formspree.io' in content:
    print('[PASS] Found Formspree form')
    
    # Find form action
    match = re.search(r'action="([^"]*formspree[^"]*)"', content)
    if match:
        print(f'   Form action: {match.group(1)[:80]}')
else:
    print('[FAIL] Formspree form NOT found')

# Check 3: Insertion location (before </article>)
if '</article>' in content:
    index = content.index('</article>')
    preceding = content[max(0, index-500):index]
    
    if 'slideshare-section' in preceding:
        print('[PASS] SlideShare section inserted BEFORE </article>')
        line_num = content[:index].count('\n') + 1
        print(f'   Insertion location: around line {line_num}')
    else:
        print('[WARN] slideshare-section NOT found before </article>')
        
print('\n[INFO] Verification completed')
