import re

# 读取文件
with open('korea-budget.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 互动式预算试算器 HTML + JavaScript
calculator_html = '''
<!-- 互动式预算试算器 -->
<div id="budget-calculator" style="background:#fff;border-radius:16px;padding:32px;margin:40px 0;box-shadow:0 4px 20px rgba(0,0,0,0.08);border:2px solid #e0f2f1;">
  <h2 style="margin:0 0 20px;color:#1a1a2e;font-size:24px;">💰 韩国旅游预算试算器</h2>
  <p style="margin:0 0 24px;color:#555;line-height:1.8;">输入你的预算分配，自动计算总费用，并与我们的建议预算比较。</p>
  
  <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));gap:20px;margin-bottom:32px;">
    <!-- 机票 -->
    <div style="background:#f5f5f5;padding:20px;border-radius:12px;">
      <label style="display:block;font-weight:700;margin-bottom:8px;color:#333;">✈️ 机票（来回）</label>
      <input type="number" id="calc-flight" placeholder="例如 8000" style="width:100%;padding:10px;border:2px solid #ddd;border-radius:8px;font-size:15px;box-sizing:border-box;">
      <p style="margin:8px 0 0;font-size:13px;color:#666;">建议：NT$4,000-15,000</p>
    </div>
    
    <!-- 住宿 -->
    <div style="background:#f5f5f5;padding:20px;border-radius:12px;">
      <label style="display:block;font-weight:700;margin-bottom:8px;color:#333;">🏨 住宿（4晚）</label>
      <input type="number" id="calc-hotel" placeholder="例如 12000" style="width:100%;padding:10px;border:2px solid #ddd;border-radius:8px;font-size:15px;box-sizing:border-box;">
      <p style="margin:8px 0 0;font-size:13px;color:#666;">建议：NT$6,000-12,000</p>
    </div>
    
    <!-- 餐食 -->
    <div style="background:#f5f5f5;padding:20px;border-radius:12px;">
      <label style="display:block;font-weight:700;margin-bottom:8px;color:#333;">🍖 餐食（5天）</label>
      <input type="number" id="calc-meal" placeholder="例如 6000" style="width:100%;padding:10px;border:2px solid #ddd;border-radius:8px;font-size:15px;box-sizing:border-box;">
      <p style="margin:8px 0 0;font-size:13px;color:#666;">建议：NT$3,000-5,000</p>
    </div>
    
    <!-- 交通 -->
    <div style="background:#f5f5f5;padding:20px;border-radius:12px;">
      <label style="display:block;font-weight:700;margin-bottom:8px;color:#333;">🚇 交通</label>
      <input type="number" id="calc-transport" placeholder="例如 2000" style="width:100%;padding:10px;border:2px solid #ddd;border-radius:8px;font-size:15px;box-sizing:border-box;">
      <p style="margin:8px 0 0;font-size:13px;color:#666;">建议：NT$1,500-2,500</p>
    </div>
    
    <!-- 购物 -->
    <div style="background:#f5f5f5;padding:20px;border-radius:12px;">
      <label style="display:block;font-weight:700;margin-bottom:8px;color:#333;">🛍️ 购物</label>
      <input type="number" id="calc-shopping" placeholder="例如 8000" style="width:100%;padding:10px;border:2px solid #ddd;border-radius:8px;font-size:15px;box-sizing:border-box;">
      <p style="margin:8px 0 0;font-size:13px;color:#666;">建议：NT$3,000-8,000</p>
    </div>
    
    <!-- 门票 -->
    <div style="background:#f5f5f5;padding:20px;border-radius:12px;">
      <label style="display:block;font-weight:700;margin-bottom:8px;color:#333;">🎫 门票/活动</label>
      <input type="number" id="calc-ticket" placeholder="例如 2000" style="width:100%;padding:10px;border:2px solid #ddd;border-radius:8px;font-size:15px;box-sizing:border-box;">
      <p style="margin:8px 0 0;font-size:13px;color:#666;">建议：NT$500-1,500</p>
    </div>
  </div>
  
  <button onclick="calculateBudget()" style="background:linear-gradient(135deg,#4db6ac,#26a69a);color:#fff;border:none;padding:14px 36px;border-radius:30px;font-size:16px;font-weight:700;cursor:pointer;transition:all .3s;box-shadow:0 4px 15px rgba(38,166,154,.35);display:block;margin:0 auto 24px;">計算總预算</button>
  
  <div id="budget-result" style="display:none;background:linear-gradient(135deg,#e8f5e9,#f1f8e9);padding:24px;border-radius:12px;margin-top:20px;border-left:4px solid #0abab5;">
    <h3 style="margin:0 0 12px;color:#1b5e20;">📊 预算试算结果</h3>
    <div id="budget-breakdown" style="line-height:2;color:#333;"></div>
    <div id="budget-comparison" style="margin-top:16px;padding:16px;background:#fff;border-radius:8px;font-size:14px;color:#555;"></div>
  </div>
</div>

<script>
function calculateBudget() {
  // 获取输入值
  var flight = parseInt(document.getElementById('calc-flight').value) || 0;
  var hotel = parseInt(document.getElementById('calc-hotel').value) || 0;
  var meal = parseInt(document.getElementById('calc-meal').value) || 0;
  var transport = parseInt(document.getElementById('calc-transport').value) || 0;
  var shopping = parseInt(document.getElementById('calc-shopping').value) || 0;
  var ticket = parseInt(document.getElementById('calc-ticket').value) || 0;
  
  // 计算总和
  var total = flight + hotel + meal + transport + shopping + ticket;
  
  // 显示结果
  var resultDiv = document.getElementById('budget-result');
  resultDiv.style.display = 'block';
  
  // 预算明细
  var breakdown = document.getElementById('budget-breakdown');
  breakdown.innerHTML = 
    '✈️ 机票：NT$' + flight.toLocaleString() + '<br>' +
    '🏨 住宿：NT$' + hotel.toLocaleString() + '<br>' +
    '🍖 餐食：NT$' + meal.toLocaleString() + '<br>' +
    '🚇 交通：NT$' + transport.toLocaleString() + '<br>' +
    '🛍️ 购物：NT$' + shopping.toLocaleString() + '<br>' +
    '🎫 门票：NT$' + ticket.toLocaleString() + '<br>' +
    '<strong style="color:#1b5e20;font-size:18px;">總计：NT$' + total.toLocaleString() + '</strong>';
  
  // 比较建议
  var comparison = document.getElementById('budget-comparison');
  var suggestedMin = 15000;
  var suggestedMax = 25000;
  
  if(total < suggestedMin) {
    comparison.innerHTML = '📉 你的预算 <strong>NT$' + (suggestedMin - total).toLocaleString() + '</strong> 低于我们建议的经济型预算（NT$' + suggestedMin.toLocaleString() + '）。\\n建议增加住宿或餐食预算，以提升旅游品质。';
    comparison.style.color = '#e65100';
  } else if(total > suggestedMax) {
    comparison.innerHTML = '📈 你的预算 <strong>NT$' + (total - suggestedMax).toLocaleString() + '</strong> 高于我们建议的舒适型预算（NT$' + suggestedMax.toLocaleString() + '）。\\n可以考虑升级住宿或增加购物预算。';
    comparison.style.color = '#c62828';
  } else {
    comparison.innerHTML = '✅ 你的预算在建议范围内（NT$' + suggestedMin.toLocaleString() + '-' + suggestedMax.toLocaleString() + '）。\\n这是一个合理的韩国自由行预算！';
    comparison.style.color = '#2e7d32';
  }
}
</script>
'''

# 在「各項目詳細拆解」标题后插入试算器
# 找到 </div> 结束标签，在 </div> 前插入
pattern = r'(<h2>各項目詳細拆解</h2>)'
replacement = r'\1' + calculator_html
content = re.sub(pattern, replacement, content, count=1)

# 写入文件
with open('korea-budget.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已在 korea-budget.html 中插入互动式预算试算器')
print('   位置：<h2>各項目詳細拆解</h2> 之后')
print('   功能：用户输入预算分配 → 自动计算总费用 → 与建议预算比较')