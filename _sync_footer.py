import re, glob

# Read index.html and extract canonical footer
c = open('index.html', 'r', encoding='utf-8').read()
start = c.index('<footer class="site-footer">')
# Find </footer> and include it
end = c.index('</footer>') + len('</footer>')
canonical_footer = c[start:end]

print(f"Canonical footer length: {len(canonical_footer)} chars")
print("First 100 chars:", canonical_footer[:100])
print("Last 100 chars:", canonical_footer[-100:])

# Now read all other HTML files and replace their footer
files = [f for f in glob.glob('*.html') if f != 'index.html']
print(f"\nFound {len(files)} HTML files to update")

updated = 0
for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    
    # Find footer start and end in this file
    idx_start = content.find('<footer class="site-footer">')
    if idx_start == -1:
        print(f"⚠️  {f}: no <footer class='site-footer'> found, skipping")
        continue
    
    idx_end = content.index('</footer>', idx_start) + len('</footer>')
    
    # Replace footer
    new_content = content[:idx_start] + canonical_footer + content[idx_end:]
    
    open(f, 'w', encoding='utf-8').write(new_content)
    updated += 1
    print(f"✅ {f}: footer replaced")

print(f"\nDone! Updated {updated} pages.")
