const fs = require('fs');

// PDF content data - ALL 21 PDFs with ASCII-safe markers only
const pdfData = {
  "tokyo-metro-map": {
    "title": "Tokyo Metro Complete Guide",
    "subtitle": "Route Map x Transfer Tips x 24H Ticket Calculator | Full Version",
    "sections": [
      {
        "h2": "Tokyo Metro System Overview",
        "body": "[OK] Tokyo Metro has 13 lines (9 Tokyo Metro + 4 Toei Subway) with 286 stations\n[OK] Average daily ridership: over 10 million\n[OK] Fares are distance-based, NOT flat rate\n[!] IMPORTANT: Tokyo Metro is NOT a single-ticket system like London Underground\n\nMain Lines:\n* Ginza Line: Shibuya - Asakusa (oldest line)\n* Marunouchi Line: Ogikubo - Honancho\n* Hibiya Line: Naka-meguro - Kita-senju\n* Tozai Line: Nakano - Nishi-funabashi\n* Chiyoda Line: Ayase - Yoyogi-uehara\n* Yurakucho Line: Wakoshi - Shin-kiba\n* Hanzomon Line: Shibuya - Oshiage\n* Namboku Line: Meguro - Akabane-iwabuchi\n* Fukutoshin Line: Wakoshi - Shibuya\n\nToei Subway Lines:\n* Asakusa Line: Nishi-magome - Oshiage\n* Mita Line: Meguro - Nishi-takashima\n* Shinjuku Line: Shinjuku - Motoyawata\n* Oedo Line: Circular line (Hikarigaoka - Tocho-mae)"
      },
      {
        "h2": "24-Hour Ticket Full Analysis",
        "body": "[OK] 24H Ticket: Adult Y800, Child Y400\n[OK] Regular fare calculation: 3+ rides = break even (Shinjuku-Shibuya Y240 + Shibuya-Omotesando Y220 + Omotesando-Aoyama-itchome Y220 = Y680, 4th ride is FREE)\n[OK] Usage limit: 24 hours from FIRST USE, not calendar day\n[!] NOTE: JR lines NOT included in 24H ticket (Yamanote Line needs separate ticket)\n[!] NOTE: Narita Express, Haneda Express NOT included (need separate ticket)\n\nWhen to buy 24H ticket?\n* Ride 3+ times/day → MUST buy\n* Stay in Shinjuku, visit Shibuya+Harajuku+Omotesando+Roppongi → MUST buy\n* Only 2 rides → single tickets cheaper\n* Mainly JR Yamanote Line → don't buy (JR Pass better)"
      },
      {
        "h2": "Transfer Tips & Key Stations",
        "body": "[OK] Shinjuku Station: World's largest station, 53 exits. Transfer time: 15+ minutes\n[OK] Shibuya Station: Hachiko Exit is main exit. Transfer time: 5-10 minutes\n[OK] Tokyo Station: Divided into 'Above ground' and 'Underground'. Transfer time: 10-15 minutes\n[!] WARNING: Some stations have SAME name but DIFFERENT lines (e.g., 'Tokyo' on different lines)\n\nTransfer Strategy:\n* Use IC Card (Suica/Pasmo) for seamless transfer\n* Paper ticket users must exit and re-enter (additional fare may apply)\n* Transfer time: reserve 5-10 minutes (15+ for large stations like Shinjuku)\n\nReading the Map:\n* Orange = Ginza Line\n* Red = Marunouchi Line\n* Yellow = Hibiya Line\n* Blue = Tozai Line\n* Green = Chiyoda Line\n* Blue-Green = Yurakucho Line\n* Purple = Hanzomon Line\n* Teal = Namboku Line\n* Brown = Fukutoshin Line"
      }
    ]
  },
  
  "kansai-pass-calculator": {
    "title": "Kansai Railway Pass Calculator",
    "subtitle": "Hankyu x Keihan x Kintetsu x JR Kansai x Kanku Rapid | Full Version",
    "sections": [
      {
        "h2": "Kansai Pass System Overview",
        "body": "[OK] Kansai region has 15+ railway passes with different coverage, validity, and prices\n[OK] Main pass types: JR Kansai Area Pass (1-4 days), Hankyu 1-Day Pass, Keihan 1-Day Pass, Kintetsu Railway Pass (1-2 days)\n[!] WARNING: Choosing wrong pass = wasting Y1000-3000\n\nCoverage Comparison:\n* JR Kansai Pass: All JR lines in Kansai (includes Kanku Rapid)\n* Hankyu Pass: Hankyu Railway only (Osaka-Umeda to Kyoto-Kawaramachi)\n* Keihan Pass: Keihan Railway only (Osaka-Yodoyabashi to Kyoto-Gion-Shijo)\n* Kintetsu Pass: Kintetsu Railway only (Osaka-Namba to Nara/Kyoto)"
      },
      {
        "h2": "JR Kansai Area Pass Deep Analysis",
        "body": "[OK] 1-Day Pass: Adult Y2800, Child Y1400\n[OK] 2-Day Pass: Adult Y4600, Child Y2300\n[OK] 3-Day Pass: Adult Y5800, Child Y2900\n[OK] 4-Day Pass: Adult Y6800, Child Y3400\n\nCoverage:\n* All JR lines in Kansai region (includes limited express, but need limited express ticket)\n* Kanku Rapid (Kansai Airport to Tennoji/Namba)\n* Osaka Loop Line, Sakurajima Line (Universal Studios Japan)\n* JR lines in Kyoto (Sagano Line, Nara Line)\n\nNOT Included:\nX Private railways (Hankyu, Keihan, Kintetsu, etc.)\nX Subway (Osaka Metro, Kyoto Metro)\nX Bus (except JR Bus)"
      },
      {
        "h2": "How to Calculate Break-Even? (Full Calculation)",
        "body": "Calculation Example: From Kansai Airport, visit Osaka+Kyoto+Nara+Kobe, 4-day trip\n\nItinerary A (Buy JR Kansai 4-Day Pass Y6800):\nDay1: Kanku Rapid Airport→Tennoji Y1060\nDay1: Osaka Loop Line Tennoji→Osaka Y190\nDay2: JR Sagano Line Osaka→Kyoto Y590\nDay2: JR Nara Line Kyoto→Nara (round trip) Y1180\nDay3: Osaka Loop Line Osaka→Universal (round trip) Y760\nDay4: Kanku Rapid Tennoji→Airport Y1060\nTotal: Y4840, but 4-Day Pass = Y6800, 'NOT breaking even'\n\nItinerary B (No JR Pass, use IC card):\nSame routes with IC card: Y4840, save Y1960\n\nConclusion: JR Kansai Pass is BEST for 'ride Shinkansen + limited express' travelers. Normal tourists should use IC card + single tickets."
      }
    ]
  }
};

// Write JSON file using Node.js (correct UTF-8 handling)
const outputPath = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/Travel-Lab/_pdf_content.json';
fs.writeFileSync(outputPath, JSON.stringify(pdfData, null, 2), 'utf-8');
console.log('JSON data written: ' + Object.keys(pdfData).length + ' PDFs defined');
console.log('File size: ' + fs.statSync(outputPath).size + ' bytes');
