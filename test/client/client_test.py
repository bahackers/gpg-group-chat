from gpg_group_chat.client.client import Client
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from socket import socket as SocketType
import sys


class ClientTest(TestCase):

    def setUp(self):
        self.create_connection = patch('socket.create_connection').start()
        self.exit = patch('sys.exit').start()
        self.readline = patch('sys.stdin.readline').start()
        self.select = patch('select.select').start()
        self.print_stdout = patch('sys.stdout.write').start()

        self.socket = Mock(SocketType)
        self.create_connection.return_value = self.socket

        self.client = Client()

    def test_connect_to_a_server(self):
        def _handle_messages():
            pass

        self.client._handle_messages = _handle_messages
        self.client.start(9999, '127.0.0.1')

        self.create_connection.assert_called_once_with(('127.0.0.1', 9999))

    def test_to_connect_to_unexist_server(self):
        def side_effect(dest):
            raise ConnectionRefusedError(111, 'connection refused')

        def _handle_messages():
            pass

        self.create_connection.side_effect = side_effect
        self.client._handle_messages = _handle_messages

        self.client.start(9999, 'server.runkown')

        self.exit.assert_called_once_with(1)

    def test_send_a_message_to_the_server(self):
        def side_effect(msg):
            self.client._working = False

        self.socket.send.side_effect = side_effect
        self.readline.return_value = 'message'
        self.select.return_value = ([sys.stdin], None, None)

        self.client.start(9999, '127.0.0.1')

        self.socket.send.assert_called_once_with(b'[*] message')

    def test_receive_a_message_from_the_server(self):
        def side_effect(size):
            self.client._working = False
            return b'message from server'

        self.socket.recv.side_effect = side_effect
        self.select.return_value = ([self.socket], None, None)

        self.client.start(9999, '127.0.0.1')

        self.print_stdout.assert_any_call('message from server')
