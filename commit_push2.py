#!/usr/bin/env python3
import os, subprocess

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

subprocess.run(['git', 'add', '-A'], capture_output=True)
msg = u'\u6dfb\u52a0\u6cd5\u5f8b\u9801\u9762\uff1a\u96c6\u6210\u689d\u6b3e\u3001\u4f7f\u7528\u689d\u6b3e\u3001\u5155\u6b77\u8072\u660e + \u5168\u7ad9footer\u66f4\u65b0'
with open('commit_msg.txt', 'w', encoding='utf-8') as f:
    f.write(msg)
subprocess.run(['git', 'commit', '-F', 'commit_msg.txt'], capture_output=True)
os.remove('commit_msg.txt')
r = subprocess.run(['git', 'push'], capture_output=True, encoding='utf-8', errors='replace', timeout=90)
print('Push:', r.stderr[:300] if r.stderr else 'OK')