import os

results = []
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_dismiss = 'leadDismissed' in c
    has_close_fix = "localStorage.setItem('leadDismissed'" in c
    # Check closeLeadPopup function
    idx = c.find('function closeLeadPopup')
    close_func = c[idx:idx+200] if idx >= 0 else 'NOT FOUND'
    results.append((f, has_dismiss, has_close_fix, close_func[:150]))

with open('__verify_fix.txt', 'w', encoding='utf-8') as out:
    for f, hd, hcf, cf in results:
        out.write(f'--- {f} ---\n')
        out.write(f'  leadDismissed in file: {hd}\n')
        out.write(f'  closePopup sets leadDismissed: {hcf}\n')
        out.write(f'  closeLeadPopup func: {cf}\n\n')

print(f'Checked {len(results)} files. See __verify_fix.txt')
