""" Sample CLI commands """
import click
import requests
from os import listdir
from os.path import isfile, join
import random
from datetime import datetime, timedelta
from constants import OPEN_WEATHER_API_KEY, CREATOR_ASCII_PROFILE_FILE_PATH, PHOTOS_LOCATION
from ..utils.cli import pretty_print_weather, pretty_print_all_covid_cases
from ..utils.my_os import select_random_picture_from_directory
from PIL import Image


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
    try:
        with open(CREATOR_ASCII_PROFILE_FILE_PATH, 'r') as file:
            data = file.read()
            click.echo(click.style(data, fg='yellow'))
    except FileNotFoundError:
        click.echo(click.style(f'ASCII art file not found at {CREATOR_ASCII_PROFILE_FILE_PATH}', fg='red'))
    except Exception as e:
        click.echo(click.style(f'Unexpected error occurred: {e}', fg='red'))


@cli.command()
def time():
    """ Prints the current time """
    click.echo(f'Current Time = {datetime.now().strftime("%H:%M:%S")}')


@cli.command()
@click.option('--town', default='Leuven', help='For which town do you want the weather (default is Leuven, Belgium)')
def weather(town):
    """ Prints the current weather for a given town (default is Leuven, Belgium) """
    click.echo(f'Retrieving weather for {click.style(town, fg="bright_green")} ...')
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

            pretty_print_weather(click, city, country, weather_description, temperature, feels_like, wind_speed)
        elif response.status_code == 404:
            click.echo(click.style(response.json()['message'], fg='red'))
        else:
            click.echo(click.style(f'Unknown error occurred: {response.status_code} HTTP CODE', fg='red'))
    except Exception as e:
        click.echo(click.style(f'Unexpected error occurred: {e}', fg='red'))


@cli.command()
@click.option('--country', default='Belgium', help='For which country do you want COVID-19 stats')
@click.option('--days', default=7, help='How many days to show stats for (e.g. last 7 days is default)')
def covid(country, days):
    """ Prints the current COVID-19 stats for a given country (default is Belgium) """
    click.echo(f'Retrieving COVID-19 info for {country} for the past {days} days')
    try:
        end_date_time = (datetime.now() + timedelta(hours=-6)).strftime("%Y-%m-%dT%H:%M:%SZ")
        start_date_time = (datetime.now() + timedelta(days=-days - 2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        response = requests.get(
            f'https://api.covid19api.com/total/country/{country}?from={start_date_time}&to={end_date_time}')

        if response.status_code == 200:
            pretty_print_all_covid_cases(click, country, days, response.json())
        elif response.status_code == 404:
            click.echo(click.style(f'HTTP 404: {response.json()["message"]}', fg='red'))
        else:
            click.echo(click.style(f'Unknown error occurred: {response.status_code} HTTP CODE', fg='red'))
    except Exception as e:
        click.echo(click.style(f'Error occurred: {e}', fg='red'))


@cli.command()
def dad_joke():
    """ Prints a random dad joke (lovely type of jokes). Want to piss your girlfriend? USE THIS!!! """
    try:
        response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
        if response.status_code == 200:
            click.echo(click.style(response.json()['joke'], fg='bright_green'))
        else:
            click.echo(click.style(f'Error occurred: {response.status_code} HTTP code', fg='red'))
    except Exception as e:
        click.echo(click.style(f'Error occurred: {e}', fg='red'))


@cli.command()
@click.option('--subf', default='', help='The sub-folder where to search')
def rand_pic(subf):
    """ Opens a random picture """
    try:
        rand_pic_location = select_random_picture_from_directory(PHOTOS_LOCATION + subf)
        click.echo(f'Opening {rand_pic_location} ...')
        Image.open(rand_pic_location).show()
    except Exception as e:
        click.echo(click.style(f'Error occurred: "{e}" (check for path correctness)', fg='red'))


if __name__ == '__main__':
    cli()
