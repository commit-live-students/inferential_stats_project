# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):

    total_houses = df['Neighborhood'].shape[0]
    houses_OldTown = df[df['Neighborhood'] == 'OldTown']['Neighborhood'].count()
    cond_prob = (houses_OldTown/ total_houses) * ((houses_OldTown - 1)/ \
    (total_houses - 1)) * ((houses_OldTown - 2)/ (total_houses - 2))

    return cond_prob
