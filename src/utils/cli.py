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


def pretty_print_weather(click, city, country, weather_description, temperature, feels_like, wind_speed):
    """
    Prints the weather forecast in a pretty format with colors with the Click CLI library.

    :param click:                   Reference to the Click library
    :param city:                    The city for the weather forecast
    :param country:                 The country for the weather forecast
    :param weather_description:     The weather_description for the weather forecast
    :param temperature:             The temperature for the weather forecast
    :param feels_like:              The temperature which is felt for the weather forecast
    :param wind_speed:              The wind_speed for the weather forecast
    """

    click.echo('Weather in ', nl=False)
    click.echo(f'{click.style(city, fg="bright_green")}, ', nl=False)
    click.echo(f'{click.style(country, fg="bright_green")}: ', nl=False)
    click.echo(f'{click.style(weather_description, fg="blue")}, ', nl=False)
    click.echo(f'temperature is {click.style(str(temperature), fg="bright_blue")} degrees C and feels ', nl=False)
    click.echo(f'like {click.style(str(feels_like), fg="bright_blue")} degrees C, wind speed ', nl=False)
    click.echo(f'{click.style(str(wind_speed), fg="bright_blue")} Km/h')


def pretty_print_all_covid_cases(click, country, days, json_response):
    """
    Prints the covid cases in a pretty format with colors with the Click CLI library.

    :param click:               Reference to the Click library
    :param country:             The country from which are the cases
    :param days:                The number of days from which are the cases
    :param json_response:       A list containing the cases, each element is a dict/json which must contain:
                                    - Confirmed     (int)  the number of confirmed cases
                                    - Active        (int)  the number of active cases
                                    - Recovered     (int)  the number of recovered cases
                                    - Deaths        (int)  the number of deaths
                                    - Date          (date) the date of the cases
    """
    last_stat = json_response[0]
    click.echo('=======================', nl=False)
    click.echo(f'  {click.style(country.upper(), fg="bright_green")} - ', nl=False)
    click.echo(f'LAST {click.style(str(days), fg="bright_green")} days  ', nl=False)
    click.echo('=======================')
    for stat in json_response[1:]:
        pretty_print_covid_case(click, stat, last_stat)
        last_stat = stat


def sign_nr_to_str(click, nr, positive_is_good) -> str:
    """ If nr is positive, returns +nr, else -nr """
    if nr > 0:
        return click.style(f'+{nr}', fg='bright_green' if positive_is_good else 'red')
    return click.style(str(nr), fg='red' if positive_is_good else 'bright_green')


def pretty_print_covid_case(click, stat, last_stat):
    """
    Prints the covid cases for a given day and the differences compared to the previous day.

    :param click:       Reference to the Click library
    :param stat:        The actual statistics. dict/json which must contain:
                            - Confirmed     (int)  the number of confirmed cases
                            - Active        (int)  the number of active cases
                            - Recovered     (int)  the number of recovered cases
                            - Deaths        (int)  the number of deaths
                            - Date          (date) the date of the cases
    :param last_stat:   The statistics from the previous day of "stat" param. A dict/json which must contain:
                            - Confirmed     (int)  the number of confirmed cases
                            - Active        (int)  the number of active cases
                            - Recovered     (int)  the number of recovered cases
                            - Deaths        (int)  the number of deaths
                            - Date          (date) the date of the cases
    """

    confirmed = click.style(str(stat["Confirmed"]), fg='bright_blue')
    confirmed_diff = sign_nr_to_str(click, stat["Confirmed"] - last_stat["Confirmed"], False)
    active = click.style(str(stat["Active"]), fg='bright_yellow')
    active_diff = sign_nr_to_str(click, stat["Active"] - last_stat["Active"], False)
    recovered = click.style(str(stat["Recovered"]), fg='bright_green')
    recovered_diff = sign_nr_to_str(click, stat["Recovered"] - last_stat["Recovered"], True)
    deaths = click.style(str(stat["Deaths"]), fg='red')
    deaths_diff = sign_nr_to_str(click, stat["Deaths"] - last_stat["Deaths"], False)

    click.echo(
        f'Confirmed: {confirmed} ({confirmed_diff})'
        + f'  Active: {active} ({active_diff})'
        + f'  Recovered: {recovered} ({recovered_diff})'
        + f'  Deaths: {deaths}  ({deaths_diff})'
        + f'  Date: {stat["Date"]}')
