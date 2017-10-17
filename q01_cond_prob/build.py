# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(df):
    total= df.shape[0]
    old= df[df['Neighborhood']=='OldTown'].shape[0]
    cond_prob = old/total*(old-1)/(total-1)*(old-2)/(total-2)
    return cond_prob
