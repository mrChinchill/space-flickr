#!/usr/bin/env python3

import flickrapi


def authenticate(api_key, api_secret):
    flickr = flickrapi.FlickrAPI(api_key, api_secret, store_token=True)

    # Only do this if we don't have a valid token already
    if not flickr.token_valid(perms='write'):
        # Get a request token
        flickr.get_request_token(oauth_callback='oob')

        # Open a browser at the authentication URL
        authorize_url = flickr.auth_url(perms='write')
        print('Go to the following URL: {0}'.format(authorize_url))

        # Get the verifier code from the user
        verifier = input('Enter verifier code: ')

        # Trade the request token for an access token
        flickr.get_access_token(verifier)

        print('Authentication successful!')

    return flickr


def upload_image(flickr, filename, is_public=0):
    title = filename.stem
    rsp = flickr.upload(filename=str(filename), title=title, is_public=is_public)

    return rsp
