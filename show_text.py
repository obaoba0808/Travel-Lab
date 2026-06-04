import fitz, sys
sys.stdout.reconfigure(encoding="utf-8")

doc = fitz.open("downloads/usj-quick-pass.pdf")
text = ""
for i in range(min(2, doc.page_count)):
    text += doc[i].get_text()
doc.close()

# 只显示前 300 字符
print("=== 实际提取的文字（前 300 字符）===")
print(repr(text[:300]))
print("")
print("=== 可读版本（前 200 字符）===")
print(text[:200])
