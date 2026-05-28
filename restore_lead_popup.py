import os
import re

WORKSPACE = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab"
WORKER_URL = "https://golightly-email.8107e1de.workers.dev"

FILES = [
    "tokyo-5days.html","kansai-pass.html","hokkaido-winter.html","okinawa.html",
    "kyoto-temples.html","osaka-food.html","osaka-usj.html","japan-budget-guide.html",
    "seoul-food.html","busan-capsule.html","jeju-island.html","korea-budget.html",
    "hualien-taitung.html","tainan-food.html","kenting.html","taipei-food.html",
    "jiufen.html","chiang-mai.html","bangkok-3days.html","bangkok-massage.html",
    "vietnam-danang.html"
]

CSS_BLOCK = """
<style>
.lead-popup-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.6);z-index:9999;align-items:center;justify-content:center}
.lead-popup-overlay.active{display:flex}
.lead-popup{background:#fff;border-radius:16px;padding:32px;max-width:480px;width:90%;position:relative;text-align:center;font-family:'Noto Sans TC',sans-serif}
.lead-popup-close{position:absolute;top:12px;right:16px;background:none;border:none;font-size:24px;cursor:pointer;color:#888}
.lead-popup h3{color:#e85d04;margin:0 0 8px;font-size:20px}
.lead-popup p{color:#444;margin:0 0 20px;font-size:15px;line-height:1.6}
.lead-popup input[type=email]{width:100%;padding:12px 16px;border:2px solid #e85d04;border-radius:8px;font-size:15px;box-sizing:border-box;margin-bottom:12px;outline:none}
.lead-popup input[type=email]:focus{border-color:#f48c06;box-shadow:0 0 0 3px rgba(232,93,4,0.15)}
.lead-popup button{width:100%;padding:14px;background:linear-gradient(135deg,#e85d04,#f48c06);color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:bold;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s}
.lead-popup button:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(232,93,4,0.35)}
.lead-popup .lead-note{font-size:12px;color:#999;margin-top:10px}
</style>
"""

POPUP_HTML = """
<div class="lead-popup-overlay" id="leadPopup">
  <div class="lead-popup">
    <button class="lead-popup-close" onclick="closeLeadPopup()">&times;</button>
    <h3>📘 小編獨家攻略，限時免費送</h3>
    <p id="leadDesc">填Email立即收到PDF下載連結<br>和最新日本自由行資訊</p>
    <form onsubmit="submitLeadForm(this,event)">
      <input type="email" placeholder="輸入你的Email" required id="leadEmail">
      <button type="submit" id="leadSubmitBtn">免費下載攻略</button>
    </form>
    <p class="lead-note">🔒 尊重隱私，隨時可取消訂閱</p>
  </div>
</div>
"""

