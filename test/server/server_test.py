from gpg_group_chat.server.app import Server
from unittest.mock import MagicMock, Mock, patch


@patch('socket.socket')
def test_should_open_a_listen_port(socket):
    port = 123
    target = '0.0.0.0'

    server = Server()
    server.start(port, target)

    server._socket.bind.assert_called_once_with((target, port))
    server._socket.listen.assert_called_once_with(1)
