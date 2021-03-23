#!/usr/bin/env python3

import requests

from helper import download_image
from pathlib import Path
from urllib.parse import urlparse


spacex_base_url = 'https://api.spacexdata.com/v4'


def get_spacex_images_links():
    url = '{}/launches'.format(spacex_base_url)

    response = requests.get(url)
    response.raise_for_status()

    launches_with_images = [launch['links']['flickr']['original'] for launch in response.json()
                            if launch['links']['flickr']['original']]

    return launches_with_images[-1]


def fetch_spacex_last_launch(images_path):
    for url in get_spacex_images_links():
        filename = Path(urlparse(url).path).name
        image_path = images_path.joinpath('spacex_{}'.format(filename))
        download_image(url, image_path)
