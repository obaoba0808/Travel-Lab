import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

PAGE_PDF_MAP = {
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

FORM_HTML = '''<section class="lead-inline">
      <div class="lead-inline-icon">📘</div>
      <h3>小編獨家攻略，限時免費送</h3>
      <p>填Email立即收到PDF下載連結和最新旅遊資訊</p>
      <form onsubmit="submitLeadForm(event);return false">
        <input type="email" placeholder="輸入你的Email" required id="leadEmail">
        <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
      <div id="leadMsg" style="font-size:13px;margin-top:8px;min-height:20px;"></div>
  </form>
      <p class="lead-note">🔒 尊重隱私，隨時可取消訂閱</p>
    </div>'''

CSS_BLOCK = '''<style>
.lead-inline{background:linear-gradient(135deg,#f1f8e9 0%,#e8f5e9 50%,#dcedc8 100%)!important;border-radius:20px!important;padding:40px!important;text-align:center;margin:56px auto;max-width:640px;box-shadow:0 8px 32px rgba(46,125,50,.12),0 2px 8px rgba(0,0,0,.06)!important;border:2px solid #a5d6a7!important;position:relative;overflow:hidden}
.lead-inline-icon{font-size:56px;margin-bottom:16px;display:inline-block;animation:bounce-lead 2s ease-in-out infinite}
@keyframes bounce-lead{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.lead-inline h3{color:#1b5e20;margin:0 0 16px;font-size:26px;font-weight:700}
.lead-inline p{color:#2e7d32;margin:0 0 12px;font-size:15px}
.lead-inline form{display:flex;flex-direction:column;align-items:center;gap:10px;max-width:400px;margin:0 auto}
.lead-inline input[type=email]{width:100%;padding:14px 20px;border:2px solid #a5d6a7;border-radius:30px;font-size:15px;outline:none;transition:border .3s;box-sizing:border-box}
.lead-inline input[type=email]:focus{border-color:#4db6ac;box-shadow:0 0 0 3px rgba(77,182,172,.2)}
.lead-inline button[type=submit]{background:linear-gradient(135deg,#4db6ac,#26a69a);color:#fff;border:none;padding:14px 36px;border-radius:30px;font-size:16px;font-weight:700;cursor:pointer;transition:all .3s;box-shadow:0 4px 15px rgba(38,166,154,.35)}
.lead-inline button:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(38,166,154,.45)}
.lead-inline .lead-note{font-size:12px;color:#666;margin:12px 0 0}
</style>'''

# Full JS with dynamic resource key mapping - built per file to avoid escaping issues
def make_js(pdf_key, fname):
    page_key = fname.replace('.html', '')
    return '''<script>
const WORKER_URL = "https://golightly-email.happybird.workers.dev";
function getResourceKey() {
  const p = location.pathname.replace("/Travel-Lab/","").replace(".html","");
  const m = {"''' + page_key + '''":"''' + pdf_key + '''"};
  return m[p] || "''' + pdf_key + '''";
}
function submitLeadForm(ev) {
  if(ev) ev.preventDefault();
  var btn=document.getElementById("leadSubmitBtn");
  var msg=document.getElementById("leadMsg");
  var email=document.getElementById("leadEmail").value;
  if(!email || !email.includes("@")) { msg.textContent="請輸入有效Email"; return; }
  btn.disabled=true; btn.textContent="傳送中..."; msg.textContent="";
  fetch(WORKER_URL,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:email,resource:getResourceKey()})})
  .then(function(r){return r.json();})
  .then(function(d){
    if(d.ok) { btn.textContent="已寄出 ✉️"; msg.style.color="#2e7d32"; msg.textContent="PDF連結已寄到信箱！"; localStorage.setItem("leadSent","1"); }
    else { btn.disabled=false; btn.textContent="免費下載攻略"; msg.style.color="#c62828"; msg.textContent="傳送失敗，請再試一次"; }
  })
  .catch(function(){ btn.disabled=false; btn.textContent="免費下載攻略"; msg.style.color="#c62828"; msg.textContent="網路錯誤，請再試一次"; });
}
if(localStorage.getItem("leadSent")){ var s=document.getElementById("leadSubmitBtn"); if(s){s.textContent="已訂閱 ✉️";s.disabled=true;} }
</script>'''

modified = []
for fname, pdf_key in PAGE_PDF_MAP.items():
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    if 'lead-inline' in c:
        print(f"SKIP (has form): {fname}")
        continue

    has_js = 'function submitLeadForm' in c

    # Insert form HTML
    inserted = False
    for marker in ['<!-- KLOOK', '</main>', '</article>', '</div><!-- content']:
        if marker in c:
            c = c.replace(marker, FORM_HTML + '\n' + marker, 1)
            inserted = True
            break

    if not inserted and '</body>' in c:
        c = c.replace('</body>', FORM_HTML + '\n</body>')
        inserted = True

    if not inserted:
        print(f"SKIP (no insert point): {fname}")
        continue

    # Add CSS
    if '.lead-inline{' not in c:
        if '</head>' in c:
            c = c.replace('</head>', CSS_BLOCK + '\n</head>')
        else:
            c = CSS_BLOCK + '\n' + c

    # Add JS
    if not has_js:
        js = make_js(pdf_key, fname)
        if '</body>' in c:
            c = c.replace('</body>', js + '\n</body>')
        else:
            c += '\n' + js

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

    modified.append(fname)
    print(f"OK: {fname} -> {pdf_key}")

print(f"\n=== Done: {len(modified)} files ===")
