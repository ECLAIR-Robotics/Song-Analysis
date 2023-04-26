import argparse
import api

parser = argparse.ArgumentParser(description='generate ML tags from a song')
parser.add_argument('-t', '--title', help = 'title of song', required= True)
parser.add_argument('-a', '--artist', help = 'artist of song', required= True)
args = parser.parse_args()        

lyrics = api.getLyrics(title, artist)
results= model.gen_tags(lyrics, 8)

print('/n results: ' + results) 
