import llm.model as model
import loadPickler
import os
import pickle

pickleDir = os.getcwd() + "\lyricPickles"
#print(pickleDir)

results = []
for file in os.listdir(pickleDir):
    data = loadPickler.main(pickleDir + "\\" + file)
    data = [i for i in data if i != '']
    results.append(model.process_user(data))
with open("modelresults") as f:
    pickle.dump(results,f)


