import os, re

count_js1 = 0
count_js2 = 0

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        content = fp.read()

    original = content

    # Fix 1: closeLeadPopup() — add localStorage.setItem('leadDismissed','1')
    # The function body is: {document.getElementById('leadPopup').classList.remove('active')}
    old_close = "function closeLeadPopup(){document.getElementById('leadPopup').classList.remove('active')}"
    new_close = "function closeLeadPopup(){localStorage.setItem('leadDismissed','1');document.getElementById('leadPopup').classList.remove('active')}"
    if old_close in content:
        content = content.replace(old_close, new_close)
        count_js1 += 1

    # Fix 2: scroll listener — add dismissed check
    # Current: if(localStorage.getItem('leadSent'))return;
    # Change to: if(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;
    old_scroll = "if(localStorage.getItem('leadSent'))return;"
    new_scroll = "if(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;"
    if old_scroll in content and old_scroll in content.replace(old_scroll, new_scroll, 1):
        content = content.replace(old_scroll, new_scroll, 1)
        count_js2 += 1

    if content != original:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)

print(f'Fix 1 (closeLeadPopup): {count_js1} files')
print(f'Fix 2 (scroll dismissed check): {count_js2} files')
