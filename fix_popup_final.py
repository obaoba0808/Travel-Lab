import os, re

# Read exact bytes from kansai-pass.html to get the exact old CSS string
with open('kansai-pass.html', 'rb') as f:
    raw = f.read()

# Find the popup CSS section in bytes
css_start = raw.find(b'.lead-popup-overlay{display:none')
if css_start == -1:
    print('ERROR: CSS not found')
    exit(1)

# Find the end of CSS - after .lead-note{...}
# Look for b'.lead-note{' then find the closing }
note_start = raw.find(b'.lead-note{', css_start)
if note_start == -1:
    print('ERROR: .lead-note not found')
    exit(1)

# Find closing } for .lead-note
brace = raw.find(b'}', note_start)
if brace == -1:
    print('ERROR: closing brace not found')
    exit(1)

css_end = brace + 1
old_css_bytes = raw[css_start:css_end]
print(f'Found old CSS: {len(old_css_bytes)} bytes')
print('Old CSS snippet:', old_css_bytes[:300].decode('utf-8', errors='replace'))

# New CSS - properly formatted, with correct .lead-popup-close
new_css_str = """.lead-popup-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.6);z-index:9999;align-items:center;justify-content:center}.lead-popup-overlay.active{display:flex}.lead-popup{background:#fff;border-radius:16px;padding:0;max-width:480px;width:90%;position:relative;text-align:center;font-family:"Noto Sans TC",sans-serif;overflow:hidden}.lead-popup-header{background:linear-gradient(135deg,#81d4ce,#4db6ac);padding:20px 32px 16px;position:relative}.lead-popup-header h3{color:#fff;margin:0;font-size:18px;line-height:1.4;text-shadow:0 1px 3px rgba(0,0,0,0.15)}.lead-popup-close{position:absolute;top:8px;right:10px;background:rgba(255,255,255,0.25);border:none;font-size:20px;cursor:pointer;color:#fff;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;line-height:1;z-index:20;transition:background 0.2s}.lead-popup-close:hover{background:rgba(255,255,255,0.55)}.lead-popup-body{padding:24px 32px 28px}.lead-popup-body p{color:#444;margin:0 0 16px;font-size:14px;line-height:1.7}.lead-popup input[type=email]{width:100%;padding:12px 16px;border:2px solid #81d4ce;border-radius:8px;font-size:15px;box-sizing:border-box;margin-bottom:12px;outline:none;transition:border-color 0.2s}.lead-popup input[type=email]:focus{border-color:#4db6ac;box-shadow:0 0 0 3px rgba(77,182,172,0.2)}.lead-popup button{width:100%;padding:14px;background:linear-gradient(135deg,#81d4ce,#4db6ac);color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:bold;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s}.lead-popup button:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(77,182,172,0.35)}.lead-popup .lead-note{font-size:11px;color:#aaa;margin-top:10px}"""

new_css_bytes = new_css_str.encode('utf-8')

# Now fix JS: closeLeadPopup + scroll listener
# Find closeLeadPopup function
js_close_old = b"function closeLeadPopup(){document.getElementById('leadPopup').classList.remove('active')}"
js_close_new = b"function closeLeadPopup(){localStorage.setItem('leadDismissed','1');document.getElementById('leadPopup').classList.remove('active')}"

# Find scroll listener check
js_scroll_old = b"\nif(localStorage.getItem('leadSent'))return;\n"
js_scroll_new = b"\nif(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;\n"

fixed_count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'rb') as fp:
        data = fp.read()

    modified = False

    # Fix CSS
    if old_css_bytes in data:
        data = data.replace(old_css_bytes, new_css_bytes)
        modified = True
        print(f'  {f}: CSS fixed')

    # Fix closeLeadPopup JS
    if js_close_old in data:
        data = data.replace(js_close_old, js_close_new)
        modified = True
        print(f'  {f}: closeLeadPopup fixed')
    elif b"function closeLeadPopup()" in data and b"localStorage.setItem('leadDismissed'" not in data:
        # Already modified but without dismissed flag - fix it
        # Find the function and add the flag
        pass  # Will handle below with regex

    # Fix scroll listener JS
    if js_scroll_old in data:
        data = data.replace(js_scroll_old, js_scroll_new)
        modified = True
        print(f'  {f}: scroll listener fixed')

    # Handle case where closeLeadPopup was already modified but needs dismissed flag
    if b"function closeLeadPopup()" in data and b"leadDismissed" not in data:
        # Use regex to find and replace the function
        pattern = re.compile(rb'function closeLeadPopup\(\)\{[^}]* \}')
        match = pattern.search(data)
        if match:
            old_func = match.group(0)
            # Insert localStorage.setItem after {
            new_func = old_func.replace(b'{', b"{localStorage.setItem('leadDismissed','1');", 1)
            data = data.replace(old_func, new_func)
            modified = True
            print(f'  {f}: closeLeadPopup patched (regex)')

    if modified:
        with open(f, 'wb') as fp:
            fp.write(data)
        fixed_count += 1

print(f'\nTotal files fixed: {fixed_count}')
