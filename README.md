## 1 git clone
## 2 安装依赖:
  Mac
    1 安装python package依赖
    2 brew install tesseract。
    3 修改/Users/yourUser/.virtualenvs/cv/lib/python2.7/site-packages/pytesseract/pytesseract.py文件,Change tesseract_cmd = 'tesseract' to tesseract_cmd = '/usr/local/bin/tesseract'
## 3 修改config.py文件
## 4 运行python auto_ding.py


