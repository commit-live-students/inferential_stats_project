# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    all_houses=df.shape[0]
    neighborhood_oldtown=df[df['Neighborhood']=='OldTown'].shape[0]
    ans=(neighborhood_oldtown/all_houses)*(neighborhood_oldtown-1)/(all_houses-1)*(neighborhood_oldtown-2)/(all_houses-2)
    return ans
    

cond_prob(df)
    





