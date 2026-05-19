import sys
sys.stdout.reconfigure(encoding='utf-8')

filepath = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\js\monetization.js'

with open(filepath, 'r', encoding='utf-8') as f:
    js = f.read()

# More robust selector: try .faq-section first, then .faq-accordion-beautify
old = "const faqSection = articleContainer.querySelector('.faq-section, .faq-accordion-beautify');"
new = "const faqSection = articleContainer.querySelector('.faq-section') || articleContainer.querySelector('.faq-accordion-beautify');"

if old in js:
    js = js.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(js)
    print('✅ Fixed: now using || fallback for FAQ selector')
    print('New line:', new)
else:
    print('⚠️ Pattern not found')
    idx = js.find('faqSection = articleContainer')
    if idx != -1:
        print('Found context:', repr(js[idx:idx+120]))
