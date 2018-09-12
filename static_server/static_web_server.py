# coding:utf-8

from multiprocessing import Process
import socket


HTML_ROOT_DIR = ''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 8000))
server_socket.listen(128)


def handle_client(client_socket):
    '''
    handle request from clients
    '''
    request_data = client_socket.recv(1024)

    # construct response
    response_start_line = 'HTTP/1.1 200 ok\r\n'
    response_header = 'Server: static_server\r\n'
    response_body = 'hello server'
    response = response_start_line + response_header + '\r\n' + response_body
    print(response)

    client_socket.send(bytes(response, 'utf-8'))

    client_socket.close()


def main():
    while True:
        client_socket, client_address = server_socket.accept()
        print('{} connected'.format(client_address))
        handle_client_process = Process(
            target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()


if __name__ == '__main__':
    main()

