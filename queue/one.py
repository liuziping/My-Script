#!/usr/bin/python
#coding:utf8
import time

def test(name,n):
	for i in xrange(n):
		print i, name
		time.sleep(1)

test('声音',2)
test('动画',2)

