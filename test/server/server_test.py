from gpg_group_chat.server.server import Server
from unittest.mock import patch


@patch('socket.socket')
def test_should_open_a_listen_port(socket):
    port = 123
    target = '0.0.0.0'

    def function():
        pass

    server = Server()
    server._accept_connections = function
    server.start(port, target)

    server._socket.bind.assert_called_once_with((target, port))
    server._socket.listen.assert_called_once_with(1)


@patch('threading.Thread')
@patch('threading.Event')
@patch('ssl.wrap_socket')
def test_should_accept_connection_and_create_a_thread_to_handle_it(Event, Thread, wrap_socket):
    server = Server()
    server._working = True

    def side_effect():
        server._working = False
        return (None, ('', 0))

    server._socket = wrap_socket
    server._socket.accept.side_effect = side_effect

    server._accept_connections()

    assert Event.called
    assert Thread.called
