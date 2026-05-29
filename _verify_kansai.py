import sys
sys.stdout.reconfigure(encoding='utf-8')
c=open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\kansai-pass.html','r',encoding='utf-8').read()
form=c.find('class="lead-inline"')
foot=c.find('<footer')
print(f'Form: @{form}, Footer: @{foot}')
print(f'Form < Footer? {form < foot}')
if form>0:
    print(f'Context: {repr(c[form-50:form+100])}')
