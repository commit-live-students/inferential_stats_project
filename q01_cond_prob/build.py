# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    num = df[df.Neighborhood == 'OldTown'].shape[0]
    den = df.Neighborhood.shape[0]

    prob = (num/den)*((num - 1)/ (den - 1)) * ((num - 2)/ (den - 2))

    return prob





