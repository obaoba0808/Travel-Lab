import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['esim-comparison.html', 'live-japan-budget.html']:
    c=open(f'C:\\Users\\FH01\\.qclaw\\workspace-cwapojim0yfmyvq8\\Travel-Lab\\{fname}','r',encoding='utf-8').read()
    form=c.find('class="lead-inline"')
    # Find where the form section STARTS (after any whitespace/newline)
    form_section_start = c.rfind('\n', max(0, form-100), form)
    # Find the </section> of the form
    form_end = c.find('</section>', form)
    print(f'\n=== {fname} ===')
    print(f'Form section starts around @{form_section_start}')
    print(f'Form: {repr(c[form_section_start:form+100])}')
    print(f'After form: {repr(c[form_end:form_end+200])}')
    
    # Find what comes BEFORE the form
    before_form = c[max(0,form-300):form]
    print(f'Before form: {repr(before_form[-150:])}')
    
    # Find last faq-item in body
    body_start = c.find('<body')
    body = c[body_start:]
    faqs = [m.start() for m in re.finditer(r'faq-item', body)]
    if faqs:
        last_faq_pos = body_start + faqs[-1]
        print(f'Last faq-item in modified file @{last_faq_pos}')
        print(f'Last faq context: {repr(c[max(0,last_faq_pos-50):last_faq_pos+80])}')
        print(f'Last faq IS IN FORM? {last_faq_pos > form and last_faq_pos < form_end}')
        print(f'Last faq IS BEFORE FORM? {last_faq_pos < form}')
