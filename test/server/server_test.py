from gpg_group_chat.server.server import Server
from unittest import TestCase
from unittest.mock import patch


class ServerTest(TestCase):

    def setUp(self):
        self.socket = patch('socket.socket').start()
        self.Thread = patch('threading.Thread').start()
        self.Event = patch('threading.Event').start()

        self.server = Server()

    def test_should_open_a_listen_port(self):
        port = 123
        target = '0.0.0.0'

        def function():
            pass

        self.server._accept_connections = function
        self.server.start(port, target)

        self.server._socket.bind.assert_called_once_with((target, port))
        self.server._socket.listen.assert_called_once_with(1)

    def test_should_accept_connection_and_create_a_thread_to_handle_it(self):
        self.server._working = True

        def side_effect():
            self.server._working = False
            return (None, ('', 0))

        self.server._socket = self.socket()
        self.server._socket.accept.side_effect = side_effect

        self.server._accept_connections()

        assert self.Event.called
        assert self.Thread.called
