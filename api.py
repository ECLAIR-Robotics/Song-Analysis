from lyricsgenius import Genius
import json
import re

genius = Genius("ekvvo28ZF9zgy2MNOGQOhdQJQ7-BKWYO_oKSu39YFLx6IMQamzoReRZwzMV0OK-u")

song = genius.search_song("Billie Jean", "Michael Jackson")

s =song.lyrics 
s = re.sub(r'.{8}$', '', s)
parts = s.split('\n')
s = '\n'.join(parts[1:])
s= re.sub(r'\[[^()]*\]', '', s)
#print(s)

song.save_lyrics()

with open('lyrics.txt', 'w') as m:
        
        m.write(s)
#with open('lyrics_michaeljackson_billiejean.json', 'r') as f:
    #with open('adele_hello.txt', 'w') as m:
        
        
       # data = json.load(f)
        #m.write(data['lyrics'])
       # s= data['lyrics']
       # s = re.sub(r'.{8}$', '', s)
       # parts = s.split('\n')
       # s = '\n'.join(parts[1:])
       # s= re.sub(r'\[[^()]*\]', '', s)
       # m.write(s)



        #pattern = r'\[[^()]*\]'
        #s = "Issachar is a rawboned[a] donkey lying down among the sheep pens."
        #t = re.sub(pattern, '', s)
        #print(t)



#data = json.load(f)
#print(data['lyrics'])


#artist = genius.search_artist("Adele", max_songs=3, sort="title")
#album = genius.search_album("Hello", "Adele")
#print(song)
#print(artist.songs)