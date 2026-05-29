import os, sys, subprocess, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

TARGET_PAGES = [
    'esim-comparison.html', 'japan-travel.html', 'korea-budget-travel-guide.html',
    'korea-travel.html', 'live-japan-budget.html', 'packing-list-online.html',
    'packing-list.html', 'seasia-budget-travel-guide.html', 'southeast-asia.html',
    'taiwan-travel-guide.html', 'taiwan-travel.html',
]

PDF_MAP = {
    'esim-comparison.html': 'japan-budget-sheet',
    'japan-travel.html': 'japan-budget-sheet',
    'korea-budget-travel-guide.html': 'korea-budget-sheet',
    'korea-travel.html': 'korea-budget-sheet',
    'live-japan-budget.html': 'japan-budget-sheet',
    'packing-list-online.html': 'hokkaido-packing-list',
    'packing-list.html': 'hokkaido-packing-list',
    'seasia-budget-travel-guide.html': 'bangkok-food-map',
    'southeast-asia.html': 'bangkok-food-map',
    'taiwan-travel-guide.html': 'taipei-food-map',
    'taiwan-travel.html': 'taipei-food-map',
}

# The complete form HTML to insert
FORM_HTML = '''
<section class="lead-inline">
  <div class="lead-inline-icon">&#128236;</div>
  <h3>小編獨家攻略，限時免費送</h3>
  <p>填Email立即收到PDF下載連結和最新旅遊資訊</p>
  <form onsubmit="submitLeadForm(event);return false">
    <input type="email" placeholder="輸入你的Email" required id="leadEmail">
    <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
  </form>
  <div id="leadMsg" style="font-size:13px;margin-top:8px;min-height:20px;"></div>
  <p class="lead-note">&#128274; 尊重隱私，隨時可取消訂閱</p>
</section>'''

CSS = '''<style>
.lead-inline{background:linear-gradient(135deg,#f1f8e9 0%,#e8f5e9 50%,#dcedc8 100%)!important;border-radius:20px!important;padding:40px!important;text-align:center;margin:40px auto;max-width:640px;box-shadow:0 8px 32px rgba(46,125,50,.12),0 2px 8px rgba(0,0,0,.06)!important;border:2px solid #a5d6a7!important}
.lead-inline-icon{font-size:56px;margin-bottom:16px;display:inline-block;animation:bounce-lead 2s ease-in-out infinite}
@keyframes bounce-lead{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.lead-inline h3{color:#1b5e20;margin:0 0 16px;font-size:26px;font-weight:700}
.lead-inline p{color:#2e7d32;margin:0 0 12px;font-size:15px}
.lead-inline form{display:flex;flex-direction:column;align-items:center;gap:10px;max-width:400px;margin:0 auto}
.lead-inline input[type=email]{width:100%;padding:14px 20px;border:2px solid #a5d6a7;border-radius:30px;font-size:15px;outline:none;transition:border .3s;box-sizing:border-box}
.lead-inline input[type=email]:focus{border-color:#4db6ac;box-shadow:0 0 0 3px rgba(77,182,172,.2)}
.lead-inline button[type=submit]{background:linear-gradient(135deg,#4db6ac,#26a69a);color:#fff;border:none;padding:14px 36px;border-radius:30px;font-size:16px;font-weight:700;cursor:pointer;transition:all .3s;box-shadow:0 4px 15px rgba(38,166,154,.35)}
.lead-inline button:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(38,166,154,.45)}
.lead-inline button:disabled{background:#ccc;cursor:not-allowed;transform:none;box-shadow:none}
.lead-inline .lead-note{font-size:12px;color:#666;margin:12px 0 0}
</style>'''

def make_js(pdf_key, fname):
    page_key = fname.replace('.html', '')
    return f'''<script>
const WORKER_URL="https://golightly-email.happybird.workers.dev";
function getResourceKey(){{const p=location.pathname.replace("/Travel-Lab/","").replace(".html","");const m={{"{page_key}":"{pdf_key}"}};return m[p]||"{pdf_key}";}}
function submitLeadForm(ev){{if(ev)ev.preventDefault();var b=document.getElementById("leadSubmitBtn"),m=document.getElementById("leadMsg"),e=document.getElementById("leadEmail").value;if(!e||!e.includes("@")){{m.textContent="請輸入有效Email";return;}}b.disabled=true;b.textContent="傳送中...";m.textContent="";fetch(WORKER_URL,{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{email:e,resource:getResourceKey()}})}}).then(function(r){{return r.json();}}).then(function(d){{if(d.ok){{b.textContent="已寄出";b.disabled=true;m.style.color="#2e7d32";m.textContent="PDF連結已寄到信箱！";localStorage.setItem("leadSent","1");}}else{{b.disabled=false;b.textContent="免費下載攻略";m.style.color="#c62828";m.textContent="傳送失敗，請再試一次";}}}}).catch(function(){{b.disabled=false;b.textContent="免費下載攻略";m.style.color="#c62828";m.textContent="網路錯誤，請再試一次";}});}}
if(localStorage.getItem("leadSent")){{var s=document.getElementById("leadSubmitBtn");if(s){{s.textContent="已訂閱";s.disabled=true;}}}}
</script>'''

