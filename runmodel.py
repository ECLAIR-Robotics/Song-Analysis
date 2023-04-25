import llm.model as model
import loadPickler
import os

pickleDir = os.getcwd() + "\lyricPickles"
#print(pickleDir)
for file in os.listdir(pickleDir):
    model.process_user(loadPickler.main(pickleDir + "\\" + file))


