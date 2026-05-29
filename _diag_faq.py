import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

for fname in ['esim-comparison.html', 'live-japan-budget.html', 'seasia-budget-travel-guide.html']:
    c = open(os.path.join(base, fname), 'r', encoding='utf-8').read()
    print(f'\n=== {fname} ({len(c)} chars) ===')
    
    # Find all faq-item positions
    faqs = [m.start() for m in re.finditer('faq-item', c)]
    print(f'FAQ positions: {faqs}')
    
    # Show 50 chars before and after each FAQ
    for i, pos in enumerate(faqs):
        ctx_before = c[max(0,pos-50):pos]
        ctx_after = c[pos:pos+80]
        print(f'  FAQ[{i}] @{pos}: before=...{ctx_before} | after={ctx_after}...')
    
    # Show what the regex is matching
    matches = list(re.finditer(r'<div class="faq-item[^"]*"[^>]*>.*?</div>\s*</div>', c, re.DOTALL))
    print(f'Regex matches: {[(m.start(), m.end()) for m in matches]}')
    if matches:
        last = matches[-1]
        print(f'Last match: @{last.start()} to @{last.end()}')
        print(f'  Content: {c[last.start():last.start()+200]}...')
