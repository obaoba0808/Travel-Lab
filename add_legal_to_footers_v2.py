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

pages = [f for f in sorted(os.listdir('.')) if f.endswith('.html')]
updated = []

for f in pages:
    with open(f, 'rb') as fh:
        raw = fh.read()
    
    # Check if already has legal links
    if b'disclaimer.html' in raw and b'\xe5\x85\x8d\xe8\xb2\xac\xe8\x81\xb2\xe6\x98\x8e' in raw:
        print(f'{f}: already has legal links')
        continue
    
    # Pattern: <p>© 2026...</p>\r\n  </div>\r\n</footer>
    # We need to insert legal div after the copyright <p>
    old_end = b'<p>\xc2\xa9 2026 \xe5\x9d\x87\xe5\x9c\xa8\xe8\xb7\xaf\xe4\xb8\x8a Travel Lab. All Rights Reserved.</p>\r\n  </div>\r\n</footer>'
    if old_end in raw:
        new_end = old_end.replace(
            b'\r\n  </div>\r\n</footer>',
            (b'\r\n' + legal_div.encode('utf-8') + b'\r\n  </div>\r\n</footer>')
        raw = raw.replace(old_end, new_end, 1)
        with open(f, 'wb') as fh:
            fh.write(raw)
        updated.append(f)
        print(f'{f}: legal div added')
    else:
        # Try different year/encoding
        if b'footer-bottom' in raw and b'All Rights Reserved' in raw:
            # Find the footer-bottom section and look at it
            idx = raw.find(b'footer-bottom')
            section = raw[idx:idx+400]
            print(f'{f}: footer-bottom found but pattern mismatch: {section[-200:]}')
        else:
            print(f'{f}: no footer-bottom section')

print(f'\nUpdated {len(updated)} pages: {updated}')