with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\japan-travel.html', 'rb') as f:
    raw = f.read()
norm = raw.replace(b'\r\r\n', b'\n').replace(b'\r\n', b'\n')
text = norm.decode('utf-8', errors='replace')

idx = text.find('category-hero')
snippet = text[idx:idx+600]
print('snippet length:', len(snippet))

for cls in ['hero-img-full','hero-title-block','hero-region-tag','hero-main-title']:
    print(cls + ':', cls in text)

# Show what class= values exist in category-hero section
import re
matches = re.findall(r'class="([^"]+)"', snippet)
print('classes in category-hero block:', matches)