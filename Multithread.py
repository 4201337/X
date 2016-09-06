from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock as LockPool
import requests

myList = [0] * 1000
myThreads = 10
myLock = LockPool()
myPool = ThreadPool(myThreads)

i = 0
def myRun(x):
    global i
    i += 1
    with myLock:
        print i

if __name__ == '__main__':
    myPool.map(myRun, myList)
    myPool.close()
    myPool.join()
