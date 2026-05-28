import re

with open('tokyo-5days.html', 'rb') as f:
    raw = f.read()

# Decode to check values
content = raw.decode('utf-8', errors='replace')

# Find the corrupted title section using raw bytes
# Pattern: <title>><title><meta name="author" content="均在路上">東京5天4夜自由行懶人包 Travel Lab</title>
# Fix: remove the ><title><meta name="author"...> part from inside the title tag

# Use raw bytes to handle properly
corrupted_pattern = b'<title>><title><meta name="author" content="\xe5\x9d\x87\xe5\x9c\xa8\xe8\xb7\xaf\xe4\xb8\x8a">\xe6\x9d\xb1\xe4\xba\xac\xe8\x87\xaa\xe7\x94\xb1\xe8\xa1\x8c5\xe5\xa4\xa94\xe5\xa4\x9c\xe8\xa1\x8c\xe7\xa8\x8b\xe8\xa1\xa8\xef\xbd\x9c\xe5\x9d\x87\xe5\x9c\xa8\xe8\xb7\xaf\xe4\xb8\x8a Travel Lab</title>'

# The fixed version: just the clean title tag
fixed_pattern = b'<title>\xe6\x9d\xb1\xe4\xba\xac\xe8\x87\xaa\xe7\x94\xb1\xe8\xa1\x8c5\xe5\xa4\xa94\xe5\xa4\x9c\xe8\xa1\x8c\xe7\xa8\x8b\xe8\xa1\xa8\xef\xbd\x9c\xe5\x9d\x87\xe5\x9c\xa8\xe8\xb7\xaf\xe4\xb8\x8a Travel Lab</title>'

if corrupted_pattern in raw:
    new_raw = raw.replace(corrupted_pattern, fixed_pattern)
    print('Found and replaced!')
    
    # Also fix the double > after description content
    # The pattern after fix will be: ...description" content="...">>...  
    # Need to fix that too
    double_gt = b'">><meta name="keywords"'
    single_gt = b'"><meta name="keywords"'
    if double_gt in new_raw:
        new_raw = new_raw.replace(double_gt, single_gt)
        print('Fixed double >> in description')
    
    with open('tokyo-5days.html', 'wb') as f:
        f.write(new_raw)
    
    # Verify
    with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
        verify = f.read()
    titles = re.findall(r'<title>.*?</title>', verify, re.DOTALL)
    for t in titles:
        print('New title tag:', repr(t[:100]))
        print('Clean?', '<' not in t[7:-8])
else:
    print('Pattern not found! Let me check raw:')
    idx = raw.find(b'<title>')
    print(raw[idx:idx+300])
