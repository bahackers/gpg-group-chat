from gpg_group_chat import Client, Server
import sys
import getopt


def main():
    args = getopt.getopt(sys.argv[1:], '', ['client', 'server', 'help'])[0]

    if len(args) < 1:
        print('Use --help for more information!')
        sys.exit(1)

    for arg in args:
        if '--server' in arg:
            Server().start(9999, '0.0.0.0')
        elif '--client' in arg:
            Client().start()
        else:
            print('Helper will be available soon!')


if __name__ == '__main__':
    main()
