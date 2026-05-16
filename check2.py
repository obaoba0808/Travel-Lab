with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\japan-travel.html', 'rb') as f:
    raw = f.read()
norm = raw.replace(b'\r\r\n', b'\n').replace(b'\r\n', b'\n')
text = norm.decode('utf-8', errors='replace')
idx = text.find('category-hero')
snippet = text[idx:idx+600]

# Check what section-divider looks like - the next element after overlay
idx2 = text.find('section-divider')
print('section-divider found:', idx2)
snippet2 = text[idx2:idx2+200]
print('snippet2:', snippet2.encode('ascii', 'backslashreplace').decode('ascii'))

# Check class names in the hero area
import re
classes = re.findall(r'class="([^"]+)"', snippet)
print('classes in category-hero:', classes)
print()
print('hero-title-block in text:', 'hero-title-block' in text)
print('hero-main-title in text:', 'hero-main-title' in text)
print('overlay in text:', 'overlay' in text)