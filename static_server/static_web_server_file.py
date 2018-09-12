# coding:utf-8

from multiprocessing import Process
import socket


HTML_ROOT_DIR = './html'




def handle_client(client_socket):
    '''
    handle request from clients
    '''
    request_data = client_socket.recv(1024)
    request_lines = request_data.splitlines()

    response_start_line = request_lines[0]
    fine_name = re.match(r'\w+ +(/[^ ]*) ', response_start_line.decode('utf-8')).group(1-)

    if '/' == file_name:
        file_name = '/index.html'

    # open file and read
    try:
        file = open(file_name, 'rb')
    except IOError:
        response_start_line = 'HTTP/1.1 200 ok\r\n'

        response_header = 'Server: static_server\r\n'
        response_body = 'file not found'
    else:
        file_data = file.read()
        file.close()

    response_start_line = 'HTTP/1.1 200 ok\r\n'
    response_header = 'Server: static_server\r\n'
    response_body = file_data.decode('utf-8')

    response = response_start_line + response_header + '\r\n' + response_body
    print(response)

    client_socket.send(bytes(response, 'utf-8'))

    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print('{} connected'.format(client_address))
        handle_client_process = Process(
            target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()


if __name__ == '__main__':
    main()
