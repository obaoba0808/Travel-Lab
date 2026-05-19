import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/monetization.js', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''    let bannerHtml = '';
    
    if (page.includes('japan') || page.includes('tokyo') || page.includes('kansai') || page.includes('hokkaido') || page.includes('okinawa') || page.includes('kyoto')
      || page.includes('korea') || page.includes('seoul') || page.includes('busan') || page.includes('jeju')
      || page.includes('taiwan') || page.includes('hualien') || page.includes('tainan') || page.includes('kenting')
      || page.includes('southeast') || page.includes('chiang-mai') || page.includes('bangkok')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17138130?Allianceid=8237671&SID=312406690&trip_sub1=" frameborder="0" scrolling="no" id="DB17138130"></iframe>';
    }'''

new = '''    let bannerHtml = '';
    
    // Destination-specific Trip.com dynamic banners
    if (page.includes('tokyo')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161314?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161314"></iframe>';
    } else if (page.includes('osaka') || page.includes('usj')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161349?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161349"></iframe>';
    } else if (page.includes('kyoto')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161349?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161349"></iframe>';
    } else if (page.includes('hokkaido') || page.includes('sapporo')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161468?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161468"></iframe>';
    } else if (page.includes('okinawa')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161314?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161314"></iframe>';
    } else if (page.includes('kansai')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161349?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161349"></iframe>';
    } else if (page.includes('seoul')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161370?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161370"></iframe>';
    } else if (page.includes('busan')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161545?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161545"></iframe>';
    } else if (page.includes('jeju')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161370?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161370"></iframe>';
    } else if (page.includes('chiang-mai')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161559?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161559"></iframe>';
    } else if (page.includes('bangkok')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161132?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161132"></iframe>';
    } else if (page.includes('taipei') || page.includes('taiwan-travel') || page.includes('hualien') || page.includes('tainan') || page.includes('kenting') || page.includes('jiufen')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17138130?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:728px;height:90px" frameborder="0" scrolling="no" style="border:none" id="DB17138130"></iframe>';
    } else if (page.includes('vietnam') || page.includes('danang')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17165612?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17165612"></iframe>';
    } else if (page.includes('southeast')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161559?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161559"></iframe>';
    } else if (page.includes('japan')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161314?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161314"></iframe>';
    } else if (page.includes('korea')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17161370?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:468px;height:60px" frameborder="0" scrolling="no" style="border:none" id="DB17161370"></iframe>';
    } else if (page.includes('taiwan')) {
      bannerHtml = '<iframe border="0" src="https://tw.trip.com/partners/ad/DB17138130?Allianceid=8237671&SID=312406690&trip_sub1=" style="width:728px;height:90px" frameborder="0" scrolling="no" style="border:none" id="DB17138130"></iframe>';
    }'''

if old in content:
    content = content.replace(old, new)
    with open('js/monetization.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Replaced OK ({len(new)} bytes)')
else:
    print('ERROR: old pattern not found')
