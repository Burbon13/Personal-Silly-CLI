""" Sample CLI commands """
import click
import requests
from datetime import datetime
from constants import OPEN_WEATHER_API_KEY


@click.group()
def cli():
    """ A sample set of silly sub-commands """
    pass


@cli.command()
def about():
    """ A short description of the idea of this CLI tool """
    click.echo(click.style('This CLI tool contains random ideas of mine. Developed in 2020! With love!', fg='green'))


@cli.command()
def creator():
    """ Prints the creator of this amazing CLI tool """
    click.echo(click.style('This CLI tool was developed by Razvan Roatis!!!', fg='green'))


@cli.command()
def time():
    """ Prints the current time """
    click.echo(f'Current Time = {datetime.now().strftime("%H:%M:%S")}')


@cli.command()
@click.option('--town', default='Leuven', help='For which town do you want the weather (default is Leuven, Belgium)')
def weather(town):
    """ Prints the current weather for a given city (default is Leuven, Belgium) """
    click.echo(f'Retrieving weather for {town} ...')
    try:
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={town}&appid={OPEN_WEATHER_API_KEY}&units=metric')
        if response.status_code == 200:
            json_response = response.json()
            city = json_response['name']
            country = json_response['sys']['country']
            weather_description = json_response['weather'][0]['description']
            temperature = json_response['main']['temp']
            feels_like = json_response['main']['feels_like']
            wind_speed = json_response['wind']['speed']
            click.echo(
                f'Weather in {city}, {country}: {weather_description}, temperature is {temperature} degrees C and feels'
                + f' like {feels_like} degrees C, wind speed {wind_speed} Km/h')
        elif response.status_code == 404:
            click.echo(response.json()['message'])
        else:
            click.echo('Unknown error occurred')
    except Exception as e:
        click.echo(f'Error occurred: {e.message}')


if __name__ == '__main__':
    cli()
