from math import ceil, floor, log, sqrt
from random import random, randint
import matplotlib.pyplot as plt    
import matplotlib.cm as cm
import pandas as pd
import numpy as np
 
modelos = pd.read_csv('digits.txt', sep=' ', header = None)
#modelos = modelos.replace({'n': 0.995, 'g': 0.92, 'b': 0.002})
#modelos = modelos.replace({'n': 0.5, 'g': 0.5, 'b': 0.5}) # 10 de Clara
#modelos = modelos.replace({'n': 0.003, 'g': 0.002, 'b': 0.001}) # 9 de Clara
#modelos = modelos.replace({'n': 0.01, 'g': 0.008, 'b': 0.98}) # 5 de Clara
modelos = modelos.replace({'n': 0.99, 'g': 0.98, 'b': 0.97}) # 8 de Clara
r = 5
c = 3
dim = r * c
n = 49
w = ceil(sqrt(n))
h = ceil(n / w)
 
f, a = plt.subplots(w, h, figsize = (1.5 * w, 2 * h), dpi = 300)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)
x = 0
y = 0
for j in range(n):
    d = randint(0, 9)
    pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
    img = pixeles.values.reshape(r, c)
    a[x, y].pcolormesh(img, edgecolors = 'gray', cmap = cm.Greys)
    a[x, y].set_title(str(d))
    a[x, y].axis('off')
    a[x, y].invert_yaxis() # cero arriba
    x += 1
    if x == w:
        x = 0
        y += 1
plt.savefig('p12pg.png')
plt.close()
