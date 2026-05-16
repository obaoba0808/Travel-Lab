#!/usr/bin/env python3
"""Read footer structure from about.html"""
import os

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find footer section
idx = content.find('<footer')
if idx >= 0:
    footer = content[idx:idx+800]
    print('Footer found:')
    print(footer)
else:
    print('No footer found')

# Check for privacy link
import re
privacy_links = re.findall(r'href="[^"]*privacy[^"]*"', content)
print('\nPrivacy links:', privacy_links)
terms_links = re.findall(r'href="[^"]*terms[^"]*"', content)
print('Terms links:', terms_links)
