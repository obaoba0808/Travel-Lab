import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'pdfs/online-usj.pdf')
text = ''
for i in range(min(2, doc.page_count)):
    text += doc[i].get_text()
doc.close()

has_cn = any('\u4e00' <= c <= '\u9fff' for c in text)
print(f'Text length: {len(text)}', flush=True)
print(f'Has Chinese: {has_cn}', flush=True)
if len(text) > 50:
    # Print first 150 chars safely
    safe_text = text[:150].encode('cp950', errors='replace').decode('cp950')
    print(f'First 150 chars (cp950 safe):')
    print(safe_text)
