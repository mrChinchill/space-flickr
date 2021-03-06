#!/usr/bin/env python3

import requests

from helper import download_image
from pathlib import Path
from urllib.parse import urlparse


SPACEX_BASE_URL = 'https://api.spacexdata.com/v4'


def get_last_spacex_launch_images_links():
    url = '{}/launches'.format(SPACEX_BASE_URL)

    response = requests.get(url)
    response.raise_for_status()

    launches_with_images = [launch['links']['flickr']['original'] for launch in response.json()
                            if launch['links']['flickr']['original']]

    return launches_with_images[-1]


def fetch_spacex_last_launch(images_path):
    for url in get_last_spacex_launch_images_links():
        filename = Path(urlparse(url).path).name
        image_path = images_path.joinpath('spacex_{}'.format(filename))
        download_image(url, image_path)
