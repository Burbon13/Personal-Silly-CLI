import click

from ..utils.services import hide_data_in_image_path_and_save, extract_data_from_image_path

@click.group()
def cli():
    """ Cryptography functions """
    pass

@cli.command()
@click.argument('photo_path')
@click.argument('text')
def hide_text(photo_path: str, text: str):
    click.echo('Hiding data ...')
    hide_data_in_image_path_and_save(text, photo_path)
    click.echo('Text successfully hidden!')


@cli.command()
@click.argument('photo_path')
def extract_text(photo_path: str):
    click.echo('Retrieving the hidden information ...')
    text = extract_data_from_image_path(photo_path)
    click.echo('=========== Text found: ===========')
    click.echo(text)
    click.echo('===================================')
