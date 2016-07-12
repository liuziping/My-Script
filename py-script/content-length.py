#!/bin/env python
import requests

def file_size(url):
    r = requests.head(url)
    size = r.headers['content-length']
    return size

if __name__=="__main__":
    #print file_size('http://dldir1.qq.com/qqfile/qq/QQ7.1/14522/QQ7.1.exe')
    print file_size('http://51reboot.com/src/blogimg/pc.jpg')
    
