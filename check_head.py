import re, sys
sys.stdout.reconfigure(encoding="utf-8")

for f in ["korea-budget-travel-guide.html", "seasia-budget-travel-guide.html", "taiwan-travel-guide.html"]:
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    head_end = c.find("</head>")
    head = c[:head_end] if head_end > 0 else c[:600]
    lines = head.split("\n")
    print(f"=== {f} (first 40 head lines) ===")
    for i, line in enumerate(lines[:40]):
        print(f"  {i+1:2d}: {line.strip()[:120]}")
    print()