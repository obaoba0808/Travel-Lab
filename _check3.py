for f in ['angkor-wat-2days.html','kualalumpur-3days.html','singapore-3days.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    has_body = '<body' in c
    has_nav = '<nav' in c
    print(f"{f}: <body={has_body} <nav={has_nav}")
    if not has_body:
        # Find DOCTYPE and <html
        dt = c.find('<!DOCTYPE')
        html = c.find('<html')
        print(f"  DOCTYPE at {dt}, <html at {html}")
        print(f"  first 200: {c[:200]}")