JS_BLOCK = """
<script>
const WORKER_URL='https://golightly-email.8107e1de.workers.dev';

const PDF_LINKS={
TOKYO_5DAYS:'https://golightly.fun/downloads/tokyo-subway-guide.pdf',
KANSAI_PASS:'https://golightly.fun/downloads/kansai-pass-guide.pdf',
HOKKAIDO_WINTER:'https://golightly.fun/downloads/hokkaido-winter-guide.pdf',
OKINAWA:'https://golightly.fun/downloads/okinawa-guide.pdf',
KYOTO_TEMPLES:'https://golightly.fun/downloads/kyoto-temples-guide.pdf',
OSAKA_FOOD:'https://golightly.fun/downloads/osaka-food-guide.pdf',
OSAKA_USJ:'https://golightly.fun/downloads/osaka-usj-guide.pdf',
JAPAN_BUDGET:'https://golightly.fun/downloads/japan-budget-guide.pdf',
SEOUL_FOOD:'https://golightly.fun/downloads/seoul-food-guide.pdf',
BUSAN_CAPSULE:'https://golightly.fun/downloads/busan-capsule-guide.pdf',
JEJU_ISLAND:'https://golightly.fun/downloads/jeju-island-guide.pdf',
KOREA_BUDGET:'https://golightly.fun/downloads/korea-budget-guide.pdf',
HUALIEN_TAITUNG:'https://golightly.fun/downloads/hualien-taitung-guide.pdf',
TAINAN_FOOD:'https://golightly.fun/downloads/tainan-food-guide.pdf',
KENTING:'https://golightly.fun/downloads/kenting-guide.pdf',
TAIPEI_FOOD:'https://golightly.fun/downloads/taipei-food-guide.pdf',
JIUFEN:'https://golightly.fun/downloads/jiufen-guide.pdf',
CHIANG_MAI:'https://golightly.fun/downloads/chiang-mai-guide.pdf',
BANGKOK_3DAYS:'https://golightly.fun/downloads/bangkok-3days-guide.pdf',
BANGKOK_MASSAGE:'https://golightly.fun/downloads/bangkok-massage-guide.pdf',
VIETNAM_DANANG:'https://golightly.fun/downloads/vietnam-danang-guide.pdf'
};

function getResourceKey(){
var m=location.pathname.match(/\\/([^\\/]+)\\.html/);
if(!m)return'';
var f=m[1].toLowerCase();
var map={'tokyo-5days':'TOKYO_5DAYS','kansai-pass':'KANSAI_PASS','hokkaido-winter':'HOKKAIDO_WINTER','okinawa':'OKINAWA','kyoto-temples':'KYOTO_TEMPLES','osaka-food':'OSAKA_FOOD','osaka-usj':'OSAKA_USJ','japan-budget-guide':'JAPAN_BUDGET','seoul-food':'SEOUL_FOOD','busan-capsule':'BUSAN_CAPSULE','jeju-island':'JEJU_ISLAND','korea-budget':'KOREA_BUDGET','hualien-taitung':'HUALIEN_TAITUNG','tainan-food':'TAINAN_FOOD','kenting':'KENTING','taipei-food':'TAIPEI_FOOD','jiufen':'JIUFEN','chiang-mai':'CHIANG_MAI','bangkok-3days':'BANGKOK_3DAYS','bangkok-massage':'BANGKOK_MASSAGE','vietnam-danang':'VIETNAM_DANANG'};
return map[f]||'';
}

function closeLeadPopup(){document.getElementById('leadPopup').classList.remove('active')}
function submitLeadForm(_0xfrm,_0xevt){
_0xevt.preventDefault();
var _0em=document.getElementById('leadEmail').value;
var _0res=getResourceKey();
var _0pg=document.title;
document.getElementById('leadSubmitBtn').textContent='傳送中...';
document.getElementById('leadSubmitBtn').disabled=true;
fetch(WORKER_URL+'?email='+encodeURIComponent(_0em)+'&resource='+encodeURIComponent(_0res)+'&page='+encodeURIComponent(_0pg))
.then(function(_0xr){return _0xr.json();})
.then(function(_0d){
if(_0d.ok||_0d.success){document.getElementById('leadSubmitBtn').textContent='已寄出 ✉️ 請收Email';localStorage.setItem('leadSent','1');setTimeout(closeLeadPopup,2000);}
else{document.getElementById('leadSubmitBtn').textContent='傳送失敗，再試一次';document.getElementById('leadSubmitBtn').disabled=false;}
})
.catch(function(_0e){document.getElementById('leadSubmitBtn').textContent='傳送失敗，再試一次';document.getElementById('leadSubmitBtn').disabled=false;});
}
window.addEventListener('scroll',function(){
if(localStorage.getItem('leadSent'))return;
var _0sy=window.scrollY;
var _0dH=document.documentElement.scrollHeight;
var _0ch=window.innerHeight;
if(_0sy/_0dH>0.58&&!document.getElementById('leadPopup').classList.contains('active')){
document.getElementById('leadPopup').classList.add('active');
}
});
document.getElementById('leadPopup').addEventListener('click',function(_0ev){if(_0ev.target===document.getElementById('leadPopup'))closeLeadPopup();});
</script>
"""

results = []
for filename in FILES:
    filepath = os.path.join(WORKSPACE, filename)
    if not os.path.exists(filepath):
        results.append("SKIP: {} not found".format(filename))
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if new popup already present
    if 'class="lead-popup-overlay"' in content:
        results.append("EXISTS: {} already has new popup".format(filename))
        continue

    new_content = content

    # Inject CSS before </head>
    if '.lead-popup-overlay' not in content:
        if '</head>' in new_content:
            new_content = new_content.replace('</head>', CSS_BLOCK + '\n</head>', 1)
        else:
            results.append("WARN: {} has no </head>".format(filename))
            continue

    # Inject popup HTML + JS before </body>
    if '<div class="lead-popup-overlay"' not in new_content:
        if '</body>' in new_content:
            new_content = new_content.replace('</body>', POPUP_HTML + '\n' + JS_BLOCK + '\n</body>', 1)
        else:
            results.append("WARN: {} has no </body>".format(filename))
            continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    results.append("OK:   {}".format(filename))

print("=== LEAD MAGNET POPUP INJECTION RESULTS ===")
for r in results:
    print(r)
ok_count = len([r for r in results if r.startswith("OK:")])
print("\nTotal: {} files processed, {} updated".format(len(results), ok_count))
