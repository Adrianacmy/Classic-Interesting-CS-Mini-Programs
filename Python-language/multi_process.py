'''
Process創建的子進程都結束後，　主進程纔會運行

 https://docs.python.org/3.6/library/multiprocessing.html

進程間默認沒關係

'''

from multiprocessing import Process, Pool
import time
import random

#######################################################################
def test():
    for i in range(5):
        print('test...')
        time.sleep(1)


p = Process(target=test)
p.start()

p.join([timeout]) #阻塞，wait child process is done then continue its below code or wait timeout

# p.terminate()

print('...main...')

##############################################################################


#另一種方法用Process創建多進程
# 需要重寫run()
class NewProcess(Process):

    # run get called while start()
    def run(self):
        while True:
            print('...test..')
            time.sleep(1)

p = NewProcess()
p.start()

while True:
    print('....main....')
    time.sleep(1)

##########################################################################

# process pool
def worker(num):
    t_start = time.time()
    print('process {} start, process id is {}'.format(msg, os.getpid()))
    time.sleep(random.random())
    t_stop = time.time()
    print(msg, 'done with {:.2f}'.format(s_stop-t_start))


po = Pool(3) # max process 3

for i in range(10):
    print('.........{}'.format(i))
    # add task to pool,３個進程輪詢任務
    po.apply_async(worker, (i,))　＃　用tuple傳參
    # po.apply(worker, (i,)) # 阻塞添加任務, 幾乎不用

    ＃　主進程一般等待，　任務都在子進程中執行

print('...start....')
po.close() #close pool, po won't accept more new request

# 住進程添加任務後，　主進程默認不會等待進程池中的任務執行完成後才結束，　而是主進程的任務完成後　立即結束，　如果沒有join,會導致進程次中的任務不會執行
po.join() # wait all child process are done, after close
print('...end....')


#########################################################################＃＃＃
ret = os.fork()
if ret == 0:
    # child process
else:
    # parent process

# 底層一般不用

##########################################################################
# 進程間傳遞信息
from multiprocessing import Queue

# q = Queue(3)
# q.size()
# q.empty()
# q.full()
# q.put('daf')
# q.get('')

# q.nowait()
# q.put(100)
# q.put([])
# q.put({})
# q.put_nowait(['a'])

def write(q):
    for value in ['a', 'b', 'c']:
        print('put {} to queue'.format(value))
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('get {} from queue'.format(value))
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print('')
    print('read and write done')

################################################################

# 進程池中進程間的通訊
from multiprocessing import Manager, Pool
def reader(q):
    print('reader start {}, parent process is {}'.format(os.getpid(, os.getppid())))
    for i in range(q.qsize()):
        print('msg from Queue: {}'.format(q.get(True)))

def writer(q):
    print('writer start {}, its parent process is {}'.format(os.getpid(), os.getppid()))
    for i in 'something':
        q.put(i)

def main():
    print('{} start'.format(os.getpid()))
    q = Manager().Queue() #
    po = Pool()
    po.apply(writer, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print('{} end'.format(os.getpid()))

if __name__ == '__main__':
    main()