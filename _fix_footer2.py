import re

f = 'tokyo-accommodation.html'
c = open(f, 'r', encoding='utf-8').read()

# The problem: footer starts at 13307, last </div> is at 13300
# We need to insert the proper closing structure between them

# Current: </div>\n<footer class="site-footer">
# Should be: </div><!-- /related-posts --></div><!-- /article-container --></div><!-- /col-center --></div><!-- /three-col-wrapper --><!-- FOOTER -->\n<footer class="site-footer">

old = '</div>\n<footer class="site-footer">'
new = '</div><!-- /related-posts --></div><!-- /article-container --></div><!-- /col-center --></div><!-- /three-col-wrapper --><!-- FOOTER -->\n<footer class="site-footer">'

if old in c:
    c = c.replace(old, new, 1)  # Replace only first occurrence
    open(f, 'w', encoding='utf-8').write(c)
    print(f'✅ Fixed {f}')
else:
    print('Pattern not found, trying alternative...')
    # Try with different whitespace
    old2 = '</div>\n\n<footer class="site-footer">'
    if old2 in c:
        c = c.replace(old2, new, 1)
        open(f, 'w', encoding='utf-8').write(c)
        print(f'✅ Fixed {f} (alternative pattern)')
    else:
        print('Still not found, checking raw bytes...')
        footer_pos = c.find('<footer class="site-footer">')
        print(f'Chars around footer: {repr(c[footer_pos-10:footer_pos+50])}')