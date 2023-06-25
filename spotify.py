import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import requests

redirect_uri = 'http://localhost:8888/callback'

scope = {
    0: "user-top-read",
    1: "user-read-recently-played",
    2: "user-read-currently-playing",
    3: "playlist-read-private",
    4: "playlist-read-collaborative",
    5: "playlist-modify-private",
    6: "playlist-modify-public",
    7: "user-library-read"
}

auth_code = requests.get(AUTH_URL, {


    
})