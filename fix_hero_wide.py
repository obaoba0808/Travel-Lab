with open('style.css', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the height:240px from category-hero media query
c = c.replace('.category-hero, .article-hero { height:240px; }',
              '.category-hero, .article-hero { height:auto; min-height:0; }')

# Fix .category-hero img to use contain (show full image)
c = c.replace('.category-hero img { width:100%; height:100%; object-fit:cover; }',
              '.category-hero img { width:100%; height:auto; object-fit:contain; display:block; }')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(c)
print('OK - style.css fixed')
