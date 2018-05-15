# %load q01_cond_prob/build.py
# So that float division is by default in python 2.7
from __future__ import division

import pandas as pd

df = pd.read_csv('data/house_pricing.csv')


# Enter Code Here

def cond_prob(df):
    totalh=df.iloc[:,13].count()
    oldh=df[df.loc[:,'Neighborhood']=='OldTown'].iloc[:,13].count()
    conditional_prob=(oldh/totalh)*((oldh-1)/(totalh-1))*((oldh-2)/(totalh-2))
    return conditional_prob

