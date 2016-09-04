#!/usr/bin/env python

from multiprocessing.dummy import Pool as Pool
from threading import Lock

myList = 'txt.txt'
myThreads = 600
myLock = Lock()

def run(username):
    username = username.strip()
    with myLock:
        print username

with open(myList) as myList:
    myList = myList.readlines()

pool = Pool(myThreads)
pool.map(run, myList)
pool.close()
pool.join()
