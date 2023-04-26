import argparse
from allsonglyrics import scrapeSong
import llm.model as model

parser = argparse.ArgumentParser(description='generate ML tags from a song')
parser.add_argument('-t', '--title', help='title of song', required=True)
parser.add_argument('-a', '--artist', help='artist of song', required=True)
parser.add_argument('--highfidelity', help='whether to use high fidelity algorithm', action=argparse.BooleanOptionalAction)
args = parser.parse_args()

lyrics = scrapeSong(args.title, args.artist)
if args.highfidelity:
    results = model.high_fidelity_gen_tags(lyrics, 4)
else:
    results = model.gen_tags(lyrics, 4)

print(results)

