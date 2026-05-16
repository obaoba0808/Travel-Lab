#!/usr/bin/env python3
"""Insert new CSS for search box and post meta into style.css"""
import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The new CSS block to insert after .site-branding p rule
new_css = '''
/* ========== SEARCH BOX ========== */
.search-box-wrap {
  max-width: 680px;
  margin: 0 auto 25px;
  padding: 0 20px;
}
.search-form {
  width: 100%;
}
.search-input-wrap {
  display: flex;
  align-items: center;
  background: #fff;
  border: 2px solid var(--tiffany);
  border-radius: 40px;
  padding: 0 20px;
  box-shadow: 0 4px 15px rgba(10,186,181,0.12);
  transition: box-shadow 0.25s;
}
.search-input-wrap:focus-within {
  box-shadow: 0 4px 20px rgba(10,186,181,0.25);
}
.search-icon {
  font-size: 18px;
  margin-right: 10px;
}
.search-input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 15px;
  padding: 12px 0;
  background: transparent;
  font-family: 'Noto Sans TC', sans-serif;
}
.search-btn {
  background: var(--tiffany);
  color: #fff;
  border: none;
  border-radius: 30px;
  padding: 8px 24px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.search-btn:hover {
  background: var(--tiffany-dark);
}

/* ========== POST META EXTRA ========== */
.post-meta-extra {
  display: flex;
  gap: 15px;
  font-size: 12px;
  color: var(--text-gray);
  margin-top: 6px;
}
.reading-time::before {
  content: "\\1F556 ";
}
.last-updated::before {
  content: "\\1F4C5 ";
}
'''

# Find insertion point: after ".site-branding p { ... }" and before next comment
import re
# Match: .site-branding p rule + possible whitespace + newline + comment line
pattern = r'(.site-branding p \{[^}]+\})\s*\n(/\* ========== TOPBAR LOGO ========== \*/)'

def repl(m):
    return m.group(1) + '\n' + new_css + '\n' + m.group(2)

new_css_content, n = re.subn(pattern, repl, css, count=1)
if n == 0:
    print('ERROR: pattern not found! Trying alternative...')
    # Try finding just the .site-branding p line
    idx = css.find('.site-branding p {')
    if idx >= 0:
        # Find end of that rule
        end_idx = css.find('}\n', idx)
        if end_idx >= 0:
            insert_pos = end_idx + 2  # after }\n
            new_css_content = css[:insert_pos] + new_css + '\n' + css[insert_pos:]
            n = 1
            print('Inserted via alternative method')
        else:
            print('ERROR: could not find end of .site-branding p rule')
    else:
        print('ERROR: could not find .site-branding p rule')

if n > 0:
    with open('style.css', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_css_content)
    print('SUCCESS: CSS inserted into style.css')
    print('  - Search box styles added')
    print('  - Post meta extra styles added')
else:
    print('FAILED to insert CSS')
