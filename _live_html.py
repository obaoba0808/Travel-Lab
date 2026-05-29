import urllib.request, sys, os
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://golightly.fun/esim-comparison'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req, timeout=10)
html = resp.read().decode('utf-8')

print(f'Total length: {len(html)}')

# Find </main> occurrences
import re
main_matches = [(m.start(), m.end()) for m in re.finditer('</main>', html)]
print(f'</main> occurrences: {len(main_matches)}')
for i, (s, e) in enumerate(main_matches):
    ctx_before = html[max(0,s-80):s]
    print(f'  [{i}] @{s}: ...{ctx_before}')

# Find last faq-item
fi = html.rfind('faq-item')
print(f'last faq-item: @{fi}')
print(f'  context: ...{html[max(0,fi-100):fi+50]}')

# Find form
form_idx = html.find('class="lead-inline"')
print(f'form: @{form_idx}')
print(f'  context: ...{html[max(0,form_idx-150):form_idx]}')

# Find footer
foot_idx = html.find('<footer')
print(f'footer: @{foot_idx}')
print(f'  context: ...{html[max(0,foot_idx-80):foot_idx+100]}')

# Show what section the form is in
section_before = html.rfind('<section', 0, form_idx)
div_before = html.rfind('<div', 0, form_idx)
print(f'\nLast <section> before form: @{section_before}')
print(f'Last <div> before form: @{div_before}')

# Save full HTML for analysis
with open(os.path.join(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab', '_live_esim.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print('\nSaved to _live_esim.html')
