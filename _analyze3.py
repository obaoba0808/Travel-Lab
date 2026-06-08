import re

# Check several pages' topbar end pattern
pages = ['bangkok-3days.html','bangkok-4days.html','tokyo-5days.html','singapore-3days.html','southeast-asia.html','vietnam-danang.html']
for f in pages:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    body_idx = c.find("<body>")
    nav_end = c.find("</nav>", body_idx)
    # Find pattern: </nav>\n<div...>\n</div>\n</div>
    after_nav = c[nav_end:nav_end+300]
    print(f"\n=== {f} (</nav> at {nav_end}) ===")
    print(after_nav[:200])
