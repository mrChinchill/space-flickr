#!/usr/bin/env python3

import urllib3
import os

from dotenv import load_dotenv
from fetch_hubble import fetch_hubble_collection
from fetch_spacex import fetch_spacex_last_launch
from flickr_upload import authenticate
from flickr_upload import upload_image
from helper import resize_images
from pathlib import Path


def main():
    load_dotenv()
    flickr_api_key = os.getenv('FLICKR_API_KEY', '')
    flickr_api_secret = os.getenv('FLICKR_API_SECRET', '')

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    root_path = Path(__file__).resolve().parent

    images_path = root_path.joinpath('images')
    images_path.mkdir(parents=True, exist_ok=True)

    resized_images_path = images_path.joinpath('resized')
    resized_images_path.mkdir(parents=True, exist_ok=True)

    print('Downloading SpaceX images...')
    fetch_spacex_last_launch(images_path)

    print('Downloading Hubble images...')
    fetch_hubble_collection(images_path, 'stsci_gallery')

    print('Resizing images...')
    resize_images(images_path, resized_images_path, 1080)

    flickr = authenticate(flickr_api_key, flickr_api_secret)
    images_list = [x for x in resized_images_path.iterdir() if x.is_file()]
    for image in images_list:
        print('Uploading {}...'.format(image))
        rsp = upload_image(flickr, image)

    print('Done\n')


if __name__ == '__main__':
    main()
