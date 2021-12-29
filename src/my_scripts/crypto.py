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
    """ 
    Hides text into an image 
    
    photo_path: Where does the image reside
    text: What text will be hidden inside the image
    """
    click.echo('Hiding data ...')
    hide_data_in_image_path_and_save(text, photo_path)
    click.echo('Text successfully hidden!')


@cli.command()
@click.argument('photo_path')
@click.argument('text_path')
def hide_text_file(photo_path: str, text_path: str):
    """ 
    Hides text from a file into an image 
    
    photo_path: Where does the image reside
    text_path: Where does the text file redise
    """
    click.echo('Reading file ...')
    with open(text_path, 'r') as text_file:
        text = ''.join(text_file.readlines())
        click.echo('Hiding text ...')
        hide_data_in_image_path_and_save(text, photo_path)
        click.echo('Text successfully hidden!')


@cli.command()
@click.argument('photo_path')
def extract_text(photo_path: str):
    """ 
    Extracts hidden text from an image 
    
    photo_path: Where does the image reside
    """
    click.echo('Retrieving the hidden information ...')
    text = extract_data_from_image_path(photo_path)
    click.echo('=========== Text found: ===========')
    click.echo(text)
    click.echo('===================================')


@cli.command()
@click.argument('photo_path')
def extract_text_file(photo_path: str):
    """ 
    Extracts hidden text from an image and saves it into a file in the same location
    
    photo_path: Where does the image reside
    """
    click.echo('Retrieving the hidden information ...')
    text = extract_data_from_image_path(photo_path)
    click.echo('Saving file ...')
    photo_name_without_extension = photo_path.split('.')[0]
    new_text_file_name = photo_name_without_extension + '.txt'
    with open(new_text_file_name, 'w+') as new_file:
        new_file.write(text)
        click.echo('Text successfully saved into file')
