'''
select: 輪詢　with limit
poll: 輪詢　without limit
epoll: 事件通知機制　without limit


'''


import select
import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 7788))
server.listen(100)

inputs = [server, sys.stdin]
# inputs max length 2048 for 64bit, 1024 for 32bit, 輪詢，　效率低
# poll without socket limit
# epoll

running = True


while True:
    readable, writable, exceptional = select.select(inputs, [], [])

for sck in readable:
    if sck == server:
        conn, addr = server.accept()
        inputs.append(conn)

    elif sck == sys.stdin:
        cmd = sys.stdin.readline()
        running = False
        break
    else:
        data = sck.recv(1024)
        if data:
            sck.send(data)
        else:
            inputs.remove(sck)
            sck.close()
