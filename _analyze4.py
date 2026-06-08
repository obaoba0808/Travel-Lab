for f in ['singapore-3days.html','southeast-asia.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    body_idx = c.find("<body>")
    print(f"\n=== {f} (body at {body_idx}) ===")
    # Show from <body> to 400 chars
    after = c[body_idx+6:body_idx+600]
    print(after)
