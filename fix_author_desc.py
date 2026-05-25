"""Fix CP950 description in resource pages + batch add author byline to all pages."""
import re, os, sys

sys.stdout.reconfigure(encoding="utf-8")

RESOURCE_FIXES = {
    "korea-budget-travel-guide.html": {
        "desc": "韓國自由行預算全攻略2026｜首爾釜山濟州島一周預算 NT$8,000 起的省錢旅遊攻略，附機票、住宿、交通、美食實際花費與行程規劃建議。"
    },
    "seasia-budget-travel-guide.html": {
        "desc": "東南亞省錢旅遊攻略2026｜泰國、越南、馬來西亞、印尼 Budget 旅行完整指南，附簽證、交通、住宿與各國日均消費比較。"
    },
    "taiwan-travel-guide.html": {
        "desc": "台灣自由行旅遊攻略2026｜環島、北中南東深度行程推薦，附台灣高鐵、台鐵、客運交通攻略與各縣市美食住宿推薦。"
    }
}

AUTHOR_HTML = '''<p class="author-line" style="color:#888;font-size:13px;margin:8px 0 16px;">📝 均在路上 Travel Lab 編輯部 · 更新於 2026 年</p>'''

def fix_resource_pages():
    for fname, data in RESOURCE_FIXES.items():
        if not os.path.exists(fname):
            print(f"  SKIP (not found): {fname}")
            continue

        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix description
        desc_pat = r'(<meta\s+name="description"\s+content=")[^"]*(")'
        if re.search(desc_pat, content):
            new_content = re.sub(desc_pat, rf'\g<1>{data["desc"]}\g<2>', content)
            with open(fname, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  FIXED desc: {fname}")
        else:
            print(f"  WARN no desc tag: {fname}")

        # Add author byline after first </h1> or early in body
        with open(fname, "r", encoding="utf-8") as f:
            c = f.read()
        if 'class="author-line"' not in c:
            if re.search(r"</h1>", c):
                new_c = re.sub(r"(</h1>)", rf"\1\n{AUTHOR_HTML}", c, count=1)
            elif re.search(r"<h2", c):
                new_c = re.sub(r"(<h2)", rf"{AUTHOR_HTML}\n<em>\1", c, count=1)
            else:
                body_start = c.find("<body>")
                if body_start >= 0:
                    body_start = c.find(">", body_start) + 1
                    new_c = c[:body_start] + AUTHOR_HTML + c[body_start:]
                else:
                    new_c = c
            with open(fname, "w", encoding="utf-8") as f:
                f.write(new_c)
            print(f"  ADDED author: {fname}")


def add_author_to_all():
    """Add author byline to all pages that don't have one."""
    for f in sorted(os.listdir(".")):
        if not f.endswith(".html") or f in ["404.html", "_live_index.html"]:
            continue
        with open(f, "r", encoding="utf-8") as fh:
            c = fh.read()
        if 'class="author-line"' in c:
            continue
        # Find </h1> or <h2
        if re.search(r"</h1>", c):
            new_c = re.sub(r"(</h1>)", rf"\1\n{AUTHOR_HTML}", c, count=1)
        else:
            continue
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(new_c)
        print(f"  author+: {f}")


print("=== Fixing resource pages ===")
fix_resource_pages()

print()
print("=== Adding author byline to all pages ===")
add_author_to_all()

print()
print("Done.")