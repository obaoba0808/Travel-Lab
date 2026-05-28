import os, re

# Read the EXACT CSS currently in kansai-pass.html
with open('kansai-pass.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the start of popup CSS
start = c.find('.lead-popup-overlay{display:none')
if start == -1:
    print('ERROR: popup CSS not found')
    exit(1)

# Find the end: after .lead-note{...} before </style>
# Look for .lead-note then }
idx_note = c.find('.lead-note', start)
if idx_note == -1:
    print('ERROR: .lead-note not found')
    exit(1)

idx_brace = c.find('}', idx_note)
if idx_brace == -1:
    print('ERROR: closing brace not found')
    exit(1)

end = idx_brace + 1
old_css = c[start:end]
print(f'Found old CSS ({len(old_css)} chars):')
print(repr(old_css[:200]))
print('...')
print(repr(old_css[-100:]))
