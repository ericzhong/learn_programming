#!/usr/bin/env python

import thread
from time import sleep, ctime

loops = [4,2]

def loop(nloops, sec, lock):
    print 'start loop %s at: %s' % (nloops, ctime())
    sleep(sec)
    print 'loop %s done at: %s' % (nloops, ctime())
    lock.release()

def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print 'all DONE at: ', ctime()


if __name__ == '__main__':
    main()
