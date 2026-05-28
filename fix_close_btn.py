import os

# Fix: move close button to top-right of the entire popup (not just header)
old_close_css = '.lead-popup-close{position:absolute;top:8px;right:12px;background:rgba(255,255,255,0.3);border:none;font-size:22px;cursor:pointer;color:#fff;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;line-height:1;transition:background 0.2s}.lead-popup-close:hover{background:rgba(255,255,255,0.5)}'

new_close_css = '.lead-popup-close{position:absolute;top:8px;right:10px;background:none;border:none;font-size:24px;cursor:pointer:#4db6ac;color:#4db6ac;z-index:10;line-height:1;padding:4px;transition:color 0.2s}.lead-popup-close:hover{color:#2a7a6e}'

count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        content = fp.read()
    if old_close_css in content:
        content = content.replace(old_close_css, new_close_css)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        count += 1

print(f'Updated {count} files - close button now at popup top-right corner')
