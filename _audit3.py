import glob

COMPLETE = set()  # 10/10 pages
PORTAL = {'index.html','404.html','about.html','contact.html','privacy.html','terms.html','disclaimer.html',
          'japan-travel.html','korea-travel.html','taiwan-travel.html','southeast-asia.html',
          'travel-tools.html','monthly-review.html','budget-calculator.html','miles-calculator.html',
          'tax-refund-calculator.html','power-plug-guide.html','packing-list.html','packing-checklist.html',
          'budget-airline-guide.html','credit-card-miles-guide.html','notion-travel-template.html',
          'esim-comparison.html','seasia-budget-travel-guide.html','korea-money-saving-tips.html',
          'japan-money-saving-tips.html','japan-drugstore-checklist.html','japan-cherry-blossom-season.html'}

# Pages that need 14-block structure
ARTICLE_PAGES = []
for f in sorted(glob.glob('*.html')):
    if f in PORTAL or f in COMPLETE: continue
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    has_wrapper = 'three-col-wrapper' in c
    has_charter = 'charter-banner' in c
    has_sidebar = 'sidebar-card' in c
    count = sum([has_wrapper, has_charter, has_sidebar])
    if count < 3:
        ARTICLE_PAGES.append(f)

print(f"Pages needing refactor: {len(ARTICLE_PAGES)}")
for f in ARTICLE_PAGES:
    with open(f,'r',encoding='utf-8') as fh: c=fh.read()
    has_wrapper = 'three-col-wrapper' in c
    has_charter = 'charter-banner' in c
    has_sidebar = 'sidebar-card' in c
    has_topbar = 'site-topbar' in c
    has_hero = 'hero-' in c
    has_faq = 'faq-section' in c
    has_lead = 'lead-inline' in c
    has_klook = 'klk-aff-widget' in c
    has_related = 'related-posts' in c
    has_trip_promo = 'TRIP PROMO' in c
    has_trip_rec = 'trip-recommend' in c
    print(f"  {f}: wrapper={has_wrapper} charter={has_charter} sidebar={has_sidebar} topbar={has_topbar} hero={has_hero} faq={has_faq} lead={has_lead} klook={has_klook} related={has_related} trip={has_trip_promo}")
