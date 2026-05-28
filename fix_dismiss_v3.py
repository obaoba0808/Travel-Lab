import os, re

CLOSE_OLD  = b"function closeLeadPopup(){document.getElementById('leadPopup').classList.remove('active')}"
CLOSE_NEW  = b"function closeLeadPopup(){localStorage.setItem('leadDismissed','1');document.getElementById('leadPopup').classList.remove('active')}"

# scroll listener - need to handle possible whitespace differences
SCROLL_OLD = b"if(localStorage.getItem('leadSent'))return;"
SCROLL_NEW = b"if(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;"

css_fixed  = 0
js_close   = 0
js_scroll  = 0

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'rb') as fp:
        data = fp.read()

    modified = False

    # 1. Fix CSS: invalid 'cursor:pointer:#4db6ac;' -> 'cursor:pointer;'
    bad = b'cursor:pointer:#4db6ac;'
    if bad in data:
        data = data.replace(bad, b'cursor:pointer;')
        modified = True
        css_fixed += 1

    # 2. Fix closeLeadPopup - add leadDismissed flag
    if CLOSE_OLD in data:
        data = data.replace(CLOSE_OLD, CLOSE_NEW)
        modified = True
        js_close += 1
    else:
        # Maybe already has leadDismissed? Check
        m = re.search(rb'function closeLeadPopup\(\)\{[^}]*\}', data)
        if m:
            func = m.group(0)
            if b'leadDismissed' not in func:
                # Insert after opening brace
                new_func = func.replace(b'{', b"{localStorage.setItem('leadDismissed','1');", 1)
                data = data.replace(func, new_func)
                modified = True
                js_close += 1

    # 3. Fix scroll listener
    if SCROLL_OLD in data:
        data = data.replace(SCROLL_OLD, SCROLL_NEW)
        modified = True
        js_scroll += 1

    if modified:
        with open(f, 'wb') as fp:
            fp.write(data)

print(f'CSS cursor fixed: {css_fixed}')
print(f'JS closeLeadPopup fixed: {js_close}')
print(f'JS scroll listener fixed: {js_scroll}')
