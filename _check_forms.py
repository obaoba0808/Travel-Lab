import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# Pages that already have forms
has_form_files = []
no_form_content = []  # content pages missing form
skip_pages = {'404.html', '_live_index.html', 'about.html', 'contact.html',
              'disclaimer.html', 'privacy.html', 'terms.html', 'index.html',
              'travel-tools.html'}

for f in sorted(os.listdir(base)):
    if not f.endswith('.html') or f in skip_pages:
        continue
    path = os.path.join(base, f)
    with open(path, 'r', encoding='utf-8') as fh:
        c = fh.read()
    if 'submitLeadForm' in c or 'lead-inline' in c:
        has_form_files.append(f)
    else:
        no_form_content.append(f)

print("=== HAS FORM ===")
for f in has_form_files:
    print(f"  {f}")

print(f"\n=== MISSING FORM ({len(no_form_content)} pages) ===")
for f in no_form_content:
    print(f"  {f}")
