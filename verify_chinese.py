import fitz
doc = fitz.open('downloads/usj-quick-pass.pdf')
text = ''
for i in range(min(2, doc.page_count)):
    text += doc[i].get_text()
doc.close()

# Check for Chinese
has_chinese = any('\u4e00' <= c <= '\u9fff' for c in text)
print(f'Text length: {len(text)}')
print(f'Has Chinese: {has_chinese}')
if len(text) > 100:
    print(f'First 200 chars: {repr(text[:200])}')
