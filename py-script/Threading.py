#!/usr/bin/env python
#coding:utf-8
import threading,time

'''
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name
        
print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
'''
# 线程锁

# 假定这是银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run(n):
    # 修改10次
    for i in range(3): 
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
            print 'thread %s is lock.' % threading.current_thread().name
        finally:
            # 改完了一定要释放锁:
            print 'thread %s lock release.' % threading.current_thread().name
            lock.release()

t1 = threading.Thread(target=run, args=(5,))
t2 = threading.Thread(target=run, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

