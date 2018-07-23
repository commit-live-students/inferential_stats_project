# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


def cond_prob(df):
    n = df[df['Neighborhood'] == 'OldTown'].shape[0]
    d = df['Neighborhood'].shape[0]
    return ((n/d)*((n-1)/(d-1))*((n-2)/(d-2)))
    
cond_prob(df)




