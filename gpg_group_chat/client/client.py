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
        
        target = 'localhost'
        port = 9999
        self._nickname = 'Riad'

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
            msg = raw_input('<You> ')                      
            self._socket.send('<'+self._nickname+'> '+msg)

