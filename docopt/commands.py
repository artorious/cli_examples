"""Greeter.

Usage:
    commands.py hello
    commands.py goodbye
    commands.py -h | --help

Options:
    -h --help   Show this screen.
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
