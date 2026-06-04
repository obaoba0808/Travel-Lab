import re

with open('contact.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 找到 ContactPage JSON-LD 的完整區塊 (從 <script type=\"application/ld+json\"> 到 </script>)
pattern = r'<script type=\"application/ld\+json\">\s*\{[^}]*\"@type\": \"ContactPage\"[^}]*\}[^<]*</script>'

# 準備正確的 ContactPage JSON-LD
new_jsonld = '''<script type=\"application/ld+json\">
{
  \"@context\": \"https://schema.org\",
  \"@type\": \"ContactPage\",
  \"name\": \"聯絡窗口 | 均在路上 Travel Lab\",
  \"description\": \"聯絡窗口均在路上 Travel Lab，歡迎用 LINE 或 Email 聯絡我們，常見問題 24 小時內回覆，合作提案與旅遊疑問歡迎來信。\",
  \"url\": \"https://golightly.fun/contact.html\",
  \"mainEntity\": {
    \"@type\": \"Organization\",
    \"name\": \"均在路上 Travel Lab\",
    \"url\": \"https://golightly.fun/\",
    \"contactPoint\": {
      \"@type\": \"ContactPoint\",
      \"contactType\": \"customer service\",
      \"availableLanguage\": [\"Chinese\", \"English\"]
    }
  }
}
</script>'''

# 使用正則替換（DOTALL 讓 . 可以匹配換行）
new_content = re.sub(
    r'<script type=\"application/ld\+json\">\s*\{[^}]*\"@type\": \"ContactPage\".*?</script>',
    new_jsonld,
    content,
    flags=re.DOTALL
)

# 寫入檔案
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('✅ 已修復 contact.html ContactPage JSON-LD')
