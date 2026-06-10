import re, glob

thin_pages = ['bangkok-4days.html', 'seoul-5days.html', 'korea-transport.html', 'vietnam-hochiminh.html',
              'korea-budget.html', 'thailand-sim.html', 'tokyo-accommodation.html']

for f in thin_pages:
    c = open(f, 'r', encoding='utf-8').read()
    
    # Find structural markers
    tw = c.find('three-col-wrapper')
    footer = c.find('<footer')
    
    if tw > 0 and footer > 0:
        chunk = c[tw:footer]
        text = re.sub(r'<[^>]+>', '', chunk).strip()
        text_len = len(text)
        
        # Count meaningful content
        h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', chunk, re.DOTALL)
        titles = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
        meaningful = [t for t in titles if '延伸閱讀' not in t and '常見問題' not in t]
        
        print(f'\n=== {f} ===')
        print(f'  Text length: {text_len} chars')
        print(f'  H2s: {titles[:5]}')
        print(f'  Meaningful H2s: {meaningful}')
        
        # Show what's between hero and first FAQ/related
        hero_end = c.find('</section>')
        faq = c.find('faq-section')
        related = c.find('related-posts')
        
        if hero_end > 0:
            end_pos = min(faq, related) if min(faq, related) > 0 else len(c)
            article_chunk = c[hero_end:end_pos]
            article_text = re.sub(r'<[^>]+>', '', article_chunk).strip()
            print(f'  Article text length: {len(article_text)} chars')
            if len(article_text) < 200:
                print(f'  ❌ VIRTUALLY NO ARTICLE CONTENT')