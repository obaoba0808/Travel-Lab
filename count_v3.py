import re, os

def count_page_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove head section entirely
    html_no_head = re.sub(r'<head.*?</head>', '', html, flags=re.DOTALL)
    
    # Remove script and style blocks
    clean = re.sub(r'<script[^>]*>.*?</script>', ' ', html_no_head, flags=re.DOTALL)
    clean = re.sub(r'<style[^>]*>.*?</style>', ' ', clean, flags=re.DOTALL)
    
    # Remove nav, footer, related-posts, sidebar, trip banners
    clean = re.sub(r'<nav[^>]*>.*?</nav>', ' ', clean, flags=re.DOTALL)
    clean = re.sub(r'<footer[^>]*>.*?</footer>', ' ', clean, flags=re.DOTALL)
    clean = re.sub(r'class="related-posts[^"]*"', ' ', clean)
    clean = re.sub(r'class="sidebar-card[^"]*"', ' ', clean)
    clean = re.sub(r'class="trip-dynamic-banner[^"]*"', ' ', clean)
    clean = re.sub(r'class="trip-promo-inline[^"]*"', ' ', clean)
    clean = re.sub(r'class="three-col-wrapper[^"]*"', ' ', clean)
    clean = re.sub(r'class="breadcrumb-bar[^"]*"', ' ', clean)
    clean = re.sub(r'class="hero[^"]*"', ' ', clean)
    clean = re.sub(r'class="hero-title[^"]*"', ' ', clean)
    clean = re.sub(r'class="site-topbar[^"]*"', ' ', clean)
    
    # Remove all remaining HTML tags
    clean = re.sub(r'<[^>]+>', ' ', clean)
    
    # Normalize whitespace
    clean = re.sub(r'\s+', ' ', clean).strip()
    
    # Count
    chinese = len(re.findall(r'[\u4e00-\u9fff]', clean))
    english = len(re.findall(r'[a-zA-Z]+', clean))
    
    return chinese + english, chinese, english, clean[:200]

pages = [f for f in os.listdir('.') if f.endswith('.html') and f not in ('404.html','_live_index.html')]
results = []
for f in pages:
    total, chinese, en, preview = count_page_content(f)
    results.append((f, total, chinese, en))

results.sort(key=lambda x: x[1])
print('=== 實際內文字數（盡可能去除模板）===')
print(f'{"File":<40} {"Total":>6} {"Chinese":>7} {"EN":>5}')
print('-' * 68)
for f, total, chinese, en in results:
    marker = ' *** <600' if total < 600 else ''
    print(f'{f:<40} {total:>6} {chinese:>7} {en:>5} {marker}')
