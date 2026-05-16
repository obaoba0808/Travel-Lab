#!/usr/bin/env python3
"""Add legal links div to all pages whose footer-bottom lacks it"""
import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

legal_div = '''    <div style="margin-top:8px;font-size:12px;">
      <a href="about.html" style="color:inherit;margin-right:12px;">關於我們</a>
      <a href="privacy.html" style="color:inherit;margin-right:12px;">隱私權政策</a>
      <a href="terms.html" style="color:inherit;margin-right:12px;">使用條款</a>
      <a href="disclaimer.html" style="color:inherit;">免責聲明</a>
    </div>'''

legal_links_snippet = 'disclaimer.html" style="color:inherit;">免責聲明</a>'

pages = [f for f in sorted(os.listdir('.')) if f.endswith('.html') and f not in ['terms.html', 'disclaimer.html']]
updated = []

for f in pages:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Skip if already has legal links
    if legal_links_snippet in content:
        continue
    
    # Find footer-bottom div
    idx = content.find('footer-bottom')
    if idx < 0:
        continue
    
    # Check if it already has the margin-top div
    footer_section = content[idx:idx+500]
    if 'margin-top:8px;font-size:12px' in footer_section:
        # Already has the div - replace it
        continue  # already handled by previous script
    
    # No margin-top div - need to add it after </p> in footer-bottom
    # Pattern: after the copyright <p> in footer-bottom
    old_pattern = '</p>\r\n  </div>\r\n</footer>'
    new_pattern = f'</p>\r\n{legal_div}\r\n  </div>\r\n</footer>'
    
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern, 1)
        with open(f, 'w', encoding='utf-8', newline='\r\n') as fh:
            fh.write(content)
        updated.append(f)
        print(f'{f}: legal div added')

if updated:
    print(f'\nUpdated {len(updated)} pages: {updated}')
else:
    print('No pages needed updating - all already have legal links')