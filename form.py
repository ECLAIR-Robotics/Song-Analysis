import cgi
from api import getLyrics
from llm/v2_final_model/model.py import processLyrics

form = cgi.FieldStorage()
title =  form.getvalue('title')
artist = form.getvalue('artist')
lyrics = getLyrics(title, artist)

result = processLyrics(lyrics)

