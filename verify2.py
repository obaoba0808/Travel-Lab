import re
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\kyoto-temples.html', 'r', encoding='utf-8') as f:
    content = f.read()
imgs = re.findall(r'src="images/(kyoto-.*?\.webp)"', content)
print("Images found:", imgs)
# check figcaption exists
caps = re.findall(r'<figcaption[^>]*>(.*?)</figcaption>', content, re.DOTALL)
print(f"Figcaptions found: {len(caps)}")
for i, c in enumerate(caps):
    clean = re.sub(r'<[^>]+>', '', c).strip()[:80]
    print(f"  Cap {i+1}: {clean}")