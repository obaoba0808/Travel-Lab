// -*- coding: utf-8 -*-
// generate_favicons.js - Generate all favicon files from source logo
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const src = 'public/images/travel-lab-logo.png';
const outDir = 'public';

if (!fs.existsSync(src)) {
    console.error(`Source not found: ${src}`);
    process.exit(1);
}

function createIco(pngBuffers) {
    // ICO file format:
    // Header: 6 bytes (reserved=0, type=1 for ICO, count)
    // Directory entries: 16 bytes each (width, height, colors, reserved, planes, bpp, size, offset)
    // Image data: raw PNG data

    const sizes = [16, 32, 48, 256];
    const headerSize = 6;
    const dirEntrySize = 16;
    const numImages = sizes.length;

    let totalSize = headerSize + (dirEntrySize * numImages);
    const offsets = [];
    const pngDataList = [];

    for (const size of sizes) {
        const buf = pngBuffers[size];
        if (!buf) { console.warn(`Missing PNG for size ${size}`); continue; }
        offsets.push(totalSize);
        pngDataList.push(buf);
        totalSize += buf.length;
    }

    const ico = Buffer.alloc(totalSize);
    let pos = 0;

    // Header
    ico.writeUInt16LE(0, pos); pos += 2;       // Reserved
    ico.writeUInt16LE(1, pos); pos += 2;       // Type: 1 = ICO
    ico.writeUInt16LE(numImages, pos); pos += 2; // Number of images

    // Directory entries
    for (let i = 0; i < sizes.length; i++) {
        const size = sizes[i];
        const pngData = pngBuffers[size];
        const displaySize = size >= 256 ? 0 : size; // 256 stored as 0 in ICO

        ico.writeUInt8(displaySize, pos); pos += 1;       // Width
        ico.writeUInt8(displaySize, pos); pos += 1;       // Height
        ico.writeUInt8(0, pos); pos += 1;                 // Colors (0 = no palette)
        ico.writeUInt8(0, pos); pos += 1;                 // Reserved
        ico.writeUInt16LE(1, pos); pos += 2;             // Color planes
        ico.writeUInt16LE(32, pos); pos += 2;            // Bits per pixel
        ico.writeUInt32LE(pngData.length, pos); pos += 4; // Image size
        ico.writeUInt32LE(offsets[i], pos); pos += 4;     // Image offset
    }

    // Image data
    for (const pngData of pngDataList) {
        pngData.copy(ico, pos);
        pos += pngData.length;
    }

    return ico;
}

async function main() {
    const sizes = [16, 32, 48, 64, 128, 192, 256];
    const pngBuffers = {};

    console.log('Generating PNG buffers...');
    for (const size of sizes) {
        pngBuffers[size] = await sharp(src)
            .resize(size, size, { fit: 'cover' })
            .png({ quality: 90 })
            .toBuffer();
        console.log(`  ${size}x${size}: ${pngBuffers[size].length}B`);
    }

    // 1. favicon.ico (multi-size)
    const ico = createIco(pngBuffers);
    fs.writeFileSync(path.join(outDir, 'favicon.ico'), ico);
    console.log('Created: favicon.ico');

    // 2. favicon.png (32x32)
    await sharp(pngBuffers[32]).toFile(path.join(outDir, 'favicon.png'));
    console.log('Created: favicon.png');

    // 3. apple-touch-icon.png (180x180)
    await sharp(src).resize(180, 180, { fit: 'cover' }).png({ quality: 90 }).toFile(path.join(outDir, 'apple-touch-icon.png'));
    console.log('Created: apple-touch-icon.png');

    // 4. android-chrome-192x192.png
    await sharp(src).resize(192, 192, { fit: 'cover' }).png({ quality: 90 }).toFile(path.join(outDir, 'android-chrome-192x192.png'));
    console.log('Created: android-chrome-192x192.png');

    // 5. android-chrome-512x512.png
    await sharp(src).resize(512, 512, { fit: 'cover' }).png({ quality: 90 }).toFile(path.join(outDir, 'android-chrome-512x512.png'));
    console.log('Created: android-chrome-512x512.png');

    // 6. mstile-150x150.png
    await sharp(src).resize(150, 150, { fit: 'cover' }).png({ quality: 90 }).toFile(path.join(outDir, 'mstile-150x150.png'));
    console.log('Created: mstile-150x150.png');

    // 7. site.webmanifest
    const manifest = {
        "name": "均在路上 Travel Lab",
        "short_name": "均在路上",
        "description": "台港旅客省錢自由行攻略平台",
        "start_url": "https://golightly.fun/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#e63946",
        "icons": [
            { "src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png" },
            { "src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png" }
        ]
    };
    fs.writeFileSync(path.join(outDir, 'site.webmanifest'), JSON.stringify(manifest, null, 2), 'utf-8');
    console.log('Created: site.webmanifest');

    // 8. favicon.svg (SVG with brand color)
    const svgContent = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <rect width="512" height="512" rx="80" fill="#e63946"/>
  <text x="256" y="320" font-family="Arial, sans-serif" font-size="280" font-weight="bold" fill="white" text-anchor="middle">旅</text>
  <circle cx="256" cy="410" r="28" fill="white" opacity="0.9"/>
</svg>`;
    fs.writeFileSync(path.join(outDir, 'favicon.svg'), svgContent, 'utf-8');
    console.log('Created: favicon.svg');

    console.log('\nAll favicon files generated!');
}

main().catch(err => { console.error('Error:', err); process.exit(1); });
