import os

folder = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'

new_col = '''<div class="footer-col">
      <h4>法律資訊</h4>
      <ul>
        <li><a href="about.html">關於我們</a></li>
        <li><a href="contact.html">聯絡我們</a></li>
        <li><a href="privacy.html">隱私權政策</a></li>
        <li><a href="terms.html">使用條款</a></li>
        <li><a href="disclaimer.html">免責聲明</a></li>
      </ul>
    </div>'''

html_files = [f for f in os.listdir(folder) if f.endswith('.html')]

changed = 0
skipped = 0

for fname in html_files:
    path = os.path.join(folder, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has "法律資訊"
    if '法律資訊' in content:
        skipped += 1
        continue

    # Find the footer columns block
    marker = '<div class="footer-col">'
    # Find the LAST footer-col div (after east asia section)
    last_pos = content.rfind(marker)

    if last_pos == -1:
        print(f'WARNING: no footer-col found in {fname}')
        continue

    # Find end of that div
    start_div = content.rfind('<div', 0, last_pos)
    # Find matching </div> for this div
    depth = 0
    pos = last_pos
    end_pos = -1
    while pos < len(content):
        if content[pos:pos+5] == '<div ' or content[pos:pos+6] == '<div>':
            depth += 1
        elif content[pos:pos+6] == '</div>':
            depth -= 1
            if depth == 0:
                end_pos = pos + 6
                break
        pos += 1

    if end_pos == -1:
        print(f'WARNING: could not find end of footer-col in {fname}')
        continue

    new_content = content[:end_pos] + '\n    ' + new_col + '\n' + content[end_pos:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    changed += 1
    print(f'Updated: {fname}')

print(f'\nDone: {changed} files updated, {skipped} skipped (already had 法律資訊)')