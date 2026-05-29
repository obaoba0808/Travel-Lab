import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# All HTML files with lead-inline form
for fname in os.listdir(base):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if 'lead-inline' not in c:
        continue
    
    form = c.find('class="lead-inline"')
    foot = c.find('<footer')
    body = c.find('<body')
    
    body_content = c[body:] if body != -1 else c
    faqs = [m.start() for m in re.finditer(r'faq-item', body_content)]
    last_faq_abs = body + faqs[-1] if faqs else -1
    
    has_faq = last_faq_abs > 0
    before_footer = form < foot if (form > 0 and foot > 0) else False
    after_last_faq = form > last_faq_abs if (form > 0 and last_faq_abs > 0) else False
    
    status = '✅' if before_footer else '❌ FORM AFTER FOOTER!'
    faq_status = 'has FAQ' if has_faq else 'no FAQ'
    
    print(f'{fname:40s} {status} ({faq_status})')
    if not before_footer:
        print(f'  form@{form}, footer@{foot}')
