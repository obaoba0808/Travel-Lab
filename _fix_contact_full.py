import re

# 讀取檔案
with open('contact.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# --- 修復 1: ContactPage JSON-LD ---
new_contact_jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "聯絡窗口 | 均在路上 Travel Lab",
  "description": "聯絡窗口均在路上 Travel Lab，歡迎用 LINE 或 Email 聯絡我們，常見問題 24 小時內回覆，合作提案與旅遊疑問歡迎來信。",
  "url": "https://golightly.fun/contact.html",
  "mainEntity": {
    "@type": "Organization",
    "name": "均在路上 Travel Lab",
    "url": "https://golightly.fun/",
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "customer service",
      "availableLanguage": ["Chinese", "English"]
    }
  }
}
</script>'''

# 使用正則替換 ContactPage JSON-LD
content = re.sub(
    r'<script type="application/ld\+json">\s*\{[^}]*"@type": "ContactPage"[^}]*\}[^<]*</script>',
    new_contact_jsonld,
    content,
    flags=re.DOTALL
)

# --- 修復 2: BreadcrumbList JSON-LD ---
new_breadcrumb_jsonld = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "首頁",
      "item": "https://golightly.fun/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "聯絡窗口",
      "item": "https://golightly.fun/contact.html"
    }
  ]
}
</script>'''

# 使用正則替換 BreadcrumbList JSON-LD (第二個 JSON-LD 區塊)
content = re.sub(
    r'<script type="application/ld\+json">\s*\{[^}]*"@type": "BreadcrumbList"[^}]*\}[^<]*</script>',
    new_breadcrumb_jsonld,
    content,
    flags=re.DOTALL
)

# 寫入檔案 (UTF-8 無 BOM)
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully fixed contact.html JSON-LD sections')
