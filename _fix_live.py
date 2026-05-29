import os, sys, subprocess
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'
fname = 'live-japan-budget.html'

# Reset to clean
subprocess.run(['git', 'checkout', f'HEAD~2', '--', fname], cwd=base, capture_output=True)

with open(os.path.join(base, fname), 'r', encoding='utf-8') as f:
    c = f.read()

FORM_HTML = '''<section class="lead-inline">
      <div class="lead-inline-icon">&#128236;</div>
      <h3>小編獨家攻略，限時免費送</h3>
      <p>填Email立即收到PDF下載連結和最新旅遊資訊</p>
      <form onsubmit="submitLeadForm(event);return false">
        <input type="email" placeholder="輸入你的Email" required id="leadEmail">
        <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
      <div id="leadMsg" style="font-size:13px;margin-top:8px;min-height:20px;"></div>
  </form>
      <p class="lead-note">&#128274; 尊重隱私，隨時可取消訂閱</p>
    </section>'''

CSS_BLOCK = '''<style>
.lead-inline{background:linear-gradient(135deg,#f1f8e9 0%,#e8f5e9 50%,#dcedc8 100%)!important;border-radius:20px!important;padding:40px!important;text-align:center;margin:56px auto;max-width:640px;box-shadow:0 8px 32px rgba(46,125,50,.12),0 2px 8px rgba(0,0,0,.06)!important;border:2px solid #a5d6a7!important;position:relative;overflow:hidden}
.lead-inline-icon{font-size:56px;margin-bottom:16px;display:inline-block;animation:bounce-lead 2s ease-in-out infinite}
@keyframes bounce-lead{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}
.lead-inline h3{color:#1b5e20;margin:0 0 16px;font-size:26px;font-weight:700}
.lead-inline p{color:#2e7d32;margin:0 0 12px;font-size:15px}
.lead-inline form{display:flex;flex-direction:column;align-items:center;gap:10px;max-width:400px;margin:0 auto}
.lead-inline input[type=email]{width:100%;padding:14px 20px;border:2px solid #a5d6a7;border-radius:30px;font-size:15px;outline:none;transition:border .3s;box-sizing:border-box}
.lead-inline input[type=email]:focus{border-color:#4db6ac;box-shadow:0 0 0 3px rgba(77,182,172,.2)}
.lead-inline button[type=submit]{background:linear-gradient(135deg,#4db6ac,#26a69a);color:#fff;border:none;padding:14px 36px;border-radius:30px;font-size:16px;font-weight:700;cursor:pointer;transition:all .3s;box-shadow:0 4px 15px rgba(38,166,154,.35)}
.lead-inline button:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(38,166,154,.45)}
.lead-inline .lead-note{font-size:12px;color:#666;margin:12px 0 0}
</style>'''

JS_CODE = '''<script>
const WORKER_URL = "https://golightly-email.happybird.workers.dev";
function getResourceKey(){
  const p=location.pathname.replace("/Travel-Lab/","").replace(".html","");
  const m={"live-japan-budget":"japan-budget-sheet"};
  return m[p]||"japan-budget-sheet";
}
function submitLeadForm(ev){
  if(ev)ev.preventDefault();
  var b=document.getElementById("leadSubmitBtn");
  var m=document.getElementById("leadMsg");
  var e=document.getElementById("leadEmail").value;
  if(!e||!e.includes("@")){m.textContent="請輸入有效Email";return;}
  b.disabled=true;b.textContent="傳送中...";m.textContent="";
  fetch(WORKER_URL,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:e,resource:getResourceKey()})})
  .then(function(r){return r.json();})
  .then(function(d){
    if(d.ok){b.textContent="已寄出 &#9993;";m.style.color="#2e7d32";m.textContent="PDF連結已寄到信箱！";localStorage.setItem("leadSent","1");}
    else{b.disabled=false;b.textContent="免費下載攻略";m.style.color="#c62828";m.textContent="傳送失敗，請再試一次";}
  })
  .catch(function(){b.disabled=false;b.textContent="免費下載攻略";m.style.color="#c62828";m.textContent="網路錯誤，請再試一次";});
}
if(localStorage.getItem("leadSent")){var s=document.getElementById("leadSubmitBtn");if(s){s.textContent="已訂閱 &#9993;";s.disabled=true;}}
</script>'''

# For live-japan-budget.html (big file), find the LAST faq-item or KLOOK or content end
# Insert before footer area
last_faq = c.rfind('faq-item')
if last_faq > len(c) // 2:
    # Find the closing of this faq-item's parent container
    # Look for </div></div> pattern after last FAQ or just use footer
    foot_idx = c.find('<footer', last_faq)
    if foot_idx > 0:
        c = c[:foot_idx] + '\n' + FORM_HTML + '\n' + c[foot_idx:]
    else:
        # Fallback to before </body>
        body_end = c.rfind('</body>')
        c = c[:body_end] + FORM_HTML + '\n' + c[body_end:]

head_end = c.find('</head>')
if head_end != -1:
    c = c[:head_end] + CSS_BLOCK + '\n' + c[head_end:]

body_end = c.rfind('</body>')
if body_end != -1:
    c = c[:body_end] + JS_CODE + '\n' + c[body_end:]

with open(os.path.join(base, fname), 'w', encoding='utf-8') as f:
    f.write(c)

# Verify
c2 = open(os.path.join(base, fname), 'r', encoding='utf-8').read()
fi = c2.find('class="lead-inline"')
faq = c2.rfind('faq-item')
foot = c2.find('<footer')
print(f"live-japan-budget.html:")
print(f"  form@{fi}, last_faq@{faq}, footer@{foot}")
print(f"  after_faq={fi>faq}, before_footer={fi<foot}")
