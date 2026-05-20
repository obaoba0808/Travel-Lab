import re

with open('tokyo-5days.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove head, script, style, nav, footer, related, sidebar, banners
clean = re.sub(r'<head.*?</head>', '', content, flags=re.DOTALL)
clean = re.sub(r'<script[^>]*>.*?</script>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'<style[^>]*>.*?</style>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'<nav[^>]*>.*?</nav>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'<footer[^>]*>.*?</footer>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="related-posts[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="sidebar-card[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="trip-dynamic-banner[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="trip-promo-inline[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="three-col-wrapper[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="breadcrumb-bar[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="hero[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="hero-title[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)
clean = re.sub(r'class="site-topbar[^"]*".*?</div>', ' ', clean, flags=re.DOTALL)

# Remove all HTML tags
clean = re.sub(r'<[^>]+>', ' ', clean)
clean = re.sub(r'\s+', ' ', clean).strip()

chinese = len(re.findall(r'[\u4e00-\u9fff]', clean))
english = len(re.findall(r'[a-zA-Z]+', clean))
total = chinese + english

print(f'=== tokyo-5days.html 擴充後字數 ===')
print(f'中文：{chinese} 字')
print(f'英文：{english} 字')
print(f'總計：{total} 字')
print(f'狀態：{"✅ 已達600字" if total >= 600 else "❌ 還差 " + str(600-total) + " 字"}')
print(f'\n前300字預覽：{clean[:300]}...')
