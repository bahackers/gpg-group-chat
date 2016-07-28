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
                        help='target connect to the server')

    parser.add_argument('-p', '--port',
                        metavar='<port>',
                        default=9999,
                        type=int,
                        help='the port to run the server')

    parser.add_argument('-H', '--host',
                        metavar='<host>',
                        default='127.0.0.1',
                        help='the host to connect to')

    return parser.parse_args()
