from lyricsgenius import Genius
import json
import shutil
import re
import config
import os

genius = Genius(config.api_key)


def getLyricsJSon(id, title, artist):
        if os.path.exists(f'lyrics_rawData/{id}.json') :
            return     
        song = genius.search_song(title, artist)
        if song is None:
                return

        s =song.lyrics 
        parts = s.split('\n')
        s = '\n'.join(parts[1:])
        s= re.sub(r'\[[^]]*\]', '', s)
        s = re.sub(r'.{8}$', '', s)

        song.lyrics = s

        song.save_lyrics(filename='lyrics.json')
        shutil.move('lyrics.json', f'lyrics_rawData/{id}.json')

def getLyrics(title, artist):
        song = genius.search_song(title, artist)
        if song is None:
                return
        s =song.lyrics 
        parts = s.split('\n')
        s = '\n'.join(parts[1:])
        s= re.sub(r'\[[^]]*\]', '', s)
        s = re.sub(r'.{8}$', '', s)

        return s

if __name__ == '__main__':
        getLyricsJSon(0,"Purple Rain", "Prince")
