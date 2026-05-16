#!/usr/bin/env python3
"""Commit and push all Travel Lab changes"""
import os, subprocess

BASE = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
os.chdir(BASE)

# Stage all changes
subprocess.run(['git', 'add', '-A'], capture_output=True)

# Commit with UTF-8 message
msg = u'优化首页：搜索框 + 阅读时间 + 最后更新 + 侧边栏升级'
with open('commit_msg.txt', 'w', encoding='utf-8') as f:
    f.write(msg)
subprocess.run(['git', 'commit', '-F', 'commit_msg.txt'], capture_output=True)
os.remove('commit_msg.txt')

# Push
r = subprocess.run(['git', 'push'], capture_output=True, encoding='utf-8', errors='replace', timeout=90)
print('Push result:', r.stderr[:300] if r.stderr else 'Success')
