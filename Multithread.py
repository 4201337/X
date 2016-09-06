from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock as LockPool
import requests
import time

myList = [0] * 1000
myThreads = 250
myLock = LockPool()
myPool = ThreadPool(myThreads)

def myRun(x):
    with myLock:
        print 0

"""
with open(myList) as myList:
    myList = myList.readlines()
"""

myStart = time.time()

if __name__ == '__main__':
    myPool.map(myRun, myList)
    myPool.close()
    myPool.join()

myEnd = time.time()

print '============================='
print 'Done!'
print '============================='
print 'Total Time    :' , round(myEnd - myStart, 2) , 'Seconds'
print 'Total Threads :' , myThreads
print 'Total Tries   :' , len(myList)
print '============================'
print 'Thank you, come again!'
print '============================'
