import pickle

def main(filepath):
  # open a file, where you stored the pickled data
  file = open(filepath, 'rb')

  # dump information to that file
  data = pickle.load(file)

  # close the file
  file.close()

  return data
  # print('Showing the pickled data:')
  # cnt = 0
  # for i in range(len(data)):
  #   if data[i] != "":
  #     cnt +=1

  # print(str(cnt) + "/"+ str(len(data)))
  #print(data)