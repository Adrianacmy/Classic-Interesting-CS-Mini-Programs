'''
計算密集型: 佔用大量cpu 資源，　多進程處理，　因爲多線程的GIL
ＩＯ密集型：　大量等待網絡數據到來，　多線程，協程處理


協程：　減少大量CPU切換時間, 不同任務切換執行, 開發者決定程序間的切換


'''


import time


def a():
    while True:
        print('......a....')
        yield
        time.sleep(1)


def b(c):
    while True:
        print('....b.....')
        c.next()
        time.sleep(1)


if __name__ == '__main__':
    a = a()
    b(a)

####################################################################

# coroutine with greenlet

import time
from greenlet import greenlet


def a():
    while True:
        print('......a....')
        gr2.switch()
        time.sleep(1)


def b(c):
    while True:
        print('....b.....')
        gr1.switch()
        time.sleep(1)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()