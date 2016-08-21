import select
import socket
import sys


class Client():

    def __init__(self):
        self._socket = None
        self._working = True

    def start(self, server_port, server_ip):
        print('Hello friend')
        dest = (server_ip, server_port)

        try:
            self._socket = socket.create_connection(dest)
        except ConnectionRefusedError as err:
            print('Connection refused')
            sys.exit(1)

        self._handle_messages()

    def _handle_messages(self):
        input_list = [sys.stdin, self._socket]
        self._prompt()
        while self._working:
            ready_to_read, _, _ = select.select(input_list, [], [])
            self._handle_input_channel(ready_to_read)

    def _handle_input_channel(self, ready_to_read):
        for input_channel in ready_to_read:
            if input_channel is self._socket:
                self._receive_data_from_server()
            else:
                self._send_message_to_server()

    def _receive_data_from_server(self):
        data = self._socket.recv(4096)
        if not data:
            print('\nDisconnected from chat server')
            sys.exit(0)
        else:
            print(data.decode('utf-8'))
            self._prompt()

    def _send_message_to_server(self):
        msg = '[*] %s' % input()
        self._socket.send(msg.encode('utf-8'))
        self._prompt()

    def _prompt(self):
        print('[Me] ', end='')
        sys.stdout.flush()
