""" Program says hello or goodbye to provided user name. """
import argparse


def hello(username):
    """ (str) -> stdout

        Say Hello <username>
    """
    print('Hello, {0}!'.format(username.name))


def goodbye(username):
    """ (str) -> stdout

        Say Goodbye <username>
    """
    print('Goodbye, {0}!'.format(username.name))

PARSER = argparse.ArgumentParser(
        description='Program says hello or goodbye to provided user name.')
SUBPARSERS = PARSER.add_subparsers()

HELLO_PARSER = SUBPARSERS.add_parser('hello', help='Say hello to user')
HELLO_PARSER.add_argument('name', help='username')  # Add name arg
HELLO_PARSER.set_defaults(func=hello)  # Set as Default function

GOODBYE_PARSER = SUBPARSERS.add_parser('goodbye', help='Say goodbye to user')
GOODBYE_PARSER.add_argument('name', help='username')
GOODBYE_PARSER.set_defaults(func=goodbye)

if __name__ == '__main__':
    ARGS = PARSER.parse_args()
    ARGS.func(ARGS)  # Call Default func
