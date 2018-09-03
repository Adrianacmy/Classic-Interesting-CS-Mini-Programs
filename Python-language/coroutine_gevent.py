'''
遇到耗時操作時　切換
單線程完成多併發
'''



import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

        # 耗時操作，　切換任務
        gevent.sleep(1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g4 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()
g4.join()



def main():
    f(5)

if __name__ == '__main__':
    main()


###########################################################

# tcp gevent server

import sys
import time

from gevent import socket, monkey

monkey.patch_all()　#會修改以下代碼,　適應gevent


def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print('recv: ', data)
        conn.send(data)

def server(port):
    s = socket.socket()
    s.bind(('', port))
    s.listen(100)
    while True:
        client, addr = s.accept() #non-blocking with gevent.socket, 耗時操作
        gevent.spawn(handle_request, client)



def main():
    server(7788)

if __name__ == '__main__':
    main()