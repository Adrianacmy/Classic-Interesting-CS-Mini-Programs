'''
線程執行循序不確定

線程間共享全局變量

進程與線程的區別：


'''
import threading
# from threading import Thread

import time


# def test():
#     print('..sleepy...')
#     time.sleep(1)


# for i in range(5):
#     t = threading.Thread(target=test)
#     t.start()


################################################################################

class CusThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print('I am {} @ {}'.format(self.name, str(i)))


# def main():
#     for i in range(5):
#         t = CusThread()
#         t.start()  # call run()


# if __name__ == '__main__':
#     main()

################################################################################
# 避免多線程對全局變量的修改
# 原子性
g_num = 0
g_flag = 1


def test1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(10000):
            g_num += 1
        g_flag = 0
    print('...test1...{}'.format(g_num))


def test２():
    global g_num
    global g_flag
    # 輪詢
    while True:
        if g_flag != 1:
            for i in range(10000):
                g_num += 1
            break
    print('...test2...{}'.format(g_num))
# above code made cpu occupied, not efficient


# t1 = threading.Thread(target=test1)
# t1.start()

#time.sleep(3)　＃很ｌｏｗ的方式

# t2 = threading.Thread(target=test2)
# t2.start()

###############################################################################
# 互斥鎖避免多線程對全局變量的修改

# where to add the lock, 儘可能小代碼塊，　更高效
# 等通知

lock = threading.Lock()

g_num = 0

# def test1():
#     global g_num
#     for i in range(10000):
#         lock.acquire()　
#         g_num += 1
#         lock.release()
#     print('...test1...{}'.format(g_num))


# def test２():
#     global g_num
#     for i in range(10000):
#         #通知release lock
#         lock.acquire()
#         g_num += 1
#         lock.release()
#     print('...test2...{}'.format(g_num))
# above code made cpu occupied, not efficient


# t1 = threading.Thread(target=test1)
# t1.start()


# t2 = threading.Thread(target=test2)
# t2.start()

###############################################################################
# 多線程使用飛全局變量
# 函數內變量不共享, 不需要加鎖

def test1():
    name = threading.current_thread().name
    print('........{}'.format(name))
    g_num = 100
    if name == 'Thread-1':
        g_num += 1
    else:
        time.sleep(1)
    print('.......{}......{}'.format(name, g_num))

t1 = threading.Thread(target=test1)
t1.start()


t2 = threading.Thread(target=test1)
t2.start()


################################################################################
threadLocal