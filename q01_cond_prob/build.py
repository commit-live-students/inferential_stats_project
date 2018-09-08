# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here
def cond_prob(df):   
    location = df.Neighborhood
    town = (df.Neighborhood).value_counts()
    x = 0
    conditional_prob = 1
    while x < 3:
        conditional_prob = ((town['OldTown']- x)/(len(location) - 0))*conditional_prob
        x = x + 1
    return conditional_prob




