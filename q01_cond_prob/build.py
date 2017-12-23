# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd
import numpy as np
df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(data):
    all_houses = df['Neighborhood'].count()
    house_oldTown = df[df['Neighborhood'] == 'OldTown'].shape[0]
    proarr = []
    for i in range(0,3):
        prob = house_oldTown/ all_houses
        proarr.append(prob)
        all_houses -= 1
        house_oldTown -= 1
    return np.product(proarr)
