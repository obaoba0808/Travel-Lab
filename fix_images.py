import os, re

workspace = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\travel-lab'

# Replacement image sets (each page gets 4 unique images)
replacements = {
    'hualien-taitung.html': {
        'photo-1596783074918-c84cb1394178': [
            'photo-1470004914212-05527e49370b',
            'photo-1506905925346-21bda4d32df4',
            'photo-1558981403-c5f9899a28bc',
            'photo-1519451241324-20b4ea2c4220',
        ]
    },
    'busan-capsule.html': {
        'photo-1508009603885-50cf7c579365': [
            'photo-1583417319070-4a69db38a482',
            'photo-1530523247026-b8e64ae7b8e4',
            'photo-1524592094714-0f0654e20314',
            'photo-1513694203232-719a280e022f',
        ]
    },
    'hokkaido-winter.html': {
        'photo-1508009603885-50cf7c579365': [
            'photo-1476514525535-07fb3b4ae5f1',
            'photo-1505228395891-9a51e7e86bf6',
            'photo-1553284965-83fd3e82fa5a',
            'photo-1519681393784-d120267933ba',
        ]
    },
    'tainan-food.html': {
        'photo-1508009603885-50cf7c579365': [
            'photo-1555939594-58d7cb561ad1',
            'photo-1540189549336-e6e99c3679fe',
            'photo-1567620905732-2d1ec7ab7445',
            'photo-1565299624946-b28f40a0ae38',
        ]
    },
    'kenting.html': {
        'photo-1508009603885-50cf7c579365': [
            'photo-1507525428034-b723cf961d3e',
            'photo-1544551763-46a013bb70d5',
            'photo-1559827291-72ee739d0d9a',
            'photo-1585909695284-32d2985ac9c0',
        ]
    }
}

def replace_images_in_file(filepath, page_replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    for old_id, new_ids in page_replacements.items():
        # Find all occurrences
        count = content.count(old_id)
        print(f'  Found {count} occurrences of {old_id}')
        
        # Replace each occurrence sequentially with different images
        for i in range(count):
            new_id = new_ids[i % len(new_ids)]
            # Replace first occurrence
            pos = content.find(old_id)
            if pos >= 0:
                content = content.replace(old_id, new_id, 1)
                print(f'  Replaced occurrence {i+1} with {new_id}')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Saved: {os.path.basename(filepath)}')
    else:
        print(f'  No changes: {os.path.basename(filepath)}')

for fname, page_replacements in replacements.items():
    path = os.path.join(workspace, fname)
    if os.path.exists(path):
        print(f'\nFixing: {fname}')
        replace_images_in_file(path, page_replacements)
    else:
        print(f'File not found: {fname}')

print('\nDone!')
