#!/usr/bin/env python3
# 全站表單加入 Cloudflare Worker 自動回覆
# 流程：用戶填表 → Formspree 收名單 + Worker 寄 PDF email → 跳轉 thank-you.html

import os, re, glob

WORKER_URL = "https://golightly-email-reply.happybird.workers.dev"
FORMSPREE_URL = "https://formspree.io/f/xredjjgb"

files = [f for f in os.listdir('.') if f.endswith('.html')]
count = 0

for fn in files:
    with open(fn, encoding='utf-8') as f:
        content = f.read()
    
    # 找 form 標籤，確認是 Formspree 表單
    if FORMSPREE_URL not in content:
        continue
    
    # 新策略：保留 Formspree action（收名單），加入 onsubmit 觸發 Worker
    # 用 fetch 非同步呼叫 Worker，不阻塞表單提交
    
    # 找 form 開始標籤
    form_pattern = r'(<form\s+action="https://formspree\.io/f/xredjjgb"[^>]*>)'
    match = re.search(form_pattern, content)
    if not match:
        continue
    
    form_tag = match.group(1)
    
    # 檢查是否已經有 worker 呼叫
    if 'golightly-email-reply' in content or WORKER_URL in content:
        print(f"SKIP (already has worker): {fn}")
        continue
    
    # 在 form 標籤中加入 onsubmit + data-resource
    # 提取 resource hidden field 的值
    resource_match = re.search(r'name="resource"\s+value="([^"]*)"', content)
    resource_val = resource_match.group(1) if resource_match else fn.replace('.html', '')
    
    # 加入 onsubmit 到 form 標籤
    new_form_tag = form_tag.replace('>', f' onsubmit="fetch(\'{WORKER_URL}\',{{method:\'POST\',headers:{{\'Content-Type\':\'application/json\'}},body:JSON.stringify({{email:this.elements.email.value,resource:\'{resource_val}\'}})}}).catch(function(){{}});" >')
    
    new_content = content.replace(form_tag, new_form_tag, 1)
    
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    count += 1
    print(f"✅ {fn} (resource: {resource_val})")

print(f"\nDone! Updated {count} forms")
