import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['index.html','about.html','contact.html','privacy.html','terms.html','disclaimer.html','sitemap.html','404.html']]

for f in sorted(html_files):
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    # Find FAQ section - count questions (h3 with Q pattern, or FAQ schema items)
    faqs = re.findall(r'<h3[^>]*>\s*(?:Q\d*[.、:]\s*)?(.+?)</h3>', c)
    if not faqs:
        # Try FAQ schema mainEntity count
        schema_faqs = c.count('"@type":"Question"')
        if schema_faqs > 0:
            faqs = ['(schema)'] * schema_faqs
    count = len(faqs)
    status = '<< NEED MORE' if count < 5 else 'OK'
    print(f'{f}: {count} FAQs {status}')
