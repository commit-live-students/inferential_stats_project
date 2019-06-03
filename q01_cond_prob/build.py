# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
# Enter Code Here
def cond_prob(df):
    no_of_houses = df.shape[0]
    no_of_oldtown_houses = df[df.Neighborhood == 'OldTown'].shape[0]
    probability = 1
    for i in range(3):
        probability *= (no_of_oldtown_houses - i)/(no_of_houses - i)
    return probability
cond_prob(df)

