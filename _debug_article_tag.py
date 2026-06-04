# -*- coding: utf-8 -*-
# Debug: 找出 tokyo-5days.html 中所有包含 "article" 的標籤

with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找出所有包含 "article" 的字串（大小寫不敏感）
import re
matches = re.findall(r'<\/?article[^>]*>', content, re.IGNORECASE)

print('[DEBUG] 找到以下 article 相關標籤:')
for i, match in enumerate(matches, 1):
    print(f'  [{i}] {match}')

# 也檢查是否有其他可能的結束標籤
print('\n[DEBUG] 檢查其他可能的結束標籤...')
if '</main>' in content:
    print('  ✅ 找到 </main>')
if '</section>' in content:
    print('  ✅ 找到 </section>')
if '</div>' in content:
    print('  ⚠️  找到 </div> (可能 article 被包在 div 中)')

# 顯示最後 50 行內容
lines = content.split('\n')
print(f'\n[DEBUG] 檔案最後 30 行:')
for i, line in enumerate(lines[-30:], len(lines)-29):
    print(f'{i:4d}: {line[:120]}')
