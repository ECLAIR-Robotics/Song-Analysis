import tensorflow as tf
import io
from tqdm import tqdm as tqdm
import numpy as np
import re
VOCAB_SIZE = 100000
CUTOFF = 329
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
        self.models = [tf.keras.models.load_model(f'demo-tags/{i}') for i in y_names]
    
    def vectorize_word(self, word: str) -> np.ndarray:
        if word == '':  # If this is a pad token
            return np.array([0] * 301 + [1], dtype=np.float64)
        if word in self.vectorizer:  # If this word is in our vocabulary
            return self.vectorizer[word]
        return np.array([0] * 300 + [1, 0], dtype=np.float64)  # Unknown token
    
    def vectorize(self, data: str) -> np.ndarray:
        data = re.sub(r'[^\w\s]', '', data)
        data = data.lower()
        data = re.split(' |\n', data)
        data = [i for i in data if i]
        data = data[:CUTOFF]
        data = data + [''] * (CUTOFF - len(data))
        return np.stack([self.vectorize_word(i) for i in data])
    
    def predict(self, data: str) -> list:
        vectorized = self.vectorize(data)
        vectorized = np.expand_dims(vectorized, axis=0)
        results = np.round([i(vectorized)[0] for i in self.models])
        return [y_names[idx] for idx, val in enumerate(results) if val > 0]
