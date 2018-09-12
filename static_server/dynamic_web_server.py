# coding:utf-8

from multiprocessing import Process
import socket
import time_m
import sys

HTML_ROOT_DIR = './html'
WSGI_PYTHON_DIR = './wsgipython'


class HTTPServer(object):
    '''

    '''

    def __init__(self, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        server_socket.listen(128)
        while True:
            client_socket, client_address = server_socket.accept()
            print('{} connected'.format(client_address))
            handle_client_process = Process(
                target=handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024)
        request_lines = request_data.splitlines()

        response_start_line = request_lines[0]
        fine_name = re.match(r'\w+ +(/[^ ]*) ', response_start_line.decode('utf-8')).group(1-)

        env = {
            'query': '',
            'path': ''
        }

    def start_response(status, headers):
        server_headers = [
            ('server': 'dynamic server')
        ]
        server_headers
        response_headers = 'HTTP/1.1' + status + '\r\n'
        for header in headrs:
            response_headers += '{}: {}\r\n'.format(header[0], headr[1])
        self.response_headers = response_headers

        if '/' == file_name:
            file_name = '/index.html'

        if file_name.endswith('.py'):
            m = __import__(file_name[1:-3])
            env = {}
            response_body = m.application(env, self.start_response)
            response = self.response_headers + '\r\n' + response_body

            # response = time_m.application()
        else:
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

    def bind(self):
        server_socket.bind(('', port))


def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(('', port))
    http_server.start()


if __name__ == '__main__':
    main()
