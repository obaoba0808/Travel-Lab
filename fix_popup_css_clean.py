import os, re

# The correct, clean CSS for the popup (replaces the entire <style> block's popup section)
new_popup_css = """.lead-popup-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.6);z-index:9999;align-items:center;justify-content:center}.lead-popup-overlay.active{display:flex}.lead-popup{background:#fff;border-radius:16px;padding:0;max-width:480px;width:90%;position:relative;text-align:center;font-family:"Noto Sans TC",sans-serif;overflow:hidden}.lead-popup-header{background:linear-gradient(135deg,#81d4ce,#4db6ac);padding:20px 32px 16px;position:relative}.lead-popup-header h3{color:#fff;margin:0;font-size:18px;line-height:1.4;text-shadow:0 1px 3px rgba(0,0,0,0.15)}.lead-popup-close{position:absolute;top:6px;right:8px;background:rgba(255,255,255,0.25);border:none;font-size:20px;cursor:pointer;color:#fff;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;line-height:1;z-index:20;transition:background 0.2s}.lead-popup-close:hover{background:rgba(255,255,255,0.55)}.lead-popup-body{padding:24px 32px 28px}.lead-popup-body p{color:#444;margin:0 0 16px;font-size:14px;line-height:1.7}.lead-popup input[type=email]{width:100%;padding:12px 16px;border:2px solid #81d4ce;border-radius:8px;font-size:15px;box-sizing:border-box;margin-bottom:12px;outline:none;transition:border-color 0.2s}.lead-popup input[type=email]:focus{border-color:#4db6ac;box-shadow:0 0 0 3px rgba(77,182,172,0.2)}.lead-popup button{width:100%;padding:14px;background:linear-gradient(135deg,#81d4ce,#4db6ac);color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:bold;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s}.lead-popup button:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(77,182,172,0.35)}.lead-popup .lead-note{font-size:11px;color:#aaa;margin-top:10px}"""

# We need to find and replace the CSS block inside each HTML file's <style> tag
# The CSS is inside a <style> block in the <head>
count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()

    # Find the popup CSS - it starts with .lead-popup-overlay after <style>
    # Use regex to find the entire CSS block from .lead-popup-overlay to .lead-note
    pattern = r'\.lead-popup-overlay\{display:none[^}]*\.lead-note\{font-size:11px;color:#aaa;margin-top:10px\}'
    if re.search(pattern, content):
        content = re.sub(pattern, new_popup_css, content)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        count += 1
    else:
        # Try alternate pattern - the CSS might have been partially modified
        # Just find from .lead-popup-overlay to the closing </style>
        idx_start = content.find('.lead-popup-overlay{display:none')
        if idx_start >= 0:
            # Find the end - next } that isn't part of the CSS (before </style>)
            idx_end = content.find('</style>', idx_start)
            if idx_end >= 0:
                # Replace everything from .lead-popup-overlay to just before </style>
                # Actually, let's be more careful - find where the popup CSS ends
                # It should end with ".lead-note{...}" followed by nothing popup-related
                # Simpler approach: replace from idx_start to a point
                # Let's find the last popup-related rule
                temp = content[idx_start:idx_end]
                last_idx = temp.rfind('.lead-note')
                if last_idx >= 0:
                    last_brace = temp.find('}', last_idx)
                    if last_brace >= 0:
                        actual_end = idx_start + last_brace + 1
                        content = content[:idx_start] + new_popup_css + content[actual_end:]
                        with open(f, 'w', encoding='utf-8') as fp:
                            fp.write(content)
                        count += 1

print(f'CSS fixed in {count} files (clean rewrite)')
