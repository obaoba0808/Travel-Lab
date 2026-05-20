import re
import os

def count_content_words(html_content):
    """計算 <main> 標籤內的實際內容字數（中文+英文）"""
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
    if not main_match:
        return 0, 0, 0
    
    main_content = main_match.group(1)
    
    # 移除 HTML 標籤
    text = re.sub(r'<[^>]+>', ' ', main_content)
    
    # 移除多餘空白
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 計算中文字數（CJK 統一表意文字）
    chinese_count = len(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))
    
    # 計算英文單字數
    english_count = len(re.findall(r'[a-zA-Z]+', text))
    
    # 總字數（中文 + 英文）
    total = chinese_count + english_count
    
    return total, chinese_count, english_count

# 掃描所有 HTML 檔案
results = []
for fname in os.listdir('.'):
    if fname.endswith('.html'):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        total, chinese, english = count_content_words(content)
        results.append((fname, total, chinese, english))

# 依內文字數排序（由小到大）
results.sort(key=lambda x: x[1])

# 輸出結果
print('實際內文字數統計（<main> 內純文字）')
print('=' * 85)
print(f'{"檔案名稱":<45} {"總字數":>8} {"中文":>8} {"英文":>8} {"低於600?":>10}')
print('-' * 85)

for fname, total, chinese, english in results:
    under = '*** <600' if total < 600 else ''
    print(f'{fname:<45} {total:>8} {chinese:>8} {english:>8} {under:>10}')
