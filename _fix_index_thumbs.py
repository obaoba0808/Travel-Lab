import re, sys
base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\index.html'
with open(base, 'rb') as f:
    content = f.read()

# Find all post-thumb img src
pattern = rb'class="post-thumb[^"]*"[^>]*>.<img[^>]*src="([^"]+)"'
matches = re.findall(pattern, content)
print(f"Found {len(matches)} post-thumb images:")
for m in matches:
    print(' ', m.decode())
