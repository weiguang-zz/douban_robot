#coding=utf8

import requests

url = 'https://www.douban.com/group/topic/96862522/add_comment'
cookie = 'bid=48b22m30B88; gr_user_id=f1f04c44-2438-4cae-b635-666811c3d059; ll="108288"; viewed="1440885_2130190"; ct=y; _ga=GA1.2.313001814.1469623233; _vwo_uuid_v2=411E04E8C09149C387FC49DC9ED769F9|8677076ceadc89260a5b497f4aaa2412; ps=y; dbcl2="95449104:+gSBFjguWlc"; ck=4nrT; ap=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1487225612%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; __utmt=1; push_doumail_num=0; _pk_id.100001.8cb4=45543911a6ab655d.1470037065.19.1487225715.1487212912.; _pk_ses.100001.8cb4=*; __utma=30149280.313001814.1469623233.1487212822.1487225612.27; __utmb=30149280.72.5.1487225715704; __utmc=30149280; __utmz=30149280.1486102750.20.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.9544; push_noty_num=1'

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':cookie

}

count = 1
while True:
    print 'ding' + str(count)

    data = {
        "rv_comment": 'ding' + str(count),
        "ck": "4nrT",
        'start': '0',
        'submit_btn': '加上去'

    }
    while True:
        rval = requests.get('https://www.douban.com/group/topic/96862522/?start=100#last',headers=header)
        #检验是否需要输入验证码?
        import re
        mat = re.search('src=\"(.*?captcha.*?)\"', rval.text)
        if mat:
            #需要识别验证码
            print '识别验证码'
            captcha_url = mat.group(1)
            import identify_code
            try:
                code = identify_code.recognize_url(captcha_url)#识别验证码
                print '识别到的验证码为:'+str(code)
            except:
                code = 'nnnn'
            data['captcha-solution'] = code
            data['captcha-id'] = re.search('id=(.*?)&', captcha_url).group(1)
            rval = requests.post(url=url,data=data,headers=header)
            import enchant
            d = enchant.Dict("en_US")
            try:
                if d.check(code):
                    break
            except:
                pass
        else:
            rval = requests.post(url=url, data=data, headers=header)
            break


    import time
    time.sleep(60)
    count+=1