import argparse
import api
import llm.model

parser = argparse.ArgumentParser(description='generate ML tags from a song')
parser.add_argument('-t', '--title', help = 'title of song', required= True)
parser.add_argument('-a', '--artist', help = 'artist of song', required= True)
args = parser.parse_args()        

lyrics = api.getLyrics(args.title, args.artist)
results= model.gen_tags(lyrics, 8)

print('/n results: ' + results) 
