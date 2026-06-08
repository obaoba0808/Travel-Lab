for f in ['singapore-3days.html','southeast-asia.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    body_idx = c.find("<body>")
    # search for nav-close-like patterns
    for pat in ['</nav', '</div', 'class="nav', 'class="dropdown', '旅遊工具', '關於我們']:
        idx = c.find(pat, body_idx)
        if idx >= 0:
            print(f"{f}: '{pat}' at char {idx}")
            if pat in ('</nav','</div','旅遊工具','關於我們'):
                print(f"  context: ...{c[max(0,idx-20):idx+40]}...")
