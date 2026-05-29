import sys
sys.stdout.reconfigure(encoding='utf-8')
c=open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\kansai-pass.html','r',encoding='utf-8').read()
forms=[i for i in range(len(c)) if c[i:i+20]=='class="lead-inline"']
print(f'Found {len(forms)} lead-inline forms: {forms}')
for i,pos in enumerate(forms):
    ctx=c[pos-30:pos+50]
    print(f'Form {i+1} @{pos}: {repr(ctx)}')
