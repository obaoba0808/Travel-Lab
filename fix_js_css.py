import re

file_path = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\js\monetization.js"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: remove extra ) in CSS grid-template-columns
old = 'grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)));'
new = 'grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));'

if old in content:
    content = content.replace(old, new)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed: extra ) removed from grid-template-columns")
else:
    print("WARN: pattern not found, checking file...")
    # Find the actual line
    for i, line in enumerate(content.split('\n')):
        if 'grid-template-columns' in line:
            print(f"  Line {i+1}: {line.strip()}")