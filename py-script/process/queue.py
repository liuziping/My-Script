import urllib2
from multiprocessing import Lock, Process, Queue, current_process

def worker(work_queue, done_queue):
    try:
        for url in iter(work_queue.get, 'STOP'):
            print "request url:", url
            status_code = print_site_status(url)
            done_queue.put("%s - %s got %s." % (current_process().name, url, status_code))
    except Exception, e:
        done_queue.put("%s failed on %s with: %s" % (current_process().name, url, e.message))
    return True


def print_site_status(url):
    http = urllib2.urlopen(url)
    return http.getcode()


def main():
    sites = (
        'http://www.100xhs.com/',
        'http://www.miaoshou.com/',
        'http://jf.100xhs.com/',
        'http://gxb.100xhs.com/',
        'http://zt.100xhs.com/',
        'http://m.miaoshou.com/',
        'http://m.100xhs.com/',
        'http://www.baidu.com/',
        'http://www.qq.com/',
    )
    workers = 3
    work_queue = Queue()
    done_queue = Queue()
    processes = []

    for url in sites:
        work_queue.put(url)

    for w in xrange(workers):
        p = Process(target=worker, args=(work_queue, done_queue))
        p.start()
        processes.append(p)
        work_queue.put('STOP')

    for p in processes:
        p.join()

    done_queue.put('STOP')

    for status in iter(done_queue.get, 'STOP'):
        print status


if __name__ == '__main__':
    main()
