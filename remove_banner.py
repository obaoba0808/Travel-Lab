# Remove charter banner from index.html
p = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab\index.html'
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

old = '''    <!-- CHARTER BANNER -->
    <div style="max-width:1100px;margin:0 auto 30px;padding:0 40px;">
      <a href="about.html"><img loading="lazy" src="images/charter-banner.webp" alt="台灣包車自由行" style="width:100%;border-radius:12px;display:block;" width="2179" height="722"></a>
    </div>
'''
c = c.replace(old, '')
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    f.write(c)
print('done')
