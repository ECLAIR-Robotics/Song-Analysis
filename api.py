import config
from lyricsgenius import Genius

genius = Genius(config.key)
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
