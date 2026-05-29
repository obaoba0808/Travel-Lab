import os, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# Check taiwan-travel.html structure - find all closing tags near the end
with open(os.path.join(base, 'taiwan-travel.html'), 'r', encoding='utf-8') as f:
    c = f.read()

# Find the last 2000 chars and look for structural elements
tail = c[-3000:]
with open(os.path.join(base, '_tail_check.txt'), 'w', encoding='utf-8') as out:
    out.write(f"File length: {len(c)}\n\n")
    out.write("--- LAST 3000 CHARS ---\n")
    out.write(tail)
    
# Also search for key markers
markers = ['</main>', '</article>', '<footer', '</body>', '</html>', 'KLOOK', 'klk-aff', 'faq-item', 'class="footer']
out2 = open(os.path.join(base, '_markers.txt'), 'w', encoding='utf-8')
for m in markers:
    positions = [i for i in range(len(c)) if c[i:].startswith(m)]
    if positions:
        out2.write(f"{m}: found at {positions[-1]} (last occurrence)\n")
        # Show context
        ctx = c[max(0,positions[-1]-50):positions[-1]+len(m)+50]
        out2.write(f"  context: ...{ctx}\n")
    else:
        out2.write(f"{m}: NOT FOUND\n")
out2.close()
print("Check _tail_check.txt and _markers.txt")
