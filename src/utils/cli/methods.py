def make_selection_in_cli(a_list, elem_to_str, click):
    """

    :param a_list:
    :param elem_to_str:
    :param click:
    :return:
    """
    if a_list is None or len(a_list) == 0:
        return None

    while True:
        for i, elem in enumerate(a_list):
            click.echo(f'{i}) {elem_to_str(elem)}')
        index = click.prompt('Please select the index (-1 to cancel)', type=int)
        if index == -1:
            return None
        if 0 <= index < len(a_list):
            return a_list[index]
        click.echo('Invalid index, try again!')
