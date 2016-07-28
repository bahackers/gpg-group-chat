import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='GPG Group Chat')
    parser.add_argument('--client',
                        default=False,
                        action='store_true',
                        help='Cliente mode')

    parser.add_argument('--server',
                        default=False,
                        action='store_true',
                        help='Server mode')

    parser.add_argument('-t', '--target',
                        metavar='<target>',
                        default='127.0.0.1',
                        help='an IP or a range of IP that is alowed to ' +
                             'connect when running in server mode')

    parser.add_argument('-p', '--port',
                        metavar='<port>',
                        default=9999,
                        type=int,
                        help='the server port')

    parser.add_argument('-H', '--host',
                        metavar='<host>',
                        default='127.0.0.1',
                        help='IP adress of the server for connection when ' +
                             'running in client mode')

    return parser.parse_args()
