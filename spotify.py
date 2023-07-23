# import libraries
import os
import json

import requests
import pandas as pd
from pandas import json_normalize
import spotipy
import spotipy.util as util

from spotifysecrets import *

# credentials
username = 'nrkjbdqb3gwxlzypjce5vvqra'
redirect_uri = 'http://localhost:8888/callback'

# dictionary of predefined scopes
scope = {
    0: 'user-top-read',
    1: 'user-read-recently-played',
    2: 'user-read-currently-playing',
    3: 'playlist-read-private',
    4: 'playlist-read-collaborative',
    5: 'playlist-modify-private',
    6: 'playlist-modify-public',
    7: 'user-library-read'
}

# authorization flow
token = util.prompt_for_user_token(
    username, scope[0], 
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, 
    redirect_uri=redirect_uri
)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print(f"Cant get token for {username}")

# get request for top artists
headers = {
    'Authorization': 'Bearer ' + token
}
params = {
    "limit": 20,  # number of artists to retrieve
    "time_range": "medium_term"  # time range for top artists (short_term, medium_term, long_term)
}
response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")

# ANALYSIS
data_str  = json.dumps(data, indent=2)
data_dict = json.loads(data_str)


top_artists = data['items']

for artist in top_artists:
    artists = artist['name']
    print(f"{artist['name']} Popularity: {artist['popularity']} Genres: {artist['genres']}")


response2 = requests.get('https://api.spotify.com/v1/recommendations/available-genre-seeds', headers=headers)

if response2.status_code == 200:
    data2 = response2.json()
else:
    print(f"Error: {response2.status_code}")

data2_str = json.dumps(data2, indent=2)
print(data2_str)