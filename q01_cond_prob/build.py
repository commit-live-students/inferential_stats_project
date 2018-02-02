# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    pd.set_option('display.max_columns',500)
    all_houses=df.shape[0]
    old_town=df[df['Neighborhood']=='OldTown'].shape[0]
    c=1
    for i in range(3):
        c=c*((old_town-i)/(all_houses-i))
    
    return c

print cond_prob(df)




