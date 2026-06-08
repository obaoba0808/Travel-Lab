import re

with open("bangkok-4days.html", "r", encoding="utf-8") as f:
    c = f.read()

body_idx = c.find("<body>")
print(f"<body> at char {body_idx}")

nav_idx = c.find("</nav>", body_idx)
print(f"</nav> at char {nav_idx}")

d1 = c.find("</div>", nav_idx)
d2 = c.find("</div>", d1 + 6)
print(f"topbar ends at char {d2+6}")

# Show what comes right after topbar
after = c[d2+6:d2+300]
print(f"\nAfter topbar:\n{after}")

# Check for existing blocks
for tag in ['charter-banner', 'three-col-wrapper', 'article-container', 'TRIP PROMO', 'faq-section', 'lead-inline', 'klk-aff-widget', 'related-posts', 'site-footer']:
    idx = c.find(tag)
    if idx >= 0:
        print(f"{tag}: char {idx}")
    else:
        print(f"{tag}: NOT FOUND")
