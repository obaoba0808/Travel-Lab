import sys
sys.stdout.reconfigure(encoding='utf-8')
c=open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\esim-comparison.html','r',encoding='utf-8').read()
# Find key structural elements
table_close=c.find('</table>')
article_close=c.rfind('</article>')
main_close=c.rfind('</main>')
footer=c.find('<footer')
print(f'table close: @{table_close}')
print(f'article close: @{article_close}')
print(f'main close: @{main_close}')
print(f'footer: @{footer}')
if table_close>0:
    print(f'Around </table>: {repr(c[table_close-80:table_close+100])}')
if article_close>0:
    print(f'Around </article>: {repr(c[article_close-80:article_close+100])}')
if main_close>0:
    print(f'Around </main>: {repr(c[main_close-80:main_close+100])}')
print(f'Around footer: {repr(c[footer-100:footer+50])}')
