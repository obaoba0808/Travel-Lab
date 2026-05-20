import re, os

def count_real_content(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to find main content container
    # Pattern 1: <div class="article-container">
    m = re.search(r'<div class="article-container">(.*?)</div>\s*<!-- /article-container -->', content, re.DOTALL)
    if not m:
        # Pattern 2: content between hero and related-posts
        m = re.search(r'class="hero-title"[^>]*>.*?</div>\s*<div[^>]*>', content, re.DOTALL)
        # Fallback: get everything after </h1> or </h2> until footer
        m = re.search(r'</h1>.*?<footer', content, re.DOTALL)
    if not m:
        m = re.search(r'<body[^>]*>(.*?)</footer', content, re.DOTALL)
    
    if m:
        text = m.group(1)
    else:
        text = content
    
    # Remove script/style/trip promo/nav/related posts
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'class="related-posts[^"]*"', '', text)
    text = re.sub(r'class="trip-dynamic-banner[^"]*"', '', text)
    text = re.sub(r'class="trip-promo-inline[^"]*"', '', text)
    
    # Remove all HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Count
    chinese = len(re.findall(r'[\u4e00-\u9fff]', text))
    english_words = len(re.findall(r'[a-zA-Z]+', text))
    return chinese + english_words, chinese, english_words, len(text)

pages = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('404.html','_live_index.html')]
results = []

for f in pages:
    total, chinese, en, raw_len = count_real_content(f)
    results.append((f, total, chinese, en, raw_len))

results.sort(key=lambda x: x[1])
print('=== 實際內文字數（修正版）===')
print(f'{"File":<38} {"Total":>6} {"Chinese":>7} {"EN":>5} {"RawLen":>7}')
print('-' * 72)
for f, total, chinese, en, raw in results:
    marker = ' *** <600' if total < 600 else ''
    print(f'{f:<38} {total:>6} {chinese:>7} {en:>5} {raw:>7} {marker}')
