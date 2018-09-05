# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    
    houses =len(df['Neighborhood'])
    oldtown =len([x for x in df['Neighborhood'] if x == 'OldTown'])
    return oldtown/houses * (oldtown-1)/(houses-1)*(oldtown-2)/(houses-2)

cond_prob(df)


