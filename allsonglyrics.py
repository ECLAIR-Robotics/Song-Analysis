import playlist_info_2
import os
import requests
from bs4 import BeautifulSoup
import re
import pickle

def isEnglish(s):
    if s is None:
       return False
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
        
def scrapeSong(title, artist):
    pattern = re.compile('(- [^-]*)$') #gets rid of - Single Version, - 2012 Remaster etc without affecting songs with an actual hyphen
    title = pattern.sub('', title)
    title= re.sub(r'\([^]]*\)', '', title)
    title = re.sub(r'\[[^]]*\]', '', title)
    title = title.strip()
    title = title.replace(" ", "+")
    artist = artist.replace(" ", "+")
    baseURL = "https://sing.whatever.social/search?q="
    searchURL = f'{baseURL}{title}+{artist}'
    
    r = requests.get(searchURL)
    soup = BeautifulSoup(r.content, 'html5lib')
    songLink = soup.find('a', attrs = {'id':"search-item"}, href=True)['href'] if soup.find('a', attrs = {'id':"search-item"}, href=True) is not None else "skip"
    if songLink != "skip":
        songLink = baseURL[:28]+songLink
    
        r = requests.get(songLink)
        soup = BeautifulSoup(r.content, 'html5lib')
        for br in soup('br'):
            br.replace_with('\n')
        lyricTable = soup.find('div', attrs = {'id':"lyrics"})
        lyrics = ""
        if lyricTable is not None:
            for row in lyricTable.findAll('a'):
                if(row.find('span') is not None):
                    lis = row.find('span').get_text()
                    lis = re.sub(r'\[[^]]*\]', '', lis)
                    if isEnglish(lis):
                        lyrics += lis +"\n"
        return lyrics
    return ''
#print(scrapeSong("Someone Like You", "Adele"))
def getLyrics():
    rootdir = os.getcwd() + "/Users"
    for subdir, dirs, files in os.walk(rootdir):
        if(subdir != rootdir):
            lyrics = []
            for file in files:
                with open(os.path.join(subdir, file)) as f:
                    for line in f.readlines():
                        title = line.split(';')[0]
                        title = re.sub(r'\([^]]*\)', '', title)
                        artist = line.split(';')[1].lstrip()
                        lyrics.append(scrapeSong(title, artist))  
            with open(os.getcwd() + "/lyricPickles/" + os.path.basename(os.path.normpath(subdir))+ "_lyrics", 'wb') as f:
                pickle.dump(lyrics, f)                                     
    return 

def main():
    userFile = open("users.txt",'r')
    Lines = userFile.readlines()
    for line in Lines:
        playlist_info_2.main(line.strip())
    getLyrics()
main()


## TRASH CODE ##

# def getUrls():
#      rootdir = os.getcwd() + "/Users"
#      urlmatrix = []
#      for subdir, dirs, files in os.walk(rootdir):
#         if(subdir != rootdir):
#             urls = []
#             for file in files:
#                 with open(os.path.join(subdir, file)) as f:
#                     for line in f.readlines():
#                         title = line.split(';')[0]
#                         title = re.sub(r'\([^]]*\)', '', title)
#                         artist = line.split(';')[1].lstrip()
#                         pattern = re.compile('(- [^-]*)$') #gets rid of - Single Version, - 2012 Remaster etc without affecting songs with an actual hyphen
#                         title = pattern.sub('', title)
#                         title= re.sub(r'\([^]]*\)', '', title)
#                         title = re.sub(r'\[[^]]*\]', '', title)
#                         title = title.strip()
#                         title = title.replace(" ", "+")
#                         artist = artist.replace(" ", "+")
#                         baseURL = "https://sing.whatever.social/search?q="
#                         searchURL = f'{baseURL}{title}+{artist}'
#                         r = requests.get(searchURL)
#                         if(r is not None):
#                             soup = BeautifulSoup(r.content, 'html5lib')
#                         if(soup is not None):
#                             songLink = soup.find('a', attrs = {'id':"search-item"}, href=True)['href']
#                         if(songLink is not None):
#                             songLink = baseURL[:28]+songLink
#                             urls.append(songLink)
#             urlmatrix.append(urls)
#      return urlmatrix

# if __name__ == '__main__':
#     # userFile = open("users.txt",'r')
#     # Lines = userFile.readlines()
#     # for line in Lines:
#     #     playlist_info_2.main(line.strip())
#     #urlmatrix= getUrls()
#     #print(getUrls())
#     p = Pool(4)
#     result = 

# def tester():
#     lis = "Smooth Criminal - 2012 Remaster"
#     pattern = re.compile('(- [^-]*)$')
#     lis = pattern.sub('', lis)
#     lis= re.sub(r'\([^]]*\)', '', lis)
#     lis = re.sub(r'\[[^]]*\]', '', lis)
#     lis = lis.strip()
#     print(lis)