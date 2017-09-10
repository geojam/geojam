#!/usr/bin/env/python3

import sys

from flask import Blueprint, Flask, render_template
import spotipy
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

    # results = sp.search(q='weezer', limit=20)
    # for i, t in enumerate(results['tracks']['items']):
    #     print(' ', i, t['name'])
    return render_template('index.html')
    

app.run(debug=True, port=8000, host='0.0.0.0')
