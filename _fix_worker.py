import re
path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\worker_email_reply.js'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Google Sheet with Formspree
code = code.replace(
    "const GOOGLE_SHEET_URL = GOOGLE_SHEET_WEBAPP_URL || '';",
    "const FORMSPREE_ENDPOINT = 'https://formspree.io/f/xredjjgb';"
)

# Remove the Google Sheets block
code = re.sub(
    r'\s*// Also save to Google Sheets[\s\S]*?\}\n',
    '\n',
    code
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print('Formspree added:', 'xredjjgb' in code)
print('Google Sheet removed:', 'GOOGLE_SHEET_URL' not in code)
print('FORMSPREE_ENDPOINT present:', 'FORMSPREE_ENDPOINT' in code)