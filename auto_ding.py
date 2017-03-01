#coding=utf8

import requests
import config

url = config.baseurl+'add_comment'
cookie = config.cookie

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':cookie

}

count = 1
while True:
    print 'ding' + str(count)

    data = {
        "rv_comment": 'ding' + str(count),
        "ck": "aubV",
        'start': '0',
        'submit_btn': '加上去'

    }
    while True:
        rval = requests.get(config.baseurl+'?start=5000#last',headers=header)
        #检验是否需要输入验证码?
        import re
        data['ck'] = re.search('ck=(\w+)', rval.text).group(1)
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
    time.sleep(config.time_interval)
    count+=1