import csv

from lyricsgenius import Genius
import pandas as pd
import numpy as np
import array

from api import getLyrics
from tqdm import tqdm


df = pd.read_csv('muse_v3.csv')
tqdm.pandas()
df['track-artist'] = df['track'].apply(lambda i: [i])
df['track-artist'] = df['track-artist'] + df['artist'].apply(lambda i: [i])

df['track-artist'].progress_apply(lambda i: getLyrics(i.name, i[0], i[1]))

# df['track-artist'] = df.apply(lambda i: (i.col_1, i.col_2))
# df.apply(lambda i: getLyrics(i.col_1, i.col_2))
print(df.head())
# Array2d_result = np.genfromtxt(df, delimiter=",")
# Array2d_result = df.to_numpy()
# print(Array2d_result)

# for i in range(9000):
#     print(Array2d_result[i][0])
#     print()

