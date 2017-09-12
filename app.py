#!/usr/bin/env/python3

import sys

from flask import Blueprint, Flask, jsonify, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

app = Flask(__name__)

# SPOTIPY_CLIENT_ID = ''
# SPOTIPY_CLIENT_SECRET = ''
# SPOTIPY_REDIRECT_URI = 'http://localhost:8000/'


def get_tracks(artist):
    '''Return top 20 tracks of given artist.'''
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q=artist, limit=20, type='track', market='JP')
    tracks = []
    for i, t in enumerate(results['tracks']['items']):
        # print(' ', i, t['name'])
        track_play_prefix = 'https://open.spotify.com/track/'
        track_id = t['id']
        track_play_url = track_play_prefix + track_id
        track_name = t['name']
        track_info = [track_play_url, track_name]
        tracks.append(track_info)

    print(tracks)

    html = '<h3 id="the-artist">' + artist + '</h3>' + ''
    for track in tracks:
        html += '<a href="' + track[0] + '" target="_blank">' + track[1] + '</a>'

    return html


@app.route('/_artist_stuff')
def artist_stuff():
    text = request.args.get('text', '', type=str)
    return jsonify(result=get_tracks(text))


'''
Views.
'''
# @app.route('/_add_numbers')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a + b)


@app.route('/')
def index():
    ''' Main view. '''

    return render_template('index.html')


# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.lower()
#     # return processed_text
#     if processed_text.strip() == '':
#         return "Back back, and enter an artist."
#     else:
#         # return get_tracks(processed_text)
#         return artist_stuff(processed_text)


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
