import tensorflow as tf
import io
from tqdm import tqdm as tqdm
import numpy as np
import re
VOCAB_SIZE = 100000
y_names = ['angry', 'bittersweet', 'dark', 'dreamy', 'epic', 'fun', 'happy', 'melancholy', 'mellow', 'romantic', 'sad', 'sexy']

# Code from https://fasttext.cc/docs/en/english-vectors.html
# Modified to use a limited vocabulary size and have a progress bar
def load_vectors(fname):
    # lines = num_lines(fname)
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    # for line in tqdm(fin, total=lines):
    for idx, line in tqdm(enumerate(fin), total=VOCAB_SIZE):
        if idx >= VOCAB_SIZE:
            break
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = np.array(list(map(float, tokens[1:])) + [0, 0])
    return data


class MultimodelClassifier:
    def __init__(self):
        self.vectorizer = load_vectors('wiki-news-300d-1M-subword-fasttext/wiki-news-300d-1M-subword.vec')
    
    def vectorize(self, data):
        data = re.sub()
