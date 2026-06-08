"""Fix CP950→UTF-8 for all HTML files in travel-lab.

Strategy: Try UTF-8 first. If the title has no valid CJK, fall back to CP950.
Write all output as UTF-8.
"""
import os, re, sys

sys.stdout.reconfigure(encoding="utf-8")

BASE_URL = "https://golightly.fun/"

def fix_file(path):
    with open(path, "rb") as f:
        raw = f.read()

    # Try UTF-8 first
    try:
        text_utf8 = raw.decode("utf-8")
        # Check title for valid CJK
        m = re.search(r"<title>(.*?)</title>", text_utf8)
        title = m.group(1).strip() if m else ""
        real_cjk = sum(1 for c in title if 0x4e00 <= ord(c) <= 0x9fff)
        if real_cjk >= 3:
            return "skip_utf8_ok", title[:60]
    except UnicodeDecodeError:
        text_utf8 = None

    # Try CP950 (Windows Traditional Chinese)
    try:
        text_cp950 = raw.decode("cp950")
        m = re.search(r"<title>(.*?)</title>", text_cp950)
        title = m.group(1).strip() if m else ""
        real_cjk = sum(1 for c in title if 0x4e00 <= ord(c) <= 0x9fff)
        if real_cjk >= 3:
            # Write as UTF-8
            with open(path, "w", encoding="utf-8") as f:
                f.write(text_cp950)
            return "fix_cp950", title[:60]
    except Exception:
        pass

    return "error_no_fix", ""


def main():
    fixed = []
    skipped = []
    errors = []

    for f in sorted(os.listdir(".")):
        if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
            continue

        result, title = fix_file(f)
        if result == "fix_cp950":
            fixed.append((f, title))
            print(f"  FIXED  {f}: {title}")
        elif result == "skip_utf8_ok":
            skipped.append(f)
        else:
            errors.append((f, result))

    print(f"\n=== Summary ===")
    print(f"Fixed (CP950→UTF-8): {len(fixed)}")
    print(f"Already UTF-8:      {len(skipped)}")
    print(f"Errors:              {len(errors)}")
    for f, r in errors:
        print(f"  ERROR {f}: {r}")

    return fixed, errors


if __name__ == "__main__":
    main()