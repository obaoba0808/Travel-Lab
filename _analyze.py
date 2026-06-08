import re

with open("bangkok-3days.html", "r", encoding="utf-8") as f:
    c = f.read()

# Find the body tag and everything after
body_idx = c.find("<body>")
print(f"<body> at char {body_idx}")

# Find end of topbar: look for </nav> followed by </div></div>
nav_idx = c.find("</nav>", body_idx)
print(f"</nav> at char {nav_idx}")
print(f"chars around </nav>: [{c[nav_idx:nav_idx+30]}]")

# After </nav>, find first </div>
d1 = c.find("</div>", nav_idx)
print(f"first </div> after </nav> at {d1}")
d2 = c.find("</div>", d1 + 6)
print(f"second </div> after </nav> at {d2}")
print(f"chars: [{c[d2:d2+20]}]")

# What comes after topbar?
after_topbar = c[d2+6:d2+200]
print(f"\nAfter topbar:\n{after_topbar[:200]}")

# Find hero section
hero_idx = c.find("hero-", body_idx)
print(f"\nFirst hero- class at char {hero_idx}")
hero_tag = c[hero_idx-50:hero_idx+100]
print(f"Context: [{hero_tag}]")

# Find charter banner
charter_idx = c.find("charter-banner")
if charter_idx >= 0:
    print(f"\ncharter-banner at char {charter_idx}")
    print(f"Context: [{c[charter_idx-20:charter_idx+100]}]")

# Find three-col-wrapper
tw_idx = c.find("three-col-wrapper")
if tw_idx >= 0:
    print(f"\nthree-col-wrapper at char {tw_idx}")
    print(f"Context: [{c[tw_idx-20:tw_idx+100]}]")

# Find article-container
ac_idx = c.find("article-container")
if ac_idx >= 0:
    print(f"\narticle-container at char {ac_idx}")
    print(f"Context: [{c[ac_idx-20:ac_idx+100]}]")

# Check what's between </body> ending and footer
footer_idx = c.find("site-footer")
if footer_idx >= 0:
    print(f"\nsite-footer at char {footer_idx}")
