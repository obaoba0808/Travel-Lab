import os, re

# Read actual content from kansai-pass.html to get exact closeLeadPopup function
with open('kansai-pass.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find closeLeadPopup function
idx = c.find('function closeLeadPopup')
if idx == -1:
    print('ERROR: closeLeadPopup not found in kansai-pass.html')
    exit(1)

# Find the end of this function (next } that matches)
# Simple approach: find the closing } after the function start
rest = c[idx:]
brace_count = 0
end_idx = 0
started = False
for i, ch in enumerate(rest):
    if ch == '{':
        brace_count += 1
        started = True
    elif ch == '}':
        brace_count -= 1
        if started and brace_count == 0:
            end_idx = i
            break

func_body = rest[:end_idx+1]
print('Found closeLeadPopup function:')
print(func_body)
print()

# Also find the scroll listener
idx2 = c.find("localStorage.getItem('leadSent')")
if idx2 >= 0:
    print('Found scroll check:')
    print(repr(c[idx2-5:idx2+60]))
else:
    print('ERROR: scroll listener not found')
