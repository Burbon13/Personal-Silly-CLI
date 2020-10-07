""" Sample CLI commands """
import click
import requests
from datetime import datetime, timedelta
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
    click.echo(click.style('This CLI tool was developed by\n'
                           + '===========  Razvan Roatis  ===========', fg='green'))


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
            click.echo(f'Unknown error occurred: {response.status_code} HTTP CODE')
    except Exception as e:
        click.echo(f'Error occurred: {e.message}')


@cli.command()
@click.option('--country', default='Belgium', help='For which country do you want COVID-19 stats')
@click.option('--days', default=7, help='How many days to show stats for (e.g. last 7 days is default)')
def covid(country, days):
    """ Prints the current COVID-19 stats for a given country (default is Belgium) """

    def sign_nr_to_str(nr):
        """ If nr is positive, returns +nr, else -nr """
        return f'+{nr}' if nr > 0 else str(nr)

    click.echo(f'Retrieving COVID-19 info for {country} for the past {days} days')
    try:
        end_date_time = (datetime.now() + timedelta(hours=-6)).strftime("%Y-%m-%dT%H:%M:%SZ")
        start_date_time = (datetime.now() + timedelta(days=-days - 2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        response = requests.get(
            f'https://api.covid19api.com/total/country/{country}?from={start_date_time}&to={end_date_time}')
        if response.status_code == 200:
            json_response = response.json()
            last = json_response[0]
            click.echo(f'=======================  {country.upper()} - LAST {days} days  =======================')
            for stat in json_response[1:]:
                click.echo(
                    f'Confirmed: {stat["Confirmed"]} ({sign_nr_to_str(stat["Confirmed"] - last["Confirmed"])})'
                    + f'  Active: {stat["Active"]} ({sign_nr_to_str(stat["Active"] - last["Active"])})'
                    + f'  Recovered: {stat["Recovered"]} ({sign_nr_to_str(stat["Recovered"] - last["Recovered"])})'
                    + f'  Deaths: {stat["Deaths"]}  ({sign_nr_to_str(stat["Deaths"] - last["Deaths"])})'
                    + f'  Date: {stat["Date"]}')
                last = stat
        elif response.status_code == 404:
            click.echo(f'HTTP 404: {response.json()["message"]}')
        else:
            click.echo(f'Unknown error occurred: {response.status_code} HTTP CODE')
    except Exception as e:
        click.echo(f'Error occurred: {e.message}')


@cli.command()
def dad_joke():
    """ Prints a random dad joke (lovely type of jokes). Want to piss your girlfriend? USE THIS!!! """
    try:
        response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
        if response.status_code == 200:
            click.echo(response.json()['joke'])
        else:
            click.echo(f'Error occurred: {response.status_code} HTTP code')
    except Exception as e:
        click.echo(f'Error occurred: {e}')


if __name__ == '__main__':
    cli()
