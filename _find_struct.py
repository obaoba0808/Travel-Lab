import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['esim-comparison.html', 'live-japan-budget.html']:
    c=open(f'C:\\Users\\FH01\\.qclaw\\workspace-cwapojim0yfmyvq8\\Travel-Lab\\{fname}','r',encoding='utf-8').read()
    
    body_start = c.find('<body')
    body = c[body_start:]
    
    # Find last content faq-q (in body, not in JS)
    # Look for faq-q in content (before the JS click handler)
    # JS starts with "document.querySelectorAll('.faq-item"
    js_marker = body.find("document.querySelectorAll('.faq-item")
    if js_marker == -1:
        js_marker = len(body)
    
    content_before_js = body[:js_marker]
    last_faq_q = content_before_js.rfind('faq-q')
    if last_faq_q == -1:
        last_faq_q = content_before_js.rfind('faq-a')
    
    print(f'\n=== {fname} ===')
    print(f'Body start: {body_start}, JS marker: {js_marker}')
    print(f'Last content faq @{body_start+last_faq_q}:')
    print(repr(body[last_faq_q:last_faq_q+150]))
    
    # From last faq-q, find closing structure
    # Strategy: look for pattern: </div>  </div>  </section>
    # Find the last </section> before the Klook/footer area
    klook = body.find('KLOOK', js_marker)
    footer = body.find('<footer')
    
    # Find last </section> between last faq and klook/footer
    search_end = min(klook if klook!=-1 else 999999999,
                     footer if footer!=-1 else 999999999)
    before_search = body[:search_end]
    last_section = before_search.rfind('</section>')
    
    # Find last </div> of FAQ section
    last_div = before_search.rfind('</div>')
    
    print(f'Last </section> before klook/footer: @{body_start+last_section}')
    print(f'Last </div> before klook/footer: @{body_start+last_div}')
    print(f'Klook: {klook}, Footer: {footer}')
    
    # Show context around last </section>
    if last_section > 0:
        print(f'Context around last </section>: {repr(body[last_section-50:last_section+100])}')
    print(f'Context around last </div>: {repr(body[last_div-100:last_div+50])}')
