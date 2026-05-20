import glob, re

def count_words(html):
    """Count Chinese characters + English words in HTML content"""
    # Remove script/style tags
    c = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.S|re.I)
    c = re.sub(r'<style[^>]*>.*?</style>', '', c, flags=re.S|re.I)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', c)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Count Chinese characters
    chinese = len(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))
    # Count English words
    english = len(re.findall(r'[a-zA-Z]{2,}', text))
    return chinese + english, text

results = []
for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    wc, text = count_words(c)
    results.append((f, wc, len(c)))

# Sort by word count
results.sort(key=lambda x: x[1])

print('=== Page word counts (ascending) ===')
print(f'{"File":<40} {"Words":>6} {"Bytes":>8}')
print('-' * 56)
for f, wc, bc in results:
    flag = ' *** UNDER 600' if wc < 600 else ''
    print(f'{f:<40} {wc:>6} {bc:>8}{flag}')
