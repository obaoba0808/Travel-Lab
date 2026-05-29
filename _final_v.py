import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

with open(os.path.join(base, 'taiwan-travel.html'), 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('lead-inline')
# Find </main> position
main_idx = c.find('</main>', idx)
head_end = c.find('</head>')
body_start = c.find('<body')
body_end = c.find('</body>')

with open(os.path.join(base, '_final_verify.txt'), 'w', encoding='utf-8') as out:
    out.write(f"File size: {len(c)}\n")
    out.write(f"lead-inline at: {idx}\n")
    out.write(f"</main> after lead: {main_idx} (diff: {main_idx-idx})\n")
    out.write(f"</head> at: {head_end}\n")
    out.write(f"<body at: {body_start}\n")
    out.write(f"</body> at: {body_end}\n")
    out.write(f"\n--- Is form in HEAD area? {idx < head_end} ---\n")
    out.write(f"\n--- 200 chars before form ---\n")
    out.write(c[max(0,idx-200):idx])
    out.write(f"\n\n--- 300 chars of form ---\n")
    out.write(c[idx:idx+300])
    out.write(f"\n\n--- 200 chars after form ---\n")
    out.write(c[idx+300:idx+500])

print("Saved to _final_verify.txt")
