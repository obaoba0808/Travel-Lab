import fitz
import os
import shutil

def add_affiliate_links(input_pdf, output_pdf):
    """为 PDF 添加联盟链接（贴心提示 + 页脚）"""
    try:
        doc = fitz.open(input_pdf)
    except Exception as e:
        print(f'  [ERROR] Cannot open {input_pdf}: {e}')
        return False
    
    # 定义联盟链接（解码后）
    USJ_TICKET = 'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=' + 'https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F46604-universal-studios-japan-e-ticket-osaka-qr-code-direct-entry%2F'
    USJ_EXP = 'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=' + 'https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F3407-universal-studios-japan-express-pass-osaka%2F'
    KANSAI_JR = 'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283449&k_site=' + 'https%3A%2F%2Fwww.klook.com%2Fzh-HK%2Factivity%2F3277-5-day-kansai-wide-area-jr-pass%2F'
    TOKYO_SUBWAY = 'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283447&k_site=' + 'https%3A%2F%2Fwww.klook.com%2Fzh-TW%2Factivity%2F1552-subway-ticket-tokyo%2F'
    TRIP_COM = 'https://tw.trip.com/hotels/list?Allianceid=8237671&SID=312406690&trip_sub1='
    GOLIGHTLY = 'https://golightly.fun'
    LINE_GROUP = 'https://line.me/ti/g/NbNGnW4Eh6'
    
    # 颜色定义
    TIP_BG = (0.91, 0.96, 0.94)  # Tiffany Green 淡背景
    TIP_BORDER = (0.3, 0.71, 0.67)  # Tiffany Green 边框
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        rect = page.rect
        w, h = rect.width, rect.height
        
        # ==========================================
        # 每页底部 footer（保留原有 + 扩展）
        # ==========================================
        footer_y = h - 55
        footer_rect = fitz.Rect(w/2 - 260, footer_y, w/2 + 260, footer_y + 35)
        
        # 添加 footer 背景
        page.draw_rect(footer_rect, color=TIP_BORDER, fill=(0.97, 0.97, 0.97), width=0.5)
        
        # Footer 文字（繁体中文）
        footer_text = '[1] 更多旅遊攻略 >> golightly.fun   |   [2] 加入 LINE 群組   |   [3] Klook 優惠   |   [4] Trip.com 優惠'
        
        try:
            page.insert_textbox(
                footer_rect,
                footer_text,
                fontsize=7.5,
                color=(0.3, 0.71, 0.67),
                align=fitz.TEXT_ALIGN_CENTER,
                fontname='helv'
            )
        except:
            pass  # 某些 PDF 可能有字体问题，跳过
        
        # Footer 超链接（4个区域）
        try:
            # golightly.fun
            page.insert_link({
                'kind': fitz.LINK_URI,
                'uri': GOLIGHTLY,
                'from': fitz.Rect(w/2 - 260, footer_y, w/2 - 120, footer_y + 35)
            })
            
            # LINE 群
            page.insert_link({
                'kind': fitz.LINK_URI,
                'uri': LINE_GROUP,
                'from': fitz.Rect(w/2 - 110, footer_y, w/2 + 20, footer_y + 35)
            })
            
            # Klook 优惠
            page.insert_link({
                'kind': fitz.LINK_URI,
                'uri': USJ_TICKET,  # 默认用 USJ 门票链接
                'from': fitz.Rect(w/2 + 30, footer_y, w/2 + 140, footer_y + 35)
            })
            
            # Trip.com 优惠
            page.insert_link({
                'kind': fitz.LINK_URI,
                'uri': TRIP_COM,
                'from': fitz.Rect(w/2 + 150, footer_y, w/2 + 260, footer_y + 35)
            })
        except:
            pass
        
        # ==========================================
        # 特定页面添加贴心提示框（根据 PDF 内容判断）
        # ==========================================
        pdf_name = os.path.basename(input_pdf).lower()
        
        # 日本相关 PDF：添加 Klook 链接
        if 'japan' in pdf_name or 'tokyo' in pdf_name or 'kyoto' in pdf_name or 'osaka' in pdf_name or 'kansai' in pdf_name or 'usj' in pdf_name or 'hokkaido' in pdf_name or 'okinawa' in pdf_name:
            if page_num == min(2, doc.page_count - 1):  # 前3页之一
                tip_rect = fitz.Rect(w - 300, h/2 - 80, w - 20, h/2 + 20)
                page.draw_rect(tip_rect, color=TIP_BORDER, fill=TIP_BG, width=1.5)
                
                tip_text = '[TIP] 編輯推薦：我們在 Klook 上幫你比價過，通常比官網便宜 5-10%，點此查看今日優惠'
                
                try:
                    page.insert_textbox(
                        tip_rect,
                        tip_text,
                        fontsize=8.5,
                        color=(0.2, 0.2, 0.2),
                        align=fitz.TEXT_ALIGN_LEFT,
                        fontname='helv'
                    )
                    
                    # 根据文件名选择链接
                    if 'usj' in pdf_name:
                        link = USJ_TICKET
                    elif 'kansai' in pdf_name:
                        link = KANSAI_JR
                    elif 'tokyo' in pdf_name:
                        link = TOKYO_SUBWAY
                    else:
                        link = USJ_TICKET  # 默认
                    
                    page.insert_link({
                        'kind': fitz.LINK_URI,
                        'uri': link,
                        'from': tip_rect
                    })
                except:
                    pass
        
        # 韓国相关 PDF：添加 Klook 链接
        elif 'korea' in pdf_name or 'seoul' in pdf_name or 'busan' in pdf_name or 'jeju' in pdf_name:
            if page_num == min(2, doc.page_count - 1):
                tip_rect = fitz.Rect(20, h/2 - 80, 320, h/2 + 20)
                page.draw_rect(tip_rect, color=TIP_BORDER, fill=TIP_BG, width=1.5)
                
                tip_text = '[TIP] 省錢技巧：在 Klook 購買通常比現場便宜，點此查看今日優惠'
                
                try:
                    page.insert_textbox(
                        tip_rect,
                        tip_text,
                        fontsize=8.5,
                        color=(0.2, 0.2, 0.2),
                        align=fitz.TEXT_ALIGN_LEFT,
                        fontname='helv'
                    )
                    
                    page.insert_link({
                        'kind': fitz.LINK_URI,
                        'uri': 'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2F',
                        'from': tip_rect
                    })
                except:
                    pass
        
        # 泰国/东南亚 PDF：添加 Klook 链接
        elif 'bangkok' in pdf_name or 'chiang' in pdf_name or 'danang' in pdf_name:
            if page_num == min(2, doc.page_count - 1):
                tip_rect = fitz.Rect(w/2 - 150, h/2 - 80, w/2 + 150, h/2 + 20)
                page.draw_rect(tip_rect, color=TIP_BORDER, fill=TIP_BG, width=1.5)
                
                tip_text = '[TIP] 推薦：在 Klook 上預訂通常更便宜，點此查看今日優惠'
                
                try:
                    page.insert_textbox(
                        tip_rect,
                        tip_text,
                        fontsize=8.5,
                        color=(0.2, 0.2, 0.2),
                        align=fitz.TEXT_ALIGN_CENTER,
                        fontname='helv'
                    )
                    
                    page.insert_link({
                        'kind': fitz.LINK_URI,
                        'uri': 'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1283452&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2F',
                        'from': tip_rect
                    })
                except:
                    pass
        
        # 台湾 PDF：添加 Klook 酒店链接
        elif 'taipei' in pdf_name or 'tainan' in pdf_name or 'hualien' in pdf_name or 'kenting' in pdf_name or 'jiufen' in pdf_name:
            if page_num == min(2, doc.page_count - 1):
                tip_rect = fitz.Rect(w/2 - 200, h/2 - 80, w/2 + 200, h/2 + 20)
                page.draw_rect(tip_rect, color=TIP_BORDER, fill=TIP_BG, width=1.5)
                
                tip_text = '[TIP] 推薦：在 Klook 上訂酒店通常有獨家優惠，點此查看'
                
                try:
                    page.insert_textbox(
                        tip_rect,
                        tip_text,
                        fontsize=8.5,
                        color=(0.2, 0.2, 0.2),
                        align=fitz.TEXT_ALIGN_CENTER,
                        fontname='helv'
                    )
                    
                    page.insert_link({
                        'kind': fitz.LINK_URI,
                        'uri': 'https://affiliate.klook.com/redirect?aid=121592&aff_adid=1282378&k_site=https%3A%2F%2Fwww.klook.com%2Fzh-TW%2F',
                        'from': tip_rect
                    })
                except:
                    pass
    
    # 保存
    try:
        doc.save(output_pdf)
        doc.close()
        return True
    except Exception as e:
        print(f'  [ERROR] Save failed {output_pdf}: {e}')
        doc.close()
        return False


