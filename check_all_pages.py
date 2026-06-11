import os
import subprocess

# Step 1: Restore korea-transport.html from a52b817
subprocess.run(['git', 'checkout', 'a52b817', '--', 'korea-transport.html'])
print("Restored korea-transport.html from a52b817")

# Step 2: Check korea-transport.html
with open('korea-transport.html', 'r', encoding='utf-8') as f:
    c = f.read()
print(f"korea-transport.html size: {len(c)} bytes")
print(f"  Div balance: {c.count('<div')} / {c.count('</div>')}")

# Step 3: Scan ALL html files for suspiciously small sizes
print("\nScanning all HTML files...")
results = []
for fname in os.listdir('.'):
    if fname.endswith('.html'):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        size = len(content)
        div_open = content.count('<div')
        div_close = content.count('</div>')
        # Check article-container content length
        ac_start = content.find('<div class="article-container">')
        ac_end = content.find('<!-- /article-container -->')
        ac_len = -1
        if ac_start > 0 and ac_end > 0:
            ac_len = ac_end - ac_start - 48
        results.append((fname, size, div_open, div_close, ac_len))

# Sort by size
results.sort(key=lambda x: x[1])
print("\nPages with size < 50000 bytes (possibly truncated):")
for fname, size, do, dc, ac in results:
    if size < 50000 or do != dc:
        print(f"  {fname}: {size} bytes, div={do}/{dc}, article-container={ac}")
