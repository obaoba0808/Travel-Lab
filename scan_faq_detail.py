import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

need_fix = ['bangkok-massage.html', 'esim-comparison.html', 'japan-budget-guide.html',
            'jiufen.html', 'korea-travel.html', 'osaka-food.html', 'osaka-usj.html',
            'packing-list.html', 'southeast-asia.html', 'taipei-food.html', 'vietnam-danang.html']

# skip _live_index
for f in need_fix:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    # Find FAQ section
    faq_match = re.search(r'<div class="faq-section"[^>]*>(.*?)</div>\s*</div>', c, re.DOTALL)
    if not faq_match:
        faq_match = re.search(r'class="faq-item"', c)
        if faq_match:
            start = max(0, faq_match.start() - 200)
            print(f'\n=== {f} (faq-item found) ===')
            print(c[start:start+500])
        else:
            # Find last h2
            h2s = list(re.finditer(r'<h2[^>]*>(.+?)</h2>', c))
            if h2s:
                last = h2s[-1]
                print(f'\n=== {f} (no faq-section, last h2) ===')
                print(last.group())
            else:
                print(f'\n=== {f} (no h2) ===')
        continue
    print(f'\n=== {f} ===')
    print(faq_match.group(0)[:600])
