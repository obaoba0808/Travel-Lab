import os, re

# Exact byte patterns from the actual file (verified via __debug_js.txt)
CLOSE_OLD   = b"function closeLeadPopup(){document.getElementById('leadPopup').classList.remove('active')}"
CLOSE_NEW   = b"function closeLeadPopup(){localStorage.setItem('leadDismissed','1');document.getElementById('leadPopup').classList.remove('active')}"

SCROLL_OLD  = b"\nif(localStorage.getItem('leadSent'))return;\n"
SCROLL_NEW  = b"\nif(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;\n"

css_fixed = 0
js_close   = 0
js_scroll  = 0

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'rb') as fp:
        data = fp.read()

    modified = False

    # 1. Fix CSS: cursor:pointer:#4db6ac; is invalid syntax - remove it
    bad_css = b'cursor:pointer:#4db6ac;'
    if bad_css in data:
        data = data.replace(bad_css, b'cursor:pointer;')
        modified = True
        css_fixed += 1

    # 2. Fix closeLeadPopup - add dismissed flag
    if CLOSE_OLD in data:
        data = data.replace(CLOSE_OLD, CLOSE_NEW)
        modified = True
        js_close += 1
    else:
        # Maybe already has localStorage set? Check if it needs patching
        # Look for closeLeadPopup function and check if it has leadDismissed
        m = re.search(rb'function closeLeadPopup\(\)\{[^}]*\}', data)
        if m:
            func_body = m.group(0)
            if b'leadDismissed' not in func_body:
                # Need to inject the setItem call after the opening brace
                new_func = func_body.replace(b'{', b"{localStorage.setItem('leadDismissed','1');", 1)
                data = data.replace(func_body, new_func)
                modified = True
                js_close += 1

    # 3. Fix scroll listener - add dismissed check
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
