'''


'''
from multiprocessing import Pool
import time
import os

def test():
    print('.....current pid {}, ppid {}'.format(os.getpid(), os.getppid()))
    for i in range(3):
        print('.......{}'.format(i))
        time.sleep(1)
    return 'test'


def test2(args):
    print('....callback  func...pid {}'.format(os.getpid()))
    print('.......callback func-args {}'.format(args)) #
    #args are from test return

pool = Pool(3)
pool.apply_async(func=test, callback=test2)

# time.sleep(5)

while True:
    time.sleep(1)
    print('.....parent process pid ={}'.format(os.getpid()))