import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

# Pages that need more FAQs (confirmed)
pages = ['jiufen.html', 'korea-travel.html', 'osaka-usj.html', 'taipei-food.html', 'vietnam-danang.html', 'esim-comparison.html', 'packing-list.html']

for fname in pages:
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    
    # Find FAQ section and show closing structure
    faq_match = re.search(r'class="faq-section"', c)
    if not faq_match:
        # For pages without faq-section class, find FAQ h2
        faq_h2 = re.search(r'>常見問題', c)
        if faq_h2:
            print(f'\n=== {fname} ===')
            # Show 300 chars after FAQ h2
            end = min(len(c), faq_h2.end() + 300)
            print(c[faq_h2.end():end])
        continue
    
    # Show closing: find last faq-item and closing divs after it
    items = list(re.finditer(r'class="faq-item"', c))
    if items:
        last = items[-1]
        end = min(len(c), last.start() + 800)
        print(f'\n=== {fname} ===')
        print(c[last.start():end])
