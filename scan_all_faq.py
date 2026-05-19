import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['index.html','about.html','contact.html','privacy.html','terms.html','disclaimer.html','sitemap.html','404.html','_live_index.html']]

for f in sorted(html_files):
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    count1 = len(re.findall(r'class="faq-item"', c))
    count2 = len(re.findall(r'faq-item-b', c))
    total = count1 + count2
    status = '<< NEED MORE' if total < 5 else 'OK'
    print(f'{f}: {total} FAQs ({status}) [faq-item={count1}, faq-item-b={count2}]')
