# import libraries
import json

import requests
import pandas as pd
from pandas import json_normalize
import spotipy
import spotipy.util as util

from spotifysecrets import *


class SpotifyAnalyzer:
    # create SpotifyAnalyzer instance
    def __init__(self, username, redirect_uri='http://localhost:8888/callback', scope=["user-top-read", "playlist-read-private"]):
        
        self.token = None
        self.sp = None
        self.username = username
        self.scope = scope
        self.redirect_uri = redirect_uri
        self.generate_token()
        
    # set/modify scope
    def set_scope(self, scope):
        self.scope = scope
        self.generate_token()
        
    
    def generate_token(self):
        token = util.prompt_for_user_token(
            self.username, 
            self.scope, 
            client_id=CLIENT_ID, 
            client_secret=CLIENT_SECRET, 
            redirect_uri=self.redirect_uri
        )
        if token:
            self.sp = spotipy.Spotify(auth=token)
            self.token = token
        else:
            print(f"Cant get token for {self.username}")

        
    # print top artists
    def get_top_artists(self):
        # get request for top artists
        headers = {
            'Authorization': 'Bearer ' + self.token
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

        return
    
    # print available genre seeds
    def get_genre_seeds(self):
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        response2 = requests.get('https://api.spotify.com/v1/recommendations/available-genre-seeds', headers=headers)

        if response2.status_code == 200:
            data2 = response2.json()
        else:
            print(f"Error: {response2.status_code}")

        data2_str = json.dumps(data2, indent=2)
        print(data2_str)


def main():

    # credentials
    username = 'nrkjbdqb3gwxlzypjce5vvqra'
    redirect_uri = 'http://localhost:8888/callback'

    # list of predefined scopes
    scope = [
        'user-top-read',
        'user-read-recently-played',
        'user-read-currently-playing', 
        'playlist-read-private', 
        'playlist-read-collaborative', 
        'playlist-modify-private', 
        'playlist-modify-public', 
        'user-library-read'
    ]

    sp = SpotifyAnalyzer(username, redirect_uri)
    sp.get_top_artists()
    sp.get_genre_seeds()



if __name__ == "__main__":
    main()