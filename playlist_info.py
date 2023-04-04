from tokenize import String
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import json
import requests

def run(user_id):
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
    user_id = user_id

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'users/' + user_id+ '/playlists?offset=0&limit=50', headers=headers)
    r = r.json()

    with open("Mehul's_playlists.json", "w") as outfile:
        json.dump(r, outfile)

    lis = [] # this is the list of playlist ids for current user
    for i in range(len(r['items'])):
     lis.append((r['items'][i]['name'],r['items'][i]['id']))

    return lis
    
def items_of_playlist(playlist_info):
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

    BASE_URL = 'https://api.spotify.com/v1/'
      
    playlist_name = playlist_info[0]
    playlist_id = playlist_info[1]
    # Track ID from the URI
    play_id = str(playlist_id)

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'playlists/' + play_id+ '/tracks?offset=0&limit=50', headers=headers)
    r = r.json()

    with open(playlist_name+".json", "w") as outfile:
        json.dump(r, outfile)

    with open(playlist_name+".txt", "w") as outfile:
        for i in range(len(r['items'])):
          if isEnglish(r['items'][i]['track']['name']) and isEnglish(r['items'][i]['track']['artists'][0]['name']): 
           outfile.write(r['items'][i]['track']['name']+ "; "+ r['items'][i]['track']['artists'][0]['name'] + "\n") #name of artist and song
          
    return playlist_name

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

if __name__ == '__main__':
    list_of_playlists = run('mmurali20')
    for i in range(len(list_of_playlists)):
      print(items_of_playlist(list_of_playlists[i]))