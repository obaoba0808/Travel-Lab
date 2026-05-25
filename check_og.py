import re

for f in ["disclaimer.html", "terms.html"]:
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    og_url = re.search(r'og:url.*?content="([^"]+)"', c, re.DOTALL)
    og_img = re.search(r'og:image.*?content="([^"]+)"', c, re.DOTALL)
    og_title = re.search(r'og:title.*?content="([^"]+)"', c, re.DOTALL)
    og_desc = re.search(r'og:description.*?content="([^"]+)"', c, re.DOTALL)
    print(f"FILE: {f}")
    print(f"  og:url   : {og_url.group(1) if og_url else 'MISSING'}")
    print(f"  og:image : {og_img.group(1) if og_img else 'MISSING'}")
    print(f"  og:title : {og_title.group(1) if og_title else 'MISSING'}")
    print(f"  og:desc  : {og_desc.group(1) if og_desc else 'MISSING'}")
    print()