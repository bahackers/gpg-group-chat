import select
import socket
import sys
import threading

class Client():

    def __init__(self):
        self._socket = None
        self._connected = False
        self._nickname = 'anonymous'
        self._key = 'no-key'

    def start(self, server_ip = None, server_port = None, nickname = None):
        if nickname != None:
            self._nickname = nickname
        if server_ip == None:
            print('no server addr')
            return
        self._key = 'no-key'
        print('Hello friend ' + self._nickname)
        dest = (server_ip, server_port)
        try:
            self._socket = socket.create_connection(dest)
        except:
            print('error opening socket')
            return;
        success = self.__start_protocol()
        if(success):
            self.__handle_messages()
        else:
            print('error to stabilish connection')

    def __start_protocol(self):
        msg = 'hello, i am ' + self._nickname + ',' + self._key
        self._socket.sendall(msg.encode('utf-8'))
        msg = self._socket.recv(1024)
        if not msg:
            print('no response from server')
        else:
            if(msg.startswith(b'ACK')):
                print('the server accepted your connection')
                print('the connected users are:')
                print(msg[3:])
            elif(msg.startswith(b'NACK')):
                print('the server refused your connection')
            else:
                print('unknown answer from server, be careful')
        return True

    def __handle_messages(self):
        #exemple found here: http://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php
        socket_list = [sys.stdin, self._socket]
        self.__prompt()
        while 1:
            ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
            for sock in ready_to_read:
                if sock == self._socket:
                    # incoming message from remote server
                    data = sock.recv(4096)
                    if not data :
                        print('\nDisconnected from chat server')
                        sys.exit()
                    else :
                        #print data
                        sys.stdout.write(data.decode('utf-8'))
                        self.__prompt()

                else :
                    # user entered a message
                    msg = sys.stdin.readline()
                    msg = '['+self._nickname+'] ' + msg
                    msg = self.__gpg_encrypt(msg)
                    self._socket.send(msg.encode('utf-8'))
                    self.__prompt()

    @staticmethod
    def __prompt():
        sys.stdout.write('[Me] ')
        sys.stdout.flush()

    def __gpg_encrypt(self,msg):
        return msg
