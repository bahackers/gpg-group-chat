import socket
import threading
import ssl


class Server():

    def __init__(self):
        self._socket = None
        self._thread_events = {}
        self._working = False

    def start(self, port, target):
        print('Server listening on %s:%d' % (target, port))
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
            print('Connection initiated with %s:%d' % addr)
            print('Verifying SSL encryption')

            try:
                ok = True
                sslsocket = ssl.wrap_socket(client_socket,
                                            server_side=True,
                                            certfile="./ssl_certs/server.crt",
                                            keyfile="./ssl_certs/server.key")

            except ssl.SSLError:
                ok = False
                client_socket.close()
                print("SSL Error")
                pass
            except socket.error:
                ok = False
                client_socket.close()
                print("Connection Error")
                pass
            finally:
                if ok:
                    thread_event = threading.Event()
                    args = (sslsocket, thread_event)
                    client_thread = threading.Thread(
                        target=self._client_handler,
                        args=args)

                    client_thread.start()
                    self._thread_events[addr] = thread_event

    def _stop_all_threads(self):
        for thread_event in self._thread_events.values():
            thread_event.set()

    @staticmethod
    def _client_handler(client_socket, thread_event):
        while not thread_event.is_set():
            data = client_socket.read()

            if not data:
                break
            else:
                print('[INFO] Received: %s' % data.decode('utf-8'))
