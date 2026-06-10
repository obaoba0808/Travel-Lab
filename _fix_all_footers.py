import glob, re

pages = ['busan-4days.html', 'fukuoka-5days.html', 'korea-transport.html', 
         'seoul-5days.html', 'seoul-food-map.html', 'thailand-sim.html', 
         'vietnam-hochiminh.html']

fix_pattern = '</div><!-- /related-posts --></div><!-- /article-container --></div><!-- /col-center --></div><!-- /three-col-wrapper --><!-- FOOTER -->'

for f in pages:
    try:
        c = open(f, 'r', encoding='utf-8').read()
        
        # Find the pattern: </div> followed by <footer (with various whitespace)
        # We need to be careful to only fix the one before footer
        
        footer_pos = c.find('<footer class="site-footer">')
        if footer_pos == -1:
            print(f'⚠️ {f}: no footer found')
            continue
        
        # Check if already fixed
        before_footer = c[footer_pos-100:footer_pos]
        if '/three-col-wrapper' in before_footer:
            print(f'✅ {f}: already fixed')
            continue
        
        # Find the last </div> before footer
        last_div_pos = c.rfind('</div>', 0, footer_pos)
        if last_div_pos == -1:
            print(f'⚠️ {f}: no </div> before footer')
            continue
        
        # Replace: </div> + whitespace + <footer
        # With: </div><!-- /related-posts -->...</div><!-- /three-col-wrapper --><!-- FOOTER --> + whitespace + <footer
        
        # Get the whitespace between </div> and <footer
        between = c[last_div_pos+6:footer_pos]
        
        # Build replacement
        old = '</div>' + between + '<footer class="site-footer">'
        new = '</div>' + fix_pattern + between + '<footer class="site-footer">'
        
        if old in c:
            c = c.replace(old, new, 1)
            open(f, 'w', encoding='utf-8').write(c)
            print(f'✅ Fixed {f}')
        else:
            print(f'⚠️ {f}: pattern not found (between: {repr(between[:20])})')
            
    except Exception as e:
        print(f'❌ {f}: error - {e}')