import os, re

'''
Fix: closeLeadPopup() should set localStorage leadDismissed flag
Fix: scroll listener should also check leadDismissed
Approach: use regex on bytes to find and patch the functions
'''

def fix_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()

    original = data
    modified = False

    # ---- Fix 1: patch closeLeadPopup to add localStorage.setItem ----
    # Find: function closeLeadPopup(){...}
    # We need to add localStorage.setItem('leadDismissed','1'); after the opening brace
    m = re.search(rb'function closeLeadPopup\(\)\{[^}]*\}', data)
    if m:
        func_bytes = m.group(0)
        if b'leadDismissed' not in func_bytes:
            # Insert after the opening brace
            # The function looks like: function closeLeadPopup(){document.getElementById(...)}
            # We want: function closeLeadPopup(){localStorage.setItem('leadDismissed','1');document.getElementById(...)}
            new_func = func_bytes.replace(b'{', b"{localStorage.setItem('leadDismissed','1');", 1)
            data = data.replace(func_bytes, new_func)
            modified = True
            print(f'  Patched closeLeadPopup in {os.path.basename(filepath)}')

    # ---- Fix 2: patch scroll listener to also check leadDismissed ----
    # Find: if(localStorage.getItem('leadSent'))return;
    # Replace with: if(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;
    old_scroll = b"if(localStorage.getItem('leadSent'))return;"
    new_scroll = b"if(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;"
    if old_scroll in data:
        data = data.replace(old_scroll, new_scroll, 1)
        modified = True
        print(f'  Patched scroll listener in {os.path.basename(filepath)}')
    else:
        # Maybe it's already patched or uses different whitespace
        # Check if leadDismissed check exists in the scroll area
        idx = data.find(b"addEventListener('scroll'")
        if idx >= 0:
            # Look at 500 bytes after the scroll listener start
            snippet = data[idx:idx+500]
            if b'leadDismissed' not in snippet and b'leadSent' in snippet:
                # Need to patch manually - the pattern might have newlines
                # Let's try a more flexible approach
                pass

    # ---- Also fix CSS: invalid 'cursor:pointer:#4db6ac;' ----
    bad_css = b'cursor:pointer:#4db6ac;'
    if bad_css in data:
        data = data.replace(bad_css, b'cursor:pointer;')
        modified = True
        print(f'  Fixed CSS cursor property in {os.path.basename(filepath)}')

    if modified:
        with open(filepath, 'wb') as f:
            f.write(data)
        return True
    return False

count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    if fix_file(f):
        count += 1

print(f'\nTotal files modified: {count}')
