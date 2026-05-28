import os

# Check what the scroll listener actually looks like in the files
with open('kansai-pass.html', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

idx = c.find('localStorage.getItem')
if idx >= 0:
    print(repr(c[idx-5:idx+80]))
else:
    print('Not found')
