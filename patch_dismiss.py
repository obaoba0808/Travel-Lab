import os, re

'''
Fix: after closing popup, set localStorage leadDismissed flag
Fix: scroll listener should also check leadDismissed before showing popup
Uses byte-level operations to avoid PowerShell encoding issues.
Results are written to a log file, NOT printed to terminal.
'''

log_lines = []

def patch_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    original = data
    modified = False
    fname = os.path.basename(filepath)

    # ---- Fix 1: patch closeLeadPopup to set the dismissed flag ----
    # Pattern: function closeLeadPopup(){...}
    # We need to add: localStorage.setItem('leadDismissed','1');
    # right after the opening brace
    m = re.search(rb'function closeLeadPopup\(\)\{[^}]*\}', data)
    if m:
        func = m.group(0)
        if b'leadDismissed' not in func:
            # Insert after the opening brace
            new_func = func.replace(b'{', b"{localStorage.setItem('leadDismissed','1');", 1)
            data = data.replace(func, new_func)
            modified = True
            log_lines.append(f'[OK] {fname}: closeLeadPopup patched')
        else:
            log_lines.append(f'[SKIP] {fname}: closeLeadPopup already has leadDismissed')
    else:
        log_lines.append(f'[WARN] {fname}: closeLeadPopup function NOT FOUND')

    # ---- Fix 2: patch scroll listener to also check leadDismissed ----
    # The scroll check is: if(localStorage.getItem('leadSent'))return;
    # We need to add ||localStorage.getItem('leadDismissed')
    old_scroll = b"if(localStorage.getItem('leadSent'))return;"
    new_scroll = b"if(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;"
    if old_scroll in data:
        data = data.replace(old_scroll, new_scroll, 1)
        modified = True
        log_lines.append(f'[OK] {fname}: scroll listener patched')
    else:
        # Maybe already patched?
        if b'leadDismissed' in data:
            log_lines.append(f'[SKIP] {fname}: scroll listener already has leadDismissed')
        else:
            log_lines.append(f'[WARN] {fname}: scroll listener pattern NOT FOUND')

    # ---- Fix 3: fix invalid CSS cursor property ----
    bad_css = b'cursor:pointer:#4db6ac;'
    if bad_css in data:
        data = data.replace(bad_css, b'cursor:pointer;')
        modified = True
        log_lines.append(f'[OK] {fname}: CSS cursor property fixed')

    if modified:
        with open(filepath, 'wb') as f:
            f.write(data)
        log_lines.append(f'>>> {fname}: FILE UPDATED')
        return True
    else:
        log_lines.append(f'[NOCHANGE] {fname}: no changes needed')
        return False


count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    if patch_file(f):
        count += 1

# Write log to file (avoid printing UTF-8 to PowerShell terminal)
with open('__patch_log.txt', 'w', encoding='utf-8') as log:
    log.write(f'Files modified: {count}\n')
    log.write('\n'.join(log_lines))

print(f'Done. {count} files modified. See __patch_log.txt for details.')
