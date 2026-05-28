import os, re

# Read one file to get exact old CSS
with open('kansai-pass.html', 'r', encoding='utf-8', errors='replace') as f:
    sample = f.read()

# Find the lead-popup CSS block
start = sample.find('.lead-popup-overlay{')
end = sample.find('}', sample.find('.lead-note')) + 1
old_css = sample[start:end]
print(f'Old CSS length: {len(old_css)}')
print(old_css[:100])

new_css = '.lead-popup-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.6);z-index:9999;align-items:center;justify-content:center}.lead-popup-overlay.active{display:flex}.lead-popup{background:#fff;border-radius:16px;padding:0;max-width:480px;width:90%;position:relative;text-align:center;font-family:"Noto Sans TC",sans-serif;overflow:hidden}.lead-popup-header{background:linear-gradient(135deg,#81d4ce,#4db6ac);padding:20px 32px 16px;position:relative}.lead-popup-header h3{color:#fff;margin:0;font-size:18px;line-height:1.4;text-shadow:0 1px 3px rgba(0,0,0,0.15)}.lead-popup-close{position:absolute;top:8px;right:12px;background:rgba(255,255,255,0.3);border:none;font-size:22px;cursor:pointer;color:#fff;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;line-height:1;transition:background 0.2s}.lead-popup-close:hover{background:rgba(255,255,255,0.5)}.lead-popup-body{padding:24px 32px 28px}.lead-popup-body p{color:#444;margin:0 0 16px;font-size:14px;line-height:1.7}.lead-popup input[type=email]{width:100%;padding:12px 16px;border:2px solid #81d4ce;border-radius:8px;font-size:15px;box-sizing:border-box;margin-bottom:12px;outline:none;transition:border-color 0.2s}.lead-popup input[type=email]:focus{border-color:#4db6ac;box-shadow:0 0 0 3px rgba(77,182,172,0.2)}.lead-popup button{width:100%;padding:14px;background:linear-gradient(135deg,#81d4ce,#4db6ac);color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:bold;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s}.lead-popup button:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(77,182,172,0.35)}.lead-popup .lead-note{font-size:11px;color:#aaa;margin-top:10px}'

count = 0
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        content = fp.read()
    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        count += 1

print(f'Updated {count} files with new Tiffany green CSS')