def find_last_faq_end(html):
    """Find the character position right after the last FAQ answer closes."""
    faq_items = list(re.finditer(r'faq-item', html))
    if not faq_items:
        return -1
    # Find the last faq-item
    last_start = faq_items[-1].start()
    # Find the closing tag of this FAQ item (look for the </div> that closes its content)
    # Strategy: find the next </div> that looks like it closes the faq-item
    # Look for </div> that comes after last faq-item and is likely the answer/section close
    after_last = html[last_start:]
    # Find all </div> after the last faq-item
    divs = [(m.start(), m.end()) for m in re.finditer(r'</div>', after_last)]
    if not divs:
        return -1
    # The last </div> in the document after the faq items is likely the close
    # But we need to find a reasonable one - let's look for the one that closes the faq
    # FAQ structure: <div class="faq-item">...<div class="faq-q">...</div><div class="faq-a">...</div></div>
    # We want the </div> that closes the faq-item
    # Strategy: find the last 'faq-item' class close - find the pattern faq-item...</div>
    faq_close = re.search(r'class="faq-item[^"]*"[^>]*>.*?</div>\s*</div>', after_last, re.DOTALL)
    if faq_close:
        return last_start + faq_close.end()
    # Fallback: last </div> in the document
    return last_start + after_last.rfind('</div>') + len('</div>')

def find_last_faq_end_v2(html):
    """More robust: find the last </div> that closes a faq-item block."""
    # Find all faq-item blocks - look for pattern: <div class="faq-item"...>...</div>
    matches = list(re.finditer(r'<div class="faq-item[^"]*"[^>]*>.*?</div>\s*</div>', html, re.DOTALL))
    if matches:
        last = matches[-1]
        return last.end()
    # Fallback: last faq-item position + look for its closing </div>
    faq_pos = html.rfind('faq-item')
    if faq_pos == -1:
        return -1
    # Find the last </div> after this
    remaining = html[faq_pos:]
    close = remaining.rfind('</div>')
    if close == -1:
        return -1
    return faq_pos + close + len('</div>')

results = []
for fname in TARGET_PAGES:
    path = os.path.join(base, fname)
    
    # Reset to truly clean version
    subprocess.run(['git', 'checkout', '0d2c549', '--', fname], cwd=base, capture_output=True)
    
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if 'lead-inline' in c:
        print(f'NOT CLEAN: {fname}')
        continue
    
    pdf_key = PDF_MAP[fname]
    
    # Find insertion point: right after last FAQ item
    insert_pos = find_last_faq_end_v2(c)
    
    if insert_pos == -1 or insert_pos == 0:
        print(f'NO FAQ FOUND: {fname}')
        # Fallback: insert before <footer>
        insert_pos = c.find('<footer')
        if insert_pos == -1:
            print(f'  NO FOOTER EITHER: {fname}')
            continue
    
    # Insert form right after last FAQ
    c = c[:insert_pos] + '\n' + FORM_HTML + '\n' + c[insert_pos:]
    
    # Add CSS before </head>
    head_end = c.find('</head>')
    if head_end != -1:
        c = c[:head_end] + CSS + '\n' + c[head_end:]
    
    # Add JS before </body>
    body_end = c.rfind('</body>')
    if body_end != -1:
        c = c[:body_end] + make_js(pdf_key, fname) + '\n' + c[body_end:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    
    # Verify
    fi = c.find('class="lead-inline"')
    faqs = [m.start() for m in re.finditer('faq-item', c)]
    last_faq = faqs[-1] if faqs else -1
    foot = c.find('<footer')
    print(f'{"OK" if fi > last_faq else "FAIL"}: {fname} (form@{fi}, last_faq@{last_faq}, footer@{foot})')
    results.append(fname)

print(f'\n=== Done: {len(results)}/{len(TARGET_PAGES)} ===')
