# douban_captcha_identify

## requirement
* pytesseract==0.1.6
* Pillow==2.8.1

> pip install -r requirement.txt

## 功能介绍
* 根据点阵颜色强制转换黑白点
* 横向扫描, 获取最大边界大小. 除去小于最大噪点大小的面积.
