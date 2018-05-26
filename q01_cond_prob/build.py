# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    all_houses = df.shape[0]
    oldtown = df[df['Neighborhood']=='OldTown'].shape[0]
    prob = (oldtown/all_houses)*((oldtown-1)/(all_houses-1))*((oldtown-2)/(all_houses-2))
    return prob

#cond_prob(df)




