import click
import platform


"""
platform - https://docs.python.org/3/library/platform.html
"""


@click.group()
def cli():
    """ System information commands """
    pass


@cli.command()
def platform_information():
    """ Prints all information about the OS """
    click.echo(f'Architecture: {platform.architecture()[0]}')
    click.echo(f'Machine: {platform.machine()}')
    click.echo(f'Node: {platform.node()}')
    click.echo(f'System: {platform.system()}')





if __name__ == '__main__':
    cli()
