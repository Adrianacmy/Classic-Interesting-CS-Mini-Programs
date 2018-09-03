'''
EPOLLIN: readable
EPOLLOUT: writeable
EPOLLET: ET


'''


import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind local ip and port
s.bind('', 7788)
s.listen(10)

epoll = select.epoll()
epoll.register(s.fileno(), select.EPOLLIN | select.EPOLLET)

connecitons = {}
addresses = {}

while True:

    # 檢測所有可收可讀的socket
    epoll_list = epoll.poll()

    # fd: file number describe
    for fd, events in epoll_list:
        if fd == s.fileno()
            conn, addr = s.accept()

            print('new client {}'.format(str(addr)))

            connecitons[conn.fileno()] = conn
            addresses[conn.fileno()] = addr

            # register writeable event
            epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)

        elif events == select.EPOLLIN:
            recvData = connecitons[fd].recv(1024)

            if len(recvData) > 0:
                print('recv {}'.format(recvData))
            else:
                epoll.unregister(fd)

                connections[fd].close()

                pirnt('..{} is offline...'.format(str(addresses[fd])))
