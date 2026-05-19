import sys, re
sys.stdout.reconfigure(encoding='utf-8')
for f in ['esim-comparison.html', 'packing-list.html']:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    items_b = len(re.findall(r'faq-item-b', c))
    items = len(re.findall(r'faq-item"', c))
    print(f'{f}: faq-item={items}, faq-item-b={items_b}')
    last = c.rfind('faq-item')
    if last > 0:
        print(c[last:last+600])
    print('---')
