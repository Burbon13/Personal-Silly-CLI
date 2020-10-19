from typing import List
from random import choice
import os


def get_all_files_from_directory(path: str, extensions: List[str]) -> List[str]:
    """
    Retrieves all files in a directory with the given extensions.

    :param path:            The folder to be searched
    :param extensions:      The desired extensions (e.g. jpg, png, etc.)
    :return:                A list with the path of all found files
    """
    selected_files = []
    for root, _, files in os.walk(path):
        for file in files:
            for ext in extensions:
                if ext == file.lower()[-len(ext):]:
                    selected_files.append(os.path.join(root, file))
                    break
    return selected_files


def select_random_picture_from_directory(path: str) -> str:
    """
    Searches for a random picture in a given path (must have jpg, jpeg or png extensions).

    :param path:    The folder to be searched.
    :return:        The path to that picture.
    """
    return choice(get_all_files_from_directory(path, ['jpg', 'jpeg', 'png']))
