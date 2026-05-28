import os

count_scroll = 0
count_close = 0

old_close = "function closeLeadPopup(){document.getElementById('leadPopup').classList.remove('active')}"
new_close = "function closeLeadPopup(){localStorage.setItem('leadDismissed','1');document.getElementById('leadPopup').classList.remove('active')}"

old_scroll = "\nif(localStorage.getItem('leadSent'))return;\n"
new_scroll = "\nif(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;\n"

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        content = fp.read()

    changed = False

    if old_close in content:
        content = content.replace(old_close, new_close)
        count_close += 1
        changed = True

    if old_scroll in content:
        content = content.replace(old_scroll, new_scroll)
        count_scroll += 1
        changed = True

    if changed:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)

print(f'closeLeadPopup fixed: {count_close} files')
print(f'scroll listener fixed:  {count_scroll} files')
