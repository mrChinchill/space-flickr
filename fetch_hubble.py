#!/usr/bin/env python3

import requests

from helper import download_image
from helper import get_image_extension


HUBBLE_BASE_URL = 'http://hubblesite.org/api/v3'


def get_hubble_image_links(image_id):
    url = '{}/image/{}'.format(HUBBLE_BASE_URL, image_id)

    response = requests.get(url)
    response.raise_for_status()

    images_links = ['https:{}'.format(image_file['file_url']) for image_file in response.json()['image_files']]

    return images_links


def download_hubble_image(images_path, image_id):
    url = get_hubble_image_links(image_id)[-1]
    filename = 'hubble_{}{}'.format(image_id, get_image_extension(url))
    image_path = images_path.joinpath(filename)
    download_image(url, image_path, verify=False)


def fetch_hubble_collection(images_path, collection_name):
    url = '{}/images/{}'.format(HUBBLE_BASE_URL, collection_name)
    payload = {'page': 'all'}

    response = requests.get(url, params=payload)
    response.raise_for_status()

    for image in response.json():
        download_hubble_image(images_path, image['id'])
