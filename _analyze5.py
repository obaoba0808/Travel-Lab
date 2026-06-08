import re
for f in ['singapore-3days.html','southeast-asia.html']:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    body_idx = c.find("<body>")
    # find ✈ pattern
    plane_idx = c.find("用最少預算", body_idx)
    if plane_idx >= 0:
        print(f"\n=== {f}: ✈ at {plane_idx} ===")
        print(c[plane_idx-10:plane_idx+100])
    else:
        # find closing </nav>
        nav_end = c.find("</nav>", body_idx)
        print(f"\n=== {f}: </nav> at {nav_end}, no ✈ found ===")
        print(c[nav_end:nav_end+200])
