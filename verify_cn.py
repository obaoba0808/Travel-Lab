import fitz, sys
sys.stdout.reconfigure(encoding="utf-8")
doc = fitz.open("downloads/usj-quick-pass.pdf")
text = ""
for i in range(min(2, doc.page_count)):
    text += doc[i].get_text()
doc.close()
has_cn = any("\u4e00" <= c <= "\u9fff" for c in text)
result = "GOOD" if (has_cn and len(text) > 100) else "BAD"
print(f"Text length: {len(text)}")
print(f"Has Chinese: {has_cn}")
print(f"Result: {result}")
