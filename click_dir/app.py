"""A program that says hello or goodbye to provided username."""
import click


@click.group()
def greet():
    """ Say hello or goodbye."""
    pass


@greet.command()
@click.argument('name')  # Add name arg
def hello(**kwargs):
    """ (str) -> stdout

        Say Hello to user <name>
    """
    print('Hello, {0}!'.format(kwargs['name']))


@greet.command()
@click.argument('name')
def goodbye(**kwargs):
    """ (str) -> stdout

        Say Goodbye to user <name>
    """
    print('Goodbye {0}!'.format(kwargs['name']))


if __name__ == '__main__':
    greet()
