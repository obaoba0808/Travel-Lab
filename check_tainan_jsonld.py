"""Find JSON-LD blocks in tainan-food.html and check for syntax errors."""
import re, json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("tainan-food.html", "r", encoding="utf-8") as f:
    c = f.read()

blocks = list(re.finditer(r'<script type="application/ld\+json">(.*?)</script>', c, re.DOTALL))

print("Found " + str(len(blocks)) + " JSON-LD block(s)\n")

for i, m in enumerate(blocks):
    raw = m.group(1).strip()
    print("=== Block #" + str(i+1) + " (chars: " + str(len(raw)) + ") ===")
    
    # Try to parse as JSON
    try:
        parsed = json.loads(raw)
        schema_type = parsed.get("@type", "unknown")
        if isinstance(schema_type, list):
            schema_type = ", ".join(schema_type)
        print("  Type: " + str(schema_type))
        print("  Status: VALID JSON")
    except json.JSONDecodeError as e:
        print("  Status: INVALID JSON!")
        print("  Error: " + str(e))
        # Show the problematic area
        err_pos = e.pos if hasattr(e, 'pos') else -1
        if err_pos >= 0:
            start = max(0, err_pos - 50)
            end = min(len(raw), err_pos + 50)
            print("  Context: ..." + raw[start:end] + "...")
    print()
