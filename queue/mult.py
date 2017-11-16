#!/usr/bin/python 

from multiprocessing import Process
import os

def run(name,n):
	print "%s Run child process %s (%s),my parent is (%s).." % (n,name,os.getpid(),os.getppid())

if __name__=='__main__':
	print 'Parent process %s' % os.getpid()
	for n in xrange(3):
		p = Process(target=run,args=('test',n,))
		print 'Process will start (%s)' % os.getpid()
		p.start()
		p.join()
	print 'Process end (%s)' % os.getpid()

