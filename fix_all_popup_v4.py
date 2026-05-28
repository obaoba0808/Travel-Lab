import os, re

# ===== 1. CSS 修復：修正 .lead-popup-close 語法錯誤 + 改白色 =====
old_css_bad = "cursor:pointer:#4db6ac;color:#4db6ac;"
new_css_fixed = "cursor:pointer;color:#fff;background:rgba(255,255,255,0.25);border-radius:50%;width:30px;height:30px;display:flex;align-items:center;justify-content:center;transition:background 0.2s;"
# Actually, let's just replace the entire .lead-popup-close block for safety
old_close_css = ".lead-popup-close{position:absolute;top:8px;right:10px;background:none;border:none;font-size:24px;cursor:pointer:#4db6ac;color:#4db6ac;z-index:10;line-height:1;padding:4px;transition:color 0.2s}.lead-popup-close:hover{color:#2a7a6e}"
new_close_css = ".lead-popup-close{position:absolute;top:10px;right:12px;background:rgba(255,255,255,0.3);border:none;font-size:22px;cursor:pointer;color:#fff;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;line-height:1;z-index:20;transition:background 0.2s}.lead-popup-close:hover{background:rgba(255,255,255,0.55)}"

# ===== 2. JS 修復：closeLeadPopup 加 leadDismissed + scroll 加判斷 =====
# Pattern for closeLeadPopup - try multiple variants
close_variants = [
    "function closeLeadPopup(){document.getElementById('leadPopup').classList.remove('active')}",
    "function closeLeadPopup(){localStorage.setItem('leadDismissed','1');document.getElementById('leadPopup').classList.remove('active')}",
]
close_fixed = "function closeLeadPopup(){localStorage.setItem('leadDismissed','1');localStorage.setItem('leadClosed','1');document.getElementById('leadPopup').classList.remove('active')}"

# Scroll listener variants
scroll_variants = [
    "\nif(localStorage.getItem('leadSent'))return;\n",
    "\nif(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed'))return;\n",
]
scroll_fixed = "\nif(localStorage.getItem('leadSent')||localStorage.getItem('leadDismissed')||localStorage.getItem('leadClosed'))return;\n"

css_count = 0
js_close_count = 0
js_scroll_count = 0

for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    original = content

    # Fix CSS
    if old_close_css in content:
        content = content.replace(old_close_css, new_close_css)
        css_count += 1

    # Fix JS: closeLeadPopup
    if "function closeLeadPopup()" in content:
        # Remove any existing version and replace with fixed one
        # Match: function closeLeadPopup(){...}
        new_content = re.sub(
            r'function closeLeadPopup\(\)\{[^}]*\}',
            close_fixed,
            content
        )
        if new_content != content:
            content = new_content
            js_close_count += 1

    # Fix JS: scroll listener
    if 'localStorage.getItem' in content and 'leadSent' in content:
        # Check if dismissed/closed check already exists
        if 'leadDismissed' not in content or 'leadClosed' not in content.split('leadSent')[1].split(';')[0]:
            # Add the extra checks
            old_scroll = "\nif(localStorage.getItem('leadSent'))return;\n"
            if old_scroll in content:
                content = content.replace(old_scroll, scroll_fixed)
                js_scroll_count += 1

    if content != original:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)

print(f'CSS fixed: {css_count}')
print(f'JS closeLeadPopup fixed: {js_close_count}')
print(f'JS scroll listener fixed: {js_scroll_count}')
