import sys, re
sys.stdout.reconfigure(encoding='utf-8')
c=open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\kansai-pass.html','r',encoding='utf-8').read()
form=c.find('class="lead-inline"')
foot=c.find('<footer')
body=c.find('<body')
body_content=c[body:]
faqs=[m.start() for m in re.finditer(r'faq-item', body_content)]
last_faq_abs=body+faqs[-1] if faqs else -1
print(f'Form: @{form}, Footer: @{foot}')
print(f'Body: @{body}, Last FAQ: @{last_faq_abs}')
print(f'Form < Footer? {form < foot}')
print(f'Form > Last FAQ? {form > last_faq_abs}')
if form > 0:
    print(f'Around form: {repr(c[form-100:form+100])}')
