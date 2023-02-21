from tokenize import String
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

client_id = 'dac0e94e73384e26bd8cb69eee39fe67'
client_secret = '3b8b407e3dc340dfa7491520722f8da7'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API



track = 'AOK'
track_info_sp = sp.search(q=' track:' + track, limit=25)
def main():
    track_uri = track_info_sp['tracks']['items'][0]['id']
    print(track_info_sp['tracks']['items'][1])
    #track_uri = "spotify:track:1sx0XsWUusUoPstbvokZjP"
    #cprint("Hello\n")
    print(sp.audio_features(track_uri)[0])


    with open("spotify_data.json", "w") as outfile:
        json.dump(sp.audio_features(track_uri)[0], outfile)
        json.dump(track_info_sp, outfile)

main()