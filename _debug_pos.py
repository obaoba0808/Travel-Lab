import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# Check a page that HAD the form correctly (tokyo-5days)
with open(os.path.join(base, 'osaka-usj.html'), 'r', encoding='utf-8') as f:
    c = f.read()

# Find lead-inline position relative to FAQ
idx = c.find('lead-inline')
if idx > 0:
    # Show 500 chars before
    before = c[max(0,idx-600):idx]
    print("=== BEFORE LEAD (osaka-usj.html) ===")
    # Write to file to avoid encoding issues
    with open(os.path.join(base, '_debug_pos.txt'), 'w', encoding='utf-8') as out:
        out.write(f"POSITION: {idx}\n\n--- BEFORE ---\n{before}\n\n--- AFTER ---\n{c[idx:idx+200]}")
    print(f"Position: {idx}, saved to _debug_pos.txt")

# Now check a broken one (taiwan-travel)
with open(os.path.join(base, 'taiwan-travel.html'), 'r', encoding='utf-8') as f:
    c2 = f.read()
idx2 = c2.find('lead-inline')
if idx2 > 0:
    with open(os.path.join(base, '_debug_pos2.txt'), 'w', encoding='utf-8') as out:
        out.write(f"POSITION: {idx2}\n\n--- BEFORE ---\n{c2[max(0,idx2-800):idx2]}\n\n--- AFTER ---\n{c2[idx2:idx2+200]}")
    print(f"Position (broken): {idx2}, saved to _debug_pos2.txt")
