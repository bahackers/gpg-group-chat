import select
import socket
import sys
import threading


class Client():

    def __init__(self):
        self._socket = None
        self._connected = False
        self._nickname = 'anonymous'

    def start(self, server_ip, server_port, nickname=None):
        if nickname is not None:
            self._nickname = nickname
        print('Hello friend ' + self._nickname)
        dest = (server_ip, server_port)
        try:
            self._socket = socket.create_connection(dest)
        except:
            print('error opening socket')
            return
        self.__handle_messages()

    def __handle_messages(self):
        socket_list = [sys.stdin, self._socket]
        self.__prompt()
        while True:
            ready_to_read, _, _ = select.select(socket_list, [], [])
            for sock in ready_to_read:
                if sock == self._socket:
                    # incoming message from remote server
                    data = sock.recv(4096)
                    if not data:
                        print('\nDisconnected from chat server')
                        sys.exit()
                    else:
                        # print data
                        sys.stdout.write(data.decode('utf-8'))
                        self.__prompt()
                else:
                    # user entered a message
                    msg = sys.stdin.readline()
                    msg = '['+self._nickname+'] ' + msg
                    self._socket.send(msg.encode('utf-8'))
                    self.__prompt()

    @staticmethod
    def __prompt():
        sys.stdout.write('[Me] ')
        sys.stdout.flush()
