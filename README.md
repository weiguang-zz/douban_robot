# douban_captcha_identify

* 识别豆瓣验证码, 主要用pytesseract做字母识别.
* 主要做了图片处理, 除去过多的干扰噪点.
* 现在成功率不高, 每张图需要去多次尝试, 因为豆瓣验证码都是英文单词, 还需要把识别的单词去词库中校对, 如果是正常单词则可信.
* 识别率率偏低


## requirement
* pytesseract==0.1.6
* Pillow==2.8.1

> pip install -r requirement.txt

## 功能介绍
* 根据点阵颜色强制转换黑白点
* 横向扫描, 获取最大边界大小. 除去小于最大噪点大小的面积.

# remove password
# donate me ？ alipay
