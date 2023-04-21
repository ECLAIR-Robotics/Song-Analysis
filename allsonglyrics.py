import api
import os
import requests
from bs4 import BeautifulSoup
import re

def tester():
    lis = "Smooth Criminal - 2012 Remaster"
    pattern = re.compile('(- [^-]*)$')
    lis = pattern.sub('', lis)
    lis= re.sub(r'\([^]]*\)', '', lis)
    lis = re.sub(r'\[[^]]*\]', '', lis)
    lis = lis.strip()
    print(lis)

#tester()

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
    songLink = soup.find('a', attrs = {'id':"search-item"})['href']
    songLink = baseURL[:28]+songLink
    
    r = requests.get(songLink)
    soup = BeautifulSoup(r.content, 'html5lib')
    for br in soup('br'):
        br.replace_with('\n')
    lyricTable = soup.find('div', attrs = {'id':"lyrics"})
    for row in lyricTable.findAll('a'):
        lis = row.find('span').get_text()
        lis = re.sub(r'\[[^]]*\]', '', lis)
        if isEnglish(lis):
         print(lis)


scrapeSong("Walk Em Down (Don't Kill Civilians) [with 21 Savage & feat. Mustafa]", "Metro Boomin")





def getLyrics():
    rootdir = os.getcwd() + "/Users"
    userdict = {}
    for subdir, dirs, files in os.walk(rootdir):
        if(subdir != rootdir):
            curList = []
            for file in files:
                with open(os.path.join(subdir, file)) as f:
                    for line in f.readlines():
                        title = line.split(';')[0]
                        title = re.sub(r'\([^]]*\)', '', title)
                        artist = line.split(';')[1].lstrip()
                        #call api here
                        lyricString = api.getLyrics(title, artist)
                        if lyricString is not None:
                            curList += lyricString.split(" ")                            
            userdict[os.path.basename(os.path.normpath(subdir))] = curList
    return userdict

#getLyrics()




    