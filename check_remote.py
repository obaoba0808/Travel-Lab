import urllib.request
url = 'https://obaoba0808.github.io/Travel-Lab/japan-travel.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req, timeout=10)
html = response.read().decode('utf-8', errors='replace')
print('hero-title-block in remote:', 'hero-title-block' in html)
print('overlay in remote:', 'class="overlay"' in html)