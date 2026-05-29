import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\Travel-Lab'

# 12 pages with duplicate forms (one correct, one at body end)
PAGES = [
    'bangkok-massage.html',
    'busan-capsule.html',
    'hualien-taitung.html',
    'japan-budget-guide.html',
    'jeju-island.html',
    'jiufen.html',
    'kansai-pass.html',
    'korea-budget.html',
    'osaka-usj.html',
    'tainan-food.html',
    'taipei-food.html',
    'vietnam-danang.html',
]

def remove_body_end_form(html):
    """Remove the duplicate form at the end of body (before </body> or </html>)."""
    # Find the last occurrence of lead-inline (should be the one at body end)
    last_form = html.rfind('class="lead-inline"')
    if last_form == -1:
        return html, False
    
    # Check if there's another lead-inline before it
    first_form = html.find('class="lead-inline"')
    if first_form == last_form:
        # Only one form, keep it
        return html, False
    
    # Find the start of the second form section
    # Look for <style> or <div class="lead-inline"> before the last_form
    style_before = html.rfind('<style>', 0, last_form)
    div_before = html.rfind('<div class="lead-inline">', 0, last_form)
    section_before = html.rfind('<section class="lead-inline">', 0, last_form)
    
    # Determine which is the body-end form
    if style_before != -1 and style_before > section_before:
        # Body-end form starts with <style> for CSS
        form_start = style_before
    elif div_before != -1 and div_before > section_before:
        # Body-end form starts with <div>
        form_start = div_before
    else:
        return html, False
    
    # Find the end of the body-end form (before </body> or end of file)
    body_end = html.find('</body>', form_start)
    if body_end == -1:
        body_end = len(html)
    
    # Remove the body-end form
    html = html[:form_start] + html[body_end:]
    return html, True

for fname in PAGES:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Count forms before
    forms_before = html.count('class="lead-inline"')
    
    # Remove body-end form
    html, changed = remove_body_end_form(html)
    
    # Count forms after
    forms_after = html.count('class="lead-inline"')
    
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✅ {fname}: {forms_before} → {forms_after} forms')
    else:
        print(f'⏭️ {fname}: {forms_before} forms (no change)')
