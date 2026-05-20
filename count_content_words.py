import re, os

pages = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('404.html','_live_index.html')]
results = []
for f in pages:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    # Extract content inside <article> tags (main content area)
    article_match = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
    if article_match:
        text = article_match.group(1)
    else:
        # Fallback: get everything after hero section, before footer
        body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
        if body_match:
            text = body_match.group(1)
            # Remove nav, footer, script, style
            text = re.sub(r'<nav[^>]*>.*?</nav>', '', text, flags=re.DOTALL)
            text = re.sub(r'<footer[^>]*>.*?</footer>', '', text, flags=re.DOTALL)
            text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
            text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        else:
            text = content
    # Strip all HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Count: Chinese chars + English words
    chinese = len(re.findall(r'[\u4e00-\u9fff]', text))
    english_words = len(re.findall(r'[a-zA-Z]+', text))
    total = chinese + english_words
    results.append((f, total, chinese, english_words))

results.sort(key=lambda x: x[1])
print('=== 實際內文內容字數（中文數+英文單字數）===')
print(f'{"File":<40} {"Total":>6} {"Chinese":>7} {"EN":>6}')
print('-' * 62)
for f, total, chinese, en in results:
    marker = ' *** <600' if total < 600 else ''
    print(f'{f:<40} {total:>6} {chinese:>7} {en:>6} {marker}')
