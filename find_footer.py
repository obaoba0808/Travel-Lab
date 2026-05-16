#!/usr/bin/env python3
"""Fix remaining footers by searching for footer-bottom div and replacing"""
import os, re

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# Read tokyo-5days as raw to find exact footer pattern
with open('tokyo-5days.html', 'rb') as f:
    raw = f.read()

# Find footer-bottom section
footer_idx = raw.find(b'footer-bottom')
if footer_idx >= 0:
    snippet = raw[footer_idx:footer_idx+500]
    print('Footer section (raw bytes):')
    print(snippet)
else:
    print('No footer-bottom found')