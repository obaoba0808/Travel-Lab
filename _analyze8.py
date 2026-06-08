for f in ['angkor-wat-2days.html','korea-transport.html','kualalumpur-3days.html','seoul-5days.html','singapore-3days.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    body_idx = c.find("<body>")
    # Show last 200 chars of first 5000 chars after body (should cover nav)
    chunk = c[body_idx:body_idx+3000]
    # Find last 300 chars
    print(f"\n=== {f} (last 300 of first 3000 after body) ===")
    print(chunk[-300:])
