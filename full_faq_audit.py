import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Pages that need FAQ supplementing - check each properly
pages = [
    'busan-capsule.html', 'hokkaido-winter.html', 'seoul-food.html',
    'tainan-food.html', 'kansai-pass.html', 'hualien-taitung.html',
    'japan-travel.html', 'southeast-asia.html', 'taiwan-travel.html',
    'korea-budget.html', 'travel-tools.html'
]

for f in pages:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    
    # Count all faq-item variants
    fi1 = len(re.findall(r'class="faq-item"', c))
    fi2 = len(re.findall(r'faq-item-b', c))
    total = fi1 + fi2
    
    # Also check FAQ schema for actual Q count
    schema_qs = len(re.findall(r'"@type"\s*:\s*"Question"', c))
    
    # Get all faq-q content
    faq_qs = re.findall(r'class="faq-q[^"]*"[^>]*>(.+?)</div>', c)
    faq_qs_b = re.findall(r'class="faq-q-b[^"]*"[^>]*>(.+?)</div>', c)
    all_qs = faq_qs + faq_qs_b
    display_qs = [re.sub(r'<[^>]+>', '', q).strip()[:50] for q in all_qs]
    
    print(f'{f}: items={total}, schema_Qs={schema_qs}, displayed_Qs={len(all_qs)}')
    for q in display_qs:
        print(f'  Q: {q}')
    print()
