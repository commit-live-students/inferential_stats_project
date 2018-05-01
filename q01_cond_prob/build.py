# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')
#df.head()

# Enter Code Here
def cond_prob(df):
    all_houses=df['Neighborhood'].shape[0]
    oldtownhouses=df[df['Neighborhood']=='OldTown'].shape[0]
    conditional_prob=float((oldtownhouses/all_houses)*((oldtownhouses-1)/(all_houses-1))*((oldtownhouses-2)/(all_houses-2)))
    return conditional_prob
   






