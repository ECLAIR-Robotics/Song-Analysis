import api
import os
import requests
from bs4 import BeautifulSoup
import re

def tester():
    lis = "C.R.E.A.M. (Cash Rules Everything Around Me) (feat. Method Man, Raekwon, Inspectah Deck & Buddha Monk)"
    lis= re.sub(r'\([^]]*\)', '', lis)
    lis = lis.strip()
    print(lis)

tester()
    
def scrapeSong(title, artist):
    title = title.replace(" ", "+")
    artist = artist.replace(" ", "+")
    baseURL = "https://dm.vern.cc/search?q="
    searchURL = f'{baseURL}{title}+{artist}'
    r = requests.get(searchURL)
    soup = BeautifulSoup(r.content, 'html5lib')
    songLink = soup.find('a', attrs = {'id':"search-item"})['href']
    songLink = baseURL[:18]+songLink
    
    r = requests.get(songLink)
    soup = BeautifulSoup(r.content, 'html5lib')
    for br in soup('br'):
        br.replace_with('\n')
    lyricTable = soup.find('div', attrs = {'id':"lyrics"})
    for row in lyricTable.findAll('a'):
        lis = row.find('span').get_text()
        lis = re.sub(r'\[[^]]*\]', '', lis)
        print(lis)


scrapeSong("Without Me", "Eminem")


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




    