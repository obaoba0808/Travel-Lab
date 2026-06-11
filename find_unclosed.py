import re

with open('korea-transport.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where net div count exceeds 3 (missing closing divs)
open_count = 0
close_count = 0
unbalanced_line = -1
for i, line in enumerate(lines):
    open_count += line.count('<div')
    close_count += line.count('</div>')
    net = open_count - close_count
    if net > 3:
        unbalanced_line = i
        print(f"First unbalanced point: line {i+1}, net={net}")
        print(f"  Content: {lines[i][:150].strip()}")
        break

# Strategy: find the FOOTER and work backwards
# The missing </div>s are likely before </body>
# Let's find all unclosed divs by scanning from end
print("\n--- Scanning from end to find where to insert </div> ---")
open_count = 0
close_count = 0
for i in range(len(lines)-1, -1, -1):
    open_count += lines[i].count('<div')
    close_count += lines[i].count('</div>')
    if close_count > open_count and open_count > 0:
        print(f"Line {i+1}: close_count={close_count}, open_count={open_count}")
        print(f"  Content: {lines[i][:100].strip()}")
        break
