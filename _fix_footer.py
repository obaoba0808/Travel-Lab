import re

f = 'tokyo-accommodation.html'
c = open(f, 'r', encoding='utf-8').read()

footer_pos = c.find('<footer class="site-footer">')
print(f'footer position: {footer_pos}')

if footer_pos > 0:
    before = c[footer_pos-150:footer_pos]
    print('150 chars before footer:')
    print(repr(before))
    
    # The issue: we need to close related-posts, article-container, col-center, three-col-wrapper
    # Find the pattern and fix it
    
    # Look for: </div> (end of related-list) followed by </div> (end of related-posts? no)
    # Actually let's check the structure more carefully
    
    # Find related-posts start
    related_pos = c.find('class="section-title">📖 延伸閱讀')
    print(f'related section position: {related_pos}')
    
    # Find all </div> after related section and before footer
    if related_pos > 0 and footer_pos > related_pos:
        chunk = c[related_pos:footer_pos]
        div_closes = chunk.count('</div>')
        print(f'</div> count between related and footer: {div_closes}')
        
        # We need: related-list (1) -> related-posts (2) -> article-container (3) -> col-center (4) -> three-col-wrapper (5)
        # That's 5 closing divs, but we only have 2 based on earlier check
        
        # The fix: add the missing closing comments and divs
        # Current: </div> </div> <footer...
        # Should be: </div><!-- /related-list? no wait -->
        
        # Actually the structure is:
        # <div class="related-posts"> <h2>...</h2> <div class="related-list"> ... </div> </div>
        # So we need to close: related-list (1), related-posts (2), article-container (3), col-center (4), three-col-wrapper (5)
        
        # Find the exact pattern to replace
        # Look for the last </div> before footer
        last_div = c.rfind('</div>', 0, footer_pos)
        print(f'last </div> before footer: {last_div}')
        print(f'content around last div: {repr(c[last_div-20:last_div+100])}')