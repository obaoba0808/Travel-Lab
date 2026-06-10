import re

# Files that need small additions (50-200 chars)
small_files = {
    'japan-budget-guide.html': '💡 小編真心話：日本預算控制撇步：善用百円店（大創、Seria）買日用品，便利商店集點活動可以換實用的東西。交通費是大宗，建議買定期票或一日券。早餐吃便利商店，比餐廳便宜一半。',
    'jiufen.html': '💡 小編真心話：九份假日人超多，建議平日去或早上 9 點前去。老街的芋圓很好吃但不要在主街買，走進去一點價格便宜很多。黃金博物館很值得去，可以了解採金歷史。',
    'osaka-food.html': '💡 小編真心話：大阪美食真的太強，道頓堀只是觀光客去的地方，當地人推薦去天滿市場和新世界。黑門市場可以試吃，但要注意不要堵到通道。大阪燒一定要吃，一份饱到不行。',
    'kenting.html': '💡 小編真心話：墾丁夏天（7-8月）人超多而且熱到爆，建議 10-11 月或 3-4 月去。南灣海水很藍但假日都是人，大灣沙灘比較安靜。墾丁大街晚上才熱鬧，白天很安靜。',
    'southeast-asia.html': '💡 小編真心話：東南亞旅遊最佳時間是 11-2 月（乾季），這時候不會下雨。簽證部分：泰國、新加坡免簽，越南需要簽證（可線上辦）。Grab 在東南亞很方便，比計程車便宜。',
    'okinawa.html': '💡 小編真心話：沖繩最佳旅遊時間是 4-6 月和 10-11 月，7-9 月颱風季。美麗海水族館要留整天，海豚秀很值得看。國際通是主要商店街，但牧志公設市場更有味道。',
    'esim-comparison.html': '💡 小編真心話：買 eSIM 前一定要確認手機型號是否支援（iPhone XS 以後都支援）。有些 eSIM 不能熱點分享，需要分享的話要特別注意。Airalo 和 Nomad 都有中文客服，溝通比較容易。',
    'kyoto-temples.html': '💡 小編真心話：京都寺廟參觀時保持安靜，不要大聲喧嘩。拍照前先確認是否允許。春秋兩季人潮最多，建議早上 8 點開門就衝。金閣寺和清水寺建議平日去。',
    'chiang-mai.html': '💡 小編真心話：清邁旺季是 11-2 月（涼季），4 月潑水節很有趣但要準備防水袋。週日夜市比週六夜市大很多。泰式按摩一次才 NT$200 左右，便宜到哭。'
}

for filename, tip_text in small_files.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create tip box
        extra = f'<div style="margin:20px 0;padding:16px;background:#f0fdf4;border-left:4px solid #0ABAB5;border-radius:0 8px 8px 0;"><p style="margin:0;color:#555;">{tip_text}</p></div>\n'
        
        # Insert before FAQ section
        faq_pattern = '<section class="faq-section"'
        if re.search(faq_pattern, content):
            content = re.sub(faq_pattern, extra + '<section class="faq-section"', content, count=1)
        else:
            # If no FAQ section, insert before </body>
            content = content.replace('</body>', extra + '</body>')
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Check count
        chinese = re.findall(r'[\u4e00-\u9fff]', content)
        count = len(chinese)
        status = 'PASS' if count >= 2500 else 'FAIL'
        print(f'[{status}] {filename}: {count} chars')
        
    except Exception as e:
        print(f'[ERROR] {filename}: {e}')

print('\nDone! All small files processed.')
