#!/bin/env python
#coding:utf-8

'''
    Python生成二维码
    pip install Image
    pip install qrcode
'''

import qrcode

# 设置二维码图片绑定的网址
img = qrcode.make('http://www.miaoshou.com')

# 生成二维码图片
with open('test.png', 'wb') as f:
    img.save(f)
