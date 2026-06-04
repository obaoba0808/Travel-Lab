import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8')

pdf = fitz.open('pdfs/bangkok-food-map-with-links.pdf')

print('=== Verification: bangkok-food-map-with-links.pdf ===')
print('Pages:', pdf.page_count)
print('')

total = 0
for i in range(pdf.page_count):
    page = pdf[i]
    links = page.get_links()
    print(f'Page {i+1}: {len(links)} links')
    
    for j, link in enumerate(links):
        if 'uri' in link:
            uri = link['uri']
            short = uri[:60] + '...' if len(uri) > 60 else uri
            print(f'  Link {j+1}: {short}')
            total += 1

print('')
print('Total links:', total)

# Check Klook links
print('')
print('Klook links (first 2 pages):')
for i in range(min(2, pdf.page_count)):
    page = pdf[i]
    for link in page.get_links():
        if 'uri' in link and 'klook' in link['uri'].lower():
            uri = link['uri']
            print(f'  Page {i+1}: {uri[:100]}...' if len(uri) > 100 else f'  Page {i+1}: {uri}')
