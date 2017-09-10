#!/usr/bin/env/python3

import sys

from flask import Blueprint, Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

app = Flask(__name__)

# SPOTIPY_CLIENT_ID = ''
# SPOTIPY_CLIENT_SECRET = ''
# SPOTIPY_REDIRECT_URI = 'http://localhost:8000/'


'''
Views.
'''
@app.route('/')
def index():
    ''' Main view. '''
    # sp = spotipy.Spotify()

    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # playlists = sp.user_playlists('spotify')
    # while playlists:
    #     for i, playlist in enumerate(playlists['items']):
    #         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    #     if playlists['next']:
    #         playlists = sp.next(playlists)
    #     else:
    #         playlists = None

    results = sp.search(q='helmet', limit=20)
    for i, t in enumerate(results['tracks']['items']):
        print(' ', i, t['name'])

    return render_template('index.html')
    

app.run(debug=True, port=8000, host='0.0.0.0')
