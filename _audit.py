import glob, re
for f in sorted(glob.glob('*.html')):
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    urls = re.findall(r'trip\.com/t/(\w+)', c)
    if urls:
        print(f'{f}: {",".join(set(urls))}')
