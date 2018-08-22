# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    ot_houses = df[df['Neighborhood']=='OldTown'].shape[0]
    tot_houses = df.shape[0]
    conditional_prob =()
    prod1 = ot_houses/tot_houses 
    prod2 = (ot_houses-1)/(tot_houses-1)
    prod3 = (ot_houses-2)/(tot_houses-2)
    conditional_prob = prod1*prod2*prod3
    return conditional_prob






