import h5py
import numpy as np
hf = h5py.File('TRBAZCS128F422CD34.h5', 'r')
hf.keys()
print(hf.keys())
n1 = hf.get('songs')
n1 = np.array(n1)
print(n1)
