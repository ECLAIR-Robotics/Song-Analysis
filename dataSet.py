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
df['track-artist'] = pd.Series(df.index).apply(lambda i: [i]) + df['track-artist']


df['track-artist'].progress_apply(lambda i: getLyrics(*i))


print(df.head())

