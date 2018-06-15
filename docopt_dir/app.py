"""Greeter.

Usage:
    app.py hello <name>
    app.py goodbye <name>
    app.py (-h | --help)

Options:
    -h --help   Show this screen.
"""
from docopt import docopt


def hello(name):
    """ (str) -> stdout

        Say Hello to <name>
    """
    print('Hello, {0}'.format(name))


def goodbye(name):
    """ (str) -> stdout

        Say Goodbye to <name>
    """
    print('Goodbye {0}'.format(name))


if __name__ == '__main__':
    ARGUMENTS = docopt(__doc__)

    # Logic - check for arument passed
    if ARGUMENTS['hello']:
        hello(ARGUMENTS['<name>'])
    elif ARGUMENTS['goodbye']:
        goodbye(ARGUMENTS['<name>'])
