import os, time, random
from multiprocessing import Pool, current_process

def long_time_task(name):
    print '%s Run task %s (%s)...' % (current_process().name, name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print '%s Task %s runs %0.2f seconds.' % (current_process().name, name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(3)
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
