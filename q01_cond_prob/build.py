# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):
    x=len(df[df.Neighborhood == 'OldTown'])
    y=len(df)
    return (x/y) * (x/(y-1)) * (x/(y-2))



x=len(df[df.Neighborhood == 'OldTown'])
y=len(df)
(x/y) * (x/y) * (x/y)
0.00045
cond_prob(df)


