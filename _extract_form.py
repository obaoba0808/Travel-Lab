import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

with open(os.path.join(base, 'tokyo-5days.html'), 'r', encoding='utf-8') as f:
    sample = f.read()

start = sample.find('class="lead-inline"')
end = sample.find('</form>', start)
end_outer = sample.find('</div>', end + 6)
end_outer2 = sample.find('</div>', end_outer + 6)

block = sample[start:end_outer2+6]

# Save to file for inspection
with open(os.path.join(base, '_form_block.txt'), 'w', encoding='utf-8') as f:
    f.write(block)

print(f"Extracted {len(block)} chars to _form_block.txt")
