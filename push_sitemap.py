#!/usr/bin/env python3
import os, subprocess
BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)
subprocess.run(['git', 'add', 'sitemap.xml'], capture_output=True)
msg = u'\u66f4\u65b0sitemap.xml\uff1a\u65b0\u589e24\u500bURL\uff081\u6cdb\u6cdb\u6cdb\u9762+3\u500b\u6cdb\u5f8b\u9801\u9762\uff09'
with open('commit_msg.txt', 'w', encoding='utf-8') as f: f.write(msg)
subprocess.run(['git', 'commit', '-F', 'commit_msg.txt'], capture_output=True)
os.remove('commit_msg.txt')
r = subprocess.run(['git', 'push'], capture_output=True, encoding='utf-8', errors='replace', timeout=90)
print('Push:', r.stderr[:300] if r.stderr else 'OK')