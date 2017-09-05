#!/usr/bin/env python
#coding:utf-8
class Response(object):
    '''response对象'''
    def __init__(self):
        self.data = None
        self.errorCode = 0 
        self.errorMessage = None

def test():
    res = Response()
    res.errorCode = 106
    res.errorMessage = "just a test"
    res.data = {'name':'wd'}
    return res 

def test1(): 
    result = test()
    print  "{}".format(result.data)

test1()    
