'''

tcp/ip 族
port: 用來標記進程, 0-65535
Dynamic port: 1024-65535
show all ports: `netstat -an`
ip: 192.168.2.2: 最後一位不能位０和２５５
udp: 用戶數據協議
tcp: 傳輸控制協議

不同電腦上的不同進程間通信用socket
'''

import socket

#tcp 通信
tcps = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)


＃udp　通信, 快但不穩定，可能丟失數據, 但在局域網中丟包的可能爲0
udps = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)
udps.bind('', port)
reData = udps.recvfrom(1024)


udps.sendto(message.endcode('tuf-8'), ('targetip', port))

###############################################################
# tcp
# server
socket()
bind()
listen()
accept()

#client
