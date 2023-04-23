import pickle

# open a file, where you stored the pickled data
file = open('lyricPickles/mmurali20_playlists_lyrics', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

print('Showing the pickled data:')
cnt = 0
for i in range(len(data)):
 if data[i] != "":
  cnt +=1

print(cnt)
#print(data)