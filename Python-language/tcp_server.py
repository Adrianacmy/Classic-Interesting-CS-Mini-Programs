'''
路由器：　鏈接不同網段的設備
tcp中，如果一方收到包，一定會發送ＡＣＫ包向對方確認收到
２２


'''

from socket import *

#####################################################################

# server side
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind('localip', 8899)
serverSocket.listen(5) # max client it can listen

print('.............1.............')


while True:

    # clientAddr: new client ip and port
    # newSocket: new client
    clientSocket, clientInfo = serverSocket.accept()
    print('.............2.............')

    while True:
        recvData = clientSocket.recv(1024)
        print('.............3.............')
        if len(recvData)>0:
            print('{}: {}'.format(str(clientInfo), recvData))
        else:
            break

        sendData = raw_input('enter msg: ')
        newSocket.send(sendData)

    newSocket.close()

clientSocket.close()
serverSocket.close()

#######################################################################
# client side

ClientSocket = socket(AF_INET, SOCK_STREAM)
ClientSocket.connect(('localip', 7788))
sendData = raw_input('enter msg: ')
ClientSocket.send(sendData.encode('gb2312'))

recvData = ClientSocket.recv(1024)
print('{}'.format(recvData)
ClientSocket.close()

##############################################################################

# tcp 服務器大體框架
def clientWorking(cSocket):
    while True:
        cSocket.recv(xxx)
        cSocket.send(xxx)

s = socket()
s.bind()
s.listen()

while True:
    cSocket, cInfo = s.accept()
    p = Process(target=clientWorking, args=(cSocket, cInfo,))
    p.start()