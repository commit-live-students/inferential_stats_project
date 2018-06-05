# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    total = df.shape[0]
    old_town = len(df[df.Neighborhood == 'OldTown'])
    prob = (old_town / total ) * ((old_town -1)/(total-1))* ((old_town -2)/(total-2))
    return prob






