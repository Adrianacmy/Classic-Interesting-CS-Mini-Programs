'''
https://www.youtube.com/watch?v=PrswE5V-RTg&index=26&list=PLe_BlddcFvNRpnlRju4J1vmcrvibke9cP
'''


from socket import *
from multiprocessing import Process


def handleClient(newSocket, destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print(str(destAddr), recvData)
        else:
            print('{} client is closed'.format(str(destAddr)))
    newSocket.close()


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    serverSocket.bind(localAddr)
    serverSocket.listen(5)

    try:
        while True:
            print('......parent process, waiting for new client....')
            newSocket, destAddr = serverSocket.accept()

            print('.....parent process, create new process to handle request from {}'.format(
                str(destAddr)))

            client = Process(target=handleClient, args=(newSocket, destAddr))
            client.start()

            #cow

            #子進程client已經複製了一份，父進程中該socket沒用了，　所以關掉
            newSocket.close()
    finally:
        serverSocket.close()


if __name__ == '__main__':
    main()
