#!/usr/bin/env python
#coding:utf-8
import requests
import threading
import sys

class downloader(object):
    # 构造函数
    def __init__(self,url,num=4):
        # 要下载的数据连接
        self.url = url
        # 要开的线程数
        self.num = num
        # 存储文件的名字，从url最后面取
        self.name=self.url.split('/')[-1]
        # head方法去请求url
        r = requests.head(self.url)
        # headers中取出数据的长度
        self.total = int(r.headers['Content-Length'])
        print  'total is %s' % (self.total)


    def get_range(self):
        ranges=[]
        # 比如total是50,线程数是4个。offset就是12
        offset = int(self.total/self.num)
        for i in  range(self.num):
             if  i==self.num-1:
                # 最后一个线程，不指定结束位置，取到最后
                ranges.append((i*offset,''))
             else:
                # 每个线程取得区间
                 ranges.append((i*offset,(i+1)*offset))
        return   ranges       # range大概是[(0,12),(12,24),(25,36),(36,'')]
    
    def download(self,start,end):
        # 拼出Range参数 获取分片数据
        headers={'Range':'Bytes=%s-%s' % (start,end),'Accept-Encoding':'*'}
        res = requests.get(self.url,headers=headers)
        print '%s:%s download success'%(start,end)
        self.fd.seek(start)
        self.fd.write(res.content)


    def run(self):
        self.fd = open(self.name,'w')
        thread_list = [] 
        n = 1
        for ran in self.get_range():
            start,end = ran
            print 'thread %d start:%s,end:%s'% (n,start,end)
            n += 1
            th = threading.Thread(target = self.download,args=(start,end))
            th.start()
            th.join()
        print 'download %s load success'% (self.name)        
        self.fd.close()

if __name__=='__main__':
    #down = downloader('http://51reboot.com/src/blogimg/pc.jpg',num=5)
    if  len(sys.argv) != 3:
        print "usage:  python download2.py url  num"
        sys.exit(1)
    down = downloader(sys.argv[1],int(sys.argv[2]))
    down.run()
