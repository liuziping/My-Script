#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process,Pool
import os,time,random

'''
# Process模块
def run(name):
    time.sleep(5)   #为 了测试子进程后退出，父进程先执行完毕的场景
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent  proce ss %s.' % os.getpid()
    p = Process(target=run, args=('wd',))
    print 'I am  parent process %s, child process will start.'  % os.getpid()
    p.start()
    p.join()    # 子进程结束后再往下执行父进程的任务,即时父进程先执行完也不会退出，会等子进程一起结束退出
    print 'I am parent process %s, child process end.'  % os.getpid()
'''
#进程池Pool模块
def run(name):
     print "Run child process %s (%s),my parent is (%s).." % (name,os.getpid(),os.getppid())
     start = time.time()
     time.sleep(random.random()*3)
     end = time.time()
     print 'Task %s runs %0.2f seconds..(%s)' % (name,(end-start),os.getpid())

if __name__=='__main__':
     print 'Parent process %s' % os.getpid()
     p = Pool(3)          # 创建进程池 p=Pool()  默认创建进程数为cpu核数
     for n in xrange(4):
         result = p.apply_async(run,args=(n,))   #用子进程处理任务
     print 'waiting for all subprocess done (%s)' % os.getpid()
     p.close()       # 调用close()会等待池中的worker进程执行结束再关闭pool,
     p.join()        # 等待所有子进程执行完毕后在执行父进程，如果父进程先退出，所有子进程也消失，任务终止
     # if result.successful(): # result.successful()表示整个调用执行的状态，如果还有worker没有执行完，则会抛出AssertionError异常。
     # print 'successful'
     print 'all subprocess end (%s)' % os.getpid()
