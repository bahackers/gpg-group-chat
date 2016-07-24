import socket
import threading

class Client():

    def __init__(self):
        self._socket = None
        self._working = False
        self._thread_events = {}
        self._fingerprint = None
        self._nickname = None

    def start(self):
        print('Starting Client...')
        
        target = raw_input('Server: ')
        port = raw_input('Port: ')
        self._nickname = raw_input('Nickname: ')

        self._working = True
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.connect((target, port))
            self._chat_handler()
        except KeyboardInterrupt:
            pass
        finally:
            self._socket.close()
            self._stop_all_threads()

    
    def _stop_all_threads(self):
        for thread_event in self._thread_events.values():
            thread_event.set()

    def _chat_handler(self):
        while self._working:
            server_socket, addr = self._socket, self._socket.getpeername()

            thread_event = threading.Event()
            args = (server_socket, thread_event)
            chat_thread = threading.Thread(target=self._chat_update, args=args)

            chat_thread.start()
            self._thread_events[addr] = thread_event

            msg = raw_input('<You> ')                     
            if not msg:
                break
            else:
                self._socket.send('<'+self._nickname+'> '+msg)

    @staticmethod
    def _chat_update(server_socket, thread_event):
        while not thread_event.is_set():    
            data = server_socket.recv(1024)
            
            if not data:
                break
            else:
                print(data)
                
