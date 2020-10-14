import click
import requests
from constants import NEWS_API_KEY


@click.group()
def cli():
    """ News aggregator from several APIs/Websites """
    pass


@cli.command()
@click.option('--country', default='be', help='From which country you want news (default Belgium)',
              type=click.Choice(['ro', 'be', 'us', 'uk'], case_sensitive=False))
@click.option('--category', default='general', help='What type of news you want (default General)',
              type=click.Choice(['general', 'health', 'science', 'sports'], case_sensitive=False))
@click.option('--count', default=20, help='How many news you want? (maximum 100 possible)')
def every(country, category, count):
    """ News aggregated by country """
    click.echo('Retrieving the latest news ...')
    try:
        response = requests.get(
            f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&pageSize={count}',
            headers={'Authorization': NEWS_API_KEY})
        if response.status_code == 200:
            response_json = response.json()
            articles = response_json['articles']
            for article in articles:
                click.echo(f'({click.style(article["publishedAt"], fg="bright_green")}) {article["title"]}')
        else:
            click.echo(click.style(f'Response: {response.status_code}', fg='red'))
    except Exception as e:
        click.echo(click.style(f'Unexpected error occurred: {e}', fg='red'))


if __name__ == '__main__':
    cli()
