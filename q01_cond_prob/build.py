# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    old_town_houses = df[df['Neighborhood'] == 'OldTown'].shape[0]
    total_houses = df['Neighborhood'].shape[0]
    conditional_prob = (old_town_houses/total_houses)*((old_town_houses-1)/(total_houses -1))*((old_town_houses-2)/(total_houses-2))
    return conditional_prob
