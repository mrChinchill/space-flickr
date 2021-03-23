#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ElementTree

from pathlib import Path
from PIL import Image
from urllib.parse import urlparse


def download_image(url, image_path, verify=True):
    response = requests.get(url, verify=verify)
    response.raise_for_status()

    with open(image_path, 'wb') as file:
        file.write(response.content)


def get_image_extension(url):
    return Path(urlparse(url).path).suffix


def resize_images(source_path, target_path, max_size):
    files_list = [x for x in source_path.iterdir() if x.is_file()]

    for file in files_list:
        new_file = target_path.joinpath(file.name).with_suffix('.jpg')

        image = Image.open(file)
        image.thumbnail((max_size, max_size))
        image = image.convert('RGB')
        image.save(new_file, format='JPEG')


def et_to_str(root):
    return ElementTree.tostring(root).decode('utf-8')
