import socket


class Server():

    def __init__(self):
        self._socket = None

    def start(self, port, target):
        print('Server is not done yet!')
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((target, port))
        self._socket.listen(1)

        # client_socket, addr = self._socket.accept()
