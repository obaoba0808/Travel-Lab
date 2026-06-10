# -*- coding: utf-8 -*-
# Update hero images for 3 Japan sub-pages

import os
import re

base_dir = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab"

updates = [
    {
        "file": "japan-budget-guide.html",
        "old_img": "images/japan-hero.webp",
        "new_img": "images/japan-budget-hero.webp"
    },
    {
        "file": "osaka-usj.html",
        "old_img": "images/kansai-hero.webp",
        "new_img": "images/osaka-usj-hero.webp"
    },
    {
        "file": "osaka-food.html",
        "old_img": "images/kansai-hero.webp",
        "new_img": "images/osaka-food-hero.webp"
    }
]

for item in updates:
    filepath = os.path.join(base_dir, item["file"])
    
    # Read in binary mode
    with open(filepath, "rb") as f:
        content = f.read()
    
    # Replace all occurrences
    old_bytes = item["old_img"].encode("utf-8")
    new_bytes = item["new_img"].encode("utf-8")
    
    if old_bytes in content:
        content = content.replace(old_bytes, new_bytes)
        
        # Write in binary mode
        with open(filepath, "wb") as f:
            f.write(content)
        
        print("[OK] Updated: " + item["file"])
    else:
        print("[SKIP] Not found: " + item["file"] + " (no " + item["old_img"] + ")")
