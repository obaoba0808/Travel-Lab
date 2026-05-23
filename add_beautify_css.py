import os

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
updated = 0

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 在 beautify-overrides.css 後面插入 beautify.css
    old = '<link rel="stylesheet" href="beautify-overrides.css">'
    new = '<link rel="stylesheet" href="beautify-overrides.css">\n<link rel="stylesheet" href="beautify.css">'
    
    if old in content and new not in content:
        content = content.replace(old, new)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f'Updated: {fname}')

print(f'\nTotal updated: {updated} files')
