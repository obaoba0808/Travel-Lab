import sys, re, os, json
sys.stdout.reconfigure(encoding='utf-8')

# Pages where schema has 5 Qs but HTML only shows 1 (or fewer)
# Need to extract FAQ from schema and rebuild HTML faq-items
pages_rebuild = [
    'busan-capsule.html', 'hokkaido-winter.html', 'seoul-food.html',
    'tainan-food.html', 'kansai-pass.html', 'hualien-taitung.html',
]

for fname in pages_rebuild:
    with open(fname, encoding='utf-8') as f:
        c = f.read()
    
    # Extract FAQPage schema
    faq_schema = re.search(r'"@type"\s*:\s*"FAQPage".*?}', c, re.DOTALL)
    if not faq_schema:
        print(f"SKIP {fname}: no FAQPage schema")
        continue
    
    # Extract questions and answers
    schema_text = faq_schema.group(0)
    questions = re.findall(r'"name"\s*:\s*"(.+?)"', schema_text)
    answers = re.findall(r'"acceptedAnswer".*?"text"\s*:\s*"(.+?)"', schema_text, re.DOTALL)
    
    if len(questions) < 5:
        print(f"WARN {fname}: only {len(questions)} Qs in schema")
    
    # Generate FAQ HTML items (onclick format)
    faq_items_html = ''
    for q, a in zip(questions, answers):
        a = a.replace('\\n', ' ').strip()
        faq_items_html += f'''<div class="faq-item" onclick="this.classList.toggle('open')"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>
'''
    
    # Find existing FAQ section and replace content between h2 and section closing
    # Pattern: <section class="faq-section" ...> <h2>...</h2> ... </section>
    section_match = re.search(r'(<section class="faq-section"[^>]*>.*?<h2[^>]*>.*?</h2>\s*)(.*?)(</section>)', c, re.DOTALL)
    
    if section_match:
        new_section = section_match.group(1) + '\n' + faq_items_html + '\n' + section_match.group(3)
        c = c[:section_match.start()] + new_section + c[section_match.end():]
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"DONE {fname}: rebuilt {len(questions)} FAQ items from schema")
    else:
        print(f"SKIP {fname}: can't match FAQ section pattern")

print("\nPhase 1 done!")
