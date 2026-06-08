for f in ['singapore-3days.html','southeast-asia.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    body_idx = c.find("<body>")
    # Show from first </div> to 500 chars
    div_idx = c.find("</div>", body_idx)
    print(f"\n=== {f} ===")
    # find the end of nav structure - search for hero section
    hero_idx = c.find("hero-", body_idx)
    if hero_idx >= 0:
        print(f"hero at {hero_idx}")
        print(f"context around hero: [{c[hero_idx-80:hero_idx+60]}]")
    
    # These pages have old navbar structure without </nav>
    # Let's find the closing </div> that ends the topbar
    # Look for pattern: </div>\n</div>\n<section or <section
    section_idx = c.find("<section", body_idx)
    if section_idx >= 0:
        print(f"<section at {section_idx}")
        print(f"before section: [{c[section_idx-100:section_idx]}]")
