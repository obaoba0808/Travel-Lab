import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# Map page basename -> PDF filename that EXISTS in downloads/
# Based on actual files in the downloads/ folder
PDF_MAP = {
    'tokyo-5days': 'tokyo-metro-map.pdf',
    'kansai-pass': 'kansai-pass-calculator.pdf',
    'hokkaido-winter': 'hokkaido-packing-list.pdf',
    'okinawa': 'okinawa-driving-map.pdf',
    'kyoto-temples': 'kyoto-momiji-schedule.pdf',
    'osaka-food': 'osaka-food-map.pdf',
    'osaka-usj': 'usj-quick-pass.pdf',
    'japan-budget-guide': 'japan-budget-sheet.pdf',
    'seoul-food': 'seoul-food-map.pdf',
    'busan-capsule': 'busan-capsule-guide.pdf',
    'jeju-island': 'jeju-driving-route.pdf',
    'korea-budget': 'korea-budget-sheet.pdf',
    'hualien-taitung': 'hualien-itinerary.pdf',
    'tainan-food': 'tainan-food-map.pdf',
    'taipei-food': 'taipei-food-map.pdf',
    'jiufen': 'jiufen-guide.pdf',
    'chiang-mai': 'chiang-mai-guide.pdf',
    'bangkok-massage': 'bangkok-massage-map.pdf',
    'bangkok-3days': 'bangkok-food-map.pdf',
    'vietnam-danang': 'danang-map.pdf',
    'packing-list': 'hokkaido-packing-list.pdf',  # reuse
    'packing-list-online': 'hokkaido-packing-list.pdf',
}

# GitHub Pages base URL
PDF_BASE = 'https://obaoba0808.github.io/Travel-Lab/downloads'

count = 0
for fname in os.listdir(base):
    if not fname.endswith('.html') or fname.startswith('_'):
        continue
    
    # Extract base name (remove .html)
    basename = fname.replace('.html', '')
    pdf_file = PDF_MAP.get(basename)
    
    if not pdf_file:
        continue
        
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    # Old URL pattern
    old_url = "https://assets.golightly.fun/pdf/"
    new_url = f'{PDF_BASE}/'
    
    if old_url in html:
        # Replace in LEAD_PDF
        html = html.replace(old_url, new_url)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ {fname}')
        count += 1

print(f'\nTotal: {count} files updated')