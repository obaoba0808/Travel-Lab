import os, re, glob

old = '#f4f0e8'
new = '#e8f8f7'

files = glob.glob('*.html') + glob.glob('*.css')
total = 0

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
    except:
        continue
    if old not in content:
        continue
    new_content = content.replace(old, new)
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(new_content)
    count = content.count(old)
    print(f"[OK] {f}: {count} replaced")
    total += count

print(f"\nTotal: {total} replacements in {files.__len__()} files")