# 主程序
if __name__ == '__main__':
    downloads_dir = 'downloads'
    pdfs_dir = 'pdfs'
    
    # 获取所有 PDF（排除已处理的 usj-quick-pass.pdf）
    pdf_files = [f for f in os.listdir(downloads_dir) if f.endswith('.pdf') and f != 'usj-quick-pass.pdf']
    
    print(f'[INFO] Found {len(pdf_files)} PDFs to process')
    print('=' * 60)
    
    success_count = 0
    fail_count = 0
    
    for pdf_file in pdf_files:
        input_path = os.path.join(downloads_dir, pdf_file)
        output_path = os.path.join(pdfs_dir, pdf_file.replace('.pdf', '-with-links.pdf'))
        
        print(f'\nProcessing: {pdf_file}')
        
        # 检查输入文件是否存在
        if not os.path.exists(input_path):
            print(f'  [WARN] File not found: {input_path}')
            fail_count += 1
            continue
        
        # 添加联盟链接
        if add_affiliate_links(input_path, output_path):
            size = os.path.getsize(output_path)
            print(f'  [SUCCESS] Saved to: {output_path}')
            print(f'  Size: {size:,} bytes')
            success_count += 1
            
            # 覆盖原文件
            try:
                shutil.copy2(output_path, input_path)
                print(f'  [SUCCESS] Overwritten: {input_path}')
            except Exception as e:
                print(f'  [WARN] Overwrite failed: {e}')
        else:
            fail_count += 1
    
    print('\n' + '=' * 60)
    print(f'[DONE] Success: {success_count}, Failed: {fail_count}')
    print(f'[INFO] Total processed: {len(pdf_files)} PDFs')
