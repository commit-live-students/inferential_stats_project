# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
def cond_prob(df):
    all_houses=df.shape[0]
    OT_house=df[df['Neighborhood'] == 'OldTown']['Neighborhood'].shape[0]

    x=(OT_house/all_houses)*((OT_house-1)/(all_houses-1))*((OT_house-2)/(all_houses-2))

    return x
