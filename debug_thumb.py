#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\tokyo-5days.html', 'rb')
c = f.read()
f.close()

# Find post-thumb img
idx = c.find(b'class="post-thumb"')
if idx == -1:
    print('NOT FOUND: post-thumb')
else:
    # Print 200 chars around it
    start = max(0, idx)
    end = min(len(c), idx + 300)
    print('FOUND post-thumb at position:', idx)
    print(c[start:end].decode('utf-8', errors='replace'))

# Also find the a tag with href
idx2 = c.find(b'<a href="tokyo-5days.html">')
if idx2 == -1:
    print('NOT FOUND: a href')
else:
    start = max(0, idx2)
    end = min(len(c), idx2 + 400)
    print('FOUND a href at position:', idx2)
    print(c[start:end].decode('utf-8', errors='replace'))
