import fitz
doc = fitz.open('downloads/bangkok-food-map.pdf')
total = sum(len(p.get_links()) for p in doc)
print(f'Links in bangkok-food-map.pdf: {total}')
if total == 0:
    print('GOOD: No links (original version)')
else:
    print('WARNING: Has links already!')
doc.close()
