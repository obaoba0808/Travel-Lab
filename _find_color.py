import os, re, glob

# Target color to replace
old = '#f4f0e8'  # 燕麥米色
# New Tiffany light shade - a very light mint/tiffany
new = '#e8f8f7'  # 淺蒂芙尼薄荷色，比 Tiffany 綠更淡，背景適用

count = 0
files_changed = []

for f in glob.glob('*.html') + glob.glob('*.css'):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
    except:
        continue
    
    if old not in content:
        continue
    
    # Count occurrences
    occurrences = content.count(old)
    files_changed.append((f, occurrences))
    count += occurrences

print(f"Found {old} in {len(files_changed)} files ({count} total occurrences):\n")
for f, n in files_changed:
    print(f"  {f}: {n} 次")