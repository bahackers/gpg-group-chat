from gpg_group_chat import Client, Server, arguments
import sys

def main():
    args = arguments.parse_args()

    if args.client:
        Client().start(args.port, args.host)
    elif args.server:
        Server().start(args.port, args.target)
    else:
        print('Use --help for more information!')
        sys.exit(1)


if __name__ == '__main__':
    main()
