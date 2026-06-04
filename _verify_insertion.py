# -*- coding: utf-8 -*-
import re

# 讀取 tokyo-5days.html
with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 檢查是否包含 SlideShare iframe
if 'slideshare.net' in content:
    print('✅ 找到 SlideShare 嵌入程式碼')
    
    # 找出所有 SlideShare 連結
    matches = re.findall(r'https://www\.slideshare\.net[^\s"\'<>]+', content)
    for i, url in enumerate(matches, 1):
        print(f'   [{i}] {url[:80]}...')
else:
    print('❌ 未找到 SlideShare 嵌入程式碼')

# 檢查是否包含 Formspree 表單
if 'formspree.io' in content:
    print('✅ 找到 Formspree 表單')
    
    # 找出 form action
    match = re.search(r'action="([^"]*formspree[^"]*)"', content)
    if match:
        print(f'   Form action: {match.group(1)}')
else:
    print('❌ 未找到 Formspree 表單')

# 檢查 </article> 前是否有插入內容
if '</article>' in content:
    index = content.index('</article>')
    preceding = content[max(0, index-500):index]
    
    if 'slideshare-section' in preceding:
        print('✅ SlideShare 區塊已正確插入在 </article> 之前')
        print(f'   插入位置: 第 {content[:index].count(chr(10))} 行附近')
    else:
        print('⚠️  </article> 前未找到 SlideShare 區塊')
        
print('\n✅ 驗證完成')
