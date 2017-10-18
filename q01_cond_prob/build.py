# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    x=len(df[df['Neighborhood']=='OldTown'])
    y=len(df['Neighborhood'])
    prob=(x/y)*((x-1)/(y-1))*((x-2)/(y-3))
    return prob

#cond_prob(df)
