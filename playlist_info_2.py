from tokenize import String
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import json
import requests
import shutil
import os



client_id = config.spotify_CLIENT_ID
client_secret = config.spotify_CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

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

def get_playlist_tracks(username,playlist_info):
    playlist_name = playlist_info[0]
    playlist_id = playlist_info[1]
    # Track ID from the URI
    play_id = str(playlist_id)
    results = sp.user_playlist_tracks(username,play_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    #if isEnglish(playlist_name) == False:
    #    playlist_name = play_id
    if os.path.exists(f'{username}_playlists/{play_id}.txt') :
            return
    with open(play_id+".txt", "w") as outfile:
        for i in range(len(tracks)):
          if tracks[i]['track'] != None:
           if isEnglish(tracks[i]['track']['name']) and isEnglish(tracks[i]['track']['artists'][0]['name']): 
            outfile.write(tracks[i]['track']['name'] +"; " + tracks[i]['track']['artists'][0]['name'] +"\n")
   
    directory = username+"_playlists"
  
    # Parent Directory path
    parent_dir = os.getcwd() + "/Users"
  
    # Path
    path = os.path.join(parent_dir, directory)
    if os.path.exists(f'Users/{username}_playlists') == False :
     os.mkdir(path)
    shutil.move(play_id+'.txt', f'Users/{username}_playlists/{play_id}.txt')

 
    return 0

def isEnglish(s):
    if s is None:
       return False
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    
    else:
        return True
    
def main(user_id):
    list_of_playlists = run(user_id)
    for i in range(len(list_of_playlists)):
      print(get_playlist_tracks(user_id,list_of_playlists[i]))
if __name__ == '__main__':
    main('mmurali20')
    #print(get_playlist_tracks("mmurali20","0KeRsGnBhW4YkE9MECH3X0"))
