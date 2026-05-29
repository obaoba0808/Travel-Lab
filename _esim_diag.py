import sys, re
sys.stdout.reconfigure(encoding='utf-8')
c=open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\esim-comparison.html','r',encoding='utf-8').read()
faqs=[(m.start(),m.group()) for m in re.finditer(r'faq-item[^-"\s]*',c)]
print('faq-item occurrences:', faqs)
# Show around last content faq
last_content_faq_pos = faqs[4][0]  # 5th (0-indexed), last content
print(f'\nLast content faq @{last_content_faq_pos}:')
print(repr(c[last_content_faq_pos:last_content_faq_pos+250]))
print('\nAfter last content FAQ (200-400 chars after):')
print(repr(c[last_content_faq_pos+200:last_content_faq_pos+450]))
