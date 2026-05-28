# -*- coding: utf-8 -*-
# Copy English-named PDFs to Chinese-named PDFs (for Worker compatibility)
import os, shutil, json, base64

DL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")

# Read the mapping from Worker
mapping = {}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "worker_email_reply.js"), "r", encoding="utf-8") as f:
    content = f.read()

# Extract key -> Chinese filename from PDF_LINKS
import re
# Pattern: 'key': 'https://golightly.fun/downloads/ChineseName.pdf'
pattern = r"'([^']+)':\s*'https://golightly\.fun/downloads/([^']+\.pdf)'"
matches = re.findall(pattern, content)

for key, chn_name in matches:
    eng_name = key + ".pdf"
    mapping[eng_name] = chn_name

print("Found " + str(len(mapping)) + " mappings")

ok = 0
for eng, chn in mapping.items():
    src = os.path.join(DL, eng)
    dst = os.path.join(DL, chn)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        ok += 1
        print("  OK: " + eng + " -> " + chn)
    else:
        print("  SKIP (not found): " + eng)

print("Copied " + str(ok) + " of " + str(len(mapping)) + " files")
