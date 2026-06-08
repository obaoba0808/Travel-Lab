import glob

for f in sorted(glob.glob('*.html')):
    if f in ('index.html','404.html'): continue
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    has_doctype = '<!DOCTYPE' in c
    has_body = '<body>' in c
    has_topbar = 'site-topbar' in c
    has_main = '<main' in c
    has_artcont = 'article-container' in c
    has_hero = 'hero-' in c
    has_wrapper = 'three-col-wrapper' in c
    has_sidebar = 'sidebar-card' in c
    has_charter = 'charter-banner' in c
    has_faq = 'faq-section' in c
    has_lead = 'lead-inline' in c
    has_klook = 'klk-aff-widget' in c
    has_related = 'related-posts' in c
    has_trip_promo = 'TRIP PROMO' in c
    has_trip_rec = 'trip-recommend' in c
    has_footer = 'site-footer' in c
    count = sum([has_wrapper, has_sidebar, has_charter, has_faq, has_lead, has_klook, has_related, has_trip_promo, has_trip_rec, has_footer])
    flags = ''.join('Y' if v else '.' for v in [has_wrapper, has_sidebar, has_charter, has_faq, has_lead, has_klook, has_related, has_trip_promo, has_trip_rec, has_footer])
    print(f'{flags} [{count:2d}] {f}')
