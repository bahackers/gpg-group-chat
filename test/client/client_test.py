from gpg_group_chat.client.client import Client
from unittest import TestCase
from unittest.mock import patch


# to test:
# - open a connection to an existent server
# - try toopen a connection to an inexistent server
# - try to open a connection without network connection
# - send a message to te server and receive response
# - receive message from the server
class ClientTest(TestCase):

    def setUp(self):
        self.create_connection = patch('socket.create_connection').start()
        self.client = Client()

    def test_connect_to_a_server(self):
        def _handle_messages():
            pass

        self.client._handle_messages = _handle_messages
        self.client.start(9999, '127.0.0.1')

        self.create_connection.assert_called_once_with(('127.0.0.1', 9999))
