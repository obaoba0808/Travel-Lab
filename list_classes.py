import re
html = open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab\southeast-asia.html', 'r', encoding='utf-8').read()
classes = set(re.findall(r'class="([^"]+)"', html))
known = {'site-topbar','topbar-inner','mobile-toggle','main-nav','nav-dropdown','dropdown-toggle','dropdown-menu','active','hero-region-new','hero-image-wrapper','hero-title-below','hero-region-tag','hero-subtitle','hero-stats','breadcrumb-container','main-content','article-container','article-section','article-intro','site-footer','footer-inner','footer-col','footer-social','footer-social-inner','footer-social-title','footer-social-sub','footer-social-links','footer-social-btn','footer-social-fb','footer-social-line','footer-bottom','footer-nav-row','footer-nav-sep','lead-inline','lead-note','faq-item','faq-q'}
custom = sorted([c for c in classes if c not in known and ' ' not in c])
for c in custom:
    print(c)