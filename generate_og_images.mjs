// P0-4: Generate cropped 1200x630 WebP og:image files using sharp (ES module)
import sharp from 'sharp';
import { readFileSync, writeFileSync, existsSync, statSync } from 'fs';
import { join } from 'path';

const BASE = 'G:\\aistudio-travel-lab';
const IMAGES_DIR = join(BASE, 'public', 'images');
const BASE_URL = 'https://golightly.fun';

const OG_IMAGES = [
    ['angkor-wat-2days.html',            'angkor-og',              'angkor.webp'],
    ['chiang-mai.html',                  'chiangmai-og',           'chiangmai-hero.webp'],
    ['fukuoka-5days.html',               'fukuoka-og',            'Fukuoka.webp'],
    ['hokkaido-winter.html',             'hokkaido-og',            'hokkaido-hero.webp'],
    ['japan-budget-guide.html',          'japan-budget-og',       'japan-budget-hero.webp'],
    ['japan-cherry-blossom-season.html', 'japan-cherry-og',       'Cherry blossom and autumn foliage viewing in Japan.webp'],
    ['japan-drugstore-checklist.html',   'japan-drugstore-og',    'Japanese drugstore cosmetics.webp'],
    ['kualalumpur-3days.html',          'kualalumpur-og',        'kualalumpur-3days.webp'],
    ['singapore-3days.html',            'singapore-og',          'singapore.webp'],
    ['tokyo-accommodation.html',         'tokyo-accommodation-og','Tokyo-Accommodation-hero.webp'],
];

const ogUrlMap = {}; // htmlFile -> ogUrl

async function processAll() {
    for (const [htmlFile, ogId, srcImg] of OG_IMAGES) {
        const srcPath = join(IMAGES_DIR, srcImg);
        const outPath = join(IMAGES_DIR, `${ogId}.webp`);

        if (!existsSync(srcPath)) {
            console.log(`  [SKIP] ${srcImg}: NOT FOUND`);
            continue;
        }

        try {
            const result = await sharp(srcPath)
                .resize(1200, 630, { fit: 'cover', position: 'center' })
                .webp({ quality: 80 })
                .toFile(outPath);

            const size = statSync(outPath).size;
            console.log(`  [OK] ${ogId}.webp (${result.width}x${result.height}, ${(size/1024).toFixed(1)}KB) <- ${srcImg}`);
            ogUrlMap[htmlFile] = `${BASE_URL}/images/${ogId}.webp`;
        } catch (err) {
            console.log(`  [ERR] ${ogId}: ${err.message}`);
        }
    }

    // Step 2: Update HTML files
    console.log('\n=== Updating HTML og:image tags ===');
    for (const [htmlFile, ogId] of OG_IMAGES) {
        const fpath = join(BASE, htmlFile);
        if (!existsSync(fpath)) {
            console.log(`  [SKIP] ${htmlFile}: NOT FOUND`);
            continue;
        }

        const ogUrl = ogUrlMap[htmlFile];
        if (!ogUrl) {
            console.log(`  [SKIP] ${htmlFile}: no og image generated`);
            continue;
        }

        let html = readFileSync(fpath, 'utf-8');
        const pattern = /<meta\s+property="og:image"\s+content="[^"]*"(\s*\/?>)/gi;
        const newTag = `<meta property="og:image" content="${ogUrl}"/>`;
        if (pattern.test(html)) {
            html = html.replace(pattern, newTag);
            writeFileSync(fpath, html, 'utf-8');
            console.log(`  [OK] ${htmlFile} -> ${ogId}.webp`);
        } else {
            console.log(`  [SKIP] ${htmlFile}: no og:image tag found`);
        }
    }

    console.log('\nDone.');
}

processAll().catch(err => { console.error(err); process.exit(1); });
