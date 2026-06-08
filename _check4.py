for f in ['angkor-wat-2days.html','kualalumpur-3days.html','singapore-3days.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    body_idx = c.find('<body')
    nav_close = c.find('</nav>', body_idx)
    marker = "用最少預算"
    marker_idx = c.find(marker)
    print(f"{f}: body={body_idx} </nav>={nav_close} marker={marker_idx}")
    if nav_close < 0 and marker_idx < 0:
        # Show content around <body> and around <nav
        nav_open = c.find('<nav', body_idx)
        print(f"  <nav at {nav_open}")
        # Show 500 chars after nav
        if nav_open >= 0:
            chunk = c[nav_open:nav_open+800]
            print(f"  after nav: ...{chunk[-200:]}")
