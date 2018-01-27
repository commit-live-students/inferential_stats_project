# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

def cond_prob(df):
    p1 = df['Neighborhood'][df['Neighborhood']=='OldTown'].count() / df['Neighborhood'].count()
    p2 = (df['Neighborhood'][df['Neighborhood']=='OldTown'].count() - 1) / (df['Neighborhood'].count() - 1)
    p3 = (df['Neighborhood'][df['Neighborhood']=='OldTown'].count() - 2) / (df['Neighborhood'].count() - 2)
    prob = p1 * p2 * p3
    return float(prob)

print cond_prob(df)
