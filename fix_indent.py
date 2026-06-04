import sys

# Read file
with open("_beautify_pdf.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Check line 86 (index 85)
if len(lines) >= 86:
    line85 = lines[85]  # 0-indexed
    print(f"\nLine 86: {repr(line85)}")
    
    # Check indentation
    stripped = line85.lstrip()
    indent = len(line85) - len(stripped)
    print(f"Indentation: {indent} spaces")
    
    # Check if "return t" is properly indented
    if "return t" in line85:
        # Should be inside make_table function
        # Look back for "def make_table"
        for i in range(84, max(0, 84-30), -1):
            if "def " in lines[i]:
                def_indent = len(lines[i]) - len(lines[i].lstrip())
                print(f"Found def at line {i+1}: {repr(lines[i].strip())}")
                print(f"Def indentation: {def_indent} spaces")
                
                if indent <= def_indent:
                    print(f"\n*** ERROR: Line 86 indent ({indent}) <= def indent ({def_indent}) ***")
                    print("Fixing: Add 4 spaces to line 86")
                    lines[85] = "    " + line85
                else:
                    print(f"\nOK: Line 86 indent ({indent}) > def indent ({def_indent})")
                break

# Write back
with open("_beautify_pdf.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\nDone. File saved.")
