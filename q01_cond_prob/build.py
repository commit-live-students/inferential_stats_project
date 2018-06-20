# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')

# Enter Code Here
def cond_prob(df):
    nhd = df.iloc[:,12]
    oldtown = nhd[nhd == 'OldTown'].size
    total = nhd.size
    return (oldtown/total) * ((oldtown-1)/(total-1)) * ((oldtown-2)/(total-2))
    





0.00045232831351218984

