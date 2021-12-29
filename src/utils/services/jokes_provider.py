import requests
from typing import List


def get_dad_joke() -> str:
    """
    Requests a random dad joke from https://icanhazdadjoke.com/
    
    :returns: the joke string
    :raises Exception: when an error occurs
    """
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    if response.status_code == 200:
        return response.json()['joke']
    else:
        raise Exception(f'Error occurred: {response.status_code} HTTP code')


def get_multiple_dad_jokes(count: int) -> List[str]:
    """
    Requests n random dad jokes from https://icanhazdadjoke.com/
    
    :returns the list of jokes
    :raises Exception: when an error occurs
    """
    return [get_dad_joke() for _ in range(count)]
