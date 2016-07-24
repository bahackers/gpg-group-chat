import socket
import threading


class Server():

    def __init__(self):
        self._socket = None
        self._thread_events = {}
        self._working = False

    def start(self, port, target):
        print('Starting server...')
        self._working = True
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.bind((target, port))
            self._socket.listen(1)
            self._accept_connections()
        except KeyboardInterrupt:
            pass
        finally:
            self._socket.close()
            self._stop_all_threads()

    def _accept_connections(self):
        while self._working:
            client_socket, addr = self._socket.accept()
            print('Connection accepted from %s:%d' % addr)

            thread_event = threading.Event()
            args = (client_socket, thread_event)
            client_thread = threading.Thread(target=self._client_handler,
                                             args=args)

            client_thread.start()
            self._thread_events[addr] = thread_event

    def _stop_all_threads(self):
        for thread_event in self._thread_events.values():
            thread_event.set()

    @staticmethod
    def _client_handler(client_socket, thread_event):
        while not thread_event.is_set():
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                print('[INFO] Received: %s' % data)
