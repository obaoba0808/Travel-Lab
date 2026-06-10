import re, glob

# Find all HTML files where content appears AFTER </main> but BEFORE <footer
# These elements are outside the .site-content container and will have no padding

files = glob.glob('*.html')
problem_pages = []

for f in files:
    c = open(f, 'r', encoding='utf-8').read()
    
    # Find </main> and <footer>
    main_end = c.find('</main>')
    footer_start = c.find('<footer')
    
    if main_end == -1 or footer_start == -1:
        continue
    
    # Check if there's significant content between </main> and <footer>
    between = c[main_end + len('</main>'):footer_start].strip()
    
    # Remove whitespace-only content
    between_clean = re.sub(r'\s+', '', between)
    
    if len(between_clean) > 50:  # More than 50 chars of actual content outside main
        problem_pages.append((f, len(between_clean)))
        print(f"❌ {f}: {len(between_clean)} chars of content OUTSIDE </main>")

print(f"\nTotal problem pages: {len(problem_pages)}")
