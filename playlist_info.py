from tokenize import String
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import json
import requests


#may not be using all of the imports in this file
CLIENT_ID = config.spotify_CLIENT_ID
CLIENT_SECRET = config.spotify_CLIENT_SECRET
#client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
user_id = 'mmurali20'

# actual GET request with proper header
r = requests.get(BASE_URL + 'users/' + user_id+ '/playlists?offset=0&limit=50', headers=headers)
r = r.json()

with open("Mehul's_playlists.json", "w") as outfile:
    json.dump(r, outfile)

for i in range(len(r['items'])):
 print(r['items'][i]['id'])
 print() 
#debugging