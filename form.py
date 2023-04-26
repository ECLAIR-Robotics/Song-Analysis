import llm.model as model
import cgi
import api 

form = cgi.FieldStorage()
title =  form.getvalue('title')
artist = form.getvalue('artist')
lyrics = api.getLyrics(title, artist)

results= model.gen_tags(lyrics, 8)

htmltext = "Results: %s" % (results)
htmlfile = open('index.html', 'a')
file.write(htmltext)
