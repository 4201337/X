#!/usr/bin/env python

from multiprocessing.dummy import Pool as Pool
from threading import Lock

myThreads = 500
myAttempts = [0] * 1000
myLock = Lock()

def run(myAttempt):
    with myLock:
        print 0

pool = Pool(myThreads)
pool.map(run, myAttempts)
pool.close()
pool.join()
