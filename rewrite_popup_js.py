import os, re

# The CLEAN correct JS block to inject
# This replaces the ENTIRE popup JS block in each HTML file
# Strategy: find the <script> block that contains WORKER_URL and closeLeadPopup, then replace it entirely

NEW_JS_BLOCK = '''<script>
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
function getResourceKey(){var p=window.location.pathname;
if(p.includes('tokyo-5days'))return'TOKYO_5DAYS';
if(p.includes('kansai-pass'))return'KANSAI_PASS';
if(p.includes('hokkaido-winter'))return'HOKKAIDO_WINTER';
if(p.includes('okinawa'))return'OKINAWA';
if(p.includes('kyoto-temples'))return'KYOTO_TEMPLES';
if(p.includes('osaka-food'))return'OSAKA_FOOD';
if(p.includes('osaka-usj'))return'OSAKA_USJ';
if(p.includes('japan-budget'))return'JAPAN_BUDGET';
if(p.includes('seoul-food'))return'SEOUL_FOOD';
if(p.includes('busan-capsule'))return'BUSAN_CAPSULE';
if(p.includes('jeju-island'))return'JEJU_ISLAND';
if(p.includes('korea-budget'))return'KOREA_BUDGET';
if(p.includes('hualien-taitung'))return'HUALIEN_TAITUNG';
if(p.includes('tainan-food'))return'TAINAN_FOOD';
if(p.includes('kenting'))return'KENTING';
if(p.includes('taipei-food'))return'TAIPEI_FOOD';
if(p.includes('jiufen'))return'JIUFEN';
if(p.includes('chiang-mai'))return'CHIANG_MAI';
if(p.includes('bangkok-3days'))return'BANGKOK_3DAYS';
if(p.includes('bangkok-massage'))return'BANGKOK_MASSAGE';
if(p.includes('vietnam-danang'))return'VIETNAM_DANANG';
return null;}

function closeLeadPopup(){localStorage.setItem('leadPopupClosed','1');document.getElementById('leadPopup').classList.remove('active')}

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
if(localStorage.getItem('leadSent')||localStorage.getItem('leadPopupClosed'))return;
var _0sy=window.scrollY;
var _0dH=document.documentElement.scrollHeight;
var _0ch=window.innerHeight;
if(_0sy/_0dH>0.58&&!document.getElementById('leadPopup').classList.contains('active')){
document.getElementById('leadPopup').classList.add('active');
}
});

document.getElementById('leadPopup').addEventListener('click',function(_0ev){if(_0ev.target===document.getElementById('leadPopup'))closeLeadPopup();});
</script>'''

# We need to find and replace the entire <script> block that contains WORKER_URL
# Pattern: <script> ... WORKER_URL ... </script>
# Replace with NEW_JS_BLOCK

ARTICLES = [
    'tokyo-5days.html', 'kansai-pass.html', 'hokkaido-winter.html', 'okinawa.html',
    'kyoto-temples.html', 'osaka-food.html', 'osaka-usj.html', 'japan-budget-guide.html',
    'seoul-food.html', 'busan-capsule.html', 'jeju-island.html', 'korea-budget.html',
    'hualien-taitung.html', 'tainan-food.html', 'kenting.html', 'taipei-food.html',
    'jiufen.html', 'chiang-mai.html', 'bangkok-3days.html', 'bangkok-massage.html',
    'vietnam-danang.html'
]

count = 0
for f in ARTICLES:
    if not os.path.exists(f):
        print(f'SKIP (not found): {f}')
        continue
    with open(f, 'rb') as fp:
        data = fp.read()

    # Find the script block containing WORKER_URL
    idx_start = data.find(b'<script>\nconst WORKER_URL')
    if idx_start == -1:
        # Try alternative start
        idx_start = data.find(b'<script>\nconst WORKER_URL', 0)
    if idx_start == -1:
        # Try finding WORKER_URL anywhere in a script block
        idx_w = data.find(b'WORKER_URL')
        if idx_w >= 0:
            # Find the <script> tag before this
            idx_start = data.rfind(b'<script>', 0, idx_w)
    
    if idx_start == -1:
        print(f'WARN: {f} - WORKER_URL script block not found')
        continue

    idx_end = data.find(b'</script>', idx_start)
    if idx_end == -1:
        print(f'WARN: {f} - </script> not found')
        continue
    idx_end += len(b'</script>')

    # Replace
    new_data = data[:idx_start] + NEW_JS_BLOCK.encode('utf-8') + data[idx_end:]
    
    with open(f, 'wb') as fp:
        fp.write(new_data)
    
    count += 1
    print(f'OK: {f} - JS block replaced')

print(f'\nTotal: {count} files updated')
