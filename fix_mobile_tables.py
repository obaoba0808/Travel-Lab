#!/usr/bin/env python3
# 全站表格手機版響應式修復
# 問題：手機版表格文字超出容器
# 解決：加入 CSS 讓表格在手機上可橫向滾動 + 文字自動換行

import os, re

# 響應式表格 CSS（加到每個有表格的頁面 <head> 後面）
TABLE_CSS = '''
<style>
/* 響應式表格 - 手機版優化 */
.table-responsive {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1rem 0;
}
.table-responsive table {
  min-width: 600px;
  width: 100%;
}
@media (max-width: 768px) {
  .table-responsive table {
    font-size: 13px;
  }
  .table-responsive th,
  .table-responsive td {
    padding: 8px 6px;
    white-space: nowrap;
  }
  .table-responsive td:last-child {
    white-space: normal;
    min-width: 120px;
  }
}
@media (max-width: 480px) {
  .table-responsive table {
    font-size: 12px;
  }
  .table-responsive th,
  .table-responsive td {
    padding: 6px 4px;
  }
}
</style>
'''

def fix_table_in_file(filepath):
    with open(filepath, encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 檢查是否有表格
    if '<table' not in content.lower():
        return False, 'no table'
    
    # 檢查是否已經有響應式 CSS
    if 'table-responsive' in content:
        return False, 'already fixed'
    
    # 找到第一個 <table 標籤
    table_match = re.search(r'<table[^>]*>', content, re.IGNORECASE)
    if not table_match:
        return False, 'table tag not found'
    
    # 在 <table 前面加上 <div class="table-responsive">
    table_tag = table_match.group(0)
    new_table_tag = f'<div class="table-responsive">{table_tag}'
    content = content.replace(table_tag, new_table_tag, 1)
    
    # 找到對應的 </table> 後面加上 </div>
    # 找最後一個 </table>
    last_table_end = content.rfind('</table>')
    if last_table_end == -1:
        return False, 'closing table not found'
    
    content = content[:last_table_end+8] + '</div>' + content[last_table_end+8:]
    
    # 在 </head> 前加入 CSS
    head_end = content.find('</head>')
    if head_end == -1:
        # 嘗試在 <body> 前加入
        body_start = content.find('<body>')
        if body_start == -1:
            return False, 'no head or body tag'
        content = content[:body_start] + TABLE_CSS + content[body_start:]
    else:
        content = content[:head_end] + TABLE_CSS + content[head_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True, 'fixed'

# 執行修復
files = [f for f in os.listdir('.') if f.endswith('.html')]
fixed = []
skipped = []

for fn in files:
    try:
        success, msg = fix_table_in_file(fn)
        if success:
            fixed.append(fn)
        else:
            skipped.append((fn, msg))
    except Exception as e:
        skipped.append((fn, str(e)))

print(f'Fixed {len(fixed)} files:')
for f in fixed:
    print(f'  ✅ {f}')

print(f'\nSkipped {len(skipped)} files:')
for f, reason in skipped:
    if reason != 'no table':
        print(f'  ⏭️  {f}: {reason}')
