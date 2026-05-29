import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# Check taiwan-travel.html (the one user showed as broken)
with open(os.path.join(base, 'taiwan-travel.html'), 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('lead-inline')
with open(os.path.join(base, '_verify_pos.txt'), 'w', encoding='utf-8') as out:
    out.write(f"Position: {idx}\n\n--- 800 chars BEFORE ---\n")
    out.write(c[max(0,idx-800):idx])
    out.write(f"\n\n--- 300 chars AFTER ---\n")
    out.write(c[idx:idx+300])
print("Saved to _verify_pos.txt")

# Also check total file size and lead-inline count
count = c.count('lead-inline')
print(f"lead-inline occurrences: {count}")
print(f"File size: {len(c)} chars")
