import os

# Move close button outside of header, into the popup container level
old_html = '''<div class="lead-popup-header">
      <button class="lead-popup-close" onclick="closeLeadPopup()">&times;</button>
      <h3>📘 小編獨家攻略，限時免費送</h3>
    </div>'''

new_html = '''<button class="lead-popup-close" onclick="closeLeadPopup()">&times;</button>
    <div class="lead-popup-header">
      <h3>📘 小編獨家攻略，限時免費送</h3>
    </div>'''

count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        content = fp.read()
    if old_html in content:
        content = content.replace(old_html, new_html)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        count += 1

print(f'Updated {count} files - close button moved to popup top-right corner')
