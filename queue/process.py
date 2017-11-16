import os,time
print 'Process (%s) start ...' % os.getpid()
pid=os.fork()
if pid == 0:
	print 'I am child process (%s) and my parent is %s' % (os.getpid(),os.getppid())
	#time.sleep(60)
else:
	print 'I (%s) just create a child process (%s)' % (os.getpid(),pid)
	#time.sleep(1)
