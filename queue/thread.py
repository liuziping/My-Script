#!/usr/bin/env python
#coding:utf8
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()
#local_school = "cjk"

def process_student():
	print 'Hello, %s (in %s)' % (local_school.name, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
	#global local_school
#	local_school = name
	local_school.name = name
	print "I am %s" % local_school.name
	process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), )
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
