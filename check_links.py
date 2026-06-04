import fitz
doc = fitz.open('pdfs/busan-capsule-guide-with-links.pdf')
total = sum(len(p.get_links()) for p in doc)
print(f'Links: {total}')
doc.close()
