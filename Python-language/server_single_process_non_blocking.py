'''

'''


from socket import *
from threading import Thread


def handleClient(newSocket, destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print(str(destAddr), recvData)
        else:
            print('{} client is closed'.format(str(destAddr)))
    newSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
localAddr = ('', 7788)
serverSocket.bind(localAddr)


serverSocket.setblocking(False)

serverSocket.listen(100)

clientAddrList = []

while True:
    # 等待新客戶端，　完成三次握手
    try:
        clientSocket, clientAddr = serverSocket.accept()
    except:
        pass
    else:
        print('new client {}'.format(str(clientAddr)))
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket, clientAddr))

    for clientSocket, clientAddr in clientAddrList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData)>0:
                print(str(clientAddr), recvData)
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket, clientAddr))
                print('{} is offline'.format(str(clientAddr)))