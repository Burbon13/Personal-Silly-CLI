def make_selection_in_cli(a_list, elem_to_str, click):
    """
    Given a list, it forces the user to select one and only one item from it.
    If the list is empty, None will be returned.

    :param a_list:          The list containing the items from which one will be selected by the user
    :param elem_to_str:     Custom to string function for the items in the a_list
    :param click:           Reference to the Click library
    :return:                The selected item by the user, None of none is selected
    """
    if a_list is None or len(a_list) == 0:
        return None

    while True:
        for i, elem in enumerate(a_list):
            click.echo(f'{click.style(f"{i})", fg="bright_yellow")} {elem_to_str(elem)}')
        index = click.prompt(f'Please select the index {click.style("(-1 to cancel)", fg="bright_yellow")}', type=int)
        if index == -1:
            return None
        if 0 <= index < len(a_list):
            return a_list[index]
        click.echo(click.style('Invalid index, try again!', fg='red'))
