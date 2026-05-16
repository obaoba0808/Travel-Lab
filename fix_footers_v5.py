#!/usr/bin/env python3
import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# The legal div to insert (as bytes)
legal_div = (
    b'    <div style="margin-top:8px;font-size:12px;">\r\n'
    b'      <a href="about.html" style="color:inherit;margin-right:12px;">\xe9\x97\x9c\xe6\x96\xbc\xe6\x88\x91\xe5\x80\x91</a>\r\n'
    b'      <a href="privacy.html" style="color:inherit;margin-right:12px;">\xe9\x9a\xb1\xe7\xa7\x81\xe6\xac\x8a\xe6\x94\xbf\xe7\xad\x96</a>\r\n'
    b'      <a href="terms.html" style="color:inherit;margin-right:12px;">\xe4\xbd\xbf\xe7\x94\xa8\xe6\xa2\x9d\xe6\xac\x92</a>\r\n'
    b'      <a href="disclaimer.html" style="color:inherit;">\xe5\x85\x8d\xe8\xb2\xac\xe8\x81\xb2\xe6\x98\x8e</a>\r\n'
    b'    </div>'
)

COPYRIGHT_B = b'\xc2\xa9 2026 \xe5\x9d\x87\xe5\x9c\xa8\xe8\xb7\xaf\xe4\xb8\x8a Travel Lab. All Rights Reserved.'

pages = [f for f in sorted(os.listdir('.')) if f.endswith('.html')]
updated = []

for f in pages:
    with open(f, 'rb') as fh:
        raw = fh.read()
    
    if b'\xe5\x85\x8d\xe8\xb2\xac\xe8\x81\xb2\xe6\x98\x8e' in raw:
        print(f + ': already has legal links')
        continue
    
    # Pattern: after copyright <p>...</p>\r\n insert legal div, then close </div>\r\n</footer>
    old_pattern = COPYRIGHT_B + b'</p>\r\n  </div>\r\n</footer>'
    if old_pattern in raw:
        new_pattern = COPYRIGHT_B + b'</p>\r\n' + legal_div + b'\r\n  </div>\r\n</footer>'
        raw = raw.replace(old_pattern, new_pattern, 1)
        with open(f, 'wb') as fh:
            fh.write(raw)
        updated.append(f)
        print(f + ': legal div added')
    else:
        if b'footer-bottom' in raw:
            idx = raw.find(b'footer-bottom')
            print(f + ': pattern differs - ' + repr(raw[idx:idx+250]))
        else:
            print(f + ': no footer-bottom')

print('Updated ' + str(len(updated)) + ' pages')