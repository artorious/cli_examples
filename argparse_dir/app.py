""" Program says hello or goodbye to provided user name. """
import argparse


def greet(cli_params):
    """ (Namespace) -> stdout

        Display custom <greeting> to user<name>
    """
    output = '{0}, {1}!'.format(cli_params.greeting, cli_params.name)
    if cli_params.caps:
        output = output.upper()
    print(output)

PARSER = argparse.ArgumentParser(description='Program displays a custom \
    greeting to provided username.')
SUBPARSERS = PARSER.add_subparsers()

HELLO_PARSER = SUBPARSERS.add_parser('hello', help='Say hello to user')
HELLO_PARSER.add_argument('name', help='username')  # Add name arg
HELLO_PARSER.add_argument('--greeting', default='Hello',
                          help='Custom greeting w/ default')
HELLO_PARSER.add_argument('--caps', action='store_true',
                          help='sets greeting to ALL CAPS - boolean flag, \
                                  default set to FALSE')
HELLO_PARSER.set_defaults(func=greet, help='Default function')

GOODBYE_PARSER = SUBPARSERS.add_parser('goodbye', help='Say goodbye to user')
GOODBYE_PARSER.add_argument('name', help='username')
GOODBYE_PARSER.add_argument('--greeting', default='goodbye',
                            help='Custom greeting w/ default')
GOODBYE_PARSER.add_argument('--caps', action='store_true',
                            help='sets greeting to ALL CAPS - boolean flag \
                                    set to FALSE')
GOODBYE_PARSER.set_defaults(func=greet, help='Default function')

if __name__ == '__main__':
    ARGS = PARSER.parse_args()
    ARGS.func(ARGS)  # Call Default func
