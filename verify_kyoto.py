import re
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\kyoto-temples.html', 'r', encoding='utf-8') as f:
    content = f.read()
imgs = re.findall(r'src="images/(kyoto-.*?\.webp)"', content)
print("插入的圖片:", imgs)
caps = re.findall(r'<figcaption[^>]*>(.*?)</figcaption>', content, re.DOTALL)
for i, c in enumerate(caps):
    clean = re.sub(r'<[^>]+>', '', c).strip()[:80]
    print(f"Caption {i+1}: {clean}")