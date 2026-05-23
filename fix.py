import re
for f,p in [
    ("vietnam-danang.html","vietnam-danang-hero.webp"),
    ("bangkok-massage.html","bangkok-massage-hero.webp"),
    ("jiufen.html","jiufen-hero.webp"),
    ("taipei-food.html","taipei-food-hero.webp"),
    ("korea-budget.html","korea-budget-hero.webp")
]:
    c = open(f,'rb').read().decode('utf-8')
    n = re.sub(
        r'<img class="hero-full-img"[^>]*src="images/[^"]*-hero\.webp"[^>]*>',
        f'<img class="hero-full-img" src="images/{p}" alt="Hero">',
        c, count=1
    )
    if n != c:
        open(f,'wb').write(n.encode('utf-8'))
        print('OK:', f, '->', p)
    else:
        print('SKIP:', f)
