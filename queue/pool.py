#!/usr/bin/python 

from multiprocessing import Pool
import os,time,random
def run(name):
	print "Run child process %s (%s),my parent is (%s).." % (name,os.getpid(),os.getppid())
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print 'Task %s runs %0.2f seconds..(%s)' % (name,(end-start),os.getpid())

if __name__=='__main__':
	print 'Parent process %s' % os.getpid()
	p = Pool(3)
	for n in xrange(4):
		p.apply_async(run,args=(n,))
	print 'waiting for all subprocess done (%s)' % os.getpid()
	p.close()
	p.join()
	print 'all subprocess end (%s)' % os.getpid()

