import csv

from lyricsgenius import Genius
import pandas as pd
import numpy as np

df = pd.read_csv('muse_v3.csv')
print(df)
Array2d_result = np.genfromtxt(df, delimiter=",")
Array2d_result = df.to_numpy()
print(Array2d_result)



