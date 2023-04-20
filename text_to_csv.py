import pandas as pd

def run(file_name):
   with open(file_name, 'r') as original: data = original.read()
   first_line = ""
   with open('file_name') as f:
    first_line = f.readline().strip()
   if first_line != "Song; Artist":
     with open('file_name', 'w') as modified: modified.write("Song; Artist\n" + data)
   dataframe1 = pd.read_csv(file_name)
  
   # storing this dataframe in a csv file
   dataframe1.to_csv('0KeRsGnBhW4YkE9MECH3X0.csv', index = None, error_bad_lines=False,delimiter =';') 
   return 0
if __name__ == '__main__':
   run('mmurali20_playlists/0KeRsGnBhW4YkE9MECH3X0.txt')