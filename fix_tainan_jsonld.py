"""Fix the JSON-LD syntax error in tainan-food.html (missing colon in FAQPage)."""
import re, json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("tainan-food.html", "r", encoding="utf-8") as f:
    c = f.read()

# Find the broken JSON-LD block and fix it
old = '"text">老屋咖啡推薦'
new = '"text":"老屋咖啡推薦'

if old not in c:
    print("ERROR: Pattern not found!")
    sys.exit(1)

c_new = c.replace(old, new, 1)

# Verify the fix
blocks = list(re.finditer(r'<script type="application/ld\+json">(.*?)</script>', c_new, re.DOTALL))
for i, m in enumerate(blocks):
    raw = m.group(1).strip()
    try:
        parsed = json.loads(raw)
        schema_type = parsed.get("@type", "unknown")
        if isinstance(schema_type, list):
            schema_type = ", ".join(schema_type)
        print("Block #" + str(i+1) + ": " + str(schema_type) + " - VALID")
    except json.JSONDecodeError as e:
        print("Block #" + str(i+1) + ": STILL INVALID - " + str(e))

with open("tainan-food.html", "w", encoding="utf-8") as f:
    f.write(c_new)

print("\nFixed! Saved tainan-food.html")
