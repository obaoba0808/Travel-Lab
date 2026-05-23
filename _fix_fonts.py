import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Only add emoji fonts if not already present
def add_emoji_fonts(match):
    ff = match.group(0)
    if 'Emoji' in ff:
        return ff  # Already has emoji fonts
    # Insert emoji fonts before the generic family
    # Handle sans-serif
    if 'sans-serif' in ff and 'Emoji' not in ff:
        ff = ff.replace('sans-serif', "'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',sans-serif")
    # Handle serif
    if 'serif' in ff and 'Emoji' not in ff:
        ff = ff.replace(',serif', ",'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',serif")
        ff = ff.replace("',serif", ",'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',serif")
    return ff

pattern = r"font-family:[^;]+"
new_css = re.sub(pattern, add_emoji_fonts, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

print('Done - all font-family declarations updated with emoji font fallbacks')